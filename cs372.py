import requests
import urllib
from bs4 import BeautifulSoup
from collections import defaultdict
import re


def extract1():
    f = open("./영화대본모음/건축학개론.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        elif '\t' in line:
            if line[0] != '\t':
                line = line.rstrip()
                character = line.split('\t')[0]
                script = line.split('\t')[-1]

                # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
                # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
                while '(' in script:
                    script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
                script = script.strip()
                key = character
                if script == '':
                    continue
                else:
                    data[key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    print(data)

def extract2():
    f = open("./영화대본모음/끝까지간다.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break

        elif '\t' in line:
            # 그냥 빈칸들인 경우 스킵
            if line.isspace():
                continue

            # 대본이후 \t 가 들어간 경우 처리 rstrip()
            elif line[0] != '\t':
                line = line.rstrip()
                character = line.split('\t')[0]
                script = line.split('\t')[-1]

                # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
                # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
                while '(' in script:
                    script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
                script = script.strip()

                # 대본이 ()만이였을경우 () 제거후 빈공백이므로 이는 대사에 추가하지 않는다.
                if script == '':
                    continue
                else:
                    key = character
                    data[key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()

                # 대본이 ()만이였을경우 () 제거후 빈공백이므로 이는 대사에 추가하지 않는다.
                if script == '':
                    continue
                else:
                    data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    print(data)
    f.close()

def extract4():
    f = open("./영화대본모음/써니.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    key = None
    key_check = False
    while True:
        line = f.readline()
        if not line:
            break
        if "     " in line :
            if line[0] != " ":
                first_space = line.find(" ")
                script_begin = first_space
                while(line[script_begin]==" "):
                    script_begin = script_begin + 1
                character = line[0:first_space]
                script = line[script_begin:]

                # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
                # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
                #while '(' in script:
                #    script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
                script = script.strip()
                key = character
                key_check = True
                if script == '':
                    continue
                else:
                    data[key].append(script)

            elif key_check == True:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                #while '(' in line:
                #    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    data[key].append(script)
        else :
            key_check = False

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    # 대본에서 괄호 제거
    data2 = defaultdict(list)
    for key in data:
        for script in data[key]:
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            if script == '':
                continue
            else:
                data2[key].append(script)
    f.close()
    print(data2)

def extract9():
    f = open("./영화대본모음/악마를보았다.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break

        elif ':' in line:
            character = line.split(':')[0].rstrip()
            script = line.split(':')[1].strip()

            if '(' in line:
                if ')' not in line:
                    script = script.split('(')[0]
            if ')' in line:
                if '(' not in line:
                    script = script.split(')')[1]

            # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
            # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            key = character
            if script == '':
                continue
            else:
                key = character
                data[key].append(script)

        # 대본이 한줄 뛰고 이어지는 경우들 처리
        elif re.match(r'[\t]', line):
            script = line.strip()
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            if script == '':
                continue
            else:
                data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

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
            if script == '':
                continue
            else:
                key = character
                data[key].append(script)

        # 대본이 한줄 뛰고 이어지는 경우들 처리
        elif re.match(r'[\t]', line):
            script = line.strip()
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            if script == '':
                continue
            else:
                data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    print(data)
    f.close()

# 등장인물 : ... 이런것들 현재 삽입되어있음
def extract11():
    f = open("./영화대본모음/파수꾼.txt", 'rt', encoding='UTF8')
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
            if script == '':
                continue
            else:
                key = character
                data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    print(data)
    f.close()

def extract12():
    f = open("./영화대본모음/신의한수.txt", 'rt', encoding='UTF8')
    data = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        elif '\t' in line and line[0] != '-':
            if line[0] != '\t':
                line = line.rstrip()
                character = line.split('\t')[0]
                script = line.split('\t')[-1]

                # (혼잣말하듯) 이러한 행동지시 ()부분을 모두 대본에서 지운다
                # script = re.sub('', '', script) 이거 쓸수 있으면 이거 쓰는게 좋을듯
                while '(' in script:
                    script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
                script = script.strip()
                key = character
                if script == '':
                    continue
                else:
                    script = script.replace('\t', '')
                    data[key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    script = script.replace('\t', '')
                    data[key].append(script)

    # 대본이 10개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    print(data)

def main():
    # 영화대본모음 폴더에 들어가서 모든 txt에 대해서 txt파일명 마지막 번호 읽어와서 그에 맞는 대본 processing후 db에 삽입
    extract11()

if __name__ == '__main__':
    main()
