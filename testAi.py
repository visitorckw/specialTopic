import requests as req
import cv2

import base64
import numpy as np


HOST = 'http://127.0.0.1:8080/ai'
obj = {
    'picture': ''
}

img = cv2.imread('test.jpg')
_, im_arr = cv2.imencode('.jpg', img)  # im_arr: image in Numpy one-dim array format.
im_bytes = im_arr.tobytes()
im_b64 = base64.b64encode(im_bytes)
pic = im_b64.decode('UTF-8')
obj['picture'] = pic

res = req.post(HOST + '/predict', data=obj)
print(res.text)
