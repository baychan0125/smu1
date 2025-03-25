def get_radius(prompt) :
    r = int(input(prompt))
    return r
def get_circle_area(rad) :
    area = 3.14 * rad * rad
    return area
rad = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
area = get_circle_area(rad)
print('반지름', rad,'인 원의 넓이 = 3.14 *', rad, '*', rad, '=', area)
