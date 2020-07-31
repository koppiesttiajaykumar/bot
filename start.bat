@echo off
TITLE TGbot
py -3.7 --version
IF "%ERRORLEVEL%" == "0" (
    py -3.7 -m bot
) ELSE (
    py -m bot
)