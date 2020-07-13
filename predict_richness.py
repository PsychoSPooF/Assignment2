import os
import fnmatch
filelist=[]
for filename in os.listdir("./"):
    if fnmatch.fnmatch(filename,"areas*.txt"):
        allfiles=filelist.append(filename);
print(filelist);
txt=os.system("python rich_pred.py "+" ".join(filelist)+" > predicted_diversities.txt");
sh=os.system("sort -k 1 -n "+" ".join(filelist)+" > predict_richness.sh");
if(txt):
    print("Python file Readed successfully");
else:
    print("Python file Reading Failed");

if(sh):
    print("Sh File Creation Success");
else:
    print("Sh File Creation Failed");
