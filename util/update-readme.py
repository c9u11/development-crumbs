import glob
import os
import time
from urllib import parse

def make_index():
    index = ""
    dir_name = './md/*'
    file_list = glob.glob(dir_name)
    
    for file_path in file_list:
        timestamp_str = time.strftime(  '%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
        file_name = file_path[5:-3]
        file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/{parse.quote(file_path[2:])}'''
        index += f'''{timestamp_str} - [{file_name}]({file_link})\n'''
    
    return index


def make_read_me(index):
    return f"""
# 개발 부스러기

남들이 먹고 남긴 개발 부스러기를 주워 먹읍시다.



## 부스러기 목차
{index}



## [부스러기 나눔](https://github.com/c9u11/development-crumbs/blob/main/%EA%B0%9C%EB%B0%9C%20%EB%B6%80%EC%8A%A4%EB%9F%AC%EA%B8%B0%20%EB%82%98%EB%88%94%20%EB%B0%A9%EB%B2%95.md)

먹다 남긴 개발 부스러기가 있다면 나눠주세요.

어떠한 향과 맛 상관없습니다. 감사합니다.

1. 포장지를 받습니다. (Fork the Project)
2. 개발 부스러기를 모읍니다. (Write .md File)
3. 개발 부스러기를 포장합니다. (Commit your Changes)
4. 포장한 부스러기를 문 앞에 놓으세요. (Push to the Branch)
5. 나눔 신청을 통해 모두에게 나누어주세요. (Open a Pull Request)
"""


def update_readme_md():
    return make_read_me(make_index())

if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)