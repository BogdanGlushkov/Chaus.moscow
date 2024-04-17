$(function () {

    $('.header__btn-menu-mobile').click(function(){
        $('.menu ul').slideToggle();
        $('.menu_footer').hide();
    });

    $('.header__btn-menu').click(function(){
        $('.menu ul').slideToggle();
        $('.menu_footer').hide();
    });

    $('.header__btn-information').click(function(){
        $('.header__link__about_mobile').hide();
        $('.header__link__events_mobile').hide();
        $('.header__link').hide();
        $('.header__buyt-btn').hide();
        $('.header-top-280px').hide();
        $('.header__btn-menu-mobile').hide();
        $('.header__btn-menu-close').show();
        $('.menu_footer').show();
    });
    $('.header__btn-menu-close').click(function(){
        $('.header__link__about_mobile').show();
        $('.header__link__events_mobile').show();
        $('.header__link').show();
        $('.header__buyt-btn').show();
        $('.header-top-280px').show();
        $('.header__btn-menu-mobile').show();
        $('.header__btn-menu-close').hide();
        $('.menu_footer').hide();
    });

    $('.event__btn__block').slick({
        arrows: false,
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2500,
        speed: 1400,
        variableWidth: true,
        leftMode: true,
    });

    $('.vacancy__slider').slick({
        arrows: false,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: false,
        speed: 1400,
        leftMode: true,
    });

    $('.vacancy__slider__mobile').slick({
        arrows: false,
        slidesToShow: 1.5,
        slidesToScroll: 1,
        autoplay: false,
        speed: 500,
        rightMode: true,
    });

    $("#tabs").tabs();

    $(".desc__info__1").hide();
    $(".desc__info__2").hide();
    $(".desc__info__3").hide();
    
    $(".info__btn__1").click(function () {
        $(".events__description__1").hide();

        $(".desc__info__1").fadeIn(1000);
    });
    $(".event__description__info__back__1").click(function () {
        $(".desc__info__1").hide();

        $(".events__description__1").fadeIn(1000);
    });

    $(".info__btn__2").click(function () {
        $(".events__description__2").hide();

        $(".desc__info__2").fadeIn(1000);
    });
    $(".event__description__info__back__2").click(function () {
        $(".desc__info__2").hide();

        $(".events__description__2").fadeIn(1000);
    });

    $(".info__btn__3").click(function () {
        $(".events__description__3").hide();

        $(".desc__info__3").fadeIn(1000);
    });
    $(".event__description__info__back__3").click(function () {
        $(".desc__info__3").hide();

        $(".events__description__3").fadeIn(1000);
    });

    
    $(".block-1").fadeOut(1);
    $(".block-2").fadeOut(1);
    $(".block-3").fadeOut(1);
    $(".block-4").fadeOut(1);
    $(".block-5").fadeOut(1);
    $(".block-6").fadeOut(1);
    $(".btn__back").fadeOut(1);

    $(".msg__btn__1").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-1").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__2").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-2").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__3").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-3").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__4").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-4").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__5").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-5").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__6").click(function () {
        $(".msg__btn__1").fadeOut(1);
        $(".msg__btn__2").fadeOut(1);
        $(".msg__btn__3").fadeOut(1);
        $(".msg__btn__4").fadeOut(1);
        $(".msg__btn__5").fadeOut(1);
        $(".msg__btn__6").fadeOut(1);

        $(".block-6").fadeIn(100);
        $(".msg__btn__back").fadeIn(100);
    });
    $(".msg__btn__back").click(function () {
        $(".block-1").fadeOut(1);
        $(".block-2").fadeOut(1);
        $(".block-3").fadeOut(1);
        $(".block-4").fadeOut(1);
        $(".block-5").fadeOut(1);
        $(".block-6").fadeOut(1);
        $(".msg__btn__back").fadeOut(1);

        $(".msg__btn__1").fadeIn(100);
        $(".msg__btn__2").fadeIn(100);
        $(".msg__btn__3").fadeIn(100);
        $(".msg__btn__4").fadeIn(100);
        $(".msg__btn__5").fadeIn(100);
        $(".msg__btn__6").fadeIn(100);
    });

    $(".advantages__icon__text__1").hide();
    $(".advantages__icon__text__2").hide();
    $(".advantages__icon__text__3").hide();
    $(".advantages__icon__text__4").hide();

    $(document).ready(function () {
        $(".advantages__icon__1").hover(function () {
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__1").show(0);
        },
            function () {
                $(".advantages__icon__text__1").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__2").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__2").show(0);
        },
            function () {
                $(".advantages__icon__text__2").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__3").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__4").hide();
            $(".advantages__icon__text__3").show(0);
        },
            function () {
                $(".advantages__icon__text__3").hide();
            });
    });

    $(document).ready(function () {
        $(".advantages__icon__4").hover(function () {
            $(".advantages__icon__text__1").hide();
            $(".advantages__icon__text__2").hide();
            $(".advantages__icon__text__3").hide();
            $(".advantages__icon__text__4").show(0);
        },
            function () {
                $(".advantages__icon__text__4").hide();
            });
    });

    $('.buy__our__tickets__slider').slick({
        prevArrow:'<button type="button" class="slick__btn slick__prev"><img class="arrow__left" src="img/arrow-buy-ticket.svg" alt=""></button>',
        nextArrow:'<button type="button" class="slick__btn slick__next"><img class="arrow__right" src="img/arrow-buy-ticket.svg" alt=""></button>',

        dots: true,
        infinite: false,
        speed: 500,
    });

});

function scrollTo(element) {
    window.scroll({
    left: 0,
    top: element.offsetTop - 40,
    behavior: 'smooth'
    })
}

var button_about = document.querySelector('.header__link__about_mobile ');
var button_events = document.querySelector('.header__link__events_mobile ');
var button_about_tablet = document.querySelector('.header__link__about');
var button_events_tablet = document.querySelector('.header__link__events');
var button_buy = document.querySelector('.hello_buyt-btn');
var button_photo = document.querySelector('.hello__photo-btn');

var about = document.querySelector('#about');
var events = document.querySelector('#events');
var buy = document.querySelector('#buy');
var photo = document.querySelector('#photo');

button_about.addEventListener('click', () => {
    $('.menu ul').hide();
    scrollTo(about);
})

button_events.addEventListener('click', () => {
    $('.menu ul').hide();
    scrollTo(events);
})
button_about_tablet.addEventListener('click', () => {
    scrollTo(about);
})

button_events_tablet.addEventListener('click', () => {
    scrollTo(events);
})

button_buy.addEventListener('click', () => {
    scrollTo(buy);
})

button_photo.addEventListener('click', () => {
    scrollTo(photo);
})