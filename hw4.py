def get_fixed_price(per, price) :
    fixed = price / (1 - per / 100)
    return fixed

rate = int(input('할인율은? '))
aprice = int(input('a의 할인된 가격은? '))
bprice = int(input('b의 할인된 가격은? '))

afixed = get_fixed_price(rate, aprice)
print('a상품의 정가는? ', afixed, '원')
bfixed = get_fixed_price(rate, bprice)
print('b상품의 정가는? ', bfixed, '원')
