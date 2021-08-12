from numpy import tri
from manimlib.imports import *
import math
import os
import pyclbr

global txtsc
txtsc=2

def title_of_video(self): # 开头
    text=Text(
        "浅谈平面几何",
        font="Microsoft YaHei",
        t2c={"平面":RED,"几何":"#2196F3"},
        stroke_width=0.5,
    ).scale(1.2*txtsc)
    line=Line(
        np.array([-5,0,0]),
        np.array([5,0,0]),
        color=BLUE,
        stroke_width=6.0,
    )
    text2=Text(
        "Chapter 1 - 三角函数",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.3*txtsc)
    text2.next_to(line,DOWN*1.2)
    v1=VGroup(text,line,text2)

    self.play(Write(text))
    self.play(text.move_to,UP*1.2)
    self.play(Write(line),run_time=0.2)
    self.play(Write(text2))
    self.wait(0.5)
    self.play(FadeOut(v1),run_time=0.2)

def thanks(self): # 结尾
    text=Text(
        "Thanks!",
        font="Microsoft YaHei",
        t2c={"T":"#EF5350","h":"#2196F3","a":"#FB8C00","n":"#00FBA5","k":"#FFA000","s":"#536DFE"},
        stroke_width=0.5,
    ).scale(1.4)
    text2=Text(
        "工具: Manim - 3Blue1Brown",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24)
    text3=Text(
        "BGM: Zeta - 3Blue1Brown",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24); text3.next_to(text2,DOWN,aligned_edge=LEFT)
    text4=Text(
        "字幕: Arctime",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24); text4.next_to(text3,DOWN,aligned_edge=LEFT)
    Vtext=VGroup(text2,text3,text4)
    Vtext.move_to(ORIGIN)

    text.move_to(ORIGIN)
    self.play(Write(text)); self.wait(1)
    Vtext.next_to(text,DOWN,buff=1.3)
    self.play(Write(Vtext))

