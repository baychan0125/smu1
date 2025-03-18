def exchange(cost):
    n500 = cost // 500
    n100 = (cost - (n500 * 500)) // 100
    n50 = (cost - (n500 * 500) - (n100 * 100)) // 50
    n10 = (cost - (n500 * 500) - (n100 * 100) - (n50 * 50)) // 10

    print('500원 동전의 개수:', n500)
    print('10원 동전의 개수: ', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)

def get_integer(put):
    return int(input(put))

cost = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(cost)
