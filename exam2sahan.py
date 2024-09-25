def rgb_to_hex(rgb):
    hex_string = "#"
    red_hex_remainder = rgb["R"]%16
    red_hex_floor = rgb["R"]//16
    blue_hex_remainder = rgb["B"] % 16
    blue_hex_floor = rgb["B"] // 16
    green_hex_remainder = rgb["G"] % 16
    green_hex_floor = rgb["G"] // 16
    if red_hex_floor == 10:
        hex_string += "A"
    elif red_hex_floor == 11:
        hex_string += "B"
    elif red_hex_floor == 12:
        hex_string += "C"
    elif red_hex_floor == 13:
        hex_string += "D"
    elif red_hex_floor == 14:
        hex_string += "E"
    elif red_hex_floor == 15:
        hex_string += "F"
    else:
        hex_string += str(red_hex_floor)
    if red_hex_remainder == 10:
        hex_string += "A"
    elif red_hex_remainder == 11:
        hex_string += "B"
    elif red_hex_remainder == 12:
        hex_string += "C"
    elif red_hex_remainder == 13:
        hex_string += "D"
    elif red_hex_remainder == 14:
        hex_string += "E"
    elif red_hex_remainder == 15:
        hex_string += "F"
    else :
        hex_string += str(red_hex_remainder)
    if green_hex_floor == 10:
        hex_string += "A"
    elif green_hex_floor == 11:
        hex_string += "B"
    elif green_hex_floor == 12:
        hex_string += "C"
    elif green_hex_floor == 13:
        hex_string += "D"
    elif green_hex_floor == 14:
        hex_string += "E"
    elif green_hex_floor == 15:
        hex_string += "F"
    else:
        hex_string += str(green_hex_floor)
    if green_hex_remainder == 10:
        hex_string += "A"
    elif green_hex_remainder == 11:
        hex_string += "B"
    elif green_hex_remainder == 12:
        hex_string += "C"
    elif green_hex_remainder == 13:
        hex_string += "D"
    elif green_hex_remainder == 14:
        hex_string += "E"
    elif green_hex_remainder == 15:
        hex_string += "F"

    else:
        hex_string += str(green_hex_remainder)
    if blue_hex_floor == 10:
        hex_string += "A"
    elif blue_hex_floor == 11:
        hex_string += "B"
    elif blue_hex_floor == 12:
        hex_string += "C"
    elif blue_hex_floor == 13:
        hex_string += "D"
    elif blue_hex_floor == 14:
        hex_string += "E"
    elif blue_hex_floor == 15:
        hex_string += "F"
    else:
        hex_string += str(blue_hex_floor)
    if blue_hex_remainder == 10:
        hex_string += "A"
    elif blue_hex_remainder == 11:
        hex_string += "B"
    elif blue_hex_remainder == 12:
        hex_string += "C"
    elif blue_hex_remainder == 13:
        hex_string += "D"
    elif blue_hex_remainder == 14:
        hex_string += "E"
    elif blue_hex_remainder == 15:
        hex_string += "F"
    else:
        hex_string += str(blue_hex_remainder)
    return hex_string


while True :
    quit_module = input(("enter the value of red(press q or quit to quit):"))
    if quit_module == "q" :
        break
    else:
        red_value = int(quit_module)
        if red_value < 256:
            green_value = int(input(("enter the value of green:")))
            blue_value = int(input(("enter the value of blue:")))
            color_dict = {"R": red_value, "G": green_value, "B": blue_value}
            hex_color_value=rgb_to_hex(color_dict)
            print(hex_color_value)
        else:
            print("make your value less than 256")
            continue



