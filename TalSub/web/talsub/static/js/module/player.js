/**
 * Created by Paul on 10/22/2014.
 *
 * This acts as an interface between interacting code and the
 * underlying audio player library.
 */

define(['jquery', 'jplayer', 'jplaylist'], function ($) {
    'use strict';
    function Player(player, container, inspector) {
        if (!(this instanceof Player)) {
            throw new TypeError("Player constructor cannot be called as a function.");
        }

        // List of episodes
        this._episodes = [];
        // Temporarily fill like this:
        for (var i = 1; i <= 538; i++) {
            this._episodes.push({
                title: "Episode " + i,
                artist: "This American Life",
                mp3: "http://audio.thisamericanlife.org/jomamashouse/ismymamashouse/" + i + ".mp3"
            });
        }

        this._player = $(player);
        this._playlist = new jPlayerPlaylist({
                jPlayer: player,
                cssSelectorAncestor: container
            },
            this._episodes, {
                swfPath: '/static/js/lib/jplayer',
                supplied: 'mp3'
            });

        Player.prototype = {
            constructor: Player
        };
    }

    return Player;
});