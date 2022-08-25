@echo off
mkdir %appdata%\pdfMerge
copy .\src\pdfMerge.bat %appdata%\pdfMerge
copy .\src\pdfMerge.py %appdata%\pdfMerge
copy .\src\pdfMerge.lnk %appdata%\Microsoft\Windows\SendTo
pip install PyPDF2
start .\src\install.vbs