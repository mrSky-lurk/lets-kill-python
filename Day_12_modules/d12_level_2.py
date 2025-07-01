# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#    generate_colors('hexa', 1) # ['#b334ef']
# ================================================================================================================
import random
import string


def get_hexa_color_code():
    hexcode = '#'
    for i in range(6):
        hexcode += random.choice(str(random.randint(0, 9)).join('abcdef'))
    return hexcode


def generate_colors(type: str, count: int):
    code_list = list()
    if type.lower() == "hexa":
        for i in range(count):
            code_list.append(get_hexa_color_code())
    else:
        code_list = get_rgb_color_code(count)
    return code_list


print(generate_colors('hexa', 3))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# ================================================================================================================

def get_rgb_color_code(count:int):
    rgb_color_list = list()
    for i in range(count):
        rgb_code = f"rgb({random.randint(0,999):03d},{random.randint(0,999):03d},{random.randint(0,999):03d})"
        rgb_color_list.append(rgb_code)
    return rgb_color_list

print(get_rgb_color_code(2))
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
# ================================================================================================================

print(generate_colors('hexa', 11))
print(generate_colors('rgb', 6))
