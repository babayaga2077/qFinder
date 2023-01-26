//webkitURL is deprecated but nevertheless
$( document ).ready(function() {
    console.log( "ready!" );
    URL = window.URL || window.webkitURL;

	var gumStream; 						//stream from getUserMedia()
	var rec; 							//Recorder.js object
	var input; 							//MediaStreamAudioSourceNode we'll be recording

	// shim for AudioContext when it's not avb. 
	var AudioContext = window.AudioContext || window.webkitAudioContext;
	var audioContext //audio context to help us record

	var recordButton = document.getElementById("recordButton");
	var stopButton = document.getElementById("stopButton");
	if (recordButton && stopButton) {
		recordButton.addEventListener("click", startRecording);
		stopButton.addEventListener("click", stopRecording);
	}
	//add events to those 2 buttons
	
	$("#fileToUpload").change(function() {
  	uploadWAV();
  	});
  	$("#ImgToUpload").change(function() {
  	uploadImg(this.files[0]);
  	});
  	

});

function startRecording() {
	document.getElementById('robot').src="/static/images/front.png"
	var res = document.getElementById('res');
	res.innerHTML='';
	/*
		Simple constraints object, for more advanced audio features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/
    
    var constraints = { audio: true, video:false }

 	/*
    	Disable the record button until we get a success or fail from getUserMedia() 
	*/

	recordButton.style ='display:none';
	stopButton.style='display:inline-block';

	/*
    	We're using the standard promise based getUserMedia() 
    	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
	*/

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {

		/*
			create an audio context after getUserMedia is called
			sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
			the sampleRate defaults to the one set in your OS for your playback device

		*/
		audioContext = new AudioContext();

		//update the format 
		/*  assign to gumStream for later use  */
		gumStream = stream;
		
		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);

		/* 
			Create the Recorder object and configure to record mono sound (1 channel)
			Recording 2 channels  will double the file size
		*/
		rec = new Recorder(input,{numChannels:1})

		//start the recording process
		rec.record()


	}).catch(function(err) {
		console.log(err);
	  	//enable the record button if getUserMedia() fails
    	recordButton.style = 'display:inline-block';
    	stopButton.style='display:none';

	});
}


function stopRecording() {
	document.getElementById('robot').src="/static/images/side.png"
	var preloader = document.getElementById("preloader");
	//disable the stop button, enable the record too allow for new recordings
	stopButton.style = 'display:none';
	recordButton.style = 'display:inline-block';
	preloader.style = 'display:block';

	//reset button just in case the recording is stopped while paused
	
	//tell the recorder to stop the recording
	rec.stop();

	//stop microphone access
	gumStream.getAudioTracks()[0].stop();

	//create the wav blob and pass it on to createDownloadLink
	rec.exportWAV(saveWAV);
}

function saveWAV(blob) {
  var res = document.getElementById('res');
  var preloader = document.getElementById("preloader");
  var xhr=new XMLHttpRequest();
  xhr.onload=function(e) {
      if(this.readyState === 4) {
      	preloader.style = 'display:none';
      	res.innerHTML=e.target.responseText;
      }
  };

  var fd=new FormData();
  fd.append("audio_data",blob);
  xhr.open("POST","upload",true);
  xhr.send(fd);

}

function  uploadWAV(){
	var res = document.getElementById('res');
	var up = document.getElementById("fileToUpload");
	var preloader = document.getElementById("preloader");
	preloader.style = 'display:block';
	res.innerHTML='';
	if (up.files && up.files[0]) {
	saveWAV(up.files[0]);
	}
	else{
		res.innerHTML='No file selected';
	}
}

function  uploadImg(blob){
	var res = document.getElementById('res');
	var xhr=new XMLHttpRequest();
	  xhr.onload=function(e) {
	      if(this.readyState === 4) {
	      	response=e.target.responseText;
	      	if (response==='True'){
	      		document.location='/login'
	      	}
	      	else{
	      	res.innerHTML=e.target.responseText;
	      	}
	      }
	  };
	  var fd=new FormData();
	  fd.append("img_data",blob);
	  xhr.open("POST","login",true);
	  xhr.send(fd);

}

function enableWebcam(){
	document.getElementById("webcam").style='display:block';
	document.getElementById("login").style='display:none';	
	Webcam.set({
			width: 640,
			height: 480,
			image_format: 'jpeg',
			jpeg_quality: 100
		});
		Webcam.on( 'error', function(err) {
			document.getElementById("webcam").style='display:none';
			document.getElementById("login").style='display:block';
    		return alert(err);
		} );
		Webcam.attach( '#my_camera' );


}

function take_snapshot() {
			// take snapshot and get image data
			Webcam.snap( function(data_uri) {
				// display results in page
				document.getElementById("webcam").style='display:none';
				document.getElementById("login").style='display:block';
				uploadImg(dataURLtoBlob(data_uri));
				Webcam.reset()
			} );
}
function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type:mime});
}