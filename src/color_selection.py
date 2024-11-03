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
    return random_rgb

def generate_new_color(rgb, min_hue_change, max_hue_change, max_sat_change, max_value_change):
    altered_hue = alter_hue(rgb, min_hue_change, max_hue_change)
    altered_sat_value = alter_saturation_value(altered_hue, max_sat_change, max_value_change)
    return altered_sat_value

def alter_hue(rgb, min_change, max_change):
    #may need to consider changes exceed range
    h, s, v = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    dir = random.choice([-1,1])

    change = random.uniform(min_change, max_change) / 360.0

    h = (h+dir*change) % 1.0

    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    return (r,g,b)

def alter_saturation_value(rgb, max_sat_change, max_value_change):
    h, s, v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
    new_sat = min(max(s + random.uniform(-max_sat_change, max_sat_change),0),1) #add direction?
    new_value = min(max(v + random.uniform(-max_value_change, max_value_change),0),1) #add direction?
    r, g, b = colorsys.hsv_to_rgb(h, new_sat, new_value)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    print(r,g,b)
    return (r,g,b)

def calculate_complementary(rgb):
    r, g, b = rgb
    return (255-r, 255-g, 255-b)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
