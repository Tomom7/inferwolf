# Pythonでもデータ構造が欲しいため、「dataclasses」を利用してみる
from dataclasses import dataclass

import my_function


@dataclass
# 各人物の情報の構造体
class Person:
    name: str 
    position: str 
    say_position: str 
    executed: bool 
    bitten: bool

# 断定されていない役職や行動者の数情報の構造体
class Remain:
    all: int
    villager: int
    seer: int
    werewolf: int
    say_seer: int

# "class Remain"　で仮定推理する際の退避構造体
class Remain_tmp:
    all: int
    villager: int
    seer: int
    werewolf: int
    say_seer: int

def printPerson( e ):
    print( '名前:' + str(e.name) + ',' + '役職:' + str(e.position) + ',' + '宣言役職:' + str(e.say_position))


def name(x, person_count):
    i = 0
    while True:
        if i == 0:
            x[i].name = input('あなた(もしくは1番目の人)の名前は？\n')
        else:
            x[i].name = input( str(i + 1) + '番目の人の名前は？\n')
            
        # 空白文字のみか無記入の時に戻る
        # 参考URL：https://pg-chain.com/python-null
        if not x[i].name:
            print('エラー：名前が無記入です！')
            i -= 1
        
        else:    
            # 名前の一致を判断
            for j in range(i):
                if x[j].name == x[i].name:
                    print('エラー：' + x[i].name + 'の名前は既に存在します！')
                    i -= 1
        
        # 終わりか判断
        if i == person_count - 1:
            break
        i += 1


def position():
    pass


def say_position():
    pass


def executed():
    pass


def bitten():
    pass

# 入力の操作
def main():
    person_count = -1
    while (person_count < 3) or (person_count > my_function.PERSON_LIMIT):
            raw_person_count = input("部屋の人数は？\n")
            # 数値以外は省く
            if str.isdecimal(raw_person_count) == False:
                continue
            person_count = int(raw_person_count)
    
    person = list(range(person_count))
    for i in person:
        person[i] = Person('(unclear)', '(unclear)', '(unclear)', False, False)
    
    name(person, person_count)
    # position
    # say_position
    # executed
    # bitten
    
    # person[0].name = 'Tom'
    
    
    for i in range(len(person)):
        printPerson( person[i] )