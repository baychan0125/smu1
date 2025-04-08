def read_single_digit(d):
    if d == '0':
        return '영'
    elif d == '1':
        return '일'
    elif d == '2':
        return '이'
    elif d == '3':
        return '삼'
    elif d == '4':
        return '사'
    elif d == '5':
        return '오'
    elif d == '6':
        return '육'
    elif d == '7':
        return '칠'
    elif d == '8':
        return '팔'
    elif d == '9':
        return '구'
    else:
        return ''

def read_number(number):
    print(read_single_digit(number[0]), read_single_digit(number[1]), read_single_digit(number[2]))

num = input("세 자리 정수 입력: ")
read_number(num)
