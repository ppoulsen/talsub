/**
 * Configuration file for requirejs modules.
 */

require.config({
    baseUrl: '/static/js',
    paths: {
        bootstrap: 'lib/bootstrap.min',
        jplayer: 'lib/jplayer/jquery.jplayer.min',
        jquery: 'http://code.jquery.com/jquery',
        lib: 'lib',
        module: 'module',
        page: 'page'
    },
    shim: {
        'bootstrap': {
            deps: ['jquery']
        },
        'jplayer': {
            deps: ['jquery']
        }
    }
});
