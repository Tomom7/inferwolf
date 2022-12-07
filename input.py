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

def name():
    i = 4


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
    input_person = input("部屋の人数を入力\n")
    person_count = int(input_person)
    
    person = list(range(person_count))
    for i in person:
        person[i] = Person('(unclear)', '(unclear)', '(unclear)', False, False)
    # name
    # position
    # say_position
    # executed
    # bitten
    
    person[0].name = 'Tom'
    for i in range(len(person)):
        printPerson( person[i] )