def cont(self): # 目录
    text=Text(
        "Content 目录",
        font="Microsoft YaHei",
        color="#2196F3",
        stroke_width=1.5,
    ).scale(0.4)
    text.to_corner(UL,buff=0.5)
    line=Line(
        np.array([-7,0,0]),
        np.array([4,0,0]),
        color="#2196F3",
        stroke_width=3.0,
    )
    line.next_to(text,DOWN*0.45,aligned_edge=LEFT)
    v1=VGroup(text,line)
    self.play(FadeInFrom(v1,LEFT),runtime=1); self.wait(1)

    dA=Dot(radius=0.05); dB=Dot(radius=0.05); dC=Dot(radius=0.05)
    dA.move_to(np.array([-6,-3,0])); dC.move_to(np.array([-4,-3,0])); dB.move_to(np.array([-4,-0.5,0]))
    tri=Polygon(np.array([-6,-3,0]),np.array([-4,-3,0]),np.array([-4,-0.5,0]))
    tA=TextMobject("A",color=WHITE,stroke_width=0).scale(0.5)
    tB=TextMobject("B",color=WHITE,stroke_width=0).scale(0.5)
    tC=TextMobject("C",color=WHITE,stroke_width=0).scale(0.5)
    tA.next_to(dA,DL*0.1)
    tB.next_to(dB,UR*0.1)
    tC.next_to(dC,DR*0.1)
    Vt=VGroup(tri,tA,tB,tC,dA,dB,dC)
    Vt.scale(0.7,about_point=np.array([-6,-3,0]))
    Vt.shift(UP*1.3+RIGHT)
    ta=TexMobject("\\sin A=\\frac{BC}{AB}\\\\ \\cos A=\\frac{AC}{AB}\\\\ \\tan A=\\frac{BC}{AC}",color=WHITE,stroke_width=0).scale(0.3)
    ta.next_to(tri,DOWN,buff=0.3)
    Vt.add(ta)

    ddA=Dot(radius=0.05,color=BLUE); ddA.move_to(np.array([-2,0,0]))
    l1=Line(np.array([-2,0,0]),np.array([1.3,0,0]),color=interpolate_color("#2196F3","#FB8C00",0.5)); l2=Line(np.array([-2,0,0]),np.array([1.3,0,0]),color="#2196F3"); l3=Line(np.array([-2,0,0]),np.array([1.3,0,0]),color="#FB8C00")
    l2.rotate(0.5,axis=OUT,about_point=np.array([-2,0,0])); l3.rotate(0.5,axis=IN,about_point=np.array([-2,0,0]))
    arc1=Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3")
    arc2=Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00")
    ang1=TextMobject("0.5 rad",color="#2196F3",stroke_width=0).scale(0.6); ang2=TextMobject("-0.5 rad",color="#FB8C00",stroke_width=0).scale(0.6)
    ang1.next_to(arc1,RIGHT*0.1); ang2.next_to(arc2,RIGHT*0.1)
    Vangle=VGroup(arc1,arc2,l1,l2,l3,ddA,ang1,ang2)
    Vangle.shift(RIGHT*0.35); Vangle.scale(0.7); Vangle.shift(DOWN*1.2)

    axes=Axes(
        x_min=-1.4,x_max=1.4,y_min=-1.4,y_max=1.4,
        axis_config={
            "tick_frequency": 0.5,
            "unit_size": 2.5,
        },
    )
    axes.add_coordinates()
    circle=Circle(stroke_color="#2196F3",stroke_width=4,radius=2.5); ddd=Dot(color=BLUE); ddp=Dot(color=BLUE); ddp.move_to(RIGHT*2.5*math.cos(50*DEGREES)+UP*2.5*math.sin(50*DEGREES))
    ll1=Line(np.array([0,0,0]),np.array([2.5,0,0]),color="#FB8C00"); ll2=Line(np.array([0,0,0]),np.array([2.5,0,0]),color="#FB8C00")
    ll3=DashedLine(np.array([2.5*math.cos(50*DEGREES),2.5*math.sin(50*DEGREES),0]),np.array([2.5*math.cos(50*DEGREES),0,0])); ll2.rotate(50*DEGREES,about_point=ORIGIN)
    arcp=Sector(arc_center=ORIGIN,radius=0.15,angle=50*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=4.8,stroke_color="#FB8C00")
    angp=TexMobject("P(\\cos\\alpha,\\sin\\alpha)",color=WHITE).scale(0.6); angp.next_to(ddp,UR*0.1)
    angg=TexMobject("\\alpha",color="#FB8C00").scale(0.7); angg.next_to(arcp,RIGHT*0.02+UP*0.01)
    Vcircle=VGroup(axes,axes.get_axis_labels(),circle,arcp,ll1,ll2,ll3,ddd,ddp,angp,angg).scale(0.5)
    Vcircle.move_to(RIGHT*5+DOWN*1.2)

    VIP=VGroup(Vt,Vangle,Vcircle); VIP.shift(LEFT*0.8)

    dot1=Dot(color=BLUE,)
    text1=Text("锐角三角函数",font="Microsoft YaHei",stroke_width=0,).scale(0.35)
    dot1.move_to(6*LEFT+2.3*UP)
    text1.next_to(dot1,RIGHT*0.8)
    V1=VGroup(dot1,text1)
    self.play(FadeInFrom(V1,LEFT),FadeInFrom(Vt,LEFT),runtime=1)
    self.wait(0.5)

    dot2=Dot(color=BLUE,)
    text2=Text("简单解三角形",font="Microsoft YaHei",stroke_width=0,).scale(0.35)
    dot2.next_to(dot1,DOWN*1.5)
    text2.next_to(dot2,RIGHT*0.8)
    V2=VGroup(dot2,text2)
    self.play(FadeInFrom(V2,LEFT),runtime=1)
    self.wait(0.5)

    dot3=Dot(color=BLUE,)
    text3=Text("任意角和弧度制",font="Microsoft YaHei",stroke_width=0,).scale(0.35)
    dot3.next_to(dot2,DOWN*1.5)
    text3.next_to(dot3,RIGHT*0.8)
    V3=VGroup(dot3,text3)
    self.play(FadeInFrom(V3,LEFT),FadeInFrom(Vangle,LEFT),runtime=1)
    self.wait(0.5)

    dot4=Dot(color=BLUE,)
    text4=Text("三角函数",font="Microsoft YaHei",stroke_width=0,).scale(0.35)
    dot4.next_to(dot3,DOWN*1.5)
    text4.next_to(dot4,RIGHT*0.8)
    V4=VGroup(dot4,text4)
    self.play(FadeInFrom(V4,LEFT),FadeInFrom(Vcircle,LEFT),runtime=1)
    self.wait(2)
    
    SVIP=VGroup(VIP,V1,V2,V3,V4,v1)
    self.play(FadeOutAndShift(SVIP,RIGHT))

def turnin(self,sss): # 章节标题开始
    text=Text("< "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8)
    self.play(FadeInFromDown(text)); self.wait(0.7)
    self.play(FadeOutAndShift(text,UP))

def turnout(self,sss): # 章节标题结束
    text=Text("< "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8)
    text2=Text("</ "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8)
    text.move_to(ORIGIN); text2.move_to(ORIGIN)

    self.play(FadeInFromDown(text)); self.wait(0.7)
    self.play(Transform(text,text2)); self.wait(0.7)
    self.play(FadeOutAndShift(text,UP))

def DownTime(self,ttt,moving=ORIGIN): # 倒计时
    sss=Text(str(ttt),color="#448AFF",font="Microsoft YaHei",); sss.move_to(DOWN*3+moving)
    self.play(FadeIn(sss),Flash(DOWN*3+moving,color="FB8C00",flash_radius=0.8),runtime=0.2); self.wait(0.3)
    for i in range(ttt-1,-1,-1):
        now=Text(str(i),color="#448AFF",font="Microsoft YaHei",); now.move_to(DOWN*3+moving)
        self.play(Transform(sss,now),Flash(DOWN*3+moving,color="FB8C00",flash_radius=0.8),runtime=0.2)
        if(i): self.wait(0.3)
    self.play(FadeOut(sss))

