import requests
import urllib
from bs4 import BeautifulSoup
from collections import defaultdict
import re

def extract2():
    f = open("./영화대본모음/끝까지간다.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        if ':' in line:
            character = line.split(':')[0].rstrip()
            script = line.split(':')[1].strip()

            # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
            # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            key = character
            data[key].append(script)
    print(data)
    f.close()

def extract9():
    f = open("./영화대본모음/악마를보았다.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        if ':' in line:
            character = line.split(':')[0].rstrip()
            script = line.split(':')[1].strip()

            # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
            # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            key = character
            data[key].append(script)
    print(data)
    f.close()

def extract10():
    f = open("./영화대본모음/타짜.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break

        elif ':' in line:
            character = line.split(':')[0].rstrip()
            script = line.split(':')[1].strip()

            # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
            # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            key = character
            data[key].append(script)

        # 대본이 한줄 뛰고 이어지는 경우들 처리
        elif re.match(r'[\t]', line):
            script = line.strip()
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            data[key].append(script)

    print(data['고니'])
    f.close()

def extract11():
    f = open("./영화대본모음/파수꾼.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        if ':' in line:
            character = line.split(':')[0].rstrip()
            script = line.split(':')[1].strip()

            # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
            # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            key = character
            data[key].append(script)

    print(data)
    f.close()

def main():
    # 영화대본모음 폴더에 들어가서 모든 txt에 대해서 txt파일명 마지막 번호 읽어와서 그에 맞는 대본 processing후 db에 삽입
    extract10()

if __name__ == '__main__':
    main()
