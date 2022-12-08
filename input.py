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


def name( x ):
    same_count = 0
    e = -1
    for i in range(10000):
        e += 1
        if e == 0:
            x[e].name = input('あなた(もしくは1番目の人)の名前は？\n')
        else:
            x[e].name = input( str(e + 1) + '番目の人の名前は？\n')
            
        # 空白文字のみか無記入の時に戻る
        # 参考URL：https://pg-chain.com/python-null
        if not x[e].name:
            print('エラー：名前が無記入です！')
            e -= 1
            continue
        
        # 名前の一致を判断
        for j in range(e):
            if x[j].name == x[e].name:
                print('エラー：' + x[j].name + 'の名前は既に存在します！')
                same_count = 1
                break
        
        if same_count == 1:
            same_count = 0
            e -= 1
            print('Go')
            continue


def position():
    i = 4


def say_position():
    i = 4


def executed():
    i = 4


def bitten():
    i = 4

# 入力の操作
def main():
    person_count = -1
    while (person_count < 3) or (person_count > my_function.PERSON_LIMIT):
        person_count = int(input("部屋の人数は？\n"))
    
    person = list(range(person_count))
    for i in person:
        person[i] = Person('(unclear)', '(unclear)', '(unclear)', False, False)
    
    name(person)
    # position
    # say_position
    # executed
    # bitten
    
    # person[0].name = 'Tom'
    
    
    for i in range(len(person)):
        printPerson( person[i] )