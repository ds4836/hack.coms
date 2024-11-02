from color_selection import *

def main():
    used_colors = []
    comp = None
    type = generate_scheme_type()

    if type=='mono' or type=='comp':
        min_hue_change = 0
        max_hue_change = 5
    else:
        min_hue_change = 15
        max_hue_change = 50

    max_sat_change = 10
    max_value_change = 10
    
    first = select_first_hue()
    used_colors.append(first)

    if type=='mono' or type=='ana':
        for _ in range(0,4):
            new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change)
            #must check similarities and color sensitivity
            used_colors.append(new_color)

    if type=='comp':
        comp = calculate_complementary(first)
        for _ in range(0,2):
            new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change)
            #must check similarities and color sensitivity
            used_colors.append(new_color)
        used_colors.append(comp) #CHANGE SAT AND VALUE
        for _ in range(0,2):
            new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change)
            #must check similarities and color sensitivity
            used_colors.append(new_color)

    for color in used_colors:
        print(color)


if __name__ == '__main__':
    main()