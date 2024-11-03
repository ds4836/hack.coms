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
    
def generate_rgb_constraints(blindness):
    if blindness==None:
        return (255,255,255)
    if blindness=='protan':
        return (25,150,255)
    if blindness=='deuter':
        return (190,25,255)
    if blindness=='tritan':
        return (255,255,25)

def select_first_hue(max_R = MAX_R, max_G = MAX_G, max_B = MAX_B):
    random_rgb = (random.randint(0,max_R), random.randint(0, max_G), random.randint(0,max_B))
    return random_rgb

def generate_new_color(rgb, min_hue_change, max_hue_change, max_sat_change, max_value_change,max_R,max_G,max_B):
    altered_hue = alter_hue(rgb, min_hue_change, max_hue_change,max_R,max_G,max_B)
    altered_sat_value = alter_saturation_value(altered_hue, max_sat_change, max_value_change)
    return altered_sat_value

def alter_hue(rgb, min_change, max_change, max_R = MAX_R, max_G = MAX_G, max_B = MAX_B):
    #may need to consider changes exceed range
    h, s, v = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    dir = random.choice([-1,1])

    change = random.uniform(min_change, max_change) / 360.0

    h = (h+dir*change) % 1.0

    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    if r > max_R:
        r = max_R
    if g > max_G:
        g = max_G
    if b > max_B:
        b = max_B

    return (r,g,b)

def alter_saturation_value(rgb, max_sat_change, max_value_change):
    h, s, v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
    dir = random.choice([-1,1])
    sat_change = dir * random.uniform(0.05, max_sat_change)
    value_change = dir * random.uniform(0.05, max_value_change)
    new_sat = min(max(s+sat_change,0),1)
    new_value = min(max(v + value_change,0),1)
    r, g, b = colorsys.hsv_to_rgb(h, new_sat, new_value)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    print(r,g,b)
    return (r,g,b)

def calculate_complementary(rgb):
    r, g, b = rgb
    return (255-r, 255-g, 255-b)

def check_similarity(rgb, rgb_list):
    for color in rgb_list:
        if rgb[0]==color[0] and rgb[1]==color[1] and rgb[2]==rgb[2]:
            return False
    return True
    #h, s, v = colorsys.rgb_to_hsv(rgb[0]/255,rgb[1]/255,rgb[2]/255)
    #hsv_list = []
    #for color in rgb_list:
        #h, s, v = colorsys.rgb_to_hsv(color[0]/255,color[1]/255,color[2]/255)
        #hsv_list.append((h,s,v))
    #for hsv in hsv_list:
        #if abs(h-hsv[0]) < 2/360 and abs(s-hsv[1]) < 0.05 and abs(v-hsv[2]) < 0.05:
            #return False
    #return True

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
