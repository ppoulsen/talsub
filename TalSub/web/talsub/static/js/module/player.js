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

        this._player = $(player);
        this._playlist = new jPlayerPlaylist({
                jPlayer: player,
                cssSelectorAncestor: container
            },
            this._episodes, {
                swfPath: '/static/js/lib/jplayer',
                supplied: 'mp3'
            });
    }

    Player.prototype = {
        constructor: Player,

        /**
         * Clear the playlist and update with the new episode_list
         */
        setPlaylist: function (episode_list) {
            this._episodes = [];
            var player = this;
            $.each(episode_list, function (index, value) {
                player._episodes.push({
                    title: "#" + value.number + " " + value.title,
                    artist: "This American Life",
                    mp3: value.audio
                });
            });
            this._playlist.setPlaylist(this._episodes);
        }
    };

    return Player;
});