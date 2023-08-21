from datetime import datetime
import sys
import pytz
from urllib import parse

README_FILE_PATH = "./README.md"
INDEX_STRING = '## 부스러기 목차\n'


def format_index(pr):
    index = INDEX_STRING
    file_link = f'''https://github.com/c9u11/development-crumbs/blob/main/md/{parse.quote(pr['title'])}.md'''
    user_link = f'''https://githuc.com/{pr['user']}'''
    index += f'''{pr['datetime']} - [{pr['title']}]({file_link}) : [{pr['user']}]({user_link})\n\n'''
    return index


def get_readme_md():
    with open(README_FILE_PATH, 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


def update_readme_md(new):
    with open(README_FILE_PATH, 'w') as file:
        file.write(new)

def utc_to_korea(utc_time_str):
    utc_datetime = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ")
    korea_tz = pytz.timezone('Asia/Seoul')
    utc_datetime = pytz.utc.localize(utc_datetime)
    korea_datetime = utc_datetime.astimezone(korea_tz)
    korea_datetime = korea_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return korea_datetime

if __name__ == "__main__":
    pr = {
        'title': sys.argv[1],
        'datetime': utc_to_korea(sys.argv[2]),
        'user': sys.argv[3]
    }
    old_readme = get_readme_md()
    new_readme = old_readme.replace(INDEX_STRING, format_index(pr))
    update_readme_md(new_readme)
