import requests
import urllib
from bs4 import BeautifulSoup
from collections import defaultdict
import re

def main():
    f = open("./타짜.txt", 'rt', encoding='UTF8')
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

if __name__ == '__main__':
    main()
