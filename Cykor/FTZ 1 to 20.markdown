## Cykor 예비 멘토링: FTZ

### Level 1

 $ ls- al
 , $ cat hint 를 통해 hint 를 읽는다. 앞으로 이 과정은 기본으로 생각하겠다.  

 setuid 가 걸린 파일을 찾으라가 hint 이다.  

 $ find / -perm +4000 -user level2 2> /dev/null  

 find 명령어로 setuid 가 있는 파일의 위치를 찾았다.

 /bin/ExecuteMe 로 파일을 실행한다.

 이제  /bin/bash 로 쉘을 휙득한다. my-pass 로 level2 의 패스워드 휙득.

 ### Level2

 hint 는
 텍스트 파일 편집 중 쉘의 명령을 실행시킬 수 있다 한다.  
 일단 find 로, /usr/bin/editor 가 setuid 가 걸려있다.  

왜인진 잘 모르겠지만 검색해보니까 ! 를 누르면 커멘드가 쳐진다... 암튼 이렇게 setuid 가 있는 파일 실행중 /bin/bash 를 하면 권한 휙득 성공. my-pass 로 얻은 다음 비번은 "can you fly?"

### Level3

힌트에는 다음과 같은 코드가 있다.

다음 코드는 autodig의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char \*\*argv){

    char cmd[100];

    if( argc!=2 ){
        printf( "Auto Digger Version 0.9\n" );
        printf( "Usage : %s host\n", argv[0] );
        exit(0);
    }

    strcpy( cmd, "dig @" );
    strcat( cmd, argv[1] );
    strcat( cmd, " version.bind chaos txt");

    system( cmd );

}

이를 이용하여 level4의 권한을 얻어라.

more hints.  
\- 동시에 여러 명령어를 사용하려면?  
\- 문자열 형태로 명령어를 전달하려면?

딱 보아하니 cmd 에 이것저것 넣어서 실행시키는 코드이다. 일단 저 위치를 find 를 통해 알아보니, /bin/autodig 이다. 그래서 argv[1] 에 해당하는걸 "my-pass" 라고 해봤다. 그런데 서버를 찾을 수 없다 하더라  
그래서 local:my-pass 라고 쳤다. 오류가 뜨긴 하는데 여전히 비밀번호는 나왔다. "suck my brian".

### Level4

누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!

고 한다. 일단 그 위치로 가는게 인지상정이다.cd /etc/xinetd.d/

그 담에 ls -al 해주자. 2011 년 누가 만든 backdoor 파일이 있다. cat 해주자. service finger 다음에 뭐라고 나오는데 잘 이해가 가진 않는다. user 가 level5 라 한다. 일단 그래서 인터넷 조사를 해봤다. 아. server 항에 있는 곳에 c 코드를 짜면 그걸 level5 권한으로 실행시켜준단다. 그래서 cat > backdoor.c 로 backdoor 코드를 짰다. system("/bin/bash") 을 넣었는데 분명 안된다. 그래서 인터넷의 방식대로 해봤는데 여전히 안됨. 뭐가 문제인지... 암튼 빡치지만 그냥 https://savefile.tistory.com/131?category=652108 여기 그대로 했다. ㅠㅠ

### Level5  

고양이 힌트
