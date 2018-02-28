(function ($) {
    jQuery(document).ready(function () {
        $('.button-collapse').sideNav();
        $('.parallax').parallax();
        $('.slick-dots').slick({
            dots: true,
            prevArrow: $('.prev'),
            nextArrow: $('.next'),
            infinite: false,
            speed: 300,
            slidesToShow: 4,
            slidesToScroll: 4,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 3,
                        infinite: true,
                        dots: true
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
        });

        /*var k = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65],
            n = 0;
        $(document).keydown(function (e) {
            if (e.keyCode === k[n++]) {
                if (n === k.length) {
                    $('.logo img').attr('src', '');
                    n = 0;
                    return false;
                }
            }
            else {
                n = 0;
            }
        });*/

        $(window).scroll(function () {
            if ($(this).scrollTop() >100) {
                $('.totop').removeClass('scale-out').addClass('scale-in');
            } else {
                $('.totop').removeClass('scale-in').addClass('scale-out');
            }
        });

        $('a').click(function(e){
            $('html, body').animate({
                scrollTop: $( $(this).attr('href') ).offset().top
            }, 800);

            e.preventDefault();
        })
    });

    function initialize() {
        var coordinates = ['La Grappe', '50.6307514', '3.055959,17', '<h4>La Grappe</h4><p>75, rue Léon Gambetta<br>59000 Lille</p><p>Métro | Bus | V’Lille : République Beaux-Arts</p>'];
        var grappe = new google.maps.LatLng(parseFloat(coordinates[1]), parseFloat(coordinates[2]));

        var map = new google.maps.Map(
            document.getElementById('map_djangocong'), {
                center: grappe,
                zoom: 11,
            }
        );

        var marker = new google.maps.Marker({
            position: grappe,
            map: map,
            title: coordinates[0],
        });

        var content = coordinates[3];
        var infowindow = new google.maps.InfoWindow();

        google.maps.event.addListener(marker, 'click', (function (marker, content, infowindow) {
            return function () {
                infowindow.setContent(content);
                infowindow.open(map, marker);
            };
        })(marker, content, infowindow));

        google.maps.event.addListener(marker, 'click', (function (marker, content, infowindow) {
            return function () {
                infowindow.setContent(content);
                infowindow.open(map, marker);
            };
        })(marker, content, infowindow));

    }

    google.maps.event.addDomListener(window, 'load', initialize);
})(jQuery);