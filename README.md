# �ٶ���������V0.1

��ǩ���ո�ָ����� δ����

---
```
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('�������ص�'+strPage+'����ҳ���洢Ϊ'+saveName+'...')
	f = open(saveName, 'w+')
	f.write(html)
	f.close()
```
- �����
```
�������ص�1����ҳ���洢Ϊ00001.html...
Traceback (most recent call last):
  File "D:\Documents\GitHub\baidupa\baidu1.py", line 33, in <module>
    save(html,page)	#ͨ��save()��html����
  File "D:\Documents\GitHub\baidupa\baidu1.py", line 22, in save
    f.write(html)#.decode('utf-8'))
TypeError: must be str, not bytes
```
- �޸�һ�£���ץ����html��utf8 decodeһ��:
```
#---------------------
#���򣺰ٶ���������
#�汾��0.1
#���ߣ�X
#���ڣ�2015-09-24 10:28:11
#���ԣ�Python 3.43
#������
#���ܣ�
#---------------------
import string
import urllib.request

def get_html(url):	#������ַ������HTML#��δ�����쳣����
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	return response.read()
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('�������ص�'+strPage+'����ҳ���洢Ϊ'+saveName+'...')
	f = open(saveName, 'w+')
	f.write(html.decode('utf-8'))

	f.close()
	
head_url = input('input the url without page_number\n')
head = int(input('input the begining page_number\n'))
tail = int(input('input the ending page_number\n'))

for page in range(head,tail+1):
	url = head_url + str(page)	#����ÿһҳurl
	html = get_html(url)	#��url����get_html������html�ı���html����
	save(html,page)	#ͨ��save()��html����

```

- �����
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-24/20090574.jpg)
Ӧ���Ǳ�������������

- ��Ϊ�ַ���д�룺
```
def save(html,page):
	strPage = str(page)
	saveName = str.zfill(strPage,5) + '.html'
	print('�������ص�'+strPage+'����ҳ���洢Ϊ'+saveName+'...')
	f = open(saveName, 'wb')
	f.write(html)#.decode('utf-8'))
	f.close()
```
- ����������
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-24/23026040.jpg)



