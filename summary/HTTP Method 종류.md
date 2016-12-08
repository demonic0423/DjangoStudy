#HTTP Method 종류

## GET 
* 리소스 취득
* Read(조회) 역할
* HTML 폼 에서 지정 가능하기 때문에 가장 많이 사용
`GET http://docs.djangoproject.com/search/?q=forms&release=1 HTTP/1.1`
  URI의 ? 뒷부분에 키=값을 쌍으로 이어붙여 보내고 URI에 길이 제한이 있기 때문에 많은 양의 데이터 보내기 어려움 
  전달되는 사용자의 데이터가 브라우저 주소창에 노출되기 때문에 보안상 불리
  
##POST
* 리소스 생성
* 리소스 데이터 추가
* Create(생성) 역할
* HTML 폼 에서 지정 가능하기 때문에 가장 많이 사용
`POST http://docs.djangoproject.com/search/HTTP/1.1`
`Content-Type: application/x-www-from-urlencoded`
`q = forms&release = 1`
파라미터들을 요청메시지의 바디에 넣기 때문에 많은 양의 정보 전달 가능

##PUT
* 리소스 변경
* Update(변경) 역할
*PUT Method는 URI결졍권이 클라이언트 쪽에 있을경우 POST역할로 사용가능*

##DELETE
* 리소스 삭제
* Delete(삭제)

##HEAD
* 리소스의 헤더(메타데이터) 취득

##OPTIONS
* 리소스가 서포트하는 메소드 취득

##TRACE
* 루프백 시험에 사용

## CONNECT
* 프록시 동작의 터널 접속으로 변경
