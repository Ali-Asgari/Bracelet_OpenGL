# This program calculate first Ring vertecies
#       and put them in clipboard
from math import *
number_of_dots = 60
thicknes_in_y = 0.01
thicknes_in_r = 0.001 
r = 0.1 # radius of bracelet
res = ""
center_x=0.25
center_y=0.75 

for i in range(number_of_dots):
    T = (i+1)*2*pi/number_of_dots
    x =r*cos(T+pi/8)
    y =r*sin(T+pi/8)
    z = thicknes_in_y*cos(8*T)
    z2 = z-thicknes_in_y
    # length = 
    x_loc = center_x+sin(T+pi/8)/4
    x_loc2 = center_x+sin(T+pi/8)/4*(2/3)
    y_loc = center_y+cos(T+pi/8)/4
    y_loc2 = center_y+cos(T+pi/8)/4*(2/3)
    res +="Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(x,y,z,212.0,175.0,55.0,x,y,z,x_loc2,y_loc2)+"Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(x,y,z2,212.0,175.0,55.0,x,y,z2,x_loc,y_loc)
import pyperclip
pyperclip.copy(res)
spam = pyperclip.paste()