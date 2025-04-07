def rep_char(c, n):
    print(c * n)

def draw_welcome_box(name):
    msg1 = f"Hello {name},"
    msg2 = "Welcome to Seoul."

    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char('-', nstr + 2)
    print(f"{msg1:<{nstr}}")
    print(f"{msg2:<{nstr}}")
    rep_char('-', nstr + 2)

name = input("Input his/her name: ")
draw_welcome_box(name)
