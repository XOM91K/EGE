#Фукциональное программирование
def get_cube_3(number):
    if len(str(number ** 3)) == 3:
        return True
    return False

print(get_cube_3(9))