def sc1(self): # 锐角三角函数
    dA=Dot(radius=0.1); dB=Dot(radius=0.1); dC=Dot(radius=0.1)
    dA.move_to(np.array([-1.5,-2,0])); dB.move_to(np.array([1.5,2,0])); dC.move_to(np.array([1.5,-2,0]))
    squ1=Square(side_length=0.2,fill_color=BLUE,fill_opacity=0.2,stroke_width=4,stroke_color=BLUE,); squ1.move_to(dC.get_center(),aligned_edge=DR)
    tri1=Polygon(dA.get_center(),dB.get_center(),dC.get_center(),color="#2196F3",stroke_width=5)
    tA=TextMobject("A",color=WHITE,stroke_width=0)
    tB=TextMobject("B",color=WHITE,stroke_width=0)
    tC=TextMobject("C",color=WHITE,stroke_width=0)
    tA.next_to(dA,DL*0.1)
    tB.next_to(dB,UR*0.1)
    tC.next_to(dC,DR*0.1)

    dD=Dot(radius=0.1); dE=Dot(radius=0.1)
    dD.move_to(np.array([0.5,2.0/3.0,0])); dE.move_to(np.array([0.5,-2,0]))
    squ2=Square(side_length=0.2,fill_color=BLUE,fill_opacity=0.2,stroke_width=4,stroke_color=BLUE,); squ2.move_to(dE.get_center(),aligned_edge=DR)
    tri2=Polygon(dA.get_center(),dD.get_center(),dE.get_center(),stroke_width=5,color="#FB8C00")
    tD=TextMobject("D",color=WHITE,stroke_width=0)
    tE=TextMobject("E",color=WHITE,stroke_width=0)
    tD.next_to(dD,UR*0.1)
    tE.next_to(dE,DR*0.1)

    Vt1=VGroup(squ1,tri1,tA,tB,tC,dA,dB,dC); Vt2=VGroup(squ2,tri2,tA,tD,tE,dA,dD,dE)
    VIP=VGroup(squ1,tri1,tA,tB,tC,dA,dB,dC,squ2,tri2,tD,tE,dD,dE); VIP.move_to(ORIGIN)
    self.play(FadeIn(Vt1)); self.wait(1); self.play(TransformFromCopy(Vt1,Vt2))
    self.wait(1.5); self.play(VIP.move_to,RIGHT*3); self.wait(1.5)

    al1=TexMobject("\\frac{AB}{AC}","=","\\frac{AD}{AE}",); al1[0].set_color("#2196F3"); al1[2].set_color("#FB8C00")
    al2=TexMobject("\\frac{AB}{BC}","=","\\frac{AD}{DE}",); al2[0].set_color("#2196F3"); al2[2].set_color("#FB8C00"); al2.next_to(al1,DOWN)
    al3=TexMobject("\\frac{AC}{BC}","=","\\frac{AE}{DE}",); al3[0].set_color("#2196F3"); al3[2].set_color("#FB8C00"); al3.next_to(al2,DOWN)
    Val=VGroup(al1,al2,al3); Val.move_to(LEFT*3)
    self.play(TransformFromCopy(VGroup(tA,tB,tC,tD,tE),al1)); self.wait(1)
    self.play(TransformFromCopy(VGroup(tA,tB,tC,tD,tE),al2)); self.wait(1)
    self.play(TransformFromCopy(VGroup(tA,tB,tC,tD,tE),al3)); self.wait(3)

    l1=Line(dB.get_center(),dC.get_center(),color="#2196F3",stroke_width=5,)
    l2=Line(dA.get_center(),dC.get_center(),color="#FB8C00",stroke_width=5,)
    l3=Line(dA.get_center(),dB.get_center(),color="#00BFA5",stroke_width=5,)
    tl1=TexMobject("a","\\ \\text{对边}",color="#2196F3"); tl2=TexMobject("b","\\ \\text{邻边}",color="#FB8C00"); tl3=TexMobject("c","\\ \\text{斜边}",color="#00BFA5")
    tl1.next_to(l1,RIGHT*0.5); tl2.next_to(l2,DOWN*0.5); tl3.next_to(l3.get_center(),UP*0.3+LEFT*0.3)
    self.play(FadeOut(Val),FadeOut(VGroup(squ2,tri2,tD,tE,dA,dB,dC,dD,dE)))
    self.play(FadeIn(VGroup(l1,tl1))); self.wait(1.5)
    self.play(FadeIn(VGroup(l2,tl2))); self.wait(1.5)
    self.play(FadeIn(VGroup(l3,tl3,dA,dB,dC))); self.wait(3.5)
    # self.play(FadeOut(tri1),FadeIn(VGroup(l1,l2,l3,tl1,tl2,tl3,dA,dB,dC))); self.wait(1.5)
    al4=TexMobject("\\sin A=\\frac{a}{c}=\\frac{\\text{对边}}{\\text{斜边}}",)
    al4[0][5].set_color("#2196F3"); al4[0][7].set_color("#00FBA5"); al4[0][9:11].set_color("#2196F3"); al4[0][12:14].set_color("#00FBA5")
    al5=TexMobject("\\cos A=\\frac{b}{c}=\\frac{\\text{邻边}}{\\text{斜边}}",)
    al5[0][5].set_color("#FB8C00"); al5[0][7].set_color("#00FBA5"); al5[0][9:11].set_color("#FB8C00"); al5[0][12:14].set_color("#00FBA5"); al5.next_to(al4,DOWN)
    al6=TexMobject("\\tan A=\\frac{a}{b}=\\frac{\\text{对边}}{\\text{邻边}}",)
    al6[0][5].set_color("#2196F3"); al6[0][7].set_color("#FB8C00"); al6[0][9:11].set_color("#2196F3"); al6[0][12:14].set_color("#FB8C00"); al6.next_to(al5,DOWN)
    Val=VGroup(al4,al5,al6); Val.move_to(LEFT*3)
    self.play(TransformFromCopy(VGroup(tl1[0],tl1[1],tl3[0],tl3[1]),al4)); self.wait(2)
    self.play(TransformFromCopy(VGroup(tl2[0],tl2[1],tl3[0],tl3[1]),al5)); self.wait(2)
    self.play(TransformFromCopy(VGroup(tl1[0],tl1[1],tl2[0],tl2[1]),al6)); self.wait(2.5)
    DownTime(self,5)
    self.play(FadeOut(VGroup(squ1,tri1,tA,tB,tC,dA,dB,dC,l1,l2,l3,tl1,tl2,tl3,al4,al5,al6)))

