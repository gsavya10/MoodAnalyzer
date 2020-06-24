function validateForm() {
    var x = document.forms["myForm"]["expression"].value;
    if (x == "") {
        conditions.innerText = "Please tell us about your day!";
        return false;
    }
    console.log(x);
    return true;
}

document.getElementById("myVideo").playbackRate = 1;

//Speech recognition
var final_transcript = '';
        var recognizing = false;

        if ('webkitSpeechRecognition' in window) {

        var recognition = new webkitSpeechRecognition();

        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onstart = function() {
          recognizing = true;
        };

        recognition.onerror = function(event) {
          console.log(event.error);
        };

        recognition.onend = function() {
          recognizing = false;
        };

        recognition.onresult = function(event) {
          var interim_transcript = '';
          for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
              final_transcript += event.results[i][0].transcript;
            } else {
              interim_transcript += event.results[i][0].transcript;
            }
          }
          final_transcript = capitalize(final_transcript);
          // search.innerHTML = linebreak(final_transcript);
          search.value = final_transcript;
          // interim_span.innerHTML = linebreak(interim_transcript);

        };
        }

        var two_line = /\n\n/g;
        var one_line = /\n/g;
        function linebreak(s) {
        return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
        }

        function capitalize(s) {
        return s.replace(s.substr(0,1), function(m) { return m.toUpperCase(); });
        }

        function startDictation(event) {
        if (recognizing) {
          recognition.stop();
          return;
        }
        final_transcript = '';
        recognition.lang = 'en-US';
        recognition.start();
        // search.innerHTML = '';
        // interim_span.innerHTML = '';
        var input = document.getElementById('start_button');
        input.addEventListener('keydown',function(){
            recognition.stop();
            document.getElementById("myForm").submit();
            return;
        });
        }