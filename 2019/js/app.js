(function ($) {
    jQuery(document).ready(function () {
        $('.button-collapse').sideNav();
        $('.parallax').parallax();
        $('.slick').slick({
            dots: true,
            adaptiveHeight: true,
            autoplay: true,
            autoplaySpeed: 2000,
            prevArrow: $('.prev'),
            nextArrow: $('.next'),
            infinite: true,
            speed: 300,
            slidesToShow: 3,
            slidesToScroll: 3,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2,
                        infinite: true,
                        dots: true
                    }
                },
                {
                    breakpoint: 620,
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

        var k = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65],
            n = 0;
        $(document).keydown(function (e) {
            if (e.keyCode === k[n++]) {
                if (n === k.length) {
                    var pony = $('<img class="pony" src="images/pony.png">');
                    $("#index-banner").append(pony);
                    pony.animate(
                        {left: "100%", bottom: "300px"},
                        {
                            easing: "linear",
                            duration: 1000,
                            complete: function(){pony.remove()}
                        });
                    n = 0;
                    return false;
                }
            }
            else {
                n = 0;
            }
        });

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
})(jQuery);


// Leaflet
var map = L.map('map_djangocong').setView([50.6307514, 3.0581], 12);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
L.marker([50.6307514, 3.0581]).addTo(map)
    .bindPopup('<h4>La Grappe</h4><p>75, rue Léon Gambetta<br>59000 Lille</p><p>Métro | Bus | V’Lille : République Beaux-Arts</p>')
