import pandas as pd
import os
import pickle
import time

root=os.getcwd()
dest=os.path.join(root,'dest')
d1=os.path.join(root,'D1')

with open("file_name.pkl","rb") as file:
	dirs=pickle.load(file)
with open("extensions.pkl","rb") as file:
	types=pickle.load(file)



mata={'name':[],'extension':[],'old_creation_time':[],'new_creation_time':[],'last_modification_time':[],'size':[],'old_path':[],'new_path':[]}
with open("mata_data.pkl","rb") as file:
	data=pickle.load(file)
for key in data.keys():
	name,ext=os.path.splitext(key)
	ctime=data[key]
	type_=types[ext]
	opath=os.path.join(d1,key)
	npath=os.path.join(dest,type_,key)
	size=os.stat(npath).st_size
	ntime=os.path.getctime(npath)
	nmtime=os.path.getmtime(npath)
	mata['name'].append(name)
	mata['extension'].append(ext)
	mata['old_creation_time'].append(ctime)
	mata['new_creation_time'].append(ntime)
	mata['last_modification_time'].append(nmtime)
	mata['size'].append(size)
	mata['old_path'].append(opath)
	mata['new_path'].append(npath)

data_table=pd.DataFrame(mata,columns=['name','extension','size','old_creation_time','new_creation_time','last_modification_time','old_path','new_path'])
data_table.to_csv("CSVlog.csv");
print(data_table)
