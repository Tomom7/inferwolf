# input文が文字化けしていたため、標準出力と標準エラー出力をutf-8で出力するようにencodingを指定
import os

import io, sys
from flask import Flask, flash, redirect, render_template, request, session
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import input

# Pythonでもデータ構造が欲しいため、「dataclasses」を利用してみる
from dataclasses import dataclass


# Flaskのおまじない
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@dataclass
class Person:
    name: str 
    position: str 
    say_position: str 
    executed: bool 
    bitten: bool

def printPerson( e ):
    print( '名前:' + str(e.name) + ',' + '役職:' + str(e.position) + ',' + '宣言役職:' + str(e.say_position))


@app.route('/')  
def main():  
    return render_template('input.html')


    person_count = (int(input("部屋の人数を入力\n")))
    
    person = list(range(person_count))
    for i in person:
        person[i] = Person('(unclear)', '(unclear)', '(unclear)', False, False)
        
    input.main
    person[0].name = 'Tom'
    for i in range(len(person)):
        printPerson( person[i] )

# Pythonとして実行された場合のみ、main関数を利用する
if __name__ == '__main__':
    app.run(debug=True, port=5000)