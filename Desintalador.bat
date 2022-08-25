@echo off
@RD /S /Q %appdata%\pdfMerge
del /Q %appdata%\Microsoft\Windows\SendTo\pdfMerge.lnk
start .\src\uninstall.vbs