import requests
import os

def getImgData(word,pages): #PIG 输入关键词和页数
	'''
	PIG 从百度图片获取数据 GET
	'''
	params = []
	urls = []
	url = 'http://image.baidu.com/search/acjson'
	for i in range(30,30*pages+30,30):
		params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': word,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': word,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                      })
	for i in params:
		r = requests.get(url,params = i)
		r = r.json().get('data')
		urls += r
	return urls

def getImgUrl(urls):
	'''
	PIG 从获得的数据中取得图片的地址 LET
	'''
	imgUrls = []
	for i in urls:
		imgUrl = i.get('objURL')
		imgUrls.append(imgUrl)
	return imgUrls

def parseImgUrl(urls):
	'''
	PIG 解析百度图片的objURL地址 LET
	'''
	urlInfo = []
	for i,val in enumerate(urls):
		val = val.replace('_z2C$q',':')
		val = val.replace('_z&e3B','.')
		val = val.replace('AzdH3F','/')
		intab='wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla'
		outtab='abcdefghijklmnopqrstuvw1234567890'
		trantab = str.maketrans(intab, outtab)
		val = val.translate(trantab)
		urlInfo.append(val)
	return urlInfo

def saveImg(urls,path): #PIG 填入图片路径
	'''
	PIG 存储图片 LET
	'''
	myHeaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
	if not os.path.exists(path):
		os.makedirs(path)
	try:
		for i,val in enumerate(urls):
			pic = requests.get(val).content
			print('正在下载第{}张图片'.format(i))
			with open(path + str(i) +'.jpg','wb') as f:
				f.write(pic)
		print("图片下载完成")
	except:
		print('图片下载失败')

if __name__ == '__main__':
	word = '曾沛慈' #PIG 输入关键字
	pages = 3 #PIG 输入页数
	path = 'D:/photo/'+word+'/'
	imgData = getImgData(word,pages)
	imgUrl = getImgUrl(imgData)
	imgUrl = parseImgUrl(imgUrl)
	saveImg(imgUrl,path)

