[TOC]

# [1] Git 초기 설정

- 최초 한 번만 설정



1. 누가 커밋 기록을 남겼는지 확인할 수 있도록 이름과 이메일 설정 

   작성자를 수정하고 싶을 때에는 이름, 메일 주소만 다르게 하여 동일하게 입력

   ```bash
   git config --global user.name "이름"
   git config --global user.email "메일 주소"
   ```

2.  작성자가 올바르게 설정되었는지 확인

   ```bash
   git config --global -1
   
   or
   
   git config --global --list
   ```

   

# [2] Git 기본 명령어

- `Working Directory (= Working Tree)` : 사용자의 일반적인 작업이 일어나는 곳
- `Staging Area (= Index)` : commit을 위한 파일 및 폴더가 추가되는 곳
- `Repository` : staging area에 있던 파일 및 폴더의 변경사항(commit)을 저장하는 곳
- Git은 **Working Directory - Staging Area - Repository**의 과정으로 버전 관리 수행



## (1) git init

```bash
git init
```

- 현재 작업중인 디렉토리를 Git으로 관리한다는 명령어

- `.git`이라는 숨김 폴더가 생성, 터미널에는 `(master)`라고 표기됨

  

:exclamation::exclamation:주의 사항:exclamation::exclamation:

```bash
1. 이미 Git 저장소인 폴더 내 또 다른 Git 저장소 생성 금지(중첩 금지)
즉, 터미널에 이미 (master)가 있다면 git init 입력 금지

2. 절대 홈 디렉토리에서 git init 입력하지 않기. 터미널의 경로가 `~`인지 확인
```



## (2) git status

```bash
git status
```

- Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어

- 상태

  1. `Untracked` : Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일)

  2. `Tracked` : Git이 관리하는 파일

     ​	a. `Unmodified` : 최신 상태

     ​	b. `Modified` : 수정되었지만 아직 Staging Area에 반영되지 않은 상태

     ​	c. `Staged` : Staging Area에 올라간 상태



## (3) git add

```bash
# 특정 파일
git add a.txt

# 특정 폴더
git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
git add .
```

- Working Directory에 있는 파일을 Staging Area로 올리는 명령어
- Git이 해당 파일을 추적(관리)할 수 있도록 만든다
- `Untracked, Modified -> Staged`로 상태 변경



## (4) git commit

```bash
git commit -m "first commit"
```

- Staging Area에 올라온 파일의 변경 사항을 하나의 버전(commit)으로 저장하는 명령어
- 각각의 커밋은 `SHA-1` 알고리즘에 의해 반환된 고유의 해시값을 ID로 가짐
- `(root-commit)`은 해당 commit이 최초의 commit일 때만 표시



## (5) git log

```bash
git log
```

- commit의 내역(`ID, 작성자, 시간, 메시지 등`)을 조회할 수 있는 명령어
- 옵션
  - `--oneline` : 한 줄로 축약
  - `--graph` : branch와 merge 내역을 그래프로 보여줌
  - `--all` : 현재 branch를 포함한 모든 branch의 내역 보여줌
  - `--reverse` : commit 내역의 순서를 반대로 보여줌(최신이 가장 아래)
  - `-p` : 파일의 변경 내용도 같이 보여줌
  - `-2` : 원하는 갯수 만큼의 내역을 보여줌 (-100쓰면 100개)