import sympy as sp
from sympy.matrices import rot_axis3

from spatialmath import *
from spatialmath.base import *

import matplotlib.pyplot as plt
import numpy as np

import roboticstoolbox as rtb

KUKA = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.4, a=0.025, alpha=np.pi/2,qlim=[np.deg2rad(-170), np.deg2rad(170)]),
        rtb.RevoluteDH(d=0, a=0.315, alpha=0, offset=np.pi/2, qlim=[np.deg2rad(-190), np.deg2rad(45)]),
        rtb.RevoluteDH(d=0, a=0.035, alpha=np.pi/2, qlim=[np.deg2rad(-120),np.deg2rad(156)]),
        rtb.RevoluteDH(d=0.365, a=0, alpha=-np.pi/2, qlim=[np.deg2rad(-185),np.deg2rad(185)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.pi/2, qlim=[np.deg2rad(-120),np.deg2rad(120)]),
        rtb.RevoluteDH(d=0.08, a=0, alpha=0, qlim=[np.deg2rad(-350),np.deg2rad(350)])
    ], name='KUKA KR 6 R700 Sixx', base=SE3(0,0,0)
)

print(KUKA)

IRB = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.78, a=0.350, alpha=np.pi/2,qlim=[np.deg2rad(-170), np.deg2rad(170)]),
        rtb.RevoluteDH(d=0, a=1.145, alpha=0, offset=np.pi/2, qlim=[np.deg2rad(-65), np.deg2rad(85)]),
        rtb.RevoluteDH(d=0, a=0.2, alpha=np.pi/2, qlim=[np.deg2rad(-180),np.deg2rad(70)]),
        rtb.RevoluteDH(d=1.2125, a=0, alpha=-np.pi/2, qlim=[np.deg2rad(-300),np.deg2rad(300)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.pi/2, qlim=[np.deg2rad(-130),np.deg2rad(130)]),
        rtb.RevoluteDH(d=0.22, a=0, alpha=0, qlim=[np.deg2rad(-360),np.deg2rad(360)])
    ], name='IRB 6700-300/2.70', base=SE3(0,0,0)
)

print(IRB)

GOFA = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.4, a=0.150, alpha=np.pi/2,qlim=[np.deg2rad(-270), np.deg2rad(270)]),
        rtb.RevoluteDH(d=0, a=0.897, alpha=0, offset=np.pi/2, qlim=[np.deg2rad(-180), np.deg2rad(180)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.pi/2, qlim=[np.deg2rad(-225),np.deg2rad(85)]),
        rtb.RevoluteDH(d=0.738, a=0, alpha=-np.pi/2, qlim=[np.deg2rad(-180),np.deg2rad(180)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.pi/2, qlim=[np.deg2rad(-180),np.deg2rad(180)]),
        rtb.RevoluteDH(d=0, a=0, alpha=0, qlim=[np.deg2rad(-270),np.deg2rad(270)])
    ], name='GoFa CRB 15000 10', base=SE3(0,0,0)
)

print(GOFA)

joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T04_DH = IRB.fkine([joint1, joint2, joint3, joint4, joint5, joint6])
print(T04_DH)