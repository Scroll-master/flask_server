# Flask Media Server

## Overview
This repository hosts a Flask-based media server that integrates FFplay from the FFmpeg suite for media playback. The server is designed to respond to network requests for playing, stopping, and querying the status of media files.

## Setup Instructions

### FFplay Installation
FFplay is essential for the media playback functionality of this server and is part of the FFmpeg suite. It must be installed separately:
- **Ubuntu:** Install FFmpeg, which includes FFplay, using:
  sudo apt update
  sudo apt install ffmpeg
- **Windows:** Download FFmpeg from the [official FFmpeg site](https://ffmpeg.org/download.html) and add the `bin` directory to your PATH.

### Server Installation
Clone this repository to your server machine:
  git clone https://github.com/yourusername/yourrepository.git
Navigate to the cloned directory and install Flask along with any other required packages using:
  pip install -r requirements.txt

## Usage

### Starting the Server
Launch the server with:
  flask run --host=0.0.0.0 --port=5000

### API Endpoints
- **Play Media:** POST to `/api/play` with `{'media_url': 'url_to_media'}` to start or change playback.
- **Stop Media:** POST to `/api/stop` to stop the current playback.
- **Check Status:** GET `/api/status` for current playback status.

### Integration with FFplay
The server utilizes Python's `subprocess` module to manage FFplay processes. For instance, when a request to play a new media file is received at `/api/play`, the server executes:
  subprocess.Popen(['ffplay', '-autoexit', 'media_url'])
The `-autoexit` option ensures that FFplay automatically exits after the media file has finished playing. The server manages ongoing media requests, allowing it to stop current playback or start new playback as needed based on the API requests it receives.

This streamlined setup allows the Flask server to efficiently handle media playback commands, utilizing FFplay's robust features.
