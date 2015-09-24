# 百度贴吧爬虫V0.1

标签（空格分隔）： 未分类

---
```
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('正在下载第'+strPage+'个网页，存储为'+saveName+'...')
	f = open(saveName, 'w+')
	f.write(html)
	f.close()
```
- 结果：
```
正在下载第1个网页，存储为00001.html...
Traceback (most recent call last):
  File "D:\Documents\GitHub\baidupa\baidu1.py", line 33, in <module>
    save(html,page)	#通过save()将html保存
  File "D:\Documents\GitHub\baidupa\baidu1.py", line 22, in save
    f.write(html)#.decode('utf-8'))
TypeError: must be str, not bytes
```
- 修改一下，把抓来的html用utf8 decode一下:
```
#---------------------
#程序：百度贴吧爬虫
#版本：0.1
#作者：X
#日期：2015-09-24 10:28:11
#语言：Python 3.43
#操作：
#功能：
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
	f = open(saveName, 'w+')
	f.write(html.decode('utf-8'))

	f.close()
	
head_url = input('input the url without page_number\n')
head = int(input('input the begining page_number\n'))
tail = int(input('input the ending page_number\n'))

for page in range(head,tail+1):
	url = head_url + str(page)	#遍历每一页url
	html = get_html(url)	#把url发给get_html，返回html文本给html变量
	save(html,page)	#通过save()将html保存

```

- 结果：
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-24/20090574.jpg)
应该是保存编码出了问题

- 改为字符串写入：
```
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('正在下载第'+strPage+'个网页，存储为'+saveName+'...')
	f = open(saveName, 'wb')
	f.write(html)#.decode('utf-8'))
	f.close()
```
- 工作正常：
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-24/23026040.jpg)



