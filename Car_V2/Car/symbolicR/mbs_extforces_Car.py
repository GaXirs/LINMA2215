#
#	MBsysTran - Release 8.1
#
#	Copyright 
#	Universite catholique de Louvain (UCLouvain) 
#	Mechatronic, Electrical Energy, and Dynamic systems (MEED Division) 
#	2, Place du Levant
#	1348 Louvain-la-Neuve 
#	Belgium 
#
#	http://www.robotran.be 
#
#	==> Generation Date: Mon Nov  4 15:48:11 2024
#	==> using automatic loading with extension .mbs 
#
#	==> Project name: Car
#
#	==> Number of joints: 44
#
#	==> Function: F19 - External Forces
#
#	==> Git hash: c9679760b1e23dc6b2c784bde05d373c9aa55aef
#
#	==> Input XML
#

from math import sin, cos, sqrt
from numpy import zeros

def extforces(frc, trq, s, tsim):
    q = s.q
    qd = s.qd
    qdd = s.qdd
    frc = s.frc
    trq = s.trq
    PxF1 = zeros(4)
    RxF1 = zeros((4, 4))
    VxF1 = zeros(4)
    OMxF1 = zeros(4)
    AxF1 = zeros(4)
    OMPxF1 = zeros(4)

    PxF2 = zeros(4)
    RxF2 = zeros((4, 4))
    VxF2 = zeros(4)
    OMxF2 = zeros(4)
    AxF2 = zeros(4)
    OMPxF2 = zeros(4)

    PxF3 = zeros(4)
    RxF3 = zeros((4, 4))
    VxF3 = zeros(4)
    OMxF3 = zeros(4)
    AxF3 = zeros(4)
    OMPxF3 = zeros(4)

    PxF4 = zeros(4)
    RxF4 = zeros((4, 4))
    VxF4 = zeros(4)
    OMxF4 = zeros(4)
    AxF4 = zeros(4)
    OMPxF4 = zeros(4)

 
# Trigonometric functions

    S4 = sin(q[4])
    C4 = cos(q[4])
    S5 = sin(q[5])
    C5 = cos(q[5])
    S6 = sin(q[6])
    C6 = cos(q[6])
    S8 = sin(q[8])
    C8 = cos(q[8])
    S9 = sin(q[9])
    C9 = cos(q[9])
    S10 = sin(q[10])
    C10 = cos(q[10])
    S11 = sin(q[11])
    C11 = cos(q[11])
    S12 = sin(q[12])
    C12 = cos(q[12])
    S13 = sin(q[13])
    C13 = cos(q[13])
    S14 = sin(q[14])
    C14 = cos(q[14])
    S15 = sin(q[15])
    C15 = cos(q[15])
    S16 = sin(q[16])
    C16 = cos(q[16])
    S17 = sin(q[17])
    C17 = cos(q[17])
    S33 = sin(q[33])
    C33 = cos(q[33])
    S34 = sin(q[34])
    C34 = cos(q[34])
    S35 = sin(q[35])
    C35 = cos(q[35])
    S36 = sin(q[36])
    C36 = cos(q[36])
    S37 = sin(q[37])
    C37 = cos(q[37])
    S38 = sin(q[38])
    C38 = cos(q[38])
 
