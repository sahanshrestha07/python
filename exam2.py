


def rgb_to_cmyk (color_dict):
    red_prime = color_dict['R']/255
    green_prime = color_dict['G']/255
    blue_prime = color_dict['B']/255
    k_prime = 1-max(red_prime,green_prime,blue_prime)
    c = round(((1-red_prime-k_prime)/(1-k_prime))*100)
    m = round(((1 - green_prime - k_prime) / (1 - k_prime)) * 100)
    y = round(((1 - blue_prime - k_prime) / (1 - k_prime)) * 100)
    k = round(k_prime*100)
    cmyk_dict = {"C" : c, "M" : m, "Y" : y, "K" : k}
    return cmyk_dict

while True:
    print("RGB To CMYK Converter")
    red_value = input("Enter the Red Color Value (enter quit or q) :")
    if red_value == "q"or red_value == "quit":
        break
    else:
        green_value = input("Enter the green Color Value :")
        blue_value = input("Enter the blue Color Value :")
        rgb_dict = {
            "R": float(red_value),
            "G": float(green_value),
            "B": float(blue_value)
        }
        equivalent_CMYK_value = rgb_to_cmyk(rgb_dict)
        print("CMYK values")
        print(f"Cyan ={equivalent_CMYK_value['C']}")
        print(f"Magenta ={equivalent_CMYK_value['M']}")
        print(f"Yellow ={equivalent_CMYK_value['Y']}")
        print(f"Key (Black) ={equivalent_CMYK_value['K']}")




