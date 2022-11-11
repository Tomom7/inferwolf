# input文が文字化けしていたため、標準出力と標準エラー出力をutf-8で出力するようにencodingを指定
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Pythonでもデータ構造が欲しいため、「dataclasses」を利用してみる
from dataclasses import dataclass

@dataclass
class Person:
    name: str = 'XXX'

    
def main():  
    # person_count = int(input("部屋の人数を入力\n"))
    
    person1 = input("名前を入力：\n")
    dataclass person1 = Person()
    Person.name = input("名前を入力：\n")

# Pythonとして実行された場合のみ、main関数を利用する
if __name__ == '__main__':
    main()