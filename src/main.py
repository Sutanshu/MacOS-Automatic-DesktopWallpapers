from google_images_download import google_images_download 
from api import weather
import applescript 
from appscript import app, mactypes
import os
import subprocess
from subprocess import Popen, PIPE


response = google_images_download.googleimagesdownload()
keywords = "wallpaper of "+weather.getWeather()
args = {
    "keywords": keywords,
    "limit": 1,
    "print_urls":True,
}

a = response.download(args)[0][keywords][0]


scpt = 'tell application "Finder" to set desktop picture to POSIX file "{}"'.format(a).encode()

p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt)