def sc2(self):
    ScaleNum=1.8
    q1=Text("Example. 在",font="Microsoft YaHei",color="#2196F3",stroke_width=0,t2c={"Example.":RED})
    q2=TexMobject("Rt\\triangle ABC",color="#2196F3",).scale(ScaleNum); q2.next_to(q1,RIGHT)
    q3=Text("中, ",font="Microsoft YaHei",color="#2196F3",stroke_width=0,); q3.next_to(q2,RIGHT)
    q4=TexMobject("\\angle C=90^\\circ,\\angle B=30^\\circ,a=\\sqrt 7",color="#2196F3",).scale(ScaleNum); q4.next_to(q3,RIGHT)
    q5=Text(", 解这个直角三角形.",font="Microsoft YaHei",color="#2196F3",stroke_width=0,); q5.next_to(q4,RIGHT)
    vq=VGroup(q1,q2,q3,q4,q5); vq.scale(0.33); vq.move_to(UP*3)
    self.play(Write(vq),run_time=2.2); self.wait(0.5)
    DownTime(self,5)

    dA=Dot(radius=0.1); dB=Dot(radius=0.1); dC=Dot(radius=0.1)
    dA.move_to(np.array([3,1,0])); dB.move_to(np.array([3-np.sqrt(3)*2.0,-1,0])); dC.move_to(np.array([3,-1,0]))
    squ1=Square(side_length=0.2,fill_color=BLUE,fill_opacity=0.2,stroke_width=4,stroke_color=BLUE,); squ1.move_to(dC.get_center(),aligned_edge=DR)
    tri1=Polygon(dA.get_center(),dB.get_center(),dC.get_center(),color="#2196F3",stroke_width=5)
    tA=TextMobject("A",color=WHITE,stroke_width=0).scale(0.5); tA.next_to(dA,UR*0.1)
    tB=TextMobject("B",color=WHITE,stroke_width=0).scale(0.5); tB.next_to(dB,DL*0.1)
    tC=TextMobject("C",color=WHITE,stroke_width=0).scale(0.5); tC.next_to(dC,DR*0.1)
    l1=TexMobject("\\sqrt 7",).scale(0.5); l1.next_to(tri1,DOWN,buff=0.12)
    l2=TexMobject("?",).scale(0.5); l2.next_to(tri1,RIGHT,buff=0.12)
    l3=TexMobject("?",).scale(0.5); l3.next_to(tri1.get_center(),LEFT,buff=0.4)
    arc1=Sector(arc_center=dB.get_center(),radius=0.3,angle=30*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=5,stroke_color="#FB8C00").scale(0.5,about_point=dB.get_center())
    ang1=TexMobject("30^\\circ",color="#FB8C00",stroke_width=0).scale(0.4); ang1.next_to(arc1,RIGHT*0.2)
    arc2=Sector(arc_center=dA.get_center(),start_angle=-90*DEGREES,radius=0.3,angle=-60*DEGREES,color="#00FBA5",fill_color="#00FBA5",fill_opacity=0.2,stroke_width=5,stroke_color="#00FBA5").scale(0.5,about_point=dA.get_center())
    ang2=TexMobject("?",color="#00FBA5",stroke_width=0).scale(0.4); ang2.next_to(arc2,DOWN*0.2)
    vt=VGroup(squ1,arc1,arc2,tri1,dA,dB,dC,tA,tB,tC,l1,l2,l3,ang1,ang2).scale(1.5); vt.move_to(ORIGIN)
    self.play(FadeIn(vt)); self.wait(2); self.play(vt.shift,LEFT*3)
    
    ans1=TexMobject(
        "& \\tan B=\\frac{b}{a}=\\frac{\\sqrt 3}{3}\\\\",
        "& \\therefore b=a\\times \\tan B=\\frac{\\sqrt{21}}{3}\\\\",
        "& \\therefore c=\\sqrt{a^2+b^2}=\\frac{2}{3}\\sqrt{21}\\\\",
        "& \\angle A=60^\\circ",
    ).scale(0.7)
    ans1.move_to(np.array([2,vt.get_center()[1],0]),aligned_edge=LEFT)
    self.play(FadeIn(ans1[0])); self.wait(2)
    self.play(FadeIn(ans1[1])); self.play(Transform(l2,TexMobject("\\frac{\\sqrt{21}}{3}").scale(0.5).move_to(l2.get_center()+RIGHT*0.1))); self.wait(1.75)
    self.play(FadeIn(ans1[2])); self.play(Transform(l3,TexMobject("\\frac{2}{3}\\sqrt{21}").scale(0.5).move_to(l3.get_center()+UP*0.1))); self.wait(1.75)
    self.play(FadeIn(ans1[3])); self.play(Transform(ang2,TexMobject("60^\\circ",color="#00FBA5").scale(0.6).move_to(ang2.get_center()))); self.wait(2.75)
    DownTime(self,5)

    self.play(FadeOut(vt),FadeOut(vq),FadeOut(ans1))
    q1=Text("Exercise. 在",font="Microsoft YaHei",color="#2196F3",stroke_width=0,t2c={"Exercise.":RED})
    q2=TexMobject("Rt\\triangle ABC",color="#2196F3",).scale(ScaleNum); q2.next_to(q1,RIGHT)
    q3=Text("中, ",font="Microsoft YaHei",color="#2196F3",stroke_width=0,); q3.next_to(q2,RIGHT)
    q4=TexMobject("a=b,c=2",color="#2196F3",).scale(ScaleNum); q4.next_to(q3,RIGHT)
    q5=Text(", 解这个直角三角形.",font="Microsoft YaHei",color="#2196F3",stroke_width=0,); q5.next_to(q4,RIGHT)
    vq=VGroup(q1,q2,q3,q4,q5); vq.scale(0.33); vq.move_to(UP*3)
    self.play(Write(vq),run_time=2.2); self.wait(0.5)
    DownTime(self,5)
    self.play(FadeOut(vq))

