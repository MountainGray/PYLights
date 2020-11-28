def rgb_to_xy(red, green, blue):
    """
    Red Green and Blue must be between 0 - 1
    """
    red = ((red+0.055)/(1.0+0.055))**2.4 if red > 0.04045 else red/12.92
    green = ((green+0.055)/(1.0+0.055))**2.4 if green > 0.04045 else green/12.92
    blue = ((blue+0.055)/(1.0+0.055))**2.4 if blue > 0.04045 else blue/12.92
    X = red*0.664511 + green*0.154324 + blue*0.162027
    Y = red*0.283881 + green*0.668433 + blue*0.47685
    Z = red*0.000088 + green*0.072310 + blue*0.986039
    x = (X/(X+Y+Z))
    y = (Y/(X+Y+Z))
    return round(x, 4), round(y, 4)


def xy_to_rgb(x, y, brightness):
    """
    Pretty sure this is broken, will fix to update color before set
    """
    z = 1-x-y
    Y = brightness
    X = (Y/y)*x
    Z = (Y/y)*z
    r = X*1.656492 - Y*0.354851 - Z*0.255038
    g =-X*0.707196 + Y*1.655397 + Z*0.036152
    b = X*0.051713 - Y*0.121364 + Z*1.011530
    r = 12.92*r if r <= 0.0031308 else (1.055)*(r**(1/2.4))-0.055
    g = 12.92*g if g <= 0.0031308 else (1.055)*(r**(1/2.4))-0.055
    b = 12.92*b if b <= 0.0031308 else (1.055)*(r**(1/2.4))-0.055
    return r, g, b

#testing conversions
"""r, g, b = 1, 1, 0
x,y=rgb_to_xy(r,g,b)
print(x)
print(y)
t,h,n=xy_to_rgb(x,y,150)
print(t)
print(h)
print(n)

"""

x,y=rgb_to_xy(0,128/256,128/256)
print(x)
print(y)
r,g,b=xy_to_rgb(x, y,254)
print(r)
print(g)
print(b)