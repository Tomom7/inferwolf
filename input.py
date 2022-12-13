# Pythonでもデータ構造が欲しいため、「dataclasses」を利用してみる
from dataclasses import dataclass

import my_function


@dataclass
class Person:
    name: str 
    position: str 
    say_position: str 
    executed: bool 
    bitten: bool


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
        person_count = int(input("部屋の人数は？\n"))
    
    person = list(range(person_count))
    for k in person:
        person[k] = Person('(unclear)', '(unclear)', '(unclear)', False, False)
    
    name(person, person_count)
    # position
    # say_position
    # executed
    # bitten
    
    # person[0].name = 'Tom'
    
    
    for k in range(len(person)):
        printPerson( person[k] )