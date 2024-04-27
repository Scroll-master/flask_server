Flask Server for Media Playback
Overview

This repository contains a Flask application designed to serve as a media player server utilizing FFplay from the FFmpeg suite to execute media playback commands. The server is structured to receive and handle API calls for playing, stopping, and checking the status of media files.
Installation and Setup

First, ensure that FFplay is installed on your device as it is necessary for media playback. FFplay is not included with Python and must be installed separately. For Ubuntu systems, you can install FFmpeg, which includes FFplay, using sudo apt update followed by sudo apt install ffmpeg. For Windows, download the latest FFmpeg builds from the FFmpeg Official Site and ensure the bin directory containing FFplay is added to your system's PATH.

After setting up FFplay, clone this repository to your device where the server will run using the command git clone https://github.com/yourusername/yourrepository.git. Navigate to the project directory, and install Flask using the requirements file with pip install -r requirements.txt.
Usage

To start the server, execute the command flask run --host=0.0.0.0 --port=5000 within the project directory. The server offers several API endpoints:

    To start or change media playback, make a POST request to /api/play with a JSON payload containing 'media_url'.
    To stop media playback, make a POST request to /api/stop.
    To get the current status of media playback, make a GET request to /api/status.

The Flask application uses Python's subprocess module to invoke ffplay for media playback. For example, to play a new media file received through the /api/play endpoint, the application executes subprocess.Popen(['ffplay', '-autoexit', media_url]). The -autoexit flag tells FFplay to exit after the media has finished playing, allowing the application to handle new media requests by either stopping current playback or starting new playback based on the received media URL.

This setup ensures that all media playback is handled efficiently, leveraging FFplay's capabilities through subprocess calls initiated by Flask's web server capabilities.
