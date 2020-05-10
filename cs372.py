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


def extract3():
    def txt2json_Busan(filename):
        name_buf = ""
        say_buf = ""
        expr = ":::"
        res_dict={}

        with open(filename, 'r', encoding='utf-8') as f:
            
            for line in f.readlines():
                if expr in line and not line.split(expr)[0].strip().replace(".","").isnumeric():
                    name_buf, say_buf = line.split(expr)[0],''.join(line.split(expr)[1:])
                    say_buf = say_buf.strip('\n')
                    if name_buf in res_dict:
                        res_dict[name_buf].append(say_buf)
                    else:
                        res_dict[name_buf] = [say_buf]
                    say_buf=""
                    name_buf=""
        return res_dict
    data=txt2json_Busan("./영화대본모음/modified-부산행.txt")
    print(data)

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

def extract6():
    def txt2json_Theking(filename):
        name_buf = ""
        say_buf = ""
        say_state = False
        expr = ":::"
        
        res_dict={}
        with open(filename, 'r', encoding='utf-8') as f:
            
            for line in f.readlines():
                if expr in line:
                    name_buf, say_buf = line.split(expr)[0],line.split(expr)[1]
                    name_buf = name_buf.split(". ")[-1]
                    say_buf = say_buf.strip('\n')
                    say_state=True
                elif line.strip()!="" and say_state==True:
                    say_buf += line.strip('\n')
                elif line.strip()=="" and say_state==True:
                    say_state=False
                
                if not say_state and say_buf!="" and name_buf!="":
                    if name_buf in res_dict:
                        res_dict[name_buf].append(say_buf)
                    else:
                        res_dict[name_buf] = [say_buf]
                    say_buf=""
                    name_buf=""
        return res_dict

    data = txt2json_Theking("./영화대본모음/modified-더킹.txt")
    print(data)

def line_count(line, expr):
    res = 0
    print(line,expr)
    while expr in line:
        print("werwerw")
        res += 1
        line = line.replace(expr,'',1)
        if res > 100:
            return -1
    print(res)
    return res

def get_expr(line, expr, state):
    if not state and line_count(line,expr) == 2:
        return line[line.index(expr)+len(expr) : -(line[::-1].index(expr)+len(expr))]
    elif not state and line_count(line,expr) == 1:
        return line[line.index(expr)+len(expr) :]
    else:
        return line[: line.index(expr)+len(expr)]

def txt2json_SinsegaeAndBudang(filename):
    name_buf = ""
    say_buf = ""
    name_state = False
    say_state = False
    name_expr = ":::"
    say_expr = "&&&"
    res_dict={}
    with open(filename, 'r', encoding='utf-8') as f:
        
        for line in f.readlines():
            if not name_state and line_count(line, name_expr) >=2:
                name_buf += get_expr(line, name_expr, name_state)
                name_state = True
            elif name_state and line_count(line, say_expr) >=2:
                say_buf += get_expr(line, say_expr, say_state)
                name_state = False
            elif name_state and not say_state and line_count(line, say_expr) ==1:
                say_buf += get_expr(line, say_expr, say_state)
                say_state = True
            elif name_state and say_state and line_count(line, say_expr) ==1:
                say_buf += get_expr(line, say_expr, say_state)
                say_state = False
                name_state = False
            if not (name_state or say_state) and say_buf != "" and name_buf !="":
                if name_buf in res_dict:
                    res_dict[name_buf].append(say_buf)
                else:
                    res_dict[name_buf] = [say_buf]
                say_buf=""
                name_buf=""
    return res_dict


def extract7():
    data = txt2json_SinsegaeAndBudang("./영화대본모음/modified-신세계.txt")
    print(data)

def extract8():
    data = txt2json_SinsegaeAndBudang("./영화대본모음/modified-부당거래.txt")
    print(data)

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
