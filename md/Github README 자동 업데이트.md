# Github README 자동 업데이트

python script를 사용하여 README를 자동으로 업데이트 하는 기능을 만들것이다.

작업 순서는 목차를 참고하자.

[TOC]

## Python Script 작성

요즘 학교에서 python도 배우고있고 여기저기 블로그를 찾아보니 python을 많이 사용하는 것 같아 python으로 작성할 것이다.

그 외 별다른 이유는 없다.

일단 아래는 python 전체 소스코드다. 성격 급한 사람들을 위해 먼저 작성했다.

``````python
import glob
import os
import time
from urllib import parse

def make_index():
    index = ""
    dir_name = './md/*'
    file_list = glob.glob(dir_name)
    file_list.sort(key=os.path.getmtime, reverse=True)
    for file_path in file_list:
        timestamp_str = time.strftime(  '%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
        file_name = file_path[5:-3]
        file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/{parse.quote(file_path[2:])}'''
        index += f'''{timestamp_str} - [{file_name}]({file_link})\n\n'''
    
    return index


def make_read_me(index):
    return f"""
# 개발 부스러기

남들이 먹고 남긴 개발 부스러기를 주워 먹읍시다.



## 부스러기 목차
{index}



## [부스러기 나눔](https://github.com/c9u11/development-crumbs/blob/main/md/%EA%B0%9C%EB%B0%9C%20%EB%B6%80%EC%8A%A4%EB%9F%AC%EA%B8%B0%20%EB%82%98%EB%88%94%20%EB%B0%A9%EB%B2%95.md)

먹다 남긴 개발 부스러기가 있다면 나눠주세요.

어떠한 향과 맛 상관없습니다. 감사합니다.

1. 포장지를 받습니다. (Fork the Project)
2. 개발 부스러기를 모읍니다. (Write .md File)
3. 개발 부스러기를 포장합니다. (Commit your Changes)
4. 포장한 부스러기를 문 앞에 놓으세요. (Push to the Branch)
5. 나눔 신청을 통해 모두에게 나누어주세요. (Open a Pull Request)
"""


def update_readme_md():
    readme = make_read_me(make_index())
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

if __name__ == "__main__":
    update_readme_md()
``````



크게 main > update_readme_md > make_readme > make_index 순서로 진행된다.



### Main

여기는 별 내용 없다.

그저 update_reamde_md를 실행한다.



### update_readme_md

실제로 readme를 업데이트 하는 부분이다.

```python
readme = make_read_me(make_index())
```

readme라는 변수에 새로운 readme 문자열을 저장한다.

```python
with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
```

README 파일을 열어 readme 변수에 저장했던 문자열을 작성한다.



### make_readme_md

index를 전달받아 기본 포맷에 index를 추가하는 작업이다.



### make_index

index를 만들어주는 함수로 사실상 핵심로직이 들어있는 함수다.

```python
    index = ""
    dir_name = './md/*'
    file_list = glob.glob(dir_name)
    file_list.sort(key=os.path.getmtime, reverse=True)
    for file_path in file_list:
        timestamp_str = time.strftime(  '%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
        file_name = file_path[5:-3]
        file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/{parse.quote(file_path[2:])}'''
        index += f'''{timestamp_str} - [{file_name}]({file_link})\n\n'''
    
    return index
```

glob을 통해 md 폴더에 있는 파일을 리스트를 뽑아낸다.

```python
file_list = glob.glob(dir_name)
```

각 파일의 getTime으로 최신순으로 정렬해준다.

```python
file_list.sort(key=os.path.getmtime, reverse=True)
```

for문을 사용하여 ```날짜 시간 - [제목](링크)``` 형태로 index 변수에 문자열을 추가해준다.

```python
for file_path in file_list:
        timestamp_str = time.strftime(  '%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
        file_name = file_path[5:-3]
        file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/{parse.quote(file_path[2:])}'''
        index += f'''{timestamp_str} - [{file_name}]({file_link})\n\n'''
```

마지막으로 index를 return하면 끝난다.





## Github Action 작성

여기도 동일하게 파일 먼저 공개한다.

```yml
name: Auto Update README

on:
  pull_request:
    types:
      - closed

jobs:
  if_merged:
    if: github.event.pull_request.merged == true

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run Python Script
      run: |
        python util/update-readme.py
    - name: Commit Changes
      run: |
        git add .
        git config --local user.email "tjrdud6412@naver.com"
        git config --local user.name "c9u11"
        git commit -m "📝 EDIT INDEX"
    - name: Push Commits
      run: |
        git push
```

### Action 생성 및 적용

action을 만들고자하는 repo의 action버튼을 누르면 아래와 같은 화면이 나온다.

![image](https://github.com/c9u11/development-crumbs/assets/29428714/088211cc-bdcc-43fd-a23d-d8b7cdbf87ed)

만약 기존에 다른 액션이 있다면 new workflow 버튼을 클릭하면 된다.

![image](https://github.com/c9u11/development-crumbs/assets/29428714/7f6ecb2e-1431-47c2-9364-3391be3ff057)

나는 python application을 선택하여 일부 수정했다.

![image](https://github.com/c9u11/development-crumbs/assets/29428714/9bf7f8c9-7200-427e-bb80-7a8b419ae519)

아래와 같은 editor가 나오는데 commit changes를 클릭하면 action이 적용된다.

![image](https://github.com/c9u11/development-crumbs/assets/29428714/f497fb51-fa3c-4477-9861-c0775fae70f5)

### Action yml 작성

yml 파일을 다시 보자.

```yml
name: Auto Update README

on:
  pull_request:
    types:
      - closed

jobs:
  if_merged:
    if: github.event.pull_request.merged == true

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run Python Script
      run: |
        python util/update-readme.py
    - name: Commit Changes
      run: |
        git add .
        git config --local user.email "tjrdud6412@naver.com"
        git config --local user.name "c9u11"
        git commit -m "📝 EDIT INDEX"
    - name: Push Commits
      run: |
        git push
```

대충 읽으면 어느정도 감이 오겠지만 조금 나누어서 읽어보자



**Action Name**

```yml
name: Auto Update README
```



**Trigger 조건**

나는 pull_request 요청이 왔을 때 내가 merge하면 update를 하고싶어 아래와 같이 작성했다.

closed가 되었다는 이벤트가 있을 때 merge가 되었는지 확인하여 업데이트하는 방식이다.

```yml
on:
  pull_request:
    types:
      - closed
```



**Jobs**

액션 동작이 정의되는 부분이다.

```yml
jobs:
  if_merged:
    if: github.event.pull_request.merged == true

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run Python Script
      run: |
        python util/update-readme.py
    - name: Commit Changes
      run: |
        git add .
        git config --local user.email "tjrdud6412@naver.com"
        git config --local user.name "c9u11"
        git commit -m "📝 EDIT INDEX"
    - name: Push Commits
      run: |
        git push
```

- if

  if를 통해서 merge되었는지 확인, 다른 조건은 [GitHub action doc](https://docs.github.com/ko/github-ae@latest/actions/using-workflows/events-that-trigger-workflows)을 통해서 알아보면 된다.

- Runs-on

  action 실행 환경

- steps

  차례로 실행되는 명령 모음





## Github Action Permission

### workflow permissions setting

![image](https://github.com/c9u11/development-crumbs/assets/29428714/633f6529-8e63-4688-b7cc-0491b68e7de7)
