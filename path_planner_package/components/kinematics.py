"""
Author: Zin Lin Htun
class: Kinematics
"""

from math import *


class Kinematics:
    def __init__(self):
        # static class => interface
        pass

    # find velocity factor
    @staticmethod
    def find_velocity_factor(dx, dy):
        w = 0.1  # 8.5 cm
        d_look = sqrt((dx**2)+(dy**2)) # look ahead distance
        print(d_look)
        alpha = atan(dy/dx)
        print(degrees(alpha))
        factor = (d_look + (w*sin(alpha))) / (d_look - (w*sin(alpha)))

        # return statement
        return factor

fac = Kinematics.find_velocity_factor(-0.4,0.1)
print(fac)