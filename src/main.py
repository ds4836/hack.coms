import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.color_selection import *
from gui import display_colors

def main(selection=None):
    blindness = selection
    max_R, max_G, max_B = generate_rgb_constraints(blindness)
    used_colors = []
    comp = None
    type = generate_scheme_type()

    if type=='mono' or type=='comp':
        min_hue_change = 6
        max_hue_change = 10
    else:
        min_hue_change = 15
        max_hue_change = 50

    max_sat_change = 0.3
    max_value_change = 0.2
    
    first = select_first_hue(max_R,max_G,max_B)
    used_colors.append(first)

    if type=='mono' or type=='ana':
        for _ in range(0,4):
            while True:
                new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change,max_R,max_G,max_B)
                if check_similarity(new_color, used_colors):
                    used_colors.append(new_color)
                    break

    if type=='comp':
        comp = calculate_complementary(first)
        for _ in range(0,2):
            while True:
                new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change,max_R,max_G,max_B)
                if check_similarity(new_color, used_colors):
                    used_colors.append(new_color)
                    break
        new = alter_saturation_value(comp, max_sat_change, max_value_change)
        print("new: ", new)
        used_colors.append(new)
        while True:
                new_color = generate_new_color(used_colors[-1], min_hue_change, max_hue_change, max_sat_change, max_value_change,max_R,max_G,max_B)
                if check_similarity(new_color, used_colors):
                    used_colors.append(new_color)
                    break

    print(blindness)
    return(used_colors)
    #display_colors(used_colors)
