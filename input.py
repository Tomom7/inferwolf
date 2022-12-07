# Pythonでもデータ構造が欲しいため、「dataclasses」を利用してみる
from dataclasses import dataclass

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
    # 入力には制限(1以上?以下の整数)が必要。
    input_person = input("部屋の人数は？\n")
    person_count = int(input_person)
    
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