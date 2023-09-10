# This program calculate second Ring vertecies
#       and put them in clipboard
from math import *
number_of_dots = 60
thicknes_in_y = 0.01
thicknes_in_r = 0.01
r = 0.0999
res = ""
for i in range(number_of_dots):
    T = (i+1)*2*pi/number_of_dots
    x =r*cos(T+pi/8)
    y =r*sin(T+pi/8)
    z = -thicknes_in_y*cos(8*T)
    z2 = z+thicknes_in_y
    res+="Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(0.5f, 0.5f)},"%(x,y,z,255.0,0.0,0.0,x,y,z)+"Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(0.5f, 0.5f)},"%(x,y,z2,255.0,0.0,0.0,x,y,z2)
import pyperclip
pyperclip.copy(res)
spam = pyperclip.paste()
