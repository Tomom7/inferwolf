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
    for i in range(len(x)):
        if i == 0:
            x[i].name = input("あなた(もしくは1番目の人)の名前は？\n")
        else:
            x[i].name = input( str(i) + "番目の人の名前は？\n")
            
        # TODO:　無記入、名前の重複（できればスペースのみ）にエラーを出す


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