# Augmented Joint Position Vectors

 
# Sensor Kinematics

    ROcp2_45 = -S4*C5
    ROcp2_55 = C4*C5
    ROcp2_75 = S4*S5
    ROcp2_85 = -C4*S5
    ROcp2_16 = -ROcp2_75*S6+C4*C6
    ROcp2_26 = -ROcp2_85*S6+S4*C6
    ROcp2_36 = -C5*S6
    ROcp2_76 = ROcp2_75*C6+C4*S6
    ROcp2_86 = ROcp2_85*C6+S4*S6
    ROcp2_96 = C5*C6
    ROcp2_48 = ROcp2_45*C8+ROcp2_76*S8
    ROcp2_58 = ROcp2_55*C8+ROcp2_86*S8
    ROcp2_68 = ROcp2_96*S8+S5*C8
    ROcp2_78 = -ROcp2_45*S8+ROcp2_76*C8
    ROcp2_88 = -ROcp2_55*S8+ROcp2_86*C8
    ROcp2_98 = ROcp2_96*C8-S5*S8
    ROcp2_19 = ROcp2_16*C9-ROcp2_78*S9
    ROcp2_29 = ROcp2_26*C9-ROcp2_88*S9
    ROcp2_39 = ROcp2_36*C9-ROcp2_98*S9
    ROcp2_79 = ROcp2_16*S9+ROcp2_78*C9
    ROcp2_89 = ROcp2_26*S9+ROcp2_88*C9
    ROcp2_99 = ROcp2_36*S9+ROcp2_98*C9
    ROcp2_410 = ROcp2_48*C10+ROcp2_79*S10
    ROcp2_510 = ROcp2_58*C10+ROcp2_89*S10
    ROcp2_610 = ROcp2_68*C10+ROcp2_99*S10
    ROcp2_710 = -ROcp2_48*S10+ROcp2_79*C10
    ROcp2_810 = -ROcp2_58*S10+ROcp2_89*C10
    ROcp2_910 = -ROcp2_68*S10+ROcp2_99*C10
    ROcp2_111 = ROcp2_19*C11+ROcp2_410*S11
    ROcp2_211 = ROcp2_29*C11+ROcp2_510*S11
    ROcp2_311 = ROcp2_39*C11+ROcp2_610*S11
    ROcp2_411 = -ROcp2_19*S11+ROcp2_410*C11
    ROcp2_511 = -ROcp2_29*S11+ROcp2_510*C11
    ROcp2_611 = -ROcp2_39*S11+ROcp2_610*C11
    ROcp2_112 = ROcp2_111*C12-ROcp2_710*S12
    ROcp2_212 = ROcp2_211*C12-ROcp2_810*S12
    ROcp2_312 = ROcp2_311*C12-ROcp2_910*S12
    ROcp2_712 = ROcp2_111*S12+ROcp2_710*C12
    ROcp2_812 = ROcp2_211*S12+ROcp2_810*C12
    ROcp2_912 = ROcp2_311*S12+ROcp2_910*C12
    OMcp2_15 = qd[5]*C4
    OMcp2_25 = qd[5]*S4
    OPcp2_15 = -qd[4]*qd[5]*S4+qdd[5]*C4
    OPcp2_25 = qd[4]*qd[5]*C4+qdd[5]*S4
    OMcp2_16 = OMcp2_15+qd[6]*ROcp2_45
    OMcp2_26 = OMcp2_25+qd[6]*ROcp2_55
    OMcp2_36 = qd[4]+qd[6]*S5
    OPcp2_16 = OPcp2_15+qd[6]*(-qd[4]*ROcp2_55+OMcp2_25*S5)+qdd[6]*ROcp2_45
    OPcp2_26 = OPcp2_25+qd[6]*(qd[4]*ROcp2_45-OMcp2_15*S5)+qdd[6]*ROcp2_55
    OPcp2_36 = qdd[4]+qd[6]*(OMcp2_15*ROcp2_55-OMcp2_25*ROcp2_45)+qdd[6]*S5
    RLcp2_17 = ROcp2_16*s.dpt[1,1]+ROcp2_45*s.dpt[2,1]+ROcp2_76*s.dpt[3,1]
    RLcp2_27 = ROcp2_26*s.dpt[1,1]+ROcp2_55*s.dpt[2,1]+ROcp2_86*s.dpt[3,1]
    RLcp2_37 = ROcp2_36*s.dpt[1,1]+ROcp2_96*s.dpt[3,1]+s.dpt[2,1]*S5
    POcp2_17 = q[1]+RLcp2_17
    POcp2_27 = q[2]+RLcp2_27
    POcp2_37 = q[3]+RLcp2_37
    OMcp2_17 = OMcp2_16+qd[8]*ROcp2_16
    OMcp2_27 = OMcp2_26+qd[8]*ROcp2_26
    OMcp2_37 = OMcp2_36+qd[8]*ROcp2_36
    ORcp2_17 = OMcp2_26*RLcp2_37-OMcp2_36*RLcp2_27
    ORcp2_27 = -OMcp2_16*RLcp2_37+OMcp2_36*RLcp2_17
    ORcp2_37 = OMcp2_16*RLcp2_27-OMcp2_26*RLcp2_17
    VIcp2_17 = qd[1]+ORcp2_17
    VIcp2_27 = qd[2]+ORcp2_27
    VIcp2_37 = qd[3]+ORcp2_37
    OPcp2_17 = OPcp2_16+qd[8]*(OMcp2_26*ROcp2_36-OMcp2_36*ROcp2_26)+qdd[8]*ROcp2_16
    OPcp2_27 = OPcp2_26+qd[8]*(-OMcp2_16*ROcp2_36+OMcp2_36*ROcp2_16)+qdd[8]*ROcp2_26
    OPcp2_37 = OPcp2_36+qd[8]*(OMcp2_16*ROcp2_26-OMcp2_26*ROcp2_16)+qdd[8]*ROcp2_36
    ACcp2_17 = qdd[1]+OMcp2_26*ORcp2_37-OMcp2_36*ORcp2_27+OPcp2_26*RLcp2_37-OPcp2_36*RLcp2_27
    ACcp2_27 = qdd[2]-OMcp2_16*ORcp2_37+OMcp2_36*ORcp2_17-OPcp2_16*RLcp2_37+OPcp2_36*RLcp2_17
    ACcp2_37 = qdd[3]+OMcp2_16*ORcp2_27-OMcp2_26*ORcp2_17+OPcp2_16*RLcp2_27-OPcp2_26*RLcp2_17
    RLcp2_18 = ROcp2_48*s.dpt[2,17]
    RLcp2_28 = ROcp2_58*s.dpt[2,17]
    RLcp2_38 = ROcp2_68*s.dpt[2,17]
    POcp2_18 = POcp2_17+RLcp2_18
    POcp2_28 = POcp2_27+RLcp2_28
    POcp2_38 = POcp2_37+RLcp2_38
    OMcp2_18 = OMcp2_17+qd[9]*ROcp2_48
    OMcp2_28 = OMcp2_27+qd[9]*ROcp2_58
    OMcp2_38 = OMcp2_37+qd[9]*ROcp2_68
    ORcp2_18 = OMcp2_27*RLcp2_38-OMcp2_37*RLcp2_28
    ORcp2_28 = -OMcp2_17*RLcp2_38+OMcp2_37*RLcp2_18
    ORcp2_38 = OMcp2_17*RLcp2_28-OMcp2_27*RLcp2_18
    VIcp2_18 = ORcp2_18+VIcp2_17
    VIcp2_28 = ORcp2_28+VIcp2_27
    VIcp2_38 = ORcp2_38+VIcp2_37
    OPcp2_18 = OPcp2_17+qd[9]*(OMcp2_27*ROcp2_68-OMcp2_37*ROcp2_58)+qdd[9]*ROcp2_48
    OPcp2_28 = OPcp2_27+qd[9]*(-OMcp2_17*ROcp2_68+OMcp2_37*ROcp2_48)+qdd[9]*ROcp2_58
    OPcp2_38 = OPcp2_37+qd[9]*(OMcp2_17*ROcp2_58-OMcp2_27*ROcp2_48)+qdd[9]*ROcp2_68
    ACcp2_18 = ACcp2_17+OMcp2_27*ORcp2_38-OMcp2_37*ORcp2_28+OPcp2_27*RLcp2_38-OPcp2_37*RLcp2_28
    ACcp2_28 = ACcp2_27-OMcp2_17*ORcp2_38+OMcp2_37*ORcp2_18-OPcp2_17*RLcp2_38+OPcp2_37*RLcp2_18
    ACcp2_38 = ACcp2_37+OMcp2_17*ORcp2_28-OMcp2_27*ORcp2_18+OPcp2_17*RLcp2_28-OPcp2_27*RLcp2_18
    OMcp2_19 = OMcp2_18+qd[10]*ROcp2_19
    OMcp2_29 = OMcp2_28+qd[10]*ROcp2_29
    OMcp2_39 = OMcp2_38+qd[10]*ROcp2_39
    OPcp2_19 = OPcp2_18+qd[10]*(OMcp2_28*ROcp2_39-OMcp2_38*ROcp2_29)+qdd[10]*ROcp2_19
    OPcp2_29 = OPcp2_28+qd[10]*(-OMcp2_18*ROcp2_39+OMcp2_38*ROcp2_19)+qdd[10]*ROcp2_29
    OPcp2_39 = OPcp2_38+qd[10]*(OMcp2_18*ROcp2_29-OMcp2_28*ROcp2_19)+qdd[10]*ROcp2_39
    OMcp2_110 = OMcp2_19+qd[11]*ROcp2_710
    OMcp2_210 = OMcp2_29+qd[11]*ROcp2_810
    OMcp2_310 = OMcp2_39+qd[11]*ROcp2_910
    OPcp2_110 = OPcp2_19+qd[11]*(OMcp2_29*ROcp2_910-OMcp2_39*ROcp2_810)+qdd[11]*ROcp2_710
    OPcp2_210 = OPcp2_29+qd[11]*(-OMcp2_19*ROcp2_910+OMcp2_39*ROcp2_710)+qdd[11]*ROcp2_810
    OPcp2_310 = OPcp2_39+qd[11]*(OMcp2_19*ROcp2_810-OMcp2_29*ROcp2_710)+qdd[11]*ROcp2_910
    RLcp2_111 = ROcp2_710*s.dpt[3,21]
    RLcp2_211 = ROcp2_810*s.dpt[3,21]
    RLcp2_311 = ROcp2_910*s.dpt[3,21]
    POcp2_111 = POcp2_18+RLcp2_111
    POcp2_211 = POcp2_28+RLcp2_211
    POcp2_311 = POcp2_38+RLcp2_311
    OMcp2_111 = OMcp2_110+qd[12]*ROcp2_411
    OMcp2_211 = OMcp2_210+qd[12]*ROcp2_511
    OMcp2_311 = OMcp2_310+qd[12]*ROcp2_611
    ORcp2_111 = OMcp2_210*RLcp2_311-OMcp2_310*RLcp2_211
    ORcp2_211 = -OMcp2_110*RLcp2_311+OMcp2_310*RLcp2_111
    ORcp2_311 = OMcp2_110*RLcp2_211-OMcp2_210*RLcp2_111
    VIcp2_111 = ORcp2_111+VIcp2_18
    VIcp2_211 = ORcp2_211+VIcp2_28
    VIcp2_311 = ORcp2_311+VIcp2_38
    OPcp2_111 = OPcp2_110+qd[12]*(OMcp2_210*ROcp2_611-OMcp2_310*ROcp2_511)+qdd[12]*ROcp2_411
    OPcp2_211 = OPcp2_210+qd[12]*(-OMcp2_110*ROcp2_611+OMcp2_310*ROcp2_411)+qdd[12]*ROcp2_511
    OPcp2_311 = OPcp2_310+qd[12]*(OMcp2_110*ROcp2_511-OMcp2_210*ROcp2_411)+qdd[12]*ROcp2_611
    ACcp2_111 = ACcp2_18+OMcp2_210*ORcp2_311-OMcp2_310*ORcp2_211+OPcp2_210*RLcp2_311-OPcp2_310*RLcp2_211
    ACcp2_211 = ACcp2_28-OMcp2_110*ORcp2_311+OMcp2_310*ORcp2_111-OPcp2_110*RLcp2_311+OPcp2_310*RLcp2_111
    ACcp2_311 = ACcp2_38+OMcp2_110*ORcp2_211-OMcp2_210*ORcp2_111+OPcp2_110*RLcp2_211-OPcp2_210*RLcp2_111
    PxF1[1] = POcp2_111
    PxF1[2] = POcp2_211
    PxF1[3] = POcp2_311
    RxF1[1,1] = ROcp2_112
    RxF1[1,2] = ROcp2_212
    RxF1[1,3] = ROcp2_312
    RxF1[2,1] = ROcp2_411
    RxF1[2,2] = ROcp2_511
    RxF1[2,3] = ROcp2_611
    RxF1[3,1] = ROcp2_712
    RxF1[3,2] = ROcp2_812
    RxF1[3,3] = ROcp2_912
    VxF1[1] = VIcp2_111
    VxF1[2] = VIcp2_211
    VxF1[3] = VIcp2_311
    OMxF1[1] = OMcp2_111
    OMxF1[2] = OMcp2_211
    OMxF1[3] = OMcp2_311
    AxF1[1] = ACcp2_111
    AxF1[2] = ACcp2_211
    AxF1[3] = ACcp2_311
    OMPxF1[1] = OPcp2_111
    OMPxF1[2] = OPcp2_211
    OMPxF1[3] = OPcp2_311
    ROcp3_45 = -S4*C5
    ROcp3_55 = C4*C5
    ROcp3_75 = S4*S5
    ROcp3_85 = -C4*S5
    ROcp3_16 = -ROcp3_75*S6+C4*C6
    ROcp3_26 = -ROcp3_85*S6+S4*C6
    ROcp3_36 = -C5*S6
    ROcp3_76 = ROcp3_75*C6+C4*S6
    ROcp3_86 = ROcp3_85*C6+S4*S6
    ROcp3_96 = C5*C6
    ROcp3_413 = ROcp3_45*C13+ROcp3_76*S13
    ROcp3_513 = ROcp3_55*C13+ROcp3_86*S13
    ROcp3_613 = ROcp3_96*S13+C13*S5
    ROcp3_713 = -ROcp3_45*S13+ROcp3_76*C13
    ROcp3_813 = -ROcp3_55*S13+ROcp3_86*C13
    ROcp3_913 = ROcp3_96*C13-S13*S5
    ROcp3_114 = ROcp3_16*C14-ROcp3_713*S14
    ROcp3_214 = ROcp3_26*C14-ROcp3_813*S14
    ROcp3_314 = ROcp3_36*C14-ROcp3_913*S14
    ROcp3_714 = ROcp3_16*S14+ROcp3_713*C14
    ROcp3_814 = ROcp3_26*S14+ROcp3_813*C14
    ROcp3_914 = ROcp3_36*S14+ROcp3_913*C14
    ROcp3_415 = ROcp3_413*C15+ROcp3_714*S15
    ROcp3_515 = ROcp3_513*C15+ROcp3_814*S15
    ROcp3_615 = ROcp3_613*C15+ROcp3_914*S15
    ROcp3_715 = -ROcp3_413*S15+ROcp3_714*C15
    ROcp3_815 = -ROcp3_513*S15+ROcp3_814*C15
    ROcp3_915 = -ROcp3_613*S15+ROcp3_914*C15
    ROcp3_116 = ROcp3_114*C16+ROcp3_415*S16
    ROcp3_216 = ROcp3_214*C16+ROcp3_515*S16
    ROcp3_316 = ROcp3_314*C16+ROcp3_615*S16
    ROcp3_416 = -ROcp3_114*S16+ROcp3_415*C16
    ROcp3_516 = -ROcp3_214*S16+ROcp3_515*C16
    ROcp3_616 = -ROcp3_314*S16+ROcp3_615*C16
    ROcp3_117 = ROcp3_116*C17-ROcp3_715*S17
    ROcp3_217 = ROcp3_216*C17-ROcp3_815*S17
    ROcp3_317 = ROcp3_316*C17-ROcp3_915*S17
    ROcp3_717 = ROcp3_116*S17+ROcp3_715*C17
    ROcp3_817 = ROcp3_216*S17+ROcp3_815*C17
    ROcp3_917 = ROcp3_316*S17+ROcp3_915*C17
    OMcp3_15 = qd[5]*C4
    OMcp3_25 = qd[5]*S4
    OPcp3_15 = -qd[4]*qd[5]*S4+qdd[5]*C4
    OPcp3_25 = qd[4]*qd[5]*C4+qdd[5]*S4
    OMcp3_16 = OMcp3_15+qd[6]*ROcp3_45
    OMcp3_26 = OMcp3_25+qd[6]*ROcp3_55
    OMcp3_36 = qd[4]+qd[6]*S5
    OPcp3_16 = OPcp3_15+qd[6]*(-qd[4]*ROcp3_55+OMcp3_25*S5)+qdd[6]*ROcp3_45
    OPcp3_26 = OPcp3_25+qd[6]*(qd[4]*ROcp3_45-OMcp3_15*S5)+qdd[6]*ROcp3_55
    OPcp3_36 = qdd[4]+qd[6]*(OMcp3_15*ROcp3_55-OMcp3_25*ROcp3_45)+qdd[6]*S5
    RLcp3_17 = ROcp3_16*s.dpt[1,2]+ROcp3_45*s.dpt[2,2]+ROcp3_76*s.dpt[3,2]
    RLcp3_27 = ROcp3_26*s.dpt[1,2]+ROcp3_55*s.dpt[2,2]+ROcp3_86*s.dpt[3,2]
    RLcp3_37 = ROcp3_36*s.dpt[1,2]+ROcp3_96*s.dpt[3,2]+s.dpt[2,2]*S5
    POcp3_17 = q[1]+RLcp3_17
    POcp3_27 = q[2]+RLcp3_27
    POcp3_37 = q[3]+RLcp3_37
    OMcp3_17 = OMcp3_16+qd[13]*ROcp3_16
    OMcp3_27 = OMcp3_26+qd[13]*ROcp3_26
    OMcp3_37 = OMcp3_36+qd[13]*ROcp3_36
    ORcp3_17 = OMcp3_26*RLcp3_37-OMcp3_36*RLcp3_27
    ORcp3_27 = -OMcp3_16*RLcp3_37+OMcp3_36*RLcp3_17
    ORcp3_37 = OMcp3_16*RLcp3_27-OMcp3_26*RLcp3_17
    VIcp3_17 = qd[1]+ORcp3_17
    VIcp3_27 = qd[2]+ORcp3_27
    VIcp3_37 = qd[3]+ORcp3_37
    OPcp3_17 = OPcp3_16+qd[13]*(OMcp3_26*ROcp3_36-OMcp3_36*ROcp3_26)+qdd[13]*ROcp3_16
    OPcp3_27 = OPcp3_26+qd[13]*(-OMcp3_16*ROcp3_36+OMcp3_36*ROcp3_16)+qdd[13]*ROcp3_26
    OPcp3_37 = OPcp3_36+qd[13]*(OMcp3_16*ROcp3_26-OMcp3_26*ROcp3_16)+qdd[13]*ROcp3_36
    ACcp3_17 = qdd[1]+OMcp3_26*ORcp3_37-OMcp3_36*ORcp3_27+OPcp3_26*RLcp3_37-OPcp3_36*RLcp3_27
    ACcp3_27 = qdd[2]-OMcp3_16*ORcp3_37+OMcp3_36*ORcp3_17-OPcp3_16*RLcp3_37+OPcp3_36*RLcp3_17
    ACcp3_37 = qdd[3]+OMcp3_16*ORcp3_27-OMcp3_26*ORcp3_17+OPcp3_16*RLcp3_27-OPcp3_26*RLcp3_17
    RLcp3_18 = ROcp3_413*s.dpt[2,23]
    RLcp3_28 = ROcp3_513*s.dpt[2,23]
    RLcp3_38 = ROcp3_613*s.dpt[2,23]
    POcp3_18 = POcp3_17+RLcp3_18
    POcp3_28 = POcp3_27+RLcp3_28
    POcp3_38 = POcp3_37+RLcp3_38
    OMcp3_18 = OMcp3_17+qd[14]*ROcp3_413
    OMcp3_28 = OMcp3_27+qd[14]*ROcp3_513
    OMcp3_38 = OMcp3_37+qd[14]*ROcp3_613
    ORcp3_18 = OMcp3_27*RLcp3_38-OMcp3_37*RLcp3_28
    ORcp3_28 = -OMcp3_17*RLcp3_38+OMcp3_37*RLcp3_18
    ORcp3_38 = OMcp3_17*RLcp3_28-OMcp3_27*RLcp3_18
    VIcp3_18 = ORcp3_18+VIcp3_17
    VIcp3_28 = ORcp3_28+VIcp3_27
    VIcp3_38 = ORcp3_38+VIcp3_37
    OPcp3_18 = OPcp3_17+qd[14]*(OMcp3_27*ROcp3_613-OMcp3_37*ROcp3_513)+qdd[14]*ROcp3_413
    OPcp3_28 = OPcp3_27+qd[14]*(-OMcp3_17*ROcp3_613+OMcp3_37*ROcp3_413)+qdd[14]*ROcp3_513
    OPcp3_38 = OPcp3_37+qd[14]*(OMcp3_17*ROcp3_513-OMcp3_27*ROcp3_413)+qdd[14]*ROcp3_613
    ACcp3_18 = ACcp3_17+OMcp3_27*ORcp3_38-OMcp3_37*ORcp3_28+OPcp3_27*RLcp3_38-OPcp3_37*RLcp3_28
    ACcp3_28 = ACcp3_27-OMcp3_17*ORcp3_38+OMcp3_37*ORcp3_18-OPcp3_17*RLcp3_38+OPcp3_37*RLcp3_18
    ACcp3_38 = ACcp3_37+OMcp3_17*ORcp3_28-OMcp3_27*ORcp3_18+OPcp3_17*RLcp3_28-OPcp3_27*RLcp3_18
    OMcp3_19 = OMcp3_18+qd[15]*ROcp3_114
    OMcp3_29 = OMcp3_28+qd[15]*ROcp3_214
    OMcp3_39 = OMcp3_38+qd[15]*ROcp3_314
    OPcp3_19 = OPcp3_18+qd[15]*(OMcp3_28*ROcp3_314-OMcp3_38*ROcp3_214)+qdd[15]*ROcp3_114
    OPcp3_29 = OPcp3_28+qd[15]*(-OMcp3_18*ROcp3_314+OMcp3_38*ROcp3_114)+qdd[15]*ROcp3_214
    OPcp3_39 = OPcp3_38+qd[15]*(OMcp3_18*ROcp3_214-OMcp3_28*ROcp3_114)+qdd[15]*ROcp3_314
    OMcp3_110 = OMcp3_19+qd[16]*ROcp3_715
    OMcp3_210 = OMcp3_29+qd[16]*ROcp3_815
    OMcp3_310 = OMcp3_39+qd[16]*ROcp3_915
    OPcp3_110 = OPcp3_19+qd[16]*(OMcp3_29*ROcp3_915-OMcp3_39*ROcp3_815)+qdd[16]*ROcp3_715
    OPcp3_210 = OPcp3_29+qd[16]*(-OMcp3_19*ROcp3_915+OMcp3_39*ROcp3_715)+qdd[16]*ROcp3_815
    OPcp3_310 = OPcp3_39+qd[16]*(OMcp3_19*ROcp3_815-OMcp3_29*ROcp3_715)+qdd[16]*ROcp3_915
    RLcp3_111 = ROcp3_715*s.dpt[3,26]
    RLcp3_211 = ROcp3_815*s.dpt[3,26]
    RLcp3_311 = ROcp3_915*s.dpt[3,26]
    POcp3_111 = POcp3_18+RLcp3_111
    POcp3_211 = POcp3_28+RLcp3_211
    POcp3_311 = POcp3_38+RLcp3_311
    OMcp3_111 = OMcp3_110+qd[17]*ROcp3_416
    OMcp3_211 = OMcp3_210+qd[17]*ROcp3_516
    OMcp3_311 = OMcp3_310+qd[17]*ROcp3_616
    ORcp3_111 = OMcp3_210*RLcp3_311-OMcp3_310*RLcp3_211
    ORcp3_211 = -OMcp3_110*RLcp3_311+OMcp3_310*RLcp3_111
    ORcp3_311 = OMcp3_110*RLcp3_211-OMcp3_210*RLcp3_111
    VIcp3_111 = ORcp3_111+VIcp3_18
    VIcp3_211 = ORcp3_211+VIcp3_28
    VIcp3_311 = ORcp3_311+VIcp3_38
    OPcp3_111 = OPcp3_110+qd[17]*(OMcp3_210*ROcp3_616-OMcp3_310*ROcp3_516)+qdd[17]*ROcp3_416
    OPcp3_211 = OPcp3_210+qd[17]*(-OMcp3_110*ROcp3_616+OMcp3_310*ROcp3_416)+qdd[17]*ROcp3_516
    OPcp3_311 = OPcp3_310+qd[17]*(OMcp3_110*ROcp3_516-OMcp3_210*ROcp3_416)+qdd[17]*ROcp3_616
    ACcp3_111 = ACcp3_18+OMcp3_210*ORcp3_311-OMcp3_310*ORcp3_211+OPcp3_210*RLcp3_311-OPcp3_310*RLcp3_211
    ACcp3_211 = ACcp3_28-OMcp3_110*ORcp3_311+OMcp3_310*ORcp3_111-OPcp3_110*RLcp3_311+OPcp3_310*RLcp3_111
    ACcp3_311 = ACcp3_38+OMcp3_110*ORcp3_211-OMcp3_210*ORcp3_111+OPcp3_110*RLcp3_211-OPcp3_210*RLcp3_111
    PxF2[1] = POcp3_111
    PxF2[2] = POcp3_211
    PxF2[3] = POcp3_311
    RxF2[1,1] = ROcp3_117
    RxF2[1,2] = ROcp3_217
    RxF2[1,3] = ROcp3_317
    RxF2[2,1] = ROcp3_416
    RxF2[2,2] = ROcp3_516
    RxF2[2,3] = ROcp3_616
    RxF2[3,1] = ROcp3_717
    RxF2[3,2] = ROcp3_817
    RxF2[3,3] = ROcp3_917
    VxF2[1] = VIcp3_111
    VxF2[2] = VIcp3_211
    VxF2[3] = VIcp3_311
    OMxF2[1] = OMcp3_111
    OMxF2[2] = OMcp3_211
    OMxF2[3] = OMcp3_311
    AxF2[1] = ACcp3_111
    AxF2[2] = ACcp3_211
    AxF2[3] = ACcp3_311
    OMPxF2[1] = OPcp3_111
    OMPxF2[2] = OPcp3_211
    OMPxF2[3] = OPcp3_311
    ROcp4_45 = -S4*C5
    ROcp4_55 = C4*C5
    ROcp4_75 = S4*S5
    ROcp4_85 = -C4*S5
    ROcp4_16 = -ROcp4_75*S6+C4*C6
    ROcp4_26 = -ROcp4_85*S6+S4*C6
    ROcp4_36 = -C5*S6
    ROcp4_76 = ROcp4_75*C6+C4*S6
    ROcp4_86 = ROcp4_85*C6+S4*S6
    ROcp4_96 = C5*C6
    ROcp4_433 = ROcp4_45*C33+ROcp4_76*S33
    ROcp4_533 = ROcp4_55*C33+ROcp4_86*S33
    ROcp4_633 = ROcp4_96*S33+C33*S5
    ROcp4_733 = -ROcp4_45*S33+ROcp4_76*C33
    ROcp4_833 = -ROcp4_55*S33+ROcp4_86*C33
    ROcp4_933 = ROcp4_96*C33-S33*S5
    ROcp4_434 = ROcp4_433*C34+ROcp4_733*S34
    ROcp4_534 = ROcp4_533*C34+ROcp4_833*S34
    ROcp4_634 = ROcp4_633*C34+ROcp4_933*S34
    ROcp4_734 = -ROcp4_433*S34+ROcp4_733*C34
    ROcp4_834 = -ROcp4_533*S34+ROcp4_833*C34
    ROcp4_934 = -ROcp4_633*S34+ROcp4_933*C34
    ROcp4_135 = ROcp4_16*C35-ROcp4_734*S35
    ROcp4_235 = ROcp4_26*C35-ROcp4_834*S35
    ROcp4_335 = ROcp4_36*C35-ROcp4_934*S35
    ROcp4_735 = ROcp4_16*S35+ROcp4_734*C35
    ROcp4_835 = ROcp4_26*S35+ROcp4_834*C35
    ROcp4_935 = ROcp4_36*S35+ROcp4_934*C35
    OMcp4_15 = qd[5]*C4
    OMcp4_25 = qd[5]*S4
    OPcp4_15 = -qd[4]*qd[5]*S4+qdd[5]*C4
    OPcp4_25 = qd[4]*qd[5]*C4+qdd[5]*S4
    OMcp4_16 = OMcp4_15+qd[6]*ROcp4_45
    OMcp4_26 = OMcp4_25+qd[6]*ROcp4_55
    OMcp4_36 = qd[4]+qd[6]*S5
    OPcp4_16 = OPcp4_15+qd[6]*(-qd[4]*ROcp4_55+OMcp4_25*S5)+qdd[6]*ROcp4_45
    OPcp4_26 = OPcp4_25+qd[6]*(qd[4]*ROcp4_45-OMcp4_15*S5)+qdd[6]*ROcp4_55
    OPcp4_36 = qdd[4]+qd[6]*(OMcp4_15*ROcp4_55-OMcp4_25*ROcp4_45)+qdd[6]*S5
    RLcp4_17 = ROcp4_16*s.dpt[1,12]+ROcp4_45*s.dpt[2,12]+ROcp4_76*s.dpt[3,12]
    RLcp4_27 = ROcp4_26*s.dpt[1,12]+ROcp4_55*s.dpt[2,12]+ROcp4_86*s.dpt[3,12]
    RLcp4_37 = ROcp4_36*s.dpt[1,12]+ROcp4_96*s.dpt[3,12]+s.dpt[2,12]*S5
    POcp4_17 = q[1]+RLcp4_17
    POcp4_27 = q[2]+RLcp4_27
    POcp4_37 = q[3]+RLcp4_37
    OMcp4_17 = OMcp4_16+qd[33]*ROcp4_16
    OMcp4_27 = OMcp4_26+qd[33]*ROcp4_26
    OMcp4_37 = OMcp4_36+qd[33]*ROcp4_36
    ORcp4_17 = OMcp4_26*RLcp4_37-OMcp4_36*RLcp4_27
    ORcp4_27 = -OMcp4_16*RLcp4_37+OMcp4_36*RLcp4_17
    ORcp4_37 = OMcp4_16*RLcp4_27-OMcp4_26*RLcp4_17
    VIcp4_17 = qd[1]+ORcp4_17
    VIcp4_27 = qd[2]+ORcp4_27
    VIcp4_37 = qd[3]+ORcp4_37
    OPcp4_17 = OPcp4_16+qd[33]*(OMcp4_26*ROcp4_36-OMcp4_36*ROcp4_26)+qdd[33]*ROcp4_16
    OPcp4_27 = OPcp4_26+qd[33]*(-OMcp4_16*ROcp4_36+OMcp4_36*ROcp4_16)+qdd[33]*ROcp4_26
    OPcp4_37 = OPcp4_36+qd[33]*(OMcp4_16*ROcp4_26-OMcp4_26*ROcp4_16)+qdd[33]*ROcp4_36
    ACcp4_17 = qdd[1]+OMcp4_26*ORcp4_37-OMcp4_36*ORcp4_27+OPcp4_26*RLcp4_37-OPcp4_36*RLcp4_27
    ACcp4_27 = qdd[2]-OMcp4_16*ORcp4_37+OMcp4_36*ORcp4_17-OPcp4_16*RLcp4_37+OPcp4_36*RLcp4_17
    ACcp4_37 = qdd[3]+OMcp4_16*ORcp4_27-OMcp4_26*ORcp4_17+OPcp4_16*RLcp4_27-OPcp4_26*RLcp4_17
    RLcp4_18 = ROcp4_433*s.dpt[2,46]
    RLcp4_28 = ROcp4_533*s.dpt[2,46]
    RLcp4_38 = ROcp4_633*s.dpt[2,46]
    POcp4_18 = POcp4_17+RLcp4_18
    POcp4_28 = POcp4_27+RLcp4_28
    POcp4_38 = POcp4_37+RLcp4_38
    OMcp4_18 = OMcp4_17+qd[34]*ROcp4_16
    OMcp4_28 = OMcp4_27+qd[34]*ROcp4_26
    OMcp4_38 = OMcp4_37+qd[34]*ROcp4_36
    ORcp4_18 = OMcp4_27*RLcp4_38-OMcp4_37*RLcp4_28
    ORcp4_28 = -OMcp4_17*RLcp4_38+OMcp4_37*RLcp4_18
    ORcp4_38 = OMcp4_17*RLcp4_28-OMcp4_27*RLcp4_18
    VIcp4_18 = ORcp4_18+VIcp4_17
    VIcp4_28 = ORcp4_28+VIcp4_27
    VIcp4_38 = ORcp4_38+VIcp4_37
    OPcp4_18 = OPcp4_17+qd[34]*(OMcp4_27*ROcp4_36-OMcp4_37*ROcp4_26)+qdd[34]*ROcp4_16
    OPcp4_28 = OPcp4_27+qd[34]*(-OMcp4_17*ROcp4_36+OMcp4_37*ROcp4_16)+qdd[34]*ROcp4_26
    OPcp4_38 = OPcp4_37+qd[34]*(OMcp4_17*ROcp4_26-OMcp4_27*ROcp4_16)+qdd[34]*ROcp4_36
    ACcp4_18 = ACcp4_17+OMcp4_27*ORcp4_38-OMcp4_37*ORcp4_28+OPcp4_27*RLcp4_38-OPcp4_37*RLcp4_28
    ACcp4_28 = ACcp4_27-OMcp4_17*ORcp4_38+OMcp4_37*ORcp4_18-OPcp4_17*RLcp4_38+OPcp4_37*RLcp4_18
    ACcp4_38 = ACcp4_37+OMcp4_17*ORcp4_28-OMcp4_27*ORcp4_18+OPcp4_17*RLcp4_28-OPcp4_27*RLcp4_18
    RLcp4_19 = ROcp4_734*s.dpt[3,49]
    RLcp4_29 = ROcp4_834*s.dpt[3,49]
    RLcp4_39 = ROcp4_934*s.dpt[3,49]
    POcp4_19 = POcp4_18+RLcp4_19
    POcp4_29 = POcp4_28+RLcp4_29
    POcp4_39 = POcp4_38+RLcp4_39
    OMcp4_19 = OMcp4_18+qd[35]*ROcp4_434
    OMcp4_29 = OMcp4_28+qd[35]*ROcp4_534
    OMcp4_39 = OMcp4_38+qd[35]*ROcp4_634
    ORcp4_19 = OMcp4_28*RLcp4_39-OMcp4_38*RLcp4_29
    ORcp4_29 = -OMcp4_18*RLcp4_39+OMcp4_38*RLcp4_19
    ORcp4_39 = OMcp4_18*RLcp4_29-OMcp4_28*RLcp4_19
    VIcp4_19 = ORcp4_19+VIcp4_18
    VIcp4_29 = ORcp4_29+VIcp4_28
    VIcp4_39 = ORcp4_39+VIcp4_38
    OPcp4_19 = OPcp4_18+qd[35]*(OMcp4_28*ROcp4_634-OMcp4_38*ROcp4_534)+qdd[35]*ROcp4_434
    OPcp4_29 = OPcp4_28+qd[35]*(-OMcp4_18*ROcp4_634+OMcp4_38*ROcp4_434)+qdd[35]*ROcp4_534
    OPcp4_39 = OPcp4_38+qd[35]*(OMcp4_18*ROcp4_534-OMcp4_28*ROcp4_434)+qdd[35]*ROcp4_634
    ACcp4_19 = ACcp4_18+OMcp4_28*ORcp4_39-OMcp4_38*ORcp4_29+OPcp4_28*RLcp4_39-OPcp4_38*RLcp4_29
    ACcp4_29 = ACcp4_28-OMcp4_18*ORcp4_39+OMcp4_38*ORcp4_19-OPcp4_18*RLcp4_39+OPcp4_38*RLcp4_19
    ACcp4_39 = ACcp4_38+OMcp4_18*ORcp4_29-OMcp4_28*ORcp4_19+OPcp4_18*RLcp4_29-OPcp4_28*RLcp4_19
    PxF3[1] = POcp4_19
    PxF3[2] = POcp4_29
    PxF3[3] = POcp4_39
    RxF3[1,1] = ROcp4_135
    RxF3[1,2] = ROcp4_235
    RxF3[1,3] = ROcp4_335
    RxF3[2,1] = ROcp4_434
    RxF3[2,2] = ROcp4_534
    RxF3[2,3] = ROcp4_634
    RxF3[3,1] = ROcp4_735
    RxF3[3,2] = ROcp4_835
    RxF3[3,3] = ROcp4_935
    VxF3[1] = VIcp4_19
    VxF3[2] = VIcp4_29
    VxF3[3] = VIcp4_39
    OMxF3[1] = OMcp4_19
    OMxF3[2] = OMcp4_29
    OMxF3[3] = OMcp4_39
    AxF3[1] = ACcp4_19
    AxF3[2] = ACcp4_29
    AxF3[3] = ACcp4_39
    OMPxF3[1] = OPcp4_19
    OMPxF3[2] = OPcp4_29
    OMPxF3[3] = OPcp4_39
    ROcp5_45 = -S4*C5
    ROcp5_55 = C4*C5
    ROcp5_75 = S4*S5
    ROcp5_85 = -C4*S5
    ROcp5_16 = -ROcp5_75*S6+C4*C6
    ROcp5_26 = -ROcp5_85*S6+S4*C6
    ROcp5_36 = -C5*S6
    ROcp5_76 = ROcp5_75*C6+C4*S6
    ROcp5_86 = ROcp5_85*C6+S4*S6
    ROcp5_96 = C5*C6
    ROcp5_436 = ROcp5_45*C36+ROcp5_76*S36
    ROcp5_536 = ROcp5_55*C36+ROcp5_86*S36
    ROcp5_636 = ROcp5_96*S36+C36*S5
    ROcp5_736 = -ROcp5_45*S36+ROcp5_76*C36
    ROcp5_836 = -ROcp5_55*S36+ROcp5_86*C36
    ROcp5_936 = ROcp5_96*C36-S36*S5
    ROcp5_437 = ROcp5_436*C37+ROcp5_736*S37
    ROcp5_537 = ROcp5_536*C37+ROcp5_836*S37
    ROcp5_637 = ROcp5_636*C37+ROcp5_936*S37
    ROcp5_737 = -ROcp5_436*S37+ROcp5_736*C37
    ROcp5_837 = -ROcp5_536*S37+ROcp5_836*C37
    ROcp5_937 = -ROcp5_636*S37+ROcp5_936*C37
    ROcp5_138 = ROcp5_16*C38-ROcp5_737*S38
    ROcp5_238 = ROcp5_26*C38-ROcp5_837*S38
    ROcp5_338 = ROcp5_36*C38-ROcp5_937*S38
    ROcp5_738 = ROcp5_16*S38+ROcp5_737*C38
    ROcp5_838 = ROcp5_26*S38+ROcp5_837*C38
    ROcp5_938 = ROcp5_36*S38+ROcp5_937*C38
    OMcp5_15 = qd[5]*C4
    OMcp5_25 = qd[5]*S4
    OPcp5_15 = -qd[4]*qd[5]*S4+qdd[5]*C4
    OPcp5_25 = qd[4]*qd[5]*C4+qdd[5]*S4
    OMcp5_16 = OMcp5_15+qd[6]*ROcp5_45
    OMcp5_26 = OMcp5_25+qd[6]*ROcp5_55
    OMcp5_36 = qd[4]+qd[6]*S5
    OPcp5_16 = OPcp5_15+qd[6]*(-qd[4]*ROcp5_55+OMcp5_25*S5)+qdd[6]*ROcp5_45
    OPcp5_26 = OPcp5_25+qd[6]*(qd[4]*ROcp5_45-OMcp5_15*S5)+qdd[6]*ROcp5_55
    OPcp5_36 = qdd[4]+qd[6]*(OMcp5_15*ROcp5_55-OMcp5_25*ROcp5_45)+qdd[6]*S5
    RLcp5_17 = ROcp5_16*s.dpt[1,13]+ROcp5_45*s.dpt[2,13]+ROcp5_76*s.dpt[3,13]
    RLcp5_27 = ROcp5_26*s.dpt[1,13]+ROcp5_55*s.dpt[2,13]+ROcp5_86*s.dpt[3,13]
    RLcp5_37 = ROcp5_36*s.dpt[1,13]+ROcp5_96*s.dpt[3,13]+s.dpt[2,13]*S5
    POcp5_17 = q[1]+RLcp5_17
    POcp5_27 = q[2]+RLcp5_27
    POcp5_37 = q[3]+RLcp5_37
    OMcp5_17 = OMcp5_16+qd[36]*ROcp5_16
    OMcp5_27 = OMcp5_26+qd[36]*ROcp5_26
    OMcp5_37 = OMcp5_36+qd[36]*ROcp5_36
    ORcp5_17 = OMcp5_26*RLcp5_37-OMcp5_36*RLcp5_27
    ORcp5_27 = -OMcp5_16*RLcp5_37+OMcp5_36*RLcp5_17
    ORcp5_37 = OMcp5_16*RLcp5_27-OMcp5_26*RLcp5_17
    VIcp5_17 = qd[1]+ORcp5_17
    VIcp5_27 = qd[2]+ORcp5_27
    VIcp5_37 = qd[3]+ORcp5_37
    OPcp5_17 = OPcp5_16+qd[36]*(OMcp5_26*ROcp5_36-OMcp5_36*ROcp5_26)+qdd[36]*ROcp5_16
    OPcp5_27 = OPcp5_26+qd[36]*(-OMcp5_16*ROcp5_36+OMcp5_36*ROcp5_16)+qdd[36]*ROcp5_26
    OPcp5_37 = OPcp5_36+qd[36]*(OMcp5_16*ROcp5_26-OMcp5_26*ROcp5_16)+qdd[36]*ROcp5_36
    ACcp5_17 = qdd[1]+OMcp5_26*ORcp5_37-OMcp5_36*ORcp5_27+OPcp5_26*RLcp5_37-OPcp5_36*RLcp5_27
    ACcp5_27 = qdd[2]-OMcp5_16*ORcp5_37+OMcp5_36*ORcp5_17-OPcp5_16*RLcp5_37+OPcp5_36*RLcp5_17
    ACcp5_37 = qdd[3]+OMcp5_16*ORcp5_27-OMcp5_26*ORcp5_17+OPcp5_16*RLcp5_27-OPcp5_26*RLcp5_17
    RLcp5_18 = ROcp5_436*s.dpt[2,51]
    RLcp5_28 = ROcp5_536*s.dpt[2,51]
    RLcp5_38 = ROcp5_636*s.dpt[2,51]
    POcp5_18 = POcp5_17+RLcp5_18
    POcp5_28 = POcp5_27+RLcp5_28
    POcp5_38 = POcp5_37+RLcp5_38
    OMcp5_18 = OMcp5_17+qd[37]*ROcp5_16
    OMcp5_28 = OMcp5_27+qd[37]*ROcp5_26
    OMcp5_38 = OMcp5_37+qd[37]*ROcp5_36
    ORcp5_18 = OMcp5_27*RLcp5_38-OMcp5_37*RLcp5_28
    ORcp5_28 = -OMcp5_17*RLcp5_38+OMcp5_37*RLcp5_18
    ORcp5_38 = OMcp5_17*RLcp5_28-OMcp5_27*RLcp5_18
    VIcp5_18 = ORcp5_18+VIcp5_17
    VIcp5_28 = ORcp5_28+VIcp5_27
    VIcp5_38 = ORcp5_38+VIcp5_37
    OPcp5_18 = OPcp5_17+qd[37]*(OMcp5_27*ROcp5_36-OMcp5_37*ROcp5_26)+qdd[37]*ROcp5_16
    OPcp5_28 = OPcp5_27+qd[37]*(-OMcp5_17*ROcp5_36+OMcp5_37*ROcp5_16)+qdd[37]*ROcp5_26
    OPcp5_38 = OPcp5_37+qd[37]*(OMcp5_17*ROcp5_26-OMcp5_27*ROcp5_16)+qdd[37]*ROcp5_36
    ACcp5_18 = ACcp5_17+OMcp5_27*ORcp5_38-OMcp5_37*ORcp5_28+OPcp5_27*RLcp5_38-OPcp5_37*RLcp5_28
    ACcp5_28 = ACcp5_27-OMcp5_17*ORcp5_38+OMcp5_37*ORcp5_18-OPcp5_17*RLcp5_38+OPcp5_37*RLcp5_18
    ACcp5_38 = ACcp5_37+OMcp5_17*ORcp5_28-OMcp5_27*ORcp5_18+OPcp5_17*RLcp5_28-OPcp5_27*RLcp5_18
    RLcp5_19 = ROcp5_737*s.dpt[3,53]
    RLcp5_29 = ROcp5_837*s.dpt[3,53]
    RLcp5_39 = ROcp5_937*s.dpt[3,53]
    POcp5_19 = POcp5_18+RLcp5_19
    POcp5_29 = POcp5_28+RLcp5_29
    POcp5_39 = POcp5_38+RLcp5_39
    OMcp5_19 = OMcp5_18+qd[38]*ROcp5_437
    OMcp5_29 = OMcp5_28+qd[38]*ROcp5_537
    OMcp5_39 = OMcp5_38+qd[38]*ROcp5_637
    ORcp5_19 = OMcp5_28*RLcp5_39-OMcp5_38*RLcp5_29
    ORcp5_29 = -OMcp5_18*RLcp5_39+OMcp5_38*RLcp5_19
    ORcp5_39 = OMcp5_18*RLcp5_29-OMcp5_28*RLcp5_19
    VIcp5_19 = ORcp5_19+VIcp5_18
    VIcp5_29 = ORcp5_29+VIcp5_28
    VIcp5_39 = ORcp5_39+VIcp5_38
    OPcp5_19 = OPcp5_18+qd[38]*(OMcp5_28*ROcp5_637-OMcp5_38*ROcp5_537)+qdd[38]*ROcp5_437
    OPcp5_29 = OPcp5_28+qd[38]*(-OMcp5_18*ROcp5_637+OMcp5_38*ROcp5_437)+qdd[38]*ROcp5_537
    OPcp5_39 = OPcp5_38+qd[38]*(OMcp5_18*ROcp5_537-OMcp5_28*ROcp5_437)+qdd[38]*ROcp5_637
    ACcp5_19 = ACcp5_18+OMcp5_28*ORcp5_39-OMcp5_38*ORcp5_29+OPcp5_28*RLcp5_39-OPcp5_38*RLcp5_29
    ACcp5_29 = ACcp5_28-OMcp5_18*ORcp5_39+OMcp5_38*ORcp5_19-OPcp5_18*RLcp5_39+OPcp5_38*RLcp5_19
    ACcp5_39 = ACcp5_38+OMcp5_18*ORcp5_29-OMcp5_28*ORcp5_19+OPcp5_18*RLcp5_29-OPcp5_28*RLcp5_19
    PxF4[1] = POcp5_19
    PxF4[2] = POcp5_29
    PxF4[3] = POcp5_39
    RxF4[1,1] = ROcp5_138
    RxF4[1,2] = ROcp5_238
    RxF4[1,3] = ROcp5_338
    RxF4[2,1] = ROcp5_437
    RxF4[2,2] = ROcp5_537
    RxF4[2,3] = ROcp5_637
    RxF4[3,1] = ROcp5_738
    RxF4[3,2] = ROcp5_838
    RxF4[3,3] = ROcp5_938
    VxF4[1] = VIcp5_19
    VxF4[2] = VIcp5_29
    VxF4[3] = VIcp5_39
    OMxF4[1] = OMcp5_19
    OMxF4[2] = OMcp5_29
    OMxF4[3] = OMcp5_39
    AxF4[1] = ACcp5_19
    AxF4[2] = ACcp5_29
    AxF4[3] = ACcp5_39
    OMPxF4[1] = OPcp5_19
    OMPxF4[2] = OPcp5_29
    OMPxF4[3] = OPcp5_39
 
