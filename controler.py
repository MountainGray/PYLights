from bridge import BRIDGE

"""
this file is for direct testing, control flow should be set up later
"""
home = BRIDGE()


print(home.ip)

def rgb_to_xy(red, green,blue):
    red= ((red+0.055)/(1.0+0.055))**2.4 if red>0.04045 else red/12.92
    green= ((green+0.055)/(1.0+0.055))**2.4 if green>0.04045 else green/12.92
    blue= ((blue+0.055)/(1.0+0.055))**2.4 if blue>0.04045 else blue/12.92
    X=red*0.664511 + green * 0.154324 + blue* 0.162027
    Y=red*0.283881 + green * 0.668433 + blue*0.47685
    Z=red*0.000088 + green*0.072310 + blue*0.986039
    x=(X/(X+Y+Z))
    y=(Y/(X+Y+Z))
    return x,y