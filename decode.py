import base64
import re
import datetime

with open("gfwlist.txt","r") as f:
    a = f.read()

text = str(base64.b64decode(a),"utf-8")

with open("PACurl.txt","w") as file:
    file.write(text)


with open("PACurl.txt","r") as f1:
    txt = f1.read().splitlines()

t = txt[18:-2]
url = []
p1 = "---"
pattern1 = re.compile(p1)
pattern2 = re.compile("!-[A-Z]")
pattern3 = re.compile("!--")
pattern4 = re.compile("###")
for line in t:
    if (re.search(pattern1,line)== None and re.search(pattern2,line) == None
            and re.search(pattern3,line)==None and re.search(pattern4,line)==None and line!=""):
        url.append(str("\""+line+"\""))

with open("Templates.txt","r") as ff:
    tf = ff.read().splitlines()
    t1 = tf[:25]
    t2 = tf[26:]

with open("pac.txt","w") as f2:
    f2.writelines("/*\n")
    f2.writelines(" * Last Updated: "+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n")
    f2.writelines(" */\n")
    for line in t1:
        f2.writelines(line+"\n")
    for i in range(len(url)):
        if i < len(url)-1:
            f2.writelines("\t"+url[i]+",\n")
        else:
            f2.writelines("\t"+url[i]+"\n")
    for line in t2:
        f2.writelines(line+"\n")

