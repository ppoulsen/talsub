/**
 * Created by Paul on 10/22/2014.
 *
 * This acts as an interface between interacting code and the
 * underlying audio player library.
 */

define(['jquery', 'jplayer', 'jplaylist'], function ($) {
    'use strict';
    function Player(options) {
        if (!(this instanceof Player)) {
            throw new TypeError("Player constructor cannot be called as a function.");
        }
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
            var filename = url.substring(url.lastIndexOf('/')+1);
            var number = filename.substring(0, filename.lastIndexOf('.'));

            // Set the transcript
            $.getJSON('/transcript/', {lang: 'en-US', episode: number}, function(transcript){
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
            var t = this_player._transcript.transcripts[0];
            var act = t.acts[0];
            var act_index = 0;
            var sub = act.subtitles[0];
            var sub_index = 0;
            var previous_sub = sub;
            while (sub.time < time) {
                sub_index++;
                previous_sub = sub;
                if (sub_index >= act.subtitles.length) {
                    act_index++;
                    if (act_index >= t.acts.length) {
                        break;
                    }
                    act = t.acts[act_index];
                    sub = act.subtitles[0];
                    sub_index = 0;
                } else {
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
        this._player.bind($.jPlayer.event.setmedia, function(event) {
            newEpisodeHandler(event);
        });

        // Bind to timeupdate so we can update subtitles
        this._player.bind($.jPlayer.event.timeupdate, function(event) {
            timeUpdateHandler(event);
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