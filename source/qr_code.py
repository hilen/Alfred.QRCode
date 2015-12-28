#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qrcode
import sys
import os
import commands

input_text = sys.argv[1]
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(input_text)
qr.make(fit=True)

# get mac temp folder
cmd = 'echo $TMPDIR'
mac_temp_folder = commands.getstatusoutput(cmd)
qr_code_image_path = mac_temp_folder[1] + 'alfred_qr_image.png'

# save QRCode
img = qr.make_image()
img.save(qr_code_image_path)

open_cmd = 'open'+' '+ qr_code_image_path
os.system(open_cmd)
