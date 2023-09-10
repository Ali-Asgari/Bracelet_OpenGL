# This program calculate second Turquoise vertecies
#       and put them in clipboard

import numpy as np
from math import *

def rotate_on_z_teta(x,y,z,teta=pi/4):
    m1 = np.array([[x,y,z]])
    m2 = np.array([[cos(teta),-sin(teta),0],[sin(teta),cos(teta),0],[0,0,1]])
    m3 = np.dot(m1,m2) 
    m4=m3[0]
    return m4


number_of_dots = 10
r = -0.100
thicknes_in_r=0.01
max_tick_ness_in_r=-0.01
center_x=0.75-0.125
center_y=0.0+0.125

x=0
allocate_y=0.0+r
z=0
X,Y,Z=rotate_on_z_teta(x,allocate_y,z)
res = "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(X,Y,Z,255.0,255.0,255.0,X,Y,Z,center_x,center_y)
for i in range(number_of_dots):
    T = (i+1)*2*pi/number_of_dots
    x =thicknes_in_r*sin(T)
    z =thicknes_in_r*cos(T)
    X,Y,Z=rotate_on_z_teta(x,allocate_y,z)
    res += "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(X,Y,Z,255.0,255.0,255.0,X,Y,Z,center_x+ thicknes_in_r*sin(T)/(8*max_tick_ness_in_r) ,center_y+thicknes_in_r*cos(T)/(8*max_tick_ness_in_r))

thicknes_in_y=-0.003
thicknes_in_r=0.005
x=0
allocate_y=0.0+r+1.5*thicknes_in_y
z=0
X,Y,Z=rotate_on_z_teta(x,allocate_y,z)
res += "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(X,Y,Z,255.0,255.0,255.0,X,Y,Z,center_x,center_y)
allocate_y=0.0+r+thicknes_in_y
for i in range(number_of_dots):
    T = (i+1)*2*pi/number_of_dots
    x =thicknes_in_r*sin(T)
    z =thicknes_in_r*cos(T)
    X,Y,Z=rotate_on_z_teta(x,allocate_y,z)
    res += "Vertex{glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec3(%sf, %sf, %sf), glm::vec2(%sf, %sf)},"%(X,Y,Z,255.0,255.0,255.0,X,Y,Z,center_x+ thicknes_in_r*sin(T)/(8*max_tick_ness_in_r) ,center_y+thicknes_in_r*cos(T)/(8*max_tick_ness_in_r))
import pyperclip
pyperclip.copy(res)
spam = pyperclip.paste()

