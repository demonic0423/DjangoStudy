from urllib2 import urlopen
f = urlopen("http://www.naver.com")
print f.read(500)
