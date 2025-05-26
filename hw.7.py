def main():
    cart = {}

    print("[구입]")
    while True:
        item = input("상품명? ")
        if item == "":
            break
        qty = int(input("수량은? "))

        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty

        print(f"장바구니에 {item} {qty}개가 담겼습니다.\n")

    print(f"\n>>> 장바구니 보기: {cart}\n")

    print("[검색]")
    search = input("장바구니에서 확인하고자 하는 상품은? ")
    if search in cart:
        print(f"{search}는(은) {cart[search]}개 담겨 있습니다.")
    else:
        print(f"{search}는(은) 장바구니에 없습니다.")

if __name__ == "__main__":
    main()
