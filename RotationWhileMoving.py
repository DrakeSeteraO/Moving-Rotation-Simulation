from PIL import Image
from math import floor, pi, cos, sin

def main():
    im = Image.new("L",(1000,200))
    
    degrees = float(input("What would you like the rotation speed to be?"))
    radius = float(input("What would you like the radius to be?"))
    steps = int(input("How many steps do you want there to be?"))
    
    cur_degree = 270
    x = 0
    im.putpixel((x,100),255)
    for s in range(steps):
        x += 1000/steps
        show_x = floor(x) - 1
        im.putpixel((show_x,100),255)
        
        cur_degree += degrees
        rot_degrees = (cur_degree % 360) * pi / 180
        rot_x = floor(cos(rot_degrees) * radius) + show_x
        rot_y = floor(sin(rot_degrees) * radius) + 100
        
        if 0 <= rot_x <= 999 and 0 <= rot_y < 199:
            im.putpixel((rot_x,rot_y),floor(s * 255 / steps))
        
        
    
    im.show()

    
    

if __name__ == '__main__':
    main()