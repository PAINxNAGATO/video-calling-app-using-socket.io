document.getElementById("connectButton").addEventListener("click", function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/connect-to-server", true);
    xhr.send();
});

// Update video element source when receiving video data
var videoElement = document.getElementById('videoElement');
var mediaSource = new MediaSource();
videoElement.src = URL.createObjectURL(mediaSource);

mediaSource.addEventListener('sourceopen', function() {
    var sourceBuffer = mediaSource.addSourceBuffer('video/mp4; codecs="avc1.42E01E"');
    var buffer = [];
    var currentData = 0;

    sourceBuffer.addEventListener('updateend', function() {
        if (buffer.length > 0 && !sourceBuffer.updating) {
            sourceBuffer.appendBuffer(buffer.shift());
        }
    });

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/video-stream', true);
    xhr.responseType = 'arraybuffer';

    xhr.onload = function() {
        buffer.push(new Uint8Array(xhr.response));
        if (!sourceBuffer.updating) {
            sourceBuffer.appendBuffer(buffer.shift());
        }
    };

    xhr.send();
});
