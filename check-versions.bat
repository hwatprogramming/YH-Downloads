@echo off
rem Checks every app's versions list (like yt-music-downloader\versions.js) against
rem the files on GitHub, and says what's missing. Double-click it after an upload.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0check-versions.ps1"
pause
