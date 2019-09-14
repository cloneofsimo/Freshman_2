
-xxxxx     1 trainer1 trainer1 xxx x월 xx xx:xx xxx
dxxxxx     2 trainer1 trainer1 xxx x월 xx xx:xx xxx
파일성격   ~ Permission ~  크기 ~ 날짜   ~~      파일명

ls -al : 숨겨진 파일, 디렉토리 보여줌. - 이 있으면 파일,  d 가 있으면 디렉토리.
 숨겨진 파일은 앞에 . 이 붙음.

 pwd: 현재 경로

 cd .. : 윗단계로 올라감  
 cd xxx : xxx 로 내려감.  
 cd / : 최상위 디렉토리로 감.  
 mkdir xxx : 디렉토리 xxx 생성  
 rmdir xxx : 디렉토리 xxx 삭제  
 cp xxx yyy : 파일 xxx 복사해서 파일 yyy 로 붙여넣기  
 rm xxx : xxx 삭제  
 mv xxx yyy : xxx ㅋ을 복사하여 yyy 로 잘라넣기.


w : 서버 접속 유저 목록 출력  
xxx &nbsp; aaa &nbsp; bbb.xxx.xxx.xxx &nbsp; tt:tt pm &nbsp; u.tts v.tts w.tt ccc

xxx: 로그인 아이디  
aaa : tty 면 콘솔, pts 는 터미널.  
bbb.xxx... : 접속 IP  
tt.tt : 접속 시간  
ccc : 사용하고 있는 커멘드  

finger -l :서버 접속 유저 목록 (더 자세히)  
inconfig: 접속한 서버의 ip 확인  
write ID/dev/pts/번호 : 쪽지 보내기  
wall "xxx" : 모든 사용자에게 xxx 라고 쪽지를 보냄.

bin: 기본적인 리눅스 실행 파일  
boot: 리눅스 부팅 관련 파일, 커널  
dev: 하드웨어 정보  
etc: 패스워드 파일, 쉐도우 파일, 리눅스 설정 파일 등등  
/etc/passwd: 사용자에 대한 정보  
/etc/shadow: 사용자들의 패스워드 (권한 없음이 기본)  
/etc/services: 하는 서비스 보여줌  
/etc/issue.net: 처음 접속될 때 나오는 화면  
/etc/motd: 로그인 후 나오는 메세지  
~/public_html : 각 사용자들의 홈페이지 파일  
home: 사용자들의 디렉토리가 들어가는 곳. (일반 사용자)  
lib : 라이브러리 파일  
mnt : mount 명령을 사용하여 마운트 시킨 시디롬, 플로피 디스켓 등이 들어간 디렉토리  
proc:  
root:  
sbin:  
tmp:  
usr:  
var:  

whoami: 자신 정보 표시  
id: 자신의 자세한 정보 표시  
cat/etc/passwd: 서버 활동중인 사람들의 계정 정보
uname -a : 리눅스의 커널 버전
cat/etc/\*release: 설치된 OS 의 버전  
 rpm -qa : 패키지의 정보  
 cat/proc/cpuinfo: cpu 정보  

패스워드 파일: 한 서버를 사용하는 사용자들의 모든 정보를 기록해 놓은 파일  
cat 파일 이름: 파일의 내용을 출력  ex)  
root: x: 0: 0: Admin:/root:/bin/bash  
1 2 3 4 5 6 7
1. 로그인할 때 사용되는 아이디  
2. 패스워드  
3. 컴퓨터에 입력되는 사용자 아이디  
4. 컴퓨터에 입력되는 그룹  
5. 사용자의 이름  
6. 로그인에 성공 했을 때 기본으로 위치하게 되는 디렉토리  
7. 처음 로그인 했을 때 실행되게 할 프로그램 (로그인 했을 때 쉘이 실행되는 것)  
tar: 파일 합치기
tar cvf xxx yyy : xxx 와 yyy 를 합침.
tar xvf xxx : xxx 를 해제한다.  
c: 새로운 파일 만들기.  
x: 압축하는 옵션  
v: 압축이 되거나 풀리는 과정 출력  
f: 파일을 백업하겠다는 옵션  
gzip:  한번에 한개의 파일 압축  
gzip xxx: xxx 을 압축.  
gzip -d xxx:  선택된 파일 해제.  

.tar: tar 로 압축된 파일  
.gz: gzip 으로 압축된 파일  
tar.gz: tar 프로그램으로 합친 후 gzip 으로 압축한 파일  
tgz: tar.gz 와 동일  

### 파일의 종류:
1. 텍스트 파일: .txt 이며, cat 으로 내용 출력

  \* *.txt 파일 생성법:*  
  1. 쉘 프롬프트 상태에서, cat > 파일이름.txt 라고 입력.
  2. 원하는 내용 입력.
  3. Ctrl + D

  \*  *수정의 경우:*
  1.  cat >> 파일이름.txt 라고 입력 후 수정.

2. 프로그램 소스 파일: 컴퓨터 언어로 입력한 파일. 컴파일 과정으로 실행.


10.
해킹엔 두가지 가 있다. Remote 와 Local.
Remote 해킹은 해킹하고자 하는 서버에 아이디가 없을 때, 아이디를 얻고자 시도하는 것.  
Local 은 해킹하고자 하는 서버에 일반 계정이 있을 때, 관리자 권한을 얻고자 하는 방법임.

SetUID: ID 를 변경하는 것임. 일반 유저가 자신의 비밀번호를 바꾸고자 할 때,

-perm
-name  
-user  
-group
