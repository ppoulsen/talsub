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
            player = new Player({
                player: '#jquery_jplayer_1',
                playlist: '#jp_container_1',
                episodeTitle: '#episode_title',
                episodeDate: '#episode_date',
                episodeSpeaker: '#episode_speaker',
                episodeRole: '#episode_role',
                subtitles: '#subtitles'
            });

            // Populate playlist with call to /episode_list?lang=en-US
            $.getJSON('/episode_list', {lang: 'en-US'}, function (list) {
                player.setPlaylist(list);
            });
        };

        // Initialize on page load
        $(function () {
            initialize();
        });
    }
);