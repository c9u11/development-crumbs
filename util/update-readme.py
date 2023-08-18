import glob
import os
import time
import sys
from urllib import parse

README_FILE_PATH = "./README.md"
INDEX_STRING = '## 부스러기 목차\n'


def format_index(pr):
    index = INDEX_STRING
    index += f'''{pr['datetime']} - [{pr['title']}]({pr['body']}) : {pr['user']}\n\n'''

    return index


def get_readme_md():
    with open(README_FILE_PATH, 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


def update_readme_md(new):
    with open(README_FILE_PATH, 'w') as file:
        file.write(new)


if __name__ == "__main__":
    pr = {
        'title': sys.argv[1],
        'body': sys.argv[2],
        'datetime': sys.argv[3],
        'user': sys.argv[4]
    }
    old_readme = get_readme_md()
    new_readme = old_readme.replace(INDEX_STRING, format_index(pr))
    update_readme_md(new_readme)
