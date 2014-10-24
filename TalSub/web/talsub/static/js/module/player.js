/**
 * Created by Paul on 10/22/2014.
 *
 * This acts as an interface between interacting code and the
 * underlying audio player library.
 */

/**
 * Define the class Player for requirejs
 */
define(['jquery', 'jplayer', 'jplaylist'], function ($) {
    'use strict';

    /**
     * Constructor for the Player class
     * @param options dictionary containing selectors for:
     * {
     *   player: 'selector-for-jplayer-div',
     *   container: 'selector-for-container-div-for-playlist',
     *   episodeTitle: 'selector-for-episode-title',
     *   episodeDate: 'selector-for-episode-date',
     *   episodeSpeaker: 'selector-for-speaker',
     *   episodeRole: 'selector-for-role',
     *   subtitles: 'selector for subtitles',
     * }
     * @constructor
     */
    function Player(options) {
        if (!(this instanceof Player)) {
            throw new TypeError("Player constructor cannot be called as a function.");
        }

        // Save this for use in callback functions within this constructor
        var this_player = this;

        // Store in temporary variables, will initialize later
        var player = options.player;
        var container = options.container;

        // Store these for performing subtitles updates
        this.episodeTitle = $(options.episodeTitle);
        this.episodeDate = $(options.episodeDate);
        this.episodeSpeaker = $(options.episodeSpeaker);
        this.episodeRole = $(options.episodeRole);
        this.subtitles = $(options.subtitles);

        // List of episodes
        this._episodes = [];

        // Initialize player and empty playlist
        // Playlist is populated by setPlaylist
        this._player = $(player);
        this._playlist = new jPlayerPlaylist({
                jPlayer: player,
                cssSelectorAncestor: container
            },
            this._episodes, {
                swfPath: '/static/js/lib/jplayer',
                supplied: 'mp3'
            });

        // Event Handlers
        /**
         * Called at start and when user sets a new episode
         * @param event Bears the url of the media being played, from which we can intuit the episode
         */
        function newEpisodeHandler(event) {
            // Find out what episode is selected by taking it from the media URL
            var url = event.jPlayer.status.src;
            var filename = url.substring(url.lastIndexOf('/') + 1);
            var number = filename.substring(0, filename.lastIndexOf('.'));

            // Set the transcript
            $.getJSON('/transcript/', {lang: 'en-US', episode: number}, function (transcript) {
                this_player._transcript = transcript;
                this_player.episodeTitle.text('#' + transcript.number + ' ' + transcript.title);
                this_player.episodeDate.text(transcript.date);
            });
        }

        /**
         * Update subtitles based on current time
         * @param event Event bearing current time in seconds
         */
        function timeUpdateHandler(event) {
            if (!this_player || !this_player._transcript) {
                return;
            }

            var time = event.jPlayer.status.currentTime;

            // First, loop through subtitles until we find last before this time
            // Do this by looping through each subtitle in an act, and then each act in the transcript

            // The transcript for this language
            var t = this_player._transcript.transcripts[0];

            // Current act being searched and its index
            var act = t.acts[0];
            var act_index = 0;

            // Current sub being searched and its index
            var sub = act.subtitles[0];
            var sub_index = 0;

            // The preceding sub. Keep track of this, so that when sub is > time, we can display the previous
            var previous_sub = sub;
            while (sub.time < time) {
                sub_index++;
                previous_sub = sub;

                // If out of subs for this act, proceed to next act
                if (sub_index >= act.subtitles.length) {
                    act_index++;
                    // If out of acts, break, returning the last subtitle in transcript
                    if (act_index >= t.acts.length) {
                        break;
                    }

                    // Otherwise, move to next act and set sub to first subtitle in it
                    act = t.acts[act_index];
                    sub = act.subtitles[0];
                    sub_index = 0;
                } else {
                    // Set sub to next subtitle in act
                    sub = act.subtitles[sub_index];
                }
            }

            // previous_sub is now the last subtitle before current time
            // Set fields accordingly
            this_player.episodeSpeaker.text(previous_sub.speaker);
            this_player.episodeRole.text(previous_sub.role);
            this_player.subtitles.text(previous_sub.paragraph);
        }

        // Bind to setmedia to capture new episode changes
        this._player.bind($.jPlayer.event.setmedia, function (event) {
            newEpisodeHandler(event);
        });

        // Bind to timeupdate so we can update subtitles
        this._player.bind($.jPlayer.event.timeupdate, function (event) {
            timeUpdateHandler(event);
        });
    }

    Player.prototype = {
        constructor: Player,

        /**
         * Clear the playlist and update with the new episode_list
         * @param episode_list: JSON list of dictionaries with members: number, title, and audio (the mp3 URL)
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