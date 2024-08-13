# This is just a basic Python script to get started learning FFmpeg within Python
# May or may not include some basic UI elements, but more likely command based to begin

""" @echo off
for %%a in ("*.mkv*") do (
	ffmpeg -i "%%a" -map "0:m:language:eng" "newfiles\%%~na.eng.srt"
	ffmpeg -i "%%a" -map 0:v -c:v libx264 -preset slow -crf 20 -map 0:a -c:a aac -b:a 160k -vf format=yuv420p -movflags +faststart "newfiles\%%~na.mp4"
	)
pause """

import ffmpeg
import os

