def calculate_area(radius):
    area = 3.1415 * radius ** 2
    return area

radius = float(input("请输入半径: "))
area = calculate_area(radius)
print("面积为:", area)
