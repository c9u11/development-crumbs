import glob
import os
import time
import sys
from urllib import parse

README_FILE_PATH = "./README.md"
INDEX_STRING = '## 부스러기 목차\n'


def format_index(pr):
    index = INDEX_STRING
    file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/{pr['title']}'''
    index += f'''{pr['datetime']} - [{pr['title']}]({parse.quote(file_link)}) : {pr['user']}\n\n'''

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
        'datetime': sys.argv[2],
        'user': sys.argv[3]
    }
    old_readme = get_readme_md()
    new_readme = old_readme.replace(INDEX_STRING, format_index(pr))
    update_readme_md(new_readme)
