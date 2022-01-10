[TOC]

# 터미널 명령어

## 1. touch 

- **파일** 생성
- 띄어쓰기로 구분하여 여러 파일을 한번에 생성 가능
- 숨김 파일: `.`을 파일명 앞에 붙이기

​	`touch text.txt`



## 2. mkdir

- make directory

- **새 폴더** 생성

- 띄어쓰기로 구분하여 여러 파일을 한번에 생성 가능

- 폴더 이름 사이에 공백을 넣고 싶다면 따옴표로 묶어서 입력

  ````bash
  mkdir 'happy day'
  ````



## 3. ls

- list segments

- **현재 작업중인** 디렉토리의 폴더/파일 목록

  ```bash
  ls #기본 사용
  
  ls all #all 옵션. 숨김 파일까지 모두 보여줌
  
  ls -a -l #long 옵션. 용량, 수정 날짜 등 상세 파일 정보 보여줌
  
  ls -al #all, long 옵션 함께 사용
  ```

  

## 4. mv

- move

- **폴더/파일을 다른 폴더 내로 이동하거나 이름을 변경**

- 다른 폴더로 이동할 때는 작성한 폴더가 반드시 있어야 한다. 없으면 이름이 바뀜

  ```bash
  #text.txt를 folder 폴더에 넣을 때
  mv text.txt folder 
  
  #text1.text의 이름을 text2.txt로 바꿀 때
  mv text1.txt text2.txt 
  ```

  

## 5. cd

- change directory

- 현재 작업중인 디렉토리를 변경하는 명령어

  ```bash
  cd #홈 디렉토리로 이동
  cd .. #위로 가기
  cd - #뒤로 가기
  
  #현재 작업중인 디렉토리에 있는 folder 폴더로 이동
  cd folder
  
  #절대 경로를 통한 디렉토리 변경
  cd C:/Users/kyle/Desktop
  
  #상대 경로를 통한 디렉토리 변경
  cd ../parent/child
  ```

  

## 6. rm

- remove

- 폴더/파일을 지우는 명령어

- `rm *.text` 로 입력시 txt 파일 전체 삭제

- `-r` : recursive 옵션. 폴더를 지울 때 사용

  ```bash
  rm test.txt
  rm -r folder
  ```



## 7. start, open

- 폴더/파일을 여는 명령어

- `Windows`에서는 start, `Mac`에서는 open

  ```bash
  #Windows
  start test.txt
  ```



## 8. vi

- 기존에 파일이 있다면 수정

- 파일이 없다면 새롭게 생성하면서 수정

  ```bash
  vi a.txt
  
  'i' : 글쓰기 (insert)
  `esc` + ':' + 'wq' : 저장
  ```



## 9. 유용한 단축키

- `위, 아래 방향키` : 과거에 작성했던 명령어 조회
- `tab` : 폴더/파일 이름 자동 완성
- `crtl + a` : 커서가 맨 앞으로 이동
- `ctrl + e` : 커서가 맨 뒤로 이동
- `ctrl + w` : 커서가 앞 단어를 삭제
- `ctrl + l` : 터미널 화면 청소(스크롤 올리면 과거 내역 조회 가능)
- `ctrl + insert` : 복사
- `shift + insert` : 붙여넣기