# input文が文字化けしていたため、標準出力と標準エラー出力をutf-8で出力するようにencodingを指定
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


import input


def main():  

    input.main()


# Pythonとして実行された場合のみ、main関数を利用する
if __name__ == '__main__':
    main()