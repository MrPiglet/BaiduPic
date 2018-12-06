import requests
import re
import os

def getUrl():
    url="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=唐艺昕"
    mid = requests.get(url)
    mid.encoding='utf-8'
    page = mid.text
    zz = r'"objURL":"(.+?)"'
    html = re.findall(zz,page,re.S)
    return html
#print(html)

def mkdir(path):
    folder = os.path.exists(path)
    if not folder: #判断是否存在文件夹如果不存在则创建
        os.makedirs(path)
        print("创建新文件夹")
        print("创建成功")
    else:
        print("该文件夹已经存在")

img_path = "D:/photo/"

mkdir(img_path)

for j,i in enumerate(getUrl()):
    pic = requests.get(i).content
    print(str(j) + " 曾沛慈 " + i)
    f = open(img_path + str(j)+".jpg","wb")
    f.write(pic)
    f.close()












