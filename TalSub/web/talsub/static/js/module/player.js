/**
 * Created by Paul on 10/22/2014.
 *
 * This acts as an interface between interacting code and the
 * underlying audio player library.
 */

define(['jquery', 'jplayer'], function ($) {
    'use strict';
    function Player(selector) {
        if (!(this instanceof Player)) {
            throw new TypeError("Player constructor cannot be called as a function.");
        }

        this._player = $(selector);

        this._player.jPlayer({
            swfPath: '/static/js/lib/jplayer',
            supplied: 'mp3'
        });
    };

    Player.prototype = {
        constructor: Player
    };

    return Player;
});