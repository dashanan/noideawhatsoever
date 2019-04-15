#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib
import os
cwd = os.getcwd()
files = os.listdir(cwd) #Relative Path
dict_file =[]
for x in files:
    try:
        
        hash_dict ={}
        openedFile = open(x,'rb')
        readFile = openedFile.read()

        md5Hash = hashlib.md5(readFile)
        md5Hashed = md5Hash.hexdigest()

        sha256Hash = hashlib.sha512(readFile)
        sha256Hashed = sha256Hash.hexdigest()
        hash_dict['sha256Hashed'] =sha256Hashed
        hash_dict['md5'] =md5Hashed
        
        hash_dict['file_name'] = x
        hash_dict['dir']= cwd
        dict_file =dict_file + [hash_dict]
    except:
        print(x)
    
print(dict_file)


# In[ ]:



        
        
    


# In[ ]:





# In[ ]:





# In[ ]:




