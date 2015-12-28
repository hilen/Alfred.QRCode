![Alfred.QRCode](./icon.png)

Alfred.QRCode
======================

A QRcode generator based on [python-qrcode](https://github.com/lincolnloop/python-qrcode) for Alfred Workflows.

##Install Python library:
1. Install the image library [pillow](https://pypi.python.org/pypi/Pillow)
```
sudo pip install pillow
```
2. Install [python-qrcode](https://github.com/lincolnloop/python-qrcode)
```
sudo easy_install python-qrcode
```

##Usage:
1. Type `qr text`;
2. Define a hotkey, select some text, press the hotkey;

##Output:
1. The QRCode image your generate will be open with Preview application.
![demo](./demo.png)
2. You can find the recently QRCode image path by this command in ternimal:
```
echo $TMPDIR'alfred_qr_image.png'
```

