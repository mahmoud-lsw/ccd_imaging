#!/usr/bin/python
import time,re,subprocess,os,sys

image_content = ""
while not (len(image_content)>0 and re.match("^(?!_)\w*(?<!_)$",image_content)):
    image_content = raw_input('\nWhat are you imaging? (Ex. jupiter, moon, m31...)\n'+
                'Please use only alphanumeric characters (a-z,0-9)\n')
    image_exposure = raw_input('\nWhat is the exposure? (Ex. 500ms, 4s)\n'+
                'Please use only alphanumeric characters (a-z,0-9)\n')

dir_name = (time.strftime("%Y%m%d"))+'_'+image_content

if not os.path.isdir(str("../data/"+dir_name+"/"+image_exposure)):
    if not os.path.isdir(str("../data/"+dir_name)):
        subprocess.call("mkdir ../data/"+dir_name,shell=True)
    subprocess.call("mkdir ../data/"+dir_name+"/"+image_exposure,shell=True)
    sub_directories = ['infrared','red','green','blue','visible','solar','darks','flats']
    for sub_dir in sub_directories:
        subprocess.call("mkdir ../data/"+dir_name+"/"+image_exposure+"/"+sub_dir,shell=True)
else:
    sys.exit(dir_name+" already exists as a directory")