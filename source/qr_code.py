#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import commands
import time
import datetime
import qrcode
import hashlib

# qr code file name
def qrcode_file_name(input_text):
    # create file name, time + qrcode content
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
    md5_string = hashlib.md5(input_text).hexdigest()
    return timestamp + '__' + md5_string + '.png'

# qr code file path
def qrcode_file_path(text):
    cmd = 'echo $TMPDIR'
    mac_temp_folder = commands.getstatusoutput(cmd)
    qr_code_folder = mkdir_qrcode_folder(mac_temp_folder[1] + 'alfred_qr_code/')
    return qr_code_folder + qrcode_file_name(text)


def mkdir_qrcode_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        return folder
    return folder

def create_qrcode(content, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    image = qr.make_image()
    image.save(file_path)

if __name__ == '__main__':
    input_text = sys.argv[1]
    file_path = qrcode_file_path(input_text)
    create_qrcode(input_text, file_path)

    preview_cmd = 'open'+' '+ '"' + file_path + '"'
    os.system(preview_cmd)