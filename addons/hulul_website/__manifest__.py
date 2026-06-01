{
    'name': 'Hulul Website',
    'version': '1.0',
    'depends': ['website'],

    'data': [
        'views/index.xml',
    ],

    'assets': {
        'web.assets_frontend': [

            # CSS Plugins
            'hulul_website/static/src/css/plugins/fontawesome.css',
            'hulul_website/static/src/css/plugins/magnific-popup.css',
            'hulul_website/static/src/css/plugins/metismenu.css',
            'hulul_website/static/src/css/plugins/odometer.css',
            'hulul_website/static/src/css/plugins/swiper.css',
            'hulul_website/static/src/css/plugins/timepickers.min.css',
            'hulul_website/static/src/css/plugins/unicons.css',

            # Main CSS
            'hulul_website/static/src/css/style.css',
            'hulul_website/static/src/css/style2c70.css',

            # JS Plugins
            'hulul_website/static/src/js/plugins/jquery-3.7.1.min.js',
            'hulul_website/static/src/js/plugins/bootstrap.min.js',
            'hulul_website/static/src/js/plugins/gsap.min.js',
            'hulul_website/static/src/js/plugins/magnific-popup.js',
            'hulul_website/static/src/js/plugins/metismenu.js',
            'hulul_website/static/src/js/plugins/odometer.js',
            'hulul_website/static/src/js/plugins/scroll-paralax.js',
            'hulul_website/static/src/js/plugins/scroll-to-plugins.js',
            'hulul_website/static/src/js/plugins/scrolltigger.js',
            'hulul_website/static/src/js/plugins/smooth-scroll.js',
            'hulul_website/static/src/js/plugins/split-text.js',
            'hulul_website/static/src/js/plugins/swiper.js',
            'hulul_website/static/src/js/plugins/vivus.js',

            # Main JS
            'hulul_website/static/src/js/main.js',
        ],
    },

    'installable': True,
    'application': True,
}