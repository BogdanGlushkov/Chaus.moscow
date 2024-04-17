import datetime
import json
import uuid

import qrcode
import qrcode.image.svg
import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Docs
from .models import Event
from .models import EventLinks
from .models import GuestList
from .models import Jobs
from .models import Partner
from .models import lendingLinks




@csrf_exempt
def TinkoffPayInit(request):
    # Get user data from the request
    user_data = {
        'name': request.POST.get('name'),
        'email': request.POST.get('email'),
        'phone': request.POST.get('phone'),
        'promo': request.POST.get('promo'),
        'order_id': str(uuid.uuid4())[:36],
    }

    payment = GuestList.objects.create(**user_data)
    order_id = payment.order_id
    this_event = Event.objects.get(id=request.POST.get('event'))

    payment_payload = {
        "TerminalKey": "*************",
        "Amount": int(str(this_event.price) + "00"),
        "OrderId": order_id,
        "Description": request.POST.get('description'),
        "Receipt": {
            "Email": payment.email,
            "Phone": "+7" + payment.phone,
            "EmailCompany": "chausmoscow@gmail.com",
            "Taxation": "usn_income",
            "FfdVersion": "1.2",
            "Items": [
                {
                    "Name": request.POST.get('description'),
                    "Price": int(str(this_event.price) + "00"),
                    "Quantity": 1.00,
                    "Amount": int(str(this_event.price) + "00"),
                    "PaymentMethod": "full_prepayment",
                    "PaymentObject": "commodity",
                    "Tax": "none",
                    "MeasurementUnit": "RUB"
                }
            ]
        }
    }

    payment_url = 'https://securepay.tinkoff.ru/v2/Init'

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(payment_url, json=payment_payload, headers=headers)
    if response.status_code == 200:
        payment_to_change = GuestList.objects.get(order_id=order_id)
        payment_to_change.status = response.json().get('Status')
        payment_to_change.amount = this_event.price
        payment_to_change.event = this_event
        payment_to_change.save()
        PaymentURL = response.json().get('PaymentURL')
        return HttpResponseRedirect(PaymentURL)

    else:
        # Payment request failed, handle the error gracefully
        error_message = response.json().get('error_message')
        return HttpResponse(f'Payment request failed: {error_message}')


def GuestAccept(request, order_id):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    payment = GuestList.objects.get(order_id=order_id)
    if payment:
        event = payment.event
        if event.data < now:
            GuestStatus = "Действителен"
        context = {

            'event_title': event.title, 'event_datatime': event.data.strftime("%d.%m %H:%M"),
            'event_place': event.place, 'amount': payment.amount, 'guest_name': payment.name,
            'order_id': payment.order_id,

        }
        return render(request, 'main/ticket.html', context)
    else:
        return render(request, 'main/ticket.html', {'NoFind': 'Билета не существует'})


def Order_ID_handler(request, order_id):
    payment = GuestList.objects.get(order_id=order_id)
    event = payment.event
    qr_data = 'https://chaus.moscow/api/v1/find/' + order_id
    print(payment.id)

    img = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=0,
        image_factory=qrcode.image.svg.SvgPathImage
    )

    img.add_data(qr_data)
    img.make(fit=True)
    img = img.make_image(attrib={'class': 'qr_code_ticket'})

    context = {
        'event_title': event.title, 'event_datatime': event.data.strftime("%d.%m %H:%M"), 'event_place': event.place,
        'amount': payment.amount, 'guest_name': payment.name,
        'event_guest': event.guest, 'event_timeDuration': event.timeDuration,
        'event_dress_style': event.dress_style,
        'order_id': payment.order_id,
        'payment_number': payment.id,
        'qr_code': img.to_string(encoding='unicode'),
    }
    return render(request, 'main/ticket.html', context)


# def generate_pdf(order_id):
#     config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
#     pdfkit.from_url('http://127.0.0.1:8000/api/v1/' + order_id, order_id + '.pdf', configuration=config)


