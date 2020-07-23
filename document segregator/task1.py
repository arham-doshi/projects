import string 
import pickle
import os
import random
import time



with open("file_name.pkl","rb") as file:
	types=pickle.load(file)
root=os.getcwd()
d1=os.path.join(root,"D1")


no1=30 #no of files of each type
data=dict()
for key in types:
	
	for i in range(1,no1+1):
		ext=random.choice(types[key])
		name=key+"_"+str(i)+ext
		location=os.path.join(d1,name)
		with open(location,'w') as file:
			file.write("this is of type "+str(key)+" and has extension "+ext)
			file.write("number of file is "+str(i))
		data[name]=time.ctime(os.path.getctime(location))
with open("mata_data.pkl","wb") as file:
	pickle.dump(data,file)