def sc3(self): # 任意角
    ddA=Dot(radius=0.05,color=BLUE,plot_depth=5,); ddA.move_to(np.array([-2,0,0]))
    l1=Line(np.array([-2,0,0]),np.array([2,0,0]),color=interpolate_color("#2196F3","#FB8C00",0.5),plot_depth=1,)
    l2=Line(np.array([-2,0,0]),np.array([2,0,0]),color="#2196F3",plot_depth=1,)
    l3=Line(np.array([-2,0,0]),np.array([2,0,0]),color="#FB8C00",plot_depth=1,)
    l2.rotate(0.5,axis=OUT,about_point=np.array([-2,0,0])); l3.rotate(0.5,axis=IN,about_point=np.array([-2,0,0]))
    arc1=Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))
    arc2=Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-arc1.angle,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))
    ang1=TexMobject("\\alpha",color="#2196F3",stroke_width=0,plot_depth=10,).scale(0.6)
    ang2=TexMobject("-\\alpha",color="#FB8C00",stroke_width=0,plot_depth=10,).scale(0.6)
    ang1.next_to(arc1,RIGHT*0.1); ang2.next_to(arc2,RIGHT*0.1)
    Vangle=VGroup(arc1,arc2,l1,l2,l3,ang1,ang2,ddA)

    self.wait(1.5)
    self.play(Write(l1),Write(ddA)); self.wait(1.5)
    self.play(TransformFromCopy(l1,l2))
    self.play(Write(arc1),Write(ang1)); self.wait(2.5)
    self.play(TransformFromCopy(l1,l3))
    self.play(Write(arc2),Write(ang2)); self.wait(2.5)
    ang1.add_updater(lambda d: d.next_to(arc1,RIGHT*0.1))
    ang2.add_updater(lambda d: d.next_to(arc2,RIGHT*0.1))
    self.play(
        Rotate(l2,angle=30*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=30*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5+30*DEGREES,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5-30*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(1)
    self.play(
        Rotate(l2,angle=40*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=40*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5-10*DEGREES,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5+10*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(1)
    self.play(
        Rotate(l2,angle=100*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=100*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5+90*DEGREES,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5-90*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(1)
    self.play(
        Rotate(l2,angle=80*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=80*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5+170*DEGREES,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5-170*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(1)
    self.play(
        Rotate(l2,angle=220*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=220*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5-50*DEGREES,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5+50*DEGREES,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(1)
    self.play(
        Rotate(l2,angle=50*DEGREES,axis=OUT,about_point=np.array([-2,0,0])),
        Rotate(l3,angle=50*DEGREES,axis=IN,about_point=np.array([-2,0,0])),
        Transform(arc1,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=0.5,color="#2196F3",fill_color="#2196F3",fill_opacity=0.2,stroke_width=2.4,stroke_color="#2196F3",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0]))),
        Transform(arc2,Sector(arc_center=np.array([-2,0,0]),radius=1,angle=-0.5,color="#FB8C00",fill_color="#FB8C00",fill_opacity=0.2,stroke_width=2.4,stroke_color="#FB8C00",plot_depth=0,).scale(0.7,about_point=np.array([-2,0,0])))
    ); self.wait(2.5)
    DownTime(self,5)
    self.play(FadeOut(Vangle))

def sc4(self): # 弧度制
    cdot1=Dot(); cdot1.move_to(30*RIGHT+30*UP)
    cdot2=Dot(); cdot2.move_to(50*RIGHT+30*UP)

    circle=Circle(stroke_color="#2196F3",stroke_width=4,radius=2.5,plot_depth=0,); d=Dot(color=BLUE)
    p1=Dot(color=BLUE,plot_depth=5,); p1.move_to(RIGHT*2.5*math.cos(30*DEGREES)+UP*2.5*math.sin(30*DEGREES))
    p2=Dot(color=BLUE,plot_depth=5,); p2.move_to(RIGHT*2.5*math.cos(50*DEGREES)+UP*2.5*math.sin(50*DEGREES))
    ap1=TexMobject("P_1",color=WHITE,plot_depth=10,).scale(0.6); ap1.next_to(p1,UR*0.1)
    ap2=TexMobject("P_2",color=WHITE,plot_depth=10,).scale(0.6); ap2.next_to(p2,UR*0.1)
    apo=TexMobject("O",color=WHITE,plot_depth=10,).scale(0.6); apo.next_to(d,DL*0.1)
    l1=Line(d.get_center(),p1.get_center(),color=BLUE,plot_depth=1,)
    l2=Line(d.get_center(),p2.get_center(),color=BLUE,plot_depth=1,)
    radi=TexMobject("1",color=WHITE,plot_depth=10,).scale(0.6); radi.next_to(l1.get_center(),DR*0.1)
    arc=Sector(radius=1,start_angle=30*DEGREES,angle=20*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7).move_to(ORIGIN,aligned_edge=DL)
    carc=Arc(radius=2.5,start_angle=30*DEGREES,angle=20*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)
    num=DecimalNumber(0,color="#00FBA5").scale(0.6); num.next_to(carc.get_center(),UR*0.3)
    num2=DecimalNumber(0,)
    text=TexMobject("\\angle O="); num2.next_to(text,RIGHT)
    text2=TexMobject("\\text{rad}",color=RED,); text2.next_to(num2,RIGHT)
    vtext=VGroup(text,num2,text2); vtext.move_to(DOWN*3)

    num.add_updater(lambda d: d.set_value(arc.angle))
    num2.add_updater(lambda d: d.set_value(arc.angle))
    l1.add_updater(lambda t: t.put_start_and_end_on(d.get_center(),RIGHT*2.5*math.cos(cdot1.get_center()[0]*DEGREES)+UP*2.5*math.sin(cdot1.get_center()[0]*DEGREES)))
    l2.add_updater(lambda t: t.put_start_and_end_on(d.get_center(),RIGHT*2.5*math.cos(cdot2.get_center()[0]*DEGREES)+UP*2.5*math.sin(cdot2.get_center()[0]*DEGREES)))
    ap1.add_updater(lambda d: d.next_to(p1,UR*0.1))
    ap2.add_updater(lambda d: d.next_to(p2,UR*0.1))
    p1.add_updater(lambda d: d.move_to(RIGHT*2.5*math.cos(cdot1.get_center()[0]*DEGREES)+UP*2.5*math.sin(cdot1.get_center()[0]*DEGREES)))
    p2.add_updater(lambda d: d.move_to(RIGHT*2.5*math.cos(cdot2.get_center()[0]*DEGREES)+UP*2.5*math.sin(cdot2.get_center()[0]*DEGREES)))
    num.add_updater(lambda d: d.next_to(carc.get_center(),UR*0.3))
    num.add_updater(lambda d: d.set_value(DEGREES*(cdot2.get_center()[0]-cdot1.get_center()[0])))
    num2.add_updater(lambda d: d.set_value(DEGREES*(cdot2.get_center()[0]-cdot1.get_center()[0])))
    radi.add_updater(lambda d: d.next_to(l1.get_center(),DR*0.1))
    num2.add_updater(lambda d: d.next_to(text,RIGHT))
    text2.add_updater(lambda d: d.next_to(num2,RIGHT))
    vtext.add_updater(lambda d: d.move_to(DOWN*3))

    # arc.set_plot_depth(0); carc.set_plot_depth(0); p1.set_plot_depth(5); p2.set_plot_depth(5); d.set_plot_depth(5)
    # circle.set_plot_depth(-1); ap1.set_plot_depth(10); ap2.set_plot_depth(10); radi.set_plot_depth(10); num.set_plot_depth(20)

    self.play(Write(VGroup(circle,d,apo))); self.wait(1.5)
    self.play(FadeIn(VGroup(ap1,ap2,l1,l2,radi,p1,p2))); self.wait(1.5)
    self.play(Write(arc),Write(carc)); self.wait(1.5)
    self.play(FadeIn(num)); self.wait(1.5)
    self.play(FadeIn(vtext)); self.wait(3)

    self.play(
        cdot2.move_to,80*RIGHT+30*UP,
        Transform(arc,Sector(radius=1,start_angle=30*DEGREES,angle=50*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7).move_to(ORIGIN,aligned_edge=DL)),
        Transform(carc,Arc(radius=2.5,start_angle=30*DEGREES,angle=50*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot1.move_to,ORIGIN+30*UP,
        cdot2.move_to,180/PI*RIGHT+30*UP,
        Transform(arc,Sector(radius=1,start_angle=0,angle=1,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7).move_to(ORIGIN,aligned_edge=DL)),
        Transform(carc,Arc(radius=2.5,start_angle=0,angle=1,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot1.move_to,20*RIGHT+30*UP,
        cdot2.move_to,30*LEFT+30*UP,
        Transform(arc,Sector(arc_center=LEFT*0.09+UP*0.02,radius=1,start_angle=20*DEGREES,angle=-50*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7)),
        Transform(carc,Arc(radius=2.5,start_angle=20*DEGREES,angle=-50*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot2.move_to,220*RIGHT+30*UP,
        Transform(arc,Sector(arc_center=DOWN*0.03,radius=1,start_angle=20*DEGREES,angle=200*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7)),
        Transform(carc,Arc(radius=2.5,start_angle=20*DEGREES,angle=200*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot1.move_to,20*LEFT+30*UP,
        cdot2.move_to,70*RIGHT+30*UP,
        Transform(arc,Sector(arc_center=DOWN*0.09+LEFT*0.14,radius=1,start_angle=-20*DEGREES,angle=90*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7)),
        Transform(carc,Arc(radius=2.5,start_angle=-20*DEGREES,angle=90*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot1.move_to,20*LEFT+30*UP,
        cdot2.move_to,160*RIGHT+30*UP,
        Transform(arc,Sector(arc_center=DOWN*0.09,radius=1,start_angle=-20*DEGREES,angle=180*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7)),
        Transform(carc,Arc(radius=2.5,start_angle=-20*DEGREES,angle=180*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    self.play(
        cdot1.move_to,30*RIGHT+30*UP,
        cdot2.move_to,50*RIGHT+30*UP,
        Transform(arc,Sector(arc_center=0.02*DOWN+0.02*LEFT,radius=1,start_angle=30*DEGREES,angle=20*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=2.4,stroke_color=BLUE,plot_depth=0,).scale(0.7)),
        Transform(carc,Arc(radius=2.5,start_angle=30*DEGREES,angle=20*DEGREES,stroke_width=5,stroke_color="#FB8C00",plot_depth=0,)),
    ); self.wait(1.5)
    DownTime(self,5,moving=RIGHT*4+UP*3)
    self.play(FadeOut(VGroup(cdot1,cdot2,arc,carc,p1,p2,ap1,ap2,apo,d,vtext,num,l1,l2,radi,circle)))

def sc5(self): # 三角函数
    cdot1=Dot(); cdot1.move_to(50*RIGHT+30*UP)

    axes=Axes(
        x_min=-1.6,x_max=1.6,y_min=-1.6,y_max=1.6,
        axis_config={
            "tick_frequency": 1,
            "unit_size": 2,
        },
    )
    axes.add_coordinates()
    circ=Circle(stroke_color="#2196F3",stroke_width=4,radius=2)
    d=Dot(color=WHITE); p=Dot(color=BLUE)
    p.move_to(axes.c2p(math.cos(50*DEGREES),math.sin(50*DEGREES)))
    l1=Line(d.get_center(),p.get_center(),color="#FB8C00")
    l2=DashedLine(np.array([p.get_center()[0],0,0]),p.get_center())
    tP=TexMobject("P(x,y)",color=WHITE).scale(0.6); tP.next_to(p.get_center(),UR,buff=0.06); tP[0][2].set_color("#00FBA5"); tP[0][4].set_color("#FB8C00")
    tO=TexMobject("O").scale(0.6); tO.next_to(ORIGIN,DL,buff=0.1)
    tA=TexMobject("A").scale(0.6); tA.next_to(axes.c2p(1,0),UR,buff=0.1)
    VA=VGroup(axes,axes.get_axis_labels(),circ,l1,l2,d,p,tO,tP,tA)

    self.play(FadeIn(VGroup(axes,VA[1]))); self.wait(1.5)
    self.play(Write(VGroup(circ,d,tO))); self.wait(1.5)
    self.play(FadeIn(VGroup(l1,l2,p,tP,tA))); self.wait(1.5)
    self.play(VA.move_to,LEFT*3)

    text=TexMobject(
        "\\angle AOP= \\\\",
        "\\sin \\angle AOP=y= \\\\",
        "\\cos \\angle AOP=x= \\\\",
        "\\tan \\angle AOP=\\frac{y}{x}=",
    ); text[1][8].set_color("#FB8C00"); text[2][8].set_color("#00FBA5"); text[3][8:11].set_color("#EF5350")
    tt=Text("(无意义)",font="Microsoft YaHei",color=RED,stroke_width=0).scale(0.45)
    nsin=DecimalNumber(0,color="#FB8C00"); nsin.add_updater(lambda t: t.next_to(text[1],RIGHT,buff=0.3))
    ncos=DecimalNumber(0,color="#00FBA5"); ncos.add_updater(lambda t: t.next_to(text[2],RIGHT,buff=0.3))
    ntan=DecimalNumber(0,color="#EF5350"); ntan.add_updater(lambda t: t.next_to(text[3],RIGHT,buff=0.3)); tt.next_to(ntan,DOWN*0.2+RIGHT*5.5)
    nang=DecimalNumber(0); nang.add_updater(lambda t: t.next_to(text[0],RIGHT,buff=0.3))
    ang=TexMobject("^\\circ"); ang.add_updater(lambda t: t.next_to(nang,UR,buff=0.03))
    VT=VGroup(text,nang,ang,nsin,ncos,ntan).scale(0.8); VT.move_to(RIGHT*3)

    nang.add_updater(lambda t: t.set_value(cdot1.get_center()[0]))
    nsin.add_updater(lambda t: t.set_value(math.sin(cdot1.get_center()[0]*DEGREES)))
    ncos.add_updater(lambda t: t.set_value(math.cos(cdot1.get_center()[0]*DEGREES)))
    ntan.add_updater(lambda t: t.set_value(math.sin(cdot1.get_center()[0]*DEGREES)/math.cos(cdot1.get_center()[0]*DEGREES)))
    p.add_updater(lambda t: t.move_to(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l1.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(0,0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l2.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    tP.add_updater(lambda t: t.next_to(p.get_center(),UR,buff=0.06))

    self.play(Write(VT[0][0]),Write(VT[1]),Write(VT[2])); self.wait(1.5)
    self.play(Write(VT[0][1]),Write(VT[3])); self.wait(2)
    self.play(Write(VT[0][2]),Write(VT[4])); self.wait(2)
    self.play(Write(VT[0][3]),Write(VT[5])); self.wait(2)
    self.play(cdot1.move_to,30*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,60*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,90*RIGHT+30*UP,run_time=2); self.play(FadeIn(tt)); self.wait(1.5); self.play(FadeOut(tt))
    self.play(cdot1.move_to,270*RIGHT+30*UP,run_time=5); self.play(FadeIn(tt)); self.wait(1.5); self.play(FadeOut(tt))
    self.play(cdot1.move_to,315*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,360*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,410*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,50*RIGHT+30*UP,run_time=5); self.wait(1)
    self.play(cdot1.move_to,-120*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,50*RIGHT+30*UP,run_time=2); self.wait(1)
    DownTime(self,5)
    self.play(FadeOut(VA),FadeOut(VT)) 

class Part1(GraphScene):
    def construct(self):
        title_of_video(self)
        cont(self)
        turnin(self,"锐角三角函数")
        sc1(self)
        turnout(self,"锐角三角函数")
        turnin(self,"简单解三角形")
        sc2(self)
        turnout(self,"简单解三角形")
        turnin(self,"任意角和弧度制")
        sc3(self)
        sc4(self)
        turnout(self,"任意角和弧度制")
        turnin(self,"三角函数")
        sc5(self)
        turnout(self,"三角函数")
        thanks(self)

# python -m manim pmjh1.py Part1 -p