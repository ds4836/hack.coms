import random
import colorsys

MAX_R = 255
MAX_G = 255
MAX_B = 255

def generate_scheme_type():
    num = random.randint(1,3)
    if num==1:
        return "mono"
    if num==2:
        return "ana"
    if num==3:
        return "comp"

def select_first_hue(max_R = MAX_R, max_G = MAX_G, max_B = MAX_B):
    random_rgb = (random.randint(0,max_R), random.randint(0, max_G), random.randint(0,max_B))
    print("rand", random_rgb)
    altered = change_saturation_value(random_rgb, random.randint(0,100), random.randint(0,100))
    return altered

def generate_new_color(rgb, min_hue_change, max_hue_change, max_sat_change, max_value_change):
    altered_hue = alter_hue(rgb, min_hue_change, max_hue_change)
    altered_sat_value = alter_saturation_value(altered_hue, max_sat_change, max_value_change)
    return altered_sat_value

def alter_hue(rgb, min_change, max_change):
    #may need to consider changes exceed range
    h, s, v = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    print("h,s,v: ", h,s,v)
    dir = random.choice([-1,1])
    
    change = random.randrange(min_change, max_change) / 360.0
    print("change: ", change)

    h = (h+dir*change) % 1.0

    print("h: ", h)

    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    r = r * 255
    g = g * 255
    b = b * 255
    print("alter_hue: ", r,g,b)
    return (r,g,b)
    
def change_saturation_value(rgb, saturation, value):
    h, s, v = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
    r, g, b = colorsys.hsv_to_rgb(h, saturation, value)
    return (r,g,b)

def alter_saturation_value(rgb, max_sat_change, max_value_change):
    h, s, v = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
    new_sat = random.randint(int(s+1), int(s+max_sat_change))
    new_value = random.randint(int(v+1), int(v+max_value_change))
    r, g, b = colorsys.hsv_to_rgb(h, new_sat, new_value)
    return (r,g,b)

def calculate_complementary(rgb):
    r, g, b = rgb
    return (255-r, 255-g, 255-b)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
