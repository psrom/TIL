[toc]

# [1] Github

## 원격 저장소(Remote Repository)

(1) **Github에서 원격 저장소 생성**



(2) **로컬 저장소와 원격 저장소 연결**

- **`git remote`**: 로컬 저장소에 원격 저자소를 `등록, 조회, 삭제`할 수 있는 명령어

  1. 원격 저장소 등록

     `git remote add <이름> <주소>`형식으로 작성

     ```bash
     git remote add origin https://github.com/blabla/bla.git
     ```

  2. 원격 저장소 조회

     ```bash
     git remote -v
     ```

  3. 원격 저장소 연결 해제

     ```bash
     git remote rm origin
     
     or
     
     git remote remove origin
     
     #로컬과 원격 저장소의 연결을 끊는 것 뿐 원격 저장소 자체를 삭제하는 것은 아님
     ```



(3) **원격 저장소에 업로드**

 1. 로컬 저장소에서 commit 생성

 2. **git push**

    - 로컬 저장소의 commit을 원격 저장소에 업로드 하는 명령어
    - `git push <저장소 이름> <branch 이름>`형식으로 작성
    - `-u` 옵션 사용시 두 번째 commit부터는 `저장소 이름, branch 이름` 작성 생략 가능

    ```bash
    git push origin master
    
    #origin이라는 이름의 원격 저장소의 master branch에 push한다
    -------------------------------------------------------
    
    git push -u origin master
    #이후에는 git push만 작성해도 push 됨
    ```





# [2] gitignore

`.gitignore`

-반드시 `.git` 폴더와 동일한 위치에 생성

-제외하고 싶은 파일은 `git add` 전에 `.gitignore` 에 작성



**관련 웹사이트 주소**

https://www.toptal.com/developers/gitignore



# [3] clone, pull

## 원격 저장소 가져오기

(1) **git clone**

- 원격 저장소의 commit 내역을 모두 가져와서 로컬 저장소를 생성하는 명령어

- 원격 저장소를 통째로 복제해서 내 컴퓨터에 옮길 수 있음

- `git clone <원격 저장소 주소>`형태 

  - 주소는 `shift` + `insert`로 붙여넣기

    ```bash
    git clone https://github.com/blabla/bla.git
    ```

- git clone을 통해 생성된 로컬 저장소는 `git init, git remote add`가 이미 수행되어 있음



(2) **git pull**

- 원격 저장소의 변경 사항을 가져와서 로컬 저장소를 업데이트하는 명령어

- 로컬 저장소와 원격 저장소의 내용이 일치할 경우 git pull을 해도 변화 없음

- `git pull <저장소 이름> <branch 이름>` 형태로 작성

  ```bash
  git pull origin master
  
  #origin이라는 원격 저장소의 master branch의 내용을 가져온다(pull)
  ```

  

