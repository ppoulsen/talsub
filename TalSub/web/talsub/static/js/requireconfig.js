/**
 * Configuration file for requirejs modules.
 */

require.config({
    baseUrl: '/static/js',
    paths: {
        bootstrap: 'lib/bootstrap.min',
        jinspector: 'lib/jplayer/add-on/jquery.jplayer.inspector',
        jplayer: 'lib/jplayer/jquery.jplayer.min',
        jplaylist: 'lib/jplayer/add-on/jplayer.playlist.min',
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
        },
        'jplaylist': {
            deps: ['jquery', 'jplayer']
        }
    }
});