# Sensor Forces 

    SWr1 = s.user_ExtForces(PxF1,RxF1,VxF1,OMxF1,AxF1,OMPxF1,s,tsim,1)
    SWr2 = s.user_ExtForces(PxF2,RxF2,VxF2,OMxF2,AxF2,OMPxF2,s,tsim,2)
    SWr3 = s.user_ExtForces(PxF3,RxF3,VxF3,OMxF3,AxF3,OMPxF3,s,tsim,3)
    SWr4 = s.user_ExtForces(PxF4,RxF4,VxF4,OMxF4,AxF4,OMPxF4,s,tsim,4)
    xfrc12 = RxF1[1,1]*SWr1[1]+RxF1[1,2]*SWr1[2]+RxF1[1,3]*SWr1[3]
    xfrc22 = RxF1[2,1]*SWr1[1]+RxF1[2,2]*SWr1[2]+RxF1[2,3]*SWr1[3]
    xfrc32 = RxF1[3,1]*SWr1[1]+RxF1[3,2]*SWr1[2]+RxF1[3,3]*SWr1[3]
    xtrq12 = RxF1[1,1]*SWr1[4]+RxF1[1,2]*SWr1[5]+RxF1[1,3]*SWr1[6]
    xtrq22 = RxF1[2,1]*SWr1[4]+RxF1[2,2]*SWr1[5]+RxF1[2,3]*SWr1[6]
    xtrq32 = RxF1[3,1]*SWr1[4]+RxF1[3,2]*SWr1[5]+RxF1[3,3]*SWr1[6]
    trqext_1_12_1 = xtrq12-xfrc22*SWr1[9]+xfrc32*SWr1[8]
    trqext_2_12_1 = xtrq22+xfrc12*SWr1[9]-xfrc32*SWr1[7]
    trqext_3_12_1 = xtrq32-xfrc12*SWr1[8]+xfrc22*SWr1[7]
    xfrc13 = RxF2[1,1]*SWr2[1]+RxF2[1,2]*SWr2[2]+RxF2[1,3]*SWr2[3]
    xfrc23 = RxF2[2,1]*SWr2[1]+RxF2[2,2]*SWr2[2]+RxF2[2,3]*SWr2[3]
    xfrc33 = RxF2[3,1]*SWr2[1]+RxF2[3,2]*SWr2[2]+RxF2[3,3]*SWr2[3]
    xtrq13 = RxF2[1,1]*SWr2[4]+RxF2[1,2]*SWr2[5]+RxF2[1,3]*SWr2[6]
    xtrq23 = RxF2[2,1]*SWr2[4]+RxF2[2,2]*SWr2[5]+RxF2[2,3]*SWr2[6]
    xtrq33 = RxF2[3,1]*SWr2[4]+RxF2[3,2]*SWr2[5]+RxF2[3,3]*SWr2[6]
    trqext_1_17_2 = xtrq13-xfrc23*SWr2[9]+xfrc33*SWr2[8]
    trqext_2_17_2 = xtrq23+xfrc13*SWr2[9]-xfrc33*SWr2[7]
    trqext_3_17_2 = xtrq33-xfrc13*SWr2[8]+xfrc23*SWr2[7]
    xfrc14 = RxF3[1,1]*SWr3[1]+RxF3[1,2]*SWr3[2]+RxF3[1,3]*SWr3[3]
    xfrc24 = RxF3[2,1]*SWr3[1]+RxF3[2,2]*SWr3[2]+RxF3[2,3]*SWr3[3]
    xfrc34 = RxF3[3,1]*SWr3[1]+RxF3[3,2]*SWr3[2]+RxF3[3,3]*SWr3[3]
    xtrq14 = RxF3[1,1]*SWr3[4]+RxF3[1,2]*SWr3[5]+RxF3[1,3]*SWr3[6]
    xtrq24 = RxF3[2,1]*SWr3[4]+RxF3[2,2]*SWr3[5]+RxF3[2,3]*SWr3[6]
    xtrq34 = RxF3[3,1]*SWr3[4]+RxF3[3,2]*SWr3[5]+RxF3[3,3]*SWr3[6]
    trqext_1_35_3 = xtrq14-xfrc24*SWr3[9]+xfrc34*SWr3[8]
    trqext_2_35_3 = xtrq24+xfrc14*SWr3[9]-xfrc34*SWr3[7]
    trqext_3_35_3 = xtrq34-xfrc14*SWr3[8]+xfrc24*SWr3[7]
    xfrc15 = RxF4[1,1]*SWr4[1]+RxF4[1,2]*SWr4[2]+RxF4[1,3]*SWr4[3]
    xfrc25 = RxF4[2,1]*SWr4[1]+RxF4[2,2]*SWr4[2]+RxF4[2,3]*SWr4[3]
    xfrc35 = RxF4[3,1]*SWr4[1]+RxF4[3,2]*SWr4[2]+RxF4[3,3]*SWr4[3]
    xtrq15 = RxF4[1,1]*SWr4[4]+RxF4[1,2]*SWr4[5]+RxF4[1,3]*SWr4[6]
    xtrq25 = RxF4[2,1]*SWr4[4]+RxF4[2,2]*SWr4[5]+RxF4[2,3]*SWr4[6]
    xtrq35 = RxF4[3,1]*SWr4[4]+RxF4[3,2]*SWr4[5]+RxF4[3,3]*SWr4[6]
    trqext_1_38_4 = xtrq15-xfrc25*SWr4[9]+xfrc35*SWr4[8]
    trqext_2_38_4 = xtrq25+xfrc15*SWr4[9]-xfrc35*SWr4[7]
    trqext_3_38_4 = xtrq35-xfrc15*SWr4[8]+xfrc25*SWr4[7]
 
