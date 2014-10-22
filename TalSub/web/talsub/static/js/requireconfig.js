/**
 * Configuration file for requirejs modules.
 */

require.config({
    baseUrl: '/static/js',
    paths: {
        jquery: 'http://code.jquery.com/jquery',
        bootstrap: 'bootstrap.min'
    },
    shim: {
        'jquery.tmpl': ['jquery'],
        'jquery.validate': ['jquery'],
        'jquery-ui': ['jquery'],
        'jquery.slinky': ['jquery'],
        'bootstrap': [
            'jquery'
        ]
    }
});
