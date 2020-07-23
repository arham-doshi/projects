import os
import shutil as shl
import pickle

def create_file(name,root):
   new_path=os.path.join(root,name)
   if(not os.path.exists(new_path)):
      os.mkdir(new_path)
   return new_path

root=os.getcwd()
#print(root)

d1=create_file("D1",root)

#print(os.getcwd())

dir_types = {
   "HTML": [".html5", ".html", ".htm", ".xhtml"],
   "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
   ".heif", ".psd"],
   "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
   ".qt", ".mpg", ".mpeg", ".3gp"],
   "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
   ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
   ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
   ".pptx"],
   "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
   ".dmg", ".rar", ".xar", ".zip"],
   "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
   ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
   "PLAINTEXT": [".txt", ".in", ".out"],
   "PDF": [".pdf"],
   "PYTHON": [".py"],
   "XML": [".xml"],
   "EXE": [".exe"],
   "SHELL": [".sh"]
}
inverted_types= dict()

for keys in dir_types.keys():
	for value in dir_types[keys]:
		inverted_types[value]=keys


print("file_name stores types of files and have",len(dir_types),"different types")
print("extensions contains names of extensions ans we have",len(inverted_types),"diffrent extensions")
print()
print("file structure is as follows")
print("->root")
print("	|->readme,open_first,task1,task2,task3")
print("        |->D1->(cantains all the files) ")
print("        |->dest->(we will move files here)")


with open("file_name.pkl","wb") as file:
	pickle.dump(dir_types,file)
with open("extensions.pkl","wb") as file:
	pickle.dump(inverted_types,file)

dest=create_file("dest",root)
for key in dir_types.keys():
   create_file(key,dest)