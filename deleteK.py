# -*- coding: UTF-8 -*-
a = '中文'
import os,shutil,sys
dirName =r'H:\documents'
names = os.listdir(dirName)
files = [os.path.join(dirName, name) for name in names        if os.path.isfile(os.path.join(dirName, name))]
dirs = [name for name in names        if os.path.isdir(os.path.join(dirName, name))]        
dirss = [os.path.join(dirName, name) for name in dirs        ]    
deleteFile=[f for f in files if r'_sample.azw' in os.path.basename(f)]    #.kfx
deleteDir=[f for f in dirss if r'_sample.sdr' in os.path.basename(f)]  
#[print(f) for f in files if '_sample.azw3' in os.path.basename(f)] #os.remove(f)
[print(f) for f in deleteFile] 
[os.remove(f) for f in deleteFile] 
sys.exit()      
#[shutil.rmtree(f) for f in deleteDir]    
for f in deleteDir:
    try:
        shutil.rmtree(f)
    except Exception as e:
        print(e)
    else: print(f)  
print('os.rmdir!!!!!!!!!!!!!!!!!!!!!!')    
for f in deleteDir:
    try:
        os.rmdir(f)
    except Exception as e:
        print(e)
    else: print(f) 
#[os.rmdir(f) for f in dirss  if r'_sample.sdr' in os.path.basename(f)]  