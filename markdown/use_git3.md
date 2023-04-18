[toc]

# 1. 복습

`*.py`

: *는 전체를 뜻함, 위는 파이썬 파일 전체를 뜻함 





## [1] git 순서

1. git init
2. .gitignore
3. git add .
4. git commit -m "commit" #여기까지가 로컬 저장소에서 하는 일



1. repository 만들기(github)
2. git remote add origin url
3. git push -u origin master #이후에는 git push만 써도 push 됨



## [2] git clone

1. `git clone url`  or `git clone url .` : .은 폴더 자체에, .이 없으면 새로운 파일 생성 
2. `git pull` : 최신 버전 가져오기
   - 같은 파일을 다르게 변경 시 conflict 발생
   - 수정 후 commit해서 다시 push



# 2. branch

- 현재 작업하고 있는 곳을 뜻함

- branch 생성
  - `git branch name`(branch 이름)

- branch 이동

  - `git switch -c 'new'` : new라는 branch 생성하며 new로 이동

  - `git switch new` : new라는 branch로 이동 (`git checkout new`도 같은 명령어)



- branch 확인

  - `git branch` : 어느 branch에 있는지 확인 가능

  - `git log --all --oneline` : 모든 branch log 확인 가능

  - `git log --all --oneline --graph` : branch log 구분하여 확인 가능



- branch merge

  - `git merge new` : branch 합치기 **현재 있는 branch에서 merge 됨**

  - `git branch -d new` : new라는 이름의 branch 지우기

***

*`code` : Visual Studio Code 실행



# 3. restore

- `git restore` : 기록이 남아있는 전  버전으로 돌아감
  - add를 한 상태면 restore를 해도 돌아가지 않음
  - restore는 취소/돌아가기 기능이 없음
- `git restore --staged <file>` : staging 하기 전으로 돌아감
- `git rm --cached <file>` : add하기 전으로 돌아감(untrack 상태)
  - `git rm --cached -r` : 전체 파일이 다 add하기 전으로 돌아감



# 4. commit 수정

- `git commit --amend` : commit message 수정 가능
  - 새로운 파일을 최상단commit에 넣을 때도 이 코드 사용
- `git diff` : 수정사항을 확인하고 싶을 때(working directory와 staging/commits 비교)
- `git diff --staged` : staging area와 commit 비교



# 5. reset, revert

| git reset [옵션] eea5 | working<br />directory | staging<br />area  |       repository        |
| :-------------------: | :--------------------: | :----------------: | :---------------------: |
|        --soft         |        안 바뀜         |      안 바뀜       | HEAD가 eea5 커밋 가리킴 |
|        --mixed        |        안 바뀜         | eea5 커밋처럼 바뀜 | HEAD가 eea5커밋 가리킴  |
|        --hard         |       eea5 커밋        | eea5 커밋처럼 바뀜 | HEAD가 eea5커밋 가리킴  |

- `git reset --hard` :몽땅 지워버림
- `git reset --soft` : working directory, staging area에는 남아 있음
  - commit 하면 원래대로 돌아올 수 있음 
- `git reset (--mixed)` : staging area에 올라오지 않은 상태
  - add, commit 하면 원래대로 돌아올 수 있음
  - reset의 경우 mixed가 default여서 commit ID만 작성해도 실행 됨



- `git reflog` : commit 리셋 기록 확인
- `git revert` : 중간에 있는 commit을 유지하면서 새로운 commit을 쌓음

- `git revert commit ID..commit ID` : 앞 commit ID는 revert 미포함



# 6. git flow

- git flow

  

- fork and pull (pull request)

- shared repository model: 동일한 저장소를 공유하여 활용하는 방식
