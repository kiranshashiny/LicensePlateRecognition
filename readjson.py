import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    data_json = json.dumps ( data);
    
    #print data["credits_monthly_total"]
    #print data['img_width']
    print ("*************************")
    print ("Vehicle Plate     Number", data['results'][0]['plate'])
    print ("Vehicle Plate Confidence", data['results'][0]['confidence'] )
    #print data['results'][0]['vehicle_region']['x'] )
    #print data['results'][0]['vehicle_region']['y'] )

    print  ( "vehicle-> Orientation-> Confidence-> ", data['results'][0]['vehicle']['orientation'][0]['confidence'] )

    print ('***'	 )
    print (  "vehicle-> Orientation-> Color ->name ", data['results'][0]['vehicle']['color'][0]['name'] )
    print (  "vehicle-> Orientation-> Color -> Confidence -> ", data['results'][0]['vehicle']['color'][0]['confidence'] )

    print ('****' )
    print (  "vehicle-> Orientation-> Make Name ", data['results'][0]['vehicle']['make'][0]['name'] )
    print (  "vehicle-> Orientation-> Make Conf ", data['results'][0]['vehicle']['make'][0]['confidence'] )

    print ('****' )
    
    print (  "vehicle-> Orientation-> Body Type-> Name ", data['results'][0]['vehicle']['body_type'][0]['name'] )
    print (  "vehicle-> Orientation-> Body Type-> Conf ", data['results'][0]['vehicle']['body_type'][0]['confidence'] )

    print ('****' )
    
    print (  "vehicle-> Orientation-> Year of Mfg -> Name ", data['results'][0]['vehicle']['year'][0]['name'] )
    print (  "vehicle-> Orientation-> Year of Mfg-> Conf ", data['results'][0]['vehicle']['year'][0]['confidence'] )

    print ('****' )
    
#    print   "vehicle-> Orientation-> MakeOfModel  -> Name ",
#    print data['results'][0]['vehicle']['make_model'][0]['name']
#    print   "vehicle-> Orientation-> MakeOfModel  -> Conf ",
#    print data['results'][0]['vehicle']['make_model'][0]['confidence']
