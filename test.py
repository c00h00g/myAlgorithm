#encoding:UTF-8
import urllib.request
fp = urllib.request.urlopen("http://www.baidu.com")
mybytes = fp.read()
mystr = mybytes.decode("utf8")

fp.close()
print(mystr)