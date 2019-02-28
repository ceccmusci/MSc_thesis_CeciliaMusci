


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os

def gen_subdir(expInfo):



    # example for expinfo-parameters (expinfo in psychopy)
    #expInfo={'participant':"01", 'date':"6_28_18",}

    # create new, individual folder for participant, named after current expinfo
    source_folder = os.getcwd()
    sub_dir = u'\\sub_%s_date_%s' %(expInfo['participant'], expInfo['date'])
    newpath = os.path.join(source_folder + sub_dir)
    print('creating new path '+newpath)
    os.makedirs(newpath)
    # move the 3 individually generated csv-files into new sub-folder
    files = os.listdir(source_folder)

    for f in files:
        if (f.startswith("run")):
            shutil.move(f, newpath)



#gen_subdir(expInfo)