@csrf_exempt
def TinkoffPayCallback(request):
    # Retrieve payment status and relevant data from the payment system's notification
    if request.method == 'POST':
        payment_data = json.loads(request.body)
        order_id = payment_data.get('OrderId')
        status = payment_data.get('Status')

        # Update payment status in your database based on the received data
        if status == "CONFIRMED":
            try:
                payment = GuestList.objects.get(order_id=order_id)
                payment.status = status

                # # sending email with ticket
                # guestMail = payment.email
                #
                # # html_content = render_to_string('main/mail_template.html',
                # #                                 {'ticket_link': 'https://chaus.moscow/api/v1/' + order_id})
                # text_content = 'Cсылка на билет: https://chaus.moscow/api/v1/' + order_id
                # subject = "Информация по билету"
                # from_email = settings.EMAIL_HOST_USER
                # to = guestMail
                # send_mail(subject, text_content, from_email, [to])
                # # email.attach_alternative(html_content, "text/html")
                # # email.send()

                payment.save()
            except GuestList.DoesNotExist:
                return JsonResponse({'message': 'Payment not found'}, status=404)
            # Handle any additional business logic based on the payment status

        return HttpResponse("OK", status=200)
    else:
        return HttpResponse(status=405)  # Method not allowed


def index(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    event_1 = Event.objects.filter(data__gt=now).order_by('data')[0]
    event_2 = Event.objects.filter(data__gt=now).order_by('data')[1]
    event_3 = Event.objects.filter(data__gt=now).order_by('data')[2]
    if len(Event.objects.filter(data__gt=now)) >= 4:
        event_4 = Event.objects.filter(data__gt=now).order_by('data')[3]
    else:
        event_4 = []
    event_1_oldprice = round(event_1.price * 100 / (100 - event_1.procents))
    event_2_oldprice = round(event_2.price * 100 / (100 - event_2.procents))
    event_3_oldprice = round(event_3.price * 100 / (100 - event_3.procents))
    links = lendingLinks.objects.get(id=1)
    photo_1 = Event.objects.filter(data__lt=now).order_by('-data')[0]
    print(photo_1)
    photo_2 = Event.objects.filter(data__lt=now).order_by('-data')[1]
    event_1_confirmed = len(GuestList.objects.filter(status="CONFIRMED", event=event_1))

    eventLinks = EventLinks.objects.all()

    return render(request, 'main/index.html',
                  {'event_1': event_1, 'event_1_oldprice': event_1_oldprice, 'event_2': event_2,
                   'event_2_oldprice': event_2_oldprice, 'event_3': event_3, 'event_3_oldprice': event_3_oldprice,
                   'event_4': event_4, 'photo_1': photo_1, 'photo_2': photo_2, 'eventLinks': eventLinks,
                   'links': links, 'event_1_confirmed': event_1_confirmed})


def rules(request):
    return render(request, 'main/rules.html')


def documents(request):
    doc = Docs.objects.all()
    return render(request, 'main/docs.html', {'doc': doc})


def contacts(request):
    return render(request, 'main/contacts.html')


def buy(request, id):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    event_1 = Event.objects.filter(data__gt=now).order_by('data')[id]
    event_1_confirmed = len(GuestList.objects.filter(status="CONFIRMED", event=event_1))
    event_1_id = event_1.id - 1
    # event_1_oldprice = round(event_1.price * 100 / (100 - event_1.procents))
    return render(request, 'main/buy.html', {'event_1': event_1, 'event_1_id': event_1_id, 'id': id, 'event_1_confirmed': event_1_confirmed})


def coop(request):
    jobs = Jobs.objects.all()
    return render(request, 'main/coop.html', {'jobs': jobs})


def partner(request):
    partner = Partner.objects.all()
    return render(request, 'main/partner.html', {'partner': partner})


def success(request):
    return render(request, 'main/buy__complete.html')


def fail(request):
    return render(request, 'main/buy__uncomplete.html')
