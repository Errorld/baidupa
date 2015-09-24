#---------------------
#程序：百度贴吧爬虫
#版本：0.1
#作者：X
#日期：2015-09-24 10:28:11
#语言：Python 3.43
#操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#功能：下载对应页码内的所有页面并存储为html文件。 
#---------------------
import string
import urllib.request

def get_html(url):	#传入网址，返回HTML#暂未加入异常处理
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	return response.read()
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('正在下载第'+strPage+'个网页，存储为'+saveName+'...')
	f = open(saveName, 'wb')
	f.write(html)#.decode('utf-8'))

	f.close()
	
head_url = input('input the url without page_number\n')
head = int(input('input the begining page_number\n'))
tail = int(input('input the ending page_number\n'))

for page in range(head,tail+1):
	url = head_url + str(page)	#遍历每一页url
	html = get_html(url)	#把url发给get_html，返回html文本给html变量
	save(html,page)	#通过save()将html保存

