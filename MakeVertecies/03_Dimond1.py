# This program calculate first Dimond vertecies
#       and put them in clipboard
from math import *
number_of_dots = 8
r = -0.102 # distance from center of bracelet


thicknes_in_r = 0.01 # radius in in Dimond in first circle
thicknes_in_y = thicknes_in_r
bo = -1
inc = True
y = -thicknes_in_y*2/3+r

center_x=0.5+0.125
center_y=1-0.125
#1
res = "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(0.0,y,0.0,255.0,255.0,255.0,0.0,y,0.0,center_x,center_y)
y = -thicknes_in_y/2+r
for i in range(number_of_dots):#8
    T = (i+1)*2*pi/number_of_dots
    x =thicknes_in_r*sin(T)
    z =thicknes_in_r*cos(T)
    y = -thicknes_in_y/2+r
    res +="Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(x,y,z,255.0,255.0,255.0,x,y,z,center_x+cos(T)/8,center_y+sin(T)/8)
for i in range(number_of_dots):#8
    T = (i+1)*2*pi/number_of_dots
    x =thicknes_in_r*1.3*cos(T+2*pi/16)
    z =thicknes_in_r*1.3*sin(T+2*pi/16)
    y = 0.0+r
    res +="Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(x,y,z,255.0,255.0,255.0,x,y,z,center_x+cos(T)/8,center_y+sin(T)/8)

y = thicknes_in_y*2/3+r
#1
res += "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(0.0,y,0.0,255.0,255.0,255.0,0.0,y,0.0,center_x,center_y)
import pyperclip
pyperclip.copy(res)
spam = pyperclip.paste()



