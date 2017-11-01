<%@ Page Title="Problem One" Language="C#"  MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ProblemOne.aspx.cs" Inherits="Nico.ProblemOne" %>


<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">


    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
        tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
        });
    </script>
    <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>

    <div class="container">
        <br />
         
        <br />
        <br />

        <div id="wait" style="display:none;width:69px;height:89px;border:1px solid black;position:absolute;top:50%;left:50%;padding:2px;"><img src='../Content/img/ajax-loader.gif' width="64" height="64" /><br></div>
        <h3>What is Nico's Problem?</h3>
                <br />
        <h4 class="centered">Nico's friend Lunara is running a race. Lunara runs at a constant speed and Nico wants to meet her at different points and times along the race route. To do this, Nico needs to figure out where and when to meet Lunara. Help Nico by filling in the blank spots in the below table.</h4>
        <br />
        <div id="microphone" style="display:none;text-align:center"><button id="start_button1" onclick ="startButton('start_img1');return false;"><img id="start_img1" src ="../Content/img/mic.gif" alt="Start" /></button></div>


       <h3 >Nico needs to fill in this table. Help Nico by explaining what to do.</h3> 
         <br />
        <div><img id="problem" src ="../Content/img/problem_one/StepOne.png"/></div>

        <br />
        <div style="text-align:center;">
          <h4><asp:LinkButton ID="ProblemOne_Nico" Text="Next Problem"  OnClick="Nico_Turn" runat="server" style="color:hsl(0, 0%, 30%)" Visible="false"/></h4>
        </div>
        <br />
                <div class="progress progress-striped">          
            <div class="progress-bar progress-bar-success" style="width: 20%">20% Complete</div>
        </div>
        <br />
        <br />
        <br />
        <br />

        <div>
        <h2>Log</h2>
        <pre id="log"></pre>
        </div>

        <br />

    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js" type="text/javascript"></script>
    <script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="../js/jquery.signalR-2.0.0.min.js"></script>
    <script src="../js/talk.js"></script>
    <script src="../js/audio.js"></script>  
    <script src="../js/recorder.js"></script>


    <script type="text/javascript">
      
        // Variables for recording
        var recorder;
        var input;
        var audio_context;

        // Variables for ASR
        var final_transcript = '';
        var ignore_onend;
        var start_timestamp;
        var recognition = new webkitSpeechRecognition();
        var recognizing = false;
        var firstTime = true;
        
        // Initialize recognition object values
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 6;


        // space bar down to start recognizing
        document.body.onkeydown = function (e) {
            if (!(recognizing)) {
                if (e.keyCode == 32) {
                    recognizing = true;
                    e.preventDefault();
                    __log("down - start recognizing");
                    startRecording();
                }
                
            }
         }

        // space bar up to stop recognizing
        document.body.onkeyup = function(e){
            if(e.keyCode == 32){
                recognizing = false;
                e.preventDefault();
                __log("on up");
                stopRecording(sendTranscript);
            }
        }

        // check if microphone is connected and if it can be used as a media stream
        function startUserMedia(stream) {
            var input = audio_context.createMediaStreamSource(stream);
            __log('Media stream created.');
            recorder = new Recorder(input);
            __log('Recorder initialised.');
        }

        // start recording the user's voice upon button push
        function startRecording() {
            recorder && recorder.record();
            __log('Calling START record');

            // reset ASR variables
            final_transcript = '';
            recognition.start();
            ignore_onend = false;
            start_timestamp = event.timeStamp;

            // begin ASR
            recognition.onstart = function () {
                recognizing = true;
                __log('Starting ASR');

            };

            recognition.onerror = function (event) {
                if (event.error == 'no-speech') {
                    __log('No speech was detectable');
                    ignore_onend = true;
                }
                if (event.error == 'audio-capture') {
                    __log('No microphone available');
                    ignore_onend = true;
                }
                if (event.error == 'not-allowed') {
                    if (event.timeStamp - start_timestamp < 100) {
                        __log('Time stamp issue');
                    } else {
                        __log('Other Not Allowed Issue');
                    }
                    ignore_onend = true;
                }
            }

            ignore_onend = false;
            start_timestamp = event.timeStamp
        }

        // function to stop recording users voice when they push the "STOP" button
        //UPDATE: Change stoprecording to no callback. Change send final transcript to 'update display' with callback
        function stopRecording(callback) {
            recorder && recorder.stop();
            __log('Calling STOP record.');


            // function to happen when recognition ends
            recognition.onend = function () {
                recognizing = false;
                if (ignore_onend) {
                    return;
                }
                if (!final_transcript) {
                    __log('No final transcript!!!');
                    return;
                }
            };

            // function to happen when recognition completes
            recognition.onresult = function (event) {
            
                for (var i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        final_transcript += event.results[i][0].transcript;
                    }
                }
                
                __log("Final Transcript posted");
                if (final_transcript) {
                    //results.innerHTML = results.innerHTML + "<br />" + final_transcript;
                    __log(final_transcript);
                    callback(final_transcript);
                }
            };

            // create WAV download link using audio captured as a blob
            createDownloadLink(sendBlob);
            recorder.clear();
        }

        // function to save response to server
        function sendBlob(blob) {
            if (object.sendToServer) {
                var url1 = (window.url || window.webkitURL);
                //__log(url1);
                var url = url1.createObjectURL(blob);

                var li = document.createElement('li');
                var au = document.createElement('audio');
                var hf = document.createElement('a');

                au.controls = true;
                au.src = url;
                hf.href = url;
                hf.download = new Date().toISOString() + '.wav';
                hf.innerHTML = hf.download;

                var data = new FormData();
                data.append('lib', blob);

                $(document).ajaxStart(function () {
                    $("#wait").css("display", "block");
                });

                $(document).ajaxStop(function () {
                    $("#wait").css("display", "none");
                });

                __log("Calling SAVE");
                $.ajax({
                    url: "../handlers/saveWav.ashx",
                    type: 'POST',
                    data: data,
                    contentType: false,
                    processData: false,
                    success: function (result) { __log(result); },
                    error: function (err) {
                        alert(err.statusText)
                    }
                });

            }
        }

        // still a part of saving response to server
        function createDownloadLink(callback) {
            recorder && recorder.exportWAV(function (blob) {
                object = new Object();
                object.sendToServer = true;
                callback(blob);
            });
        }

        function updateDisplay(callback) {
            callback(final_transcript);
            __log('calling update trans on page load');
        }

        function sendTranscript(final_transcript){
            __log("Calling Transcript Save");
            $.ajax({
                url: "../handlers/saveTranscript.ashx",
                type: 'POST',
                data: final_transcript,
                success: function (result) {
                    __log(result);
                    $('#problem').attr('src', result);
                },
                error: function (err) {
                    alert(err.statusText)
                }
            });
        }

        

        // Window loading initializations
        window.onload = function init() {
            try {
                window.AudioContext = window.AudioContext || window.webkitAudioContext;
                navigator.getUserMedia = (navigator.getUserMedia || navigator.webkitGetUserMedia);
                window.URL = (window.URL || window.webkitURL);

                audio_context = new AudioContext;
                __log('Audio context set up.');
                __log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));

                if (!('webkitSpeechRecognition' in window)) {
                    upgrade();
                }
            }
            catch (e) { alert('No web audio support in this browser!'); }

            if (navigator.getUserMedia) {
                navigator.getUserMedia({audio: true},

                    // successCallback
                    function (stream) {
                        input = audio_context.createMediaStreamSource(stream);
                        __log('Media stream created.');
                        recorder = new Recorder(input);
                        __log('Recorder initialised.');
                        recording = false;
                    },

                    // errorCallback
                    function (err) {console.log("The following error occured: " + err); }
                );
            } else {
                __log('getUserMedia not supported');
            }

            updateDisplay(sendTranscript);

        }

        // function for writing data to window
        function __log(e, data) {
            log.innerHTML += "\n" + e + " " + (data || '');
        }

        // response if need to upgrade window
        function upgrade() {
            __log('info_upgrade');
        }

    </script>

</asp:Content>