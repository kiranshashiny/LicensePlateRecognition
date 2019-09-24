#!/usr/bin/python

import requests
import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
IMAGE_PATH = '20190831_095103.jpg'
IMAGE_PATH = 'vehicles_23_sep_2019/20190923_100343.jpg'

SECRET_KEY = 'sk_067..'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=in&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))
#data = json.load(r.json());
data  = json.dumps(r.json())
#
#
#
##with open('data.txt') as json_file:
#    #data = json.load(json_file)
##data_json = json.dumps ( data);
#
##print data["credits_monthly_total"]
##print data['img_width']
#print "Vehicle Plate     Number",
#print data['results'][0]['plate']
#print "Vehicle Plate Confidence",
#print data['results'][0]['confidence']
##print data['results'][0]['vehicle_region']['x']
##print data['results'][0]['vehicle_region']['y']
#
#print   "vehicle-> Orientation-> Confidence-> ",
#print data['results'][0]['vehicle']['orientation'][0]['confidence']
#
#print '***'	
#print   "vehicle-> Orientation-> Color ->name ",
#print data['results'][0]['vehicle']['color'][0]['name']
#print   "vehicle-> Orientation-> Color -> Confidence -> ",
#print data['results'][0]['vehicle']['color'][0]['confidence']
#
#print '****'
#print   "vehicle-> Orientation-> Make Name ",
#print data['results'][0]['vehicle']['make'][0]['name']
#print   "vehicle-> Orientation-> Make Conf ",
#print data['results'][0]['vehicle']['make'][0]['confidence']
#
#print '****'
#
#print   "vehicle-> Orientation-> Body Type-> Name ",
#print data['results'][0]['vehicle']['body_type'][0]['name']
#print   "vehicle-> Orientation-> Body Type-> Conf ",
#print data['results'][0]['vehicle']['body_type'][0]['confidence']
#
#print '****'
#
#print   "vehicle-> Orientation-> Year of Mfg -> Name ",
#print data['results'][0]['vehicle']['year'][0]['name']
#print   "vehicle-> Orientation-> Year of Mfg-> Conf ",
#print data['results'][0]['vehicle']['year'][0]['confidence']
#
#print '****'
#
#print   "vehicle-> Orientation-> MakeOfModel  -> Name ",
#print data['results'][0]['vehicle']['make_model'][0]['name']
#print   "vehicle-> Orientation-> MakeOfModel  -> Conf ",
#print data['results'][0]['vehicle']['make_model'][0]['confidence']