# Symbolic model output

    frc[1,12] = s.frc[1,12]+xfrc12
    frc[2,12] = s.frc[2,12]+xfrc22
    frc[3,12] = s.frc[3,12]+xfrc32
    trq[1,12] = s.trq[1,12]+trqext_1_12_1
    trq[2,12] = s.trq[2,12]+trqext_2_12_1
    trq[3,12] = s.trq[3,12]+trqext_3_12_1
    frc[1,17] = s.frc[1,17]+xfrc13
    frc[2,17] = s.frc[2,17]+xfrc23
    frc[3,17] = s.frc[3,17]+xfrc33
    trq[1,17] = s.trq[1,17]+trqext_1_17_2
    trq[2,17] = s.trq[2,17]+trqext_2_17_2
    trq[3,17] = s.trq[3,17]+trqext_3_17_2
    frc[1,35] = s.frc[1,35]+xfrc14
    frc[2,35] = s.frc[2,35]+xfrc24
    frc[3,35] = s.frc[3,35]+xfrc34
    trq[1,35] = s.trq[1,35]+trqext_1_35_3
    trq[2,35] = s.trq[2,35]+trqext_2_35_3
    trq[3,35] = s.trq[3,35]+trqext_3_35_3
    frc[1,38] = s.frc[1,38]+xfrc15
    frc[2,38] = s.frc[2,38]+xfrc25
    frc[3,38] = s.frc[3,38]+xfrc35
    trq[1,38] = s.trq[1,38]+trqext_1_38_4
    trq[2,38] = s.trq[2,38]+trqext_2_38_4
    trq[3,38] = s.trq[3,38]+trqext_3_38_4

# Number of continuation lines = 0

