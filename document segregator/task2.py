import os
import pickle
import shutil
import time

root=os.getcwd()
d1=os.path.join(root,"D1")
dest=os.path.join(root,"dest")
file_list=os.listdir(d1)
with open("file_name.pkl","rb") as file:
	dirs=pickle.load(file)
with open("extensions.pkl","rb") as file:
	types=pickle.load(file)



for i in file_list:

	names,ext=os.path.splitext(i)
	type_=types[ext]
	move_to=os.path.join(dest,type_)
	move_from=os.path.join(d1,i)
	#print(move_from,"	"*5,move_to)
	shutil.move(move_from,move_to)