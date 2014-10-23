/**
 * Created by Paul on 10/22/2014.
 *
 * Main script for configuring index.html
 */

require(['jquery', 'module/player', 'bootstrap'],
    function ($, Player, boot) {
        'use strict';

        // Stores the Player variable for index.html
        var player;

        // Perform basic initialization tasks to setup index.html
        function initialize() {
            player = new Player('#jquery_jplayer_1', '#jp_container_1', '#jplayer_inspector_1');
        };

        // Initialize on page load
        $(function () {
            initialize();
        });
    }
);