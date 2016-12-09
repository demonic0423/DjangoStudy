#-*-coding:utf-8-*-


from urllib2 import urlopen
from HTMLParser import HTMLParser

class ImageParser(HTMLParser):
	def handle_starttag(self, tag, attrs): #HTMLParser 내부의 handle_starttag함수 오버라이드
		if tag != 'img': #img 태그 찾기
			return
		if not hasattr(self, 'result'):
			self.result = []
		for name, value in attrs:
			if name == 'src':	#img src 속성을 찾으면 속성값을 result리스트에 추가
				self.result.append(value)
def parseImage(data):	# HTML문장이 주어지면 ImageParser클래스를 사용해서 이미지를 찾고, 리스트 출력
	parser = ImageParser()
	parser.feed(data) # HTML문장을 feed 함수로 넘겨주면 바로 파싱하고 결과를 parser.result리스트 추가
	dataSet = set(x for x in parser.result) # 파싱 결과를 set 타입의 dataSet으로 모아줌
	print '\n'.join(sorted(dataSet)) # dataSet으로 모은 파싱 결과를 정렬한 후에 출력

def main():
	url = "http://www.naver.com"
	f = urlopen(url)
	charset = f.info().getparam('charset') #인코딩 방식을 알아내기
	data = f.read().decode(charset)	# 해당 인코딩 방식을 디코딩 해줌
	f.close()

	print "\n>>>>>>>>>> Fetch Image from", url
	parseImage(data)	#이미지를 찾기 위한 paseImage함수 호출

if __name__ == '__main__':
	main()

