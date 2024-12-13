import pyqrcode
url='https://www.instagram.com/naveen__sathiyamoorthy__?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=4)