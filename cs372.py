from nltk import *
import requests
import urllib
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import os
from konlpy.tag import Okt as Tagger
from Make_Trainset import *
import random

tagger = Tagger()

def extract01():
    f = open("./영화대본모음/건축학개론01.txt", 'rt', encoding='UTF8')
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
                    data['건축학개론 ' + key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    data['건축학개론 ' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    return data

def extract02():
    f = open("./영화대본모음/끝까지간다02.txt", 'rt', encoding='UTF8')
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
                    data['끝까지간다 ' + key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()

                # 대본이 ()만이였을경우 () 제거후 빈공백이므로 이는 대사에 추가하지 않는다.
                if script == '':
                    continue
                else:
                    data['끝까지간다' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    return data


def remv_motion(line):
    if '(' in line and ')' in line:
        return remv_motion(line[:line.index('(')]+line[line.index(')')+1:])

    return line

def extract03():
    def txt2json_Busan(filename):
        name_buf = ""
        say_buf = ""
        expr = ":::"
        res_dict=defaultdict(list)

        with open(filename, 'r', encoding='utf-8') as f:

            for line in f.readlines():
                if expr in line and not line.split(expr)[0].strip().replace(".","").isnumeric():
                    name_buf, say_buf = line.split(expr)[0],''.join(line.split(expr)[1:])
                    say_buf = remv_motion(say_buf.strip('\n'))
                    res_dict['부산행 ' + name_buf].append(say_buf)

                    say_buf=""
                    name_buf=""
        return res_dict
    data=txt2json_Busan("./영화대본모음/부산행03.txt")

    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]
    return data


def extract04():
    f = open("./영화대본모음/써니04.txt", 'rt', encoding='UTF8')
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
                    data['써니 ' + key].append(script)

            elif key_check == True:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                #while '(' in line:
                #    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    data['써니 ' + key].append(script)
        else :
            key_check = False

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
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
    return data2

def extract05():
    def txt2json_Theking(filename):
        name_buf = ""
        say_buf = ""
        say_state = False
        expr = ":::"

        res_dict=defaultdict(list)
        with open(filename, 'r', encoding='utf-8') as f:

            for line in f.readlines():
                if expr in line:
                    name_buf, say_buf = line.split(expr)[0],line.split(expr)[1]
                    name_buf = name_buf.split(". ")[-1]
                    say_buf = remv_motion(say_buf.strip('\n'))
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

        return(res_dict)

    data = txt2json_Theking("./영화대본모음/더킹05.txt")
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    keys = list(data.keys())
    for i in range(len(keys)):
        data['더킹 ' + keys[i]] = data.pop(keys[i])
    return data

def line_count(line, expr):
    res = 0
    while expr in line:
        res += 1
        line = line.replace(expr,'',1)
        if res > 100:
            return -1
    return res

def get_expr(line, expr, state):
    if line_count(line,expr) == 2:
        return line[line.index(expr)+len(expr) : -(line[::-1].index(expr)+len(expr))]
    elif not state and line_count(line,expr) == 1:
        return line[line.index(expr)+len(expr) :]
    elif line_count(line,expr) == 1:
        return line[: line.index(expr)+len(expr)]
    else:
        return ""

def txt2json_SinsegaeAndBudang(filename):
    name_buf = ""
    say_buf = ""
    name_state = False
    say_state = False
    name_expr = ":::"
    say_expr = "&&&"
    res_dict=defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as f:

        for line in f.readlines():
            if not name_state and line_count(line, name_expr) >=2:
                name_buf += get_expr(line, name_expr, name_state)
                name_state = True
            elif name_state and line_count(line, say_expr) >=2:
                say_buf += remv_motion(get_expr(line, say_expr, say_state))
                say_state = True
            elif name_state and not say_state and line_count(line, say_expr) ==1:
                say_buf += remv_motion(get_expr(line, say_expr, say_state))
                say_state = True
            elif name_state and say_state and line_count(line, say_expr) ==1:
                say_buf += remv_motion(get_expr(line, say_expr, say_state))
            elif name_state and say_state and line_count(line, say_expr) ==0:
                say_state = False
                name_state = False

            if not (name_state or say_state) and say_buf != "" and name_buf !="":
                res_dict[name_buf].append(say_buf)
                say_buf=""
                name_buf=""
    return(res_dict)


def extract06():
    data = txt2json_SinsegaeAndBudang("./영화대본모음/신세계06.txt")
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    keys = list(data.keys())
    for i in range(len(keys)):
        data['신세계 ' + keys[i]] = data.pop(keys[i])
    return data

def extract07():
    data = txt2json_SinsegaeAndBudang("./영화대본모음/부당거래07.txt")
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    keys = list(data.keys())
    for i in range(len(keys)):
        data['부당거래 ' + keys[i]] = data.pop(keys[i])
    return data

def extract08():
    f = open("./영화대본모음/악마를보았다08.txt", 'rt', encoding='UTF8')
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
                data['악마를보았다 ' + key].append(script)

        # 대본이 한줄 뛰고 이어지는 경우들 처리
        elif re.match(r'[\t]', line):
            script = line.strip()
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            if script == '':
                continue
            else:
                data['악마를보았다 ' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    return data

def extract09():
    f = open("./영화대본모음/타짜09.txt", 'rt', encoding='UTF8')
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
                data['타짜 ' + key].append(script)

        # 대본이 한줄 뛰고 이어지는 경우들 처리
        elif re.match(r'[\t]', line):
            script = line.strip()
            while '(' in script:
                script = script.split('(')[0] + script.replace(script.split(')')[0] + ')', '')
            script = script.strip()
            if script == '':
                continue
            else:
                data['타짜 ' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    return data

# 등장인물 : ... 이런것들 현재 삽입되어있음
def extract10():
    f = open("./영화대본모음/파수꾼10.txt", 'rt', encoding='UTF8')
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
                data['파수꾼 ' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    return data
    f.close()

def extract11():
    f = open("./영화대본모음/신의한수11.txt", 'rt', encoding='UTF8')
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
                    data['신의한수 ' + key].append(script)

            else:
                # 대본이 한줄 뛰고 이어지는 경우들 처리
                while '(' in line:
                    line = line.split('(')[0] + line.replace(line.split(')')[0] + ')', '')
                script = line.strip()
                if script == '':
                    continue
                else:
                    script = script.replace('\t', '')
                    data['신의한수 ' + key].append(script)

    # 대본이 20개 이하인 중요하지 않은 인물들 dictionary key 에서 제외
    useless = []
    for key in data:
        if len(data[key]) < 20:
            useless.append(key)
    for character in useless:
        del data[character]

    f.close()
    return data

def extract_call(index):
    switcher = {'01' : extract01, '02' : extract02, '03' : extract03, '04' : extract04, '05' : extract05, '06' : extract06, '07' : extract07, '08' : extract08, '09' : extract09, '10' : extract10, '11' : extract11}
    func = switcher.get(index, lambda index: invalid(index))
    return func()


#######################################
def feature1(data):
    # 말 끝을 흐리는지
    dic = defaultdict(int)
    for person in data:
        num = 0
        for script in data[person]:
            if script[-1] == '.' and script[-2] == '.':
                num = num + 1
        dic[person] = num
    return dic

def feature2(data):
    dic = defaultdict(None)
    for person in data:
        l = 0
        num = 0
        for script in data[person]:
            l = l + len(script)
            num = num + 1
        dic[person] = l/num
    return dic

def feature3(data):  #어휘 복잡도
    dic = defaultdict(int)
    for person in data:
        
        ratio = 0
        for script in data[person]:
            words = script.split(' ')
            words_unique = set(words)
            ratio = ratio + (len(words_unique)/len(words))
            
        ratio = ratio / len(data[person])
        dic[person] = ratio
        
    return dic


# 의문문?, 감탄문!개수
# 효진
def feature4(data):
    dic = defaultdict(int)
    for person in data:
        num = 0
        for script in data[person]:
            if '?' in script or '!' in script:
                num = num + 1
        dic[person] = num
    return dic

def person_feat_score(script_ls, feature):
    score = 0
    for line in script_ls:
        score += feature(line)
        # print(f'score: {score}')
    return round(score/len(script_ls),2)


def dict_feat_score(ddict, feature):
    res_dict=defaultdict()
    for p in ddict:
        res_dict[p] = person_feat_score(ddict[p], feature)
    return res_dict

def feature5_extractor(sc):
    # 수식어구를 많이 사용하는가??
    # 재진
    # 나누기 문장 단어수
    sc_tagged = tagger.pos(sc)
    res = filter(lambda a: a[-1] in ['Adjective','Adverb'], sc_tagged)
    return len(list(res))/len(sc.split())

def feature5(data):
    return dict_feat_score(data, feature5_extractor)

# 복잡한 문장 사용(chunker) tree height
#def feature6(data):

def evaluate(data, centroids, labels, ref=None):
# DB 인물의 문장 n개를 뽑아와서 feature extraction -> cluster를 거쳤을 때 제대로 된 cluster에 들어가는지 확인
    characters = list(data.keys())
    testIndex = random.randrange(len(characters))
    character = characters[testIndex]
    allSent = data[character]
    # randomSent 에는 random character의 20개의 문장이 들어간다.
    randomSent = random.sample(allSent, 20)

    database = defaultdict(list)
    for sent in randomSent:
        database[character].append(sent)

    all_lst = []
    feature_dics = []
    feature_dics.append(feature1(database))
    feature_dics.append(feature2(database))
    feature_dics.append(feature3(database))
    feature_dics.append(feature4(database))
    feature_dics.append(feature5(database))
    lst = []
    for dic in feature_dics:
        lst.append(dic[character])
    all_lst.append(lst)

    if ref:
        des = normalizer(np.array(all_lst + ref))[:len(all_lst)]
    else:
        des = normalizer(np.array(all_lst))
    # 현재 des [[ 0.15       19.4         0.10798122  0.35      ]] 이런식으로 들어가있음

    print(all_lst + ref)
    exit()
    label = get_labels(des, centroids)

    # print("In evaluating process")
    if (label[0] == labels[testIndex]):
        # print("Correctly Clusterd")
        return 1
    else:
        # print("UnCorrectly Clustered")
        return 0


def test(centroids):
    f = open("./testset.txt", 'rt', encoding='UTF8')
    database = defaultdict(list)
    while True:
        line = f.readline()
        if not line:
            break
        if line in ['\n', '\r\n']:
            continue
        elif line.startswith('등장인물'):
            key = line.split(':')[1].strip()
        else:
            database[key].append(line.rstrip())

    all_lst = []
    feature_dics = []
    feature_dics.append(feature1(database))
    feature_dics.append(feature2(database))
    feature_dics.append(feature3(database))
    feature_dics.append(feature4(database))
    feature_dics.append(feature5(database))

    characters = list(database.keys())
    for character in characters:
        lst = []
        for dic in feature_dics:
            lst.append(dic[character])
        all_lst.append(lst)

    des = np.array(all_lst)

    label = get_labels(des, centroids)
    print(label)
    for i in range(len(characters)):
        print("Test 데이타 {0}는 {1}번재 클러스터로 분류됨".format(characters[i], label[i]))

    f.close()


def main():
    # 영화대본모음 폴더의 모든 txt에 대해서 txt파일명 마지막 번호 읽어와서 그에 맞는 대본 processing후 db에 삽입
    database = defaultdict(list)
    files = []
    path = './영화대본모음'
    for i in os.listdir(path):
        if i.endswith('.txt'):
            files.append(i)

    for file in files:
        database.update(extract_call(file[-6:-4]))

    all_lst = []
    feature_dics = []
    feature_dics.append(feature1(database))
    feature_dics.append(feature2(database))
    feature_dics.append(feature3(database))
    feature_dics.append(feature4(database))
    feature_dics.append(feature5(database))
    for person in database:
        lst = []
        for dic in feature_dics:
            lst.append(dic[person])
        all_lst.append(lst)

    des = normalizer(np.array(all_lst))
    centroids = get_cluster(des, 5, 1e-1)
    labels = get_labels(des, centroids)

    print(f'centroids: {centroids}')
    print(f'labels: {labels}')
    
    for i, key in enumerate(database.keys()):
        print("name:", key)
        print("label:", labels[i])
    
    

    # evaluate(database, centroids, labels, ref=all_lst)
    score = 0
    for i in range(100):
        score += evaluate(database, centroids, labels, ref=all_lst)

    #나중에 만약 더 정교한 f_score가 필요한 경우 sklearn.metrics import confusion_matrix 이용
    print("Evaluation 정확도 : {0}%".format(score))

    # test(centroids)
if __name__ == '__main__':
    main()
