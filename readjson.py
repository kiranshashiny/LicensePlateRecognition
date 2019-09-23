import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    data_json = json.dumps ( data);
    
    #print data["credits_monthly_total"]
    #print data['img_width']
    print "Vehicle Plate     Number",
    print data['results'][0]['plate']
    print "Vehicle Plate Confidence",
    print data['results'][0]['confidence']
    #print data['results'][0]['vehicle_region']['x']
    #print data['results'][0]['vehicle_region']['y']

    print   "vehicle-> Orientation-> Confidence-> ",
    print data['results'][0]['vehicle']['orientation'][0]['confidence']

    print '***'	
    print   "vehicle-> Orientation-> Color ->name ",
    print data['results'][0]['vehicle']['color'][0]['name']
    print   "vehicle-> Orientation-> Color -> Confidence -> ",
    print data['results'][0]['vehicle']['color'][0]['confidence']

    print '****'
    print   "vehicle-> Orientation-> Make Name ",
    print data['results'][0]['vehicle']['make'][0]['name']
    print   "vehicle-> Orientation-> Make Conf ",
    print data['results'][0]['vehicle']['make'][0]['confidence']

    print '****'
    
    print   "vehicle-> Orientation-> Body Type-> Name ",
    print data['results'][0]['vehicle']['body_type'][0]['name']
    print   "vehicle-> Orientation-> Body Type-> Conf ",
    print data['results'][0]['vehicle']['body_type'][0]['confidence']

    print '****'
    
    print   "vehicle-> Orientation-> Year of Mfg -> Name ",
    print data['results'][0]['vehicle']['year'][0]['name']
    print   "vehicle-> Orientation-> Year of Mfg-> Conf ",
    print data['results'][0]['vehicle']['year'][0]['confidence']

    print '****'
    
    print   "vehicle-> Orientation-> MakeOfModel  -> Name ",
    print data['results'][0]['vehicle']['make_model'][0]['name']
    print   "vehicle-> Orientation-> MakeOfModel  -> Conf ",
    print data['results'][0]['vehicle']['make_model'][0]['confidence']
