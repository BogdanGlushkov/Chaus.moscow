from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rules', views.rules, name='rules'),
    path('contacts', views.contacts, name='contacts'),
    path('documents', views.documents, name='documents'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('coop', views.coop, name='coop'),
    path('partner', views.partner, name='partner'),
    path('success', views.success, name='success'),
    path('fail', views.fail, name='fail'),

    path('api/v1/TinkoffPayInit', views.TinkoffPayInit, name='TinkoffPayInit'),
    path('api/v1/TinkoffPayCallback', views.TinkoffPayCallback, name='TinkoffPayCallback'),
    path('api/v1/<str:order_id>', views.Order_ID_handler, name='order_id'),
    path('api/v1/find/<str:order_id>', views.GuestAccept, name='order_id')

]
