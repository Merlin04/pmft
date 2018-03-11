setx PYTHONHOME c:\Python27
setx PYTHONPATH c:\Python27\Lib
pip install pyserial
mkdir C:\avrdude-pmft
copy "C:\Program Files (x86)\pmft\avrdude-pmft.exe" C:\avrdude-pmft\avrdude-pmft.exe
copy "C:\Program Files (x86)\pmft\avrdude-pmft.conf" C:\avrdude-pmft\avrdude-pmft.conf
copy "C:\Program Files (x86)\pmft\libusb0.dll" C:\avrdude-pmft\libusb0.dll