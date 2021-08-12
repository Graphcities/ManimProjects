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
        "Chapter 2 - 平面向量初步",
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
        t2c={"T":"#00FBA5","h":"#536DFE","a":"#EF5350","n":"#FB8C00","k":"#2196F3","s":"#FFA000"},
        stroke_width=0.5,
    ).scale(1.4*txtsc)
    text2=Text(
        "工具: Manim - 3Blue1Brown",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc)
    text3=Text(
        "BGM1: Lake of Opportunity - Through the Fog",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text3.next_to(text2,DOWN,aligned_edge=LEFT)
    text31=Text(
        "BGM2: Head in the Clouds - Through the Fog",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text31.next_to(text3,DOWN,aligned_edge=LEFT)
    text4=Text(
        "字幕: Arctime",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text4.next_to(text31,DOWN,aligned_edge=LEFT)
    text5=Text(
        "剪辑: DaVinci Resolve 17",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text5.next_to(text4,DOWN,aligned_edge=LEFT)
    Vtext=VGroup(text2,text3,text31,text4,text5)
    Vtext.move_to(ORIGIN)

    text.move_to(ORIGIN)
    self.play(Write(text)); self.wait(1)
    Vtext.next_to(text,DOWN,buff=0.8)
    self.play(Write(Vtext))

def cont(self): # 目录
    text=Text(
        "Content 目录",
        font="Microsoft YaHei",
        color="#2196F3",
        stroke_width=1.5,
    ).scale(0.4*txtsc)
    text.to_corner(UL,buff=0.5)
    line=Line(
        np.array([-7,0,0]),
        np.array([4,0,0]),
        color="#2196F3",
        stroke_width=3.0,
    )
    line.next_to(text,DOWN*0.45,aligned_edge=LEFT)
    v1=VGroup(text,line); VIP=VGroup(v1)
    self.play(FadeInFrom(v1,LEFT),runtime=1); self.wait(1)

    dot=[Dot()]*6
    tit=["","向量的定义和性质","向量的线性运算","平面向量的坐标表示","向量的点积和叉积"]
    tt=[Text("",font="Microsoft YaHei",)]*6
    Vt=[VGroup()]*6

    for i in range(1,5):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc)
        if(i==1): dot[i].move_to(6*LEFT+2.3*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        tt[i].next_to(dot[i],RIGHT*0.8); Vt[i]=VGroup(dot[i],tt[i])
        self.play(FadeInFrom(Vt[i],LEFT),runtime=1); self.wait(0.5); VIP.add(Vt[i])

    self.wait(0.75)
    self.play(FadeOutAndShift(VIP,RIGHT))

def turnin(self,sss): # 章节标题开始
    text=Text("< "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8*txtsc)
    self.play(FadeInFromDown(text)); self.wait(0.7)
    self.play(FadeOutAndShift(text,UP))

def turnout(self,sss): # 章节标题结束
    text=Text("< "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8*txtsc)
    text2=Text("</ "+sss+" >",color="#448AFF",font="Microsoft YaHei",stroke_width=0.5,).scale(0.8*txtsc)
    text.move_to(ORIGIN); text2.move_to(ORIGIN)

    self.play(FadeInFromDown(text)); self.wait(0.7)
    self.play(Transform(text,text2)); self.wait(0.7)
    self.play(FadeOutAndShift(text,UP))

def DownTime(self,ttt,moving=ORIGIN): # 倒计时
    sss=Text(str(ttt),color="#448AFF",font="Microsoft YaHei",stroke_width=4,).scale(txtsc); sss.move_to(DOWN*3+moving)
    self.play(FadeIn(sss),Flash(DOWN*3+moving,color="FB8C00",flash_radius=0.8),runtime=0.2); self.wait(0.3)
    for i in range(ttt-1,-1,-1):
        now=Text(str(i),color="#448AFF",font="Microsoft YaHei",stroke_width=4,).scale(txtsc); now.move_to(DOWN*3+moving)
        self.play(Transform(sss,now),Flash(DOWN*3+moving,color="FB8C00",flash_radius=0.8),runtime=0.2)
        if(i): self.wait(0.3)
    self.play(FadeOut(sss))

def Car(self,opa=1): # 小车车
    cir1=Circle(radius=2,color="#546E7A",fill_color="#546E7A",fill_opacity=opa,stroke_width=0).scale(0.21).move_to(DOWN+LEFT)
    cir2=Circle(radius=2,color="#546E7A",fill_color="#546E7A",fill_opacity=opa,stroke_width=0).scale(0.21).move_to(DOWN+RIGHT)
    rect=Rectangle(height=2,weight=3,color="#546E7A",fill_color="#546E7A",fill_opacity=opa,stroke_width=0)
    car=VGroup(rect,cir1,cir2)
    return car

def sc1(self): # 向量的定义
    car=Car(self).scale(0.7).move_to(LEFT*4)
    car2=Car(self,opa=0.6).scale(0.7).move_to(RIGHT*4); car2.set_plot_depth(-1)
    dot=Dot(radius=0.1,plot_depth=5,color=BLUE); dot.move_to(car.get_center()+UP*0.2)
    a1=Arrow(car.get_center()+UP*0.2,RIGHT*4+UP*0.2,color="#2196F3",buff=0,plot_depth=1); t1=TexMobject("x",color="#2196F3",plot_depth=10,); t1.next_to(a1,UP,aligned_edge=RIGHT,buff=0.1); VA1=VGroup(a1,t1)
    a2=Arrow(car.get_center()+UP*0.2,RIGHT*2+UP*0.2,color="#FB8C00",buff=0,plot_depth=2); t2=TexMobject("F",color="#FB8C00",plot_depth=10,); t2.next_to(a2,UP,aligned_edge=RIGHT,buff=0.1); VA2=VGroup(a2,t2)
    a3=Arrow(car.get_center()+UP*0.2,RIGHT*0+UP*0.2,color="#00FBA5",buff=0,plot_depth=3); t3=TexMobject("v",color="#00FBA5",plot_depth=10,); t3.next_to(a3,UP,aligned_edge=RIGHT,buff=0.1); VA3=VGroup(a3,t3)
    text=TexMobject("v","\\ \\ \\","F","\\ \\ \\","x").scale(2.0); text[4].set_color("#2196F3"); text[2].set_color("#FB8C00"); text[0].set_color("#00FBA5"); text.move_to(DOWN*1)
    
    self.play(FadeIn(car)); self.wait(1.2)
    self.play(Write(dot),Write(VA1),TransformFromCopy(car,car2),run_time=1.2); self.wait(1.2)
    self.play(Write(VA2),run_time=1.2); self.wait(1.2)
    self.play(Write(VA3),run_time=1.2); self.wait(1.2)
    self.play(TransformFromCopy(VGroup(t3,t2,t1).copy(),text)); self.wait(4.5)
    DownTime(self,3)
    self.play(FadeOut(VGroup(car,car2,dot,VA1,VA2,VA3,text)))

    l1=Line(LEFT*20+UP*2.7,RIGHT*20+UP*2.7,color=TEAL_C,stroke_width=6)
    l2=Line(UP*20,DOWN*20,color=TEAL_C,stroke_width=6); prel=VGroup(l1,l2)
    self.play(Write(prel)); self.wait(1.2)
    tit1=Text("Vector 向量",font="Microsoft YaHei",color="#2196F3",stroke_width=0,).scale(0.65*txtsc); tit1.move_to(np.array([-3.55,3.35,0]))
    tit2=Text("Scalar 标量",font="Microsoft YaHei",color="#2196F3",stroke_width=0,).scale(0.65*txtsc); tit2.move_to(np.array([ 3.55,3.35,0]))

    dot=[Dot()]*7
    tit=["","速度","力","位移","质量","面积","温度"]
    sgn=["","v"   ,"F" ,"x"   ,"m"   ,"S"   ,"T"]
    tt=[Text("",font="Microsoft YaHei",)]*7
    ttt=[TexMobject("")]*7
    Vt=[VGroup()]*7; VIP1=VGroup(); VIP2=VGroup()
    for i in range(1,4):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc); ttt[i]=TexMobject(sgn[i]).scale(0.7)
        if(i==1): dot[i].move_to(6*LEFT+2*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        tt[i].next_to(dot[i],RIGHT*0.8); ttt[i].next_to(tt[i],RIGHT,buff=0.15); Vt[i]=VGroup(dot[i],tt[i],ttt[i])
        VIP1.add(Vt[i])
    for i in range(4,7):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc); ttt[i]=TexMobject(sgn[i]).scale(0.7)
        if(i==4): dot[i].move_to(1.2*RIGHT+2*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        tt[i].next_to(dot[i],RIGHT*0.8); ttt[i].next_to(tt[i],RIGHT,buff=0.15); Vt[i]=VGroup(dot[i],tt[i],ttt[i])
        VIP2.add(Vt[i])
    anims=AnimationGroup(*[FadeInFrom(mob,LEFT) for mob in VIP1],lag_ratio=0.08); self.play(FadeInFrom(tit1,LEFT)); self.play(anims); self.wait(1.2)
    anims=AnimationGroup(*[FadeInFrom(mob,LEFT) for mob in VIP2],lag_ratio=0.08); self.play(FadeInFrom(tit2,LEFT)); self.play(anims); self.wait(1.2)
    self.play(l2.put_start_and_end_on,UP*20,DOWN*2); DownTime(self,3); self.play(l2.put_start_and_end_on,UP*20,DOWN*20)
    self.play(FadeOutAndShift(VGroup(VIP1,VIP2,tit1,tit2,l1,l2),RIGHT))

def sc2(self): # 向量的性质
    d1=Dot(radius=0.1,color=BLUE,plot_depth= 5); d1.move_to(np.array([-3,-2,0]))
    d2=Dot(radius=0.1,color=BLUE,plot_depth=-1); d2.move_to(np.array([ 3, 2,0]))
    tA=TexMobject("A",color="#2196F3",plot_depth=10); tA.next_to(d1.get_center(),DR,buff=0.01)
    tB=TexMobject("B",color="#2196F3",plot_depth=10); tB.next_to(d2.get_center(),DR,buff=0.07)
    a1=Arrow(d1.get_center(),d2.get_center(),color="#2196F3",buff=0,plot_depth=0)
    tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.05)
    dc1=DecimalNumber(0,color="#00FBA5").scale(0.6); dc1.next_to(a1.get_center(),DR*0.3); dc1.set_value(np.sqrt(40))
    dc2=DecimalNumber(0,color="#00FBA5");                                                 dc2.set_value(np.sqrt(40))
    alg1=TexMobject("|\\vec a|","="); alg1[0].set_color("#2196F3"); dc2.next_to(alg1,RIGHT,buff=0.2); VA1=VGroup(alg1,dc2); VA1.move_to(DOWN*1.7)
    vec1=VGroup(d2,a1,d1,tA,tB)
    self.play(Write(vec1)); self.wait(1.2)
    self.play(ShowCreationThenDestructionAround(VGroup(d1,tA))); self.wait(1.2)
    self.play(ShowCreationThenDestructionAround(VGroup(d2,tB))); self.wait(1.2)
    self.play(GrowArrow(a1)); self.wait(1.2)
    self.play(Write(tv1)); self.wait(1.2)
    self.play(Write(dc1),Write(VA1)); self.wait(1.2)
    DownTime(self,3)
    self.play(FadeOut(VGroup(d1,d2,tA,tB,dc1,VA1)))
    
    vec1=VGroup(a1,tv1)
    a2=Arrow(np.array([-2.1,-1.4,0]),np.array([2.1,1.4,0]),color="#FB8C00",buff=0,plot_depth=0)
    tv2=TexMobject("\\vec b",color="#FB8C00",plot_depth=10); tv2.next_to(a2.get_center(),UL,buff=0.05)
    vec2=VGroup(a2,tv2)
    a3=Arrow(np.array([3.9,2.6,0]),np.array([-3.9,-2.6,0]),color="#00FBA5",buff=0,plot_depth=0)
    tv3=TexMobject("\\vec c",color="#00FBA5",plot_depth=10); tv3.next_to(a3.get_center(),UL,buff=0.05)
    vec3=VGroup(a3,tv3)
    self.play(vec1.scale,0.75); vec2.scale(0.75); vec3.scale(0.75)
    vec2.move_to(ORIGIN); vec3.move_to(RIGHT*3)
    self.play(vec1.move_to,LEFT*3,Write(vec2),Write(vec3)); self.wait(1.5)
    self.play(
        a1.put_start_and_end_on,ORIGIN,np.array([6*0.75,4*0.75,0]),MaintainPositionRelativeTo(tv1,a1),
        a2.put_start_and_end_on,ORIGIN,np.array([4.2*0.75,2.8*0.75,0]),MaintainPositionRelativeTo(tv2,a2),
        a3.put_start_and_end_on,ORIGIN,np.array([-7.8*0.75,-5.2*0.75,0]),MaintainPositionRelativeTo(tv3,a3),
    ); self.wait(1.5)
    self.play(
        vec1.move_to,LEFT*3,
        vec2.move_to,ORIGIN,
        vec3.move_to,RIGHT*3,
    ); self.wait(1.5)
    self.play(a2.put_start_and_end_on,np.array([-3*0.75,-2*0.75,0]),np.array([3*0.75,2*0.75,0])); self.wait(2.5)
    self.play(a3.put_start_and_end_on,np.array([3*0.75+3,2*0.75,0]),np.array([-3*0.75+3,-2*0.75,0])); self.wait(2.5)
    DownTime(self,3)
    self.play(FadeOutAndShift(vec1,UR),FadeOutAndShift(vec2,UR),FadeOutAndShift(vec3,DL))

def sc3(self): # 向量的加减法
    ttll=0.25; mnt=1.25
    a1=Arrow(np.array([-4,-2+mnt,0]),np.array([0,2+mnt,0]),color="#2196F3",buff=0,plot_depth=0,tip_length=ttll)
    tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.03)
    vec1=VGroup(a1,tv1)
    a2=Arrow(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0,plot_depth=0,tip_length=ttll)
    tv2=TexMobject("\\vec b",color="#FB8C00",plot_depth=10); tv2.next_to(a2.get_center(),UR,buff=0.1)
    vec2=VGroup(a2,tv2)
    a3=Arrow(np.array([-4,-2+mnt,0]),np.array([4,1.5+mnt,0]),color="#00FBA5",buff=0,plot_depth=0,tip_length=ttll)
    tv3=TexMobject("\\vec c",color="#00FBA5",plot_depth=10); tv3.next_to(a3.get_center(),DR,buff=0.08)
    vec3=VGroup(a3,tv3)
    self.play(Write(VGroup(vec1,vec2,vec3))); self.wait(1.2)

    dot=Dot(); dot.move_to(np.array([-4,-2+mnt,0])); self.play(FadeIn(dot)); self.wait(1)
    self.play(dot.move_to,np.array([0,2+mnt,0])); self.wait(0.5); self.play(dot.move_to,np.array([4,1.5+mnt,0])); self.wait(1)
    self.play(FadeOut(dot)); dot.move_to(np.array([-4,-2+mnt,0])); self.play(FadeIn(dot)); self.wait(1)
    self.play(dot.move_to,np.array([4,1.5+mnt,0])); self.wait(0.5); self.play(FadeOut(dot)); self.wait(2.4)
    alg1=TexMobject("\\vec a","+","\\vec b","=","\\vec c").scale(1.25); alg1[0].set_color("#2196F3"); alg1[2].set_color("#FB8C00"); alg1[4].set_color("#00FBA5")
    alg2=TexMobject("\\vec c","-","\\vec b","=","\\vec a").scale(1.25); alg2[0].set_color("#00FBA5"); alg2[2].set_color("#2196F3"); alg2[4].set_color("#FB8C00")
    alg1.move_to(DOWN*2); alg2.move_to(DOWN*2)
    self.play(TransformFromCopy(VGroup(tv1,tv2,tv3),alg1)); self.wait(1.5)
    self.play(CyclicReplace(alg1[0],alg1[4]),Transform(alg1[1],alg2[1])); self.wait(2.5)
    self.play(FadeOut(vec3),FadeOut(alg1),vec2.shift,4*LEFT+4*DOWN); self.wait(1.2)

    a4=DashedLine(np.array([0,-2.5+mnt,0]),np.array([4,1.5+mnt,0]),color="#2196F3",buff=0); a4.add_tip(ttll)
    a5=DashedLine(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0); a5.add_tip(ttll)
    self.play(TransformFromCopy(a1,a4),TransformFromCopy(a2,a5)); self.wait(1.2)
    self.play(Write(vec3)); self.wait(1.2)
    alg3=TexMobject("\\vec a","+","\\vec b","=","\\vec c").scale(1.25); alg3[0].set_color("#2196F3"); alg3[2].set_color("#FB8C00"); alg3[4].set_color("#00FBA5")
    alg4=TexMobject("\\vec c","-","\\vec b","=","\\vec a").scale(1.25); alg4[0].set_color("#00FBA5"); alg4[2].set_color("#2196F3"); alg4[4].set_color("#FB8C00")
    alg3.move_to(DOWN*2); alg4.move_to(DOWN*2)
    self.play(TransformFromCopy(VGroup(tv1,tv2,tv3),alg3)); self.wait(1.2)
    self.play(CyclicReplace(alg3[0],alg3[4]),Transform(alg3[1],alg4[1])); self.wait(1.2)
    DownTime(self,3,moving=UP*3+RIGHT*4.5)
    self.play(FadeOut(VGroup(vec1,vec2,vec3,a4,a5,alg3)))

def sc4(self): # 向量的数乘
    a1=Arrow(np.array([-4,-1.5,0]),np.array([-2,-0.75,0]),color="#2196F3",buff=5)
    tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.03);
    vec1=VGroup(a1,tv1)
    vec2=vec1.copy(); vec2.next_to(np.array([-2,-0.75,0]),UR,buff=0)
    vec3=vec1.copy(); vec3.next_to(np.array([-2+(-2+4),-0.75+(-0.75+1.5),0]),UR,buff=0)
    vec4=vec1.copy(); vec4.next_to(np.array([-2+2*(-2+4),-0.75+2*(-0.75+1.5),0]),UR,buff=0)
    a5=Arrow(np.array([-4,-1.5,0]),np.array([-2+3*(-2+4),-0.75+3*(-0.75+1.5),0]),color="#FB8C00",buff=0,plot_depth=0)
    tv5=TexMobject("\\vec b",color="#FB8C00",plot_depth=10); tv5.next_to(a5.get_center(),DR,buff=0.06)
    vec5=VGroup(a5,tv5)
    alg1=TexMobject("\\vec b","=","4 ","\\vec a",plot_depth=10).scale(1.25); alg1[0].set_color("#FB8C00"); alg1[2].set_color(RED); alg1[3].set_color("#2196F3")
    alg1.move_to(DOWN*2+RIGHT*2)

    a11=a1.copy(); tv11=tv1.copy(); vec11=vec1.copy(); vec11.set_plot_depth(5); a22=a11.copy()

    self.play(Write(vec1)); self.wait(1.2)
    self.play(TransformFromCopy(vec1,vec2),TransformFromCopy(vec1,vec3),TransformFromCopy(vec1,vec4)); self.wait(1.2)
    self.play(ReplacementTransform(VGroup(vec1,vec2,vec3,vec4),vec5)); self.wait(1); self.play(Write(vec11)); self.wait(1.2)
    self.play(TransformFromCopy(tv11,alg1[3]),TransformFromCopy(tv5,alg1[0]),FadeIn(alg1[1]),FadeIn(alg1[2])); self.wait(2.5)
    self.play(ReplacementTransform(a5.copy(),a22),FadeOut(alg1)); self.wait(1.2)
    alg1=TexMobject("\\vec a","=","\\frac{1}{4}","\\vec b",plot_depth=10).scale(1.25); alg1[0].set_color("#2196F3"); alg1[2].set_color(RED); alg1[3].set_color("#FB8C00")
    alg1.move_to(DOWN*2+RIGHT*2)
    self.play(TransformFromCopy(tv11,alg1[3]),TransformFromCopy(tv5,alg1[0]),FadeIn(alg1[1]),FadeIn(alg1[2])); self.wait(1.2)
    self.play(FadeOut(VGroup(vec11,vec5,alg1,a1,a11,a22))); self.wait(1.2)

def sc5(self): # 向量的线性运算总结
    def sscc1(self):
        ttll=0.25; mnt=1.25
        a1=Arrow(np.array([-4,-2+mnt,0]),np.array([0,2+mnt,0]),color="#2196F3",buff=0,plot_depth=0,tip_length=ttll)
        tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.03)
        vec1=VGroup(a1,tv1)
        a2=Arrow(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0,plot_depth=0,tip_length=ttll)
        tv2=TexMobject("\\vec b",color="#FB8C00",plot_depth=10); tv2.next_to(a2.get_center(),UR,buff=0.1)
        vec2=VGroup(a2,tv2)
        a3=Arrow(np.array([-4,-2+mnt,0]),np.array([4,1.5+mnt,0]),color="#00FBA5",buff=0,plot_depth=0,tip_length=ttll)
        tv3=TexMobject("\\vec a+\\vec b",color="#00FBA5",plot_depth=10); tv3.next_to(a3.get_center(),DR,buff=0.01)
        vec3=VGroup(a3,tv3)
        vec2.shift(4*LEFT+4*DOWN);
        a4=DashedLine(np.array([0,-2.5+mnt,0]),np.array([4,1.5+mnt,0]),color="#2196F3",buff=0); a4.add_tip(ttll)
        a5=DashedLine(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0); a5.add_tip(ttll)
        SC1=VGroup(vec1,vec2,vec3,a4,a5)
        return SC1

    def sscc2(self):
        ttll=0.25; mnt=1.25
        a1=Arrow(np.array([-4,-2+mnt,0]),np.array([0,2+mnt,0]),color="#2196F3",buff=0,plot_depth=0,tip_length=ttll)
        tv1=TexMobject("\\vec b",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.03)
        vec1=VGroup(a1,tv1)
        a2=Arrow(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0,plot_depth=0,tip_length=ttll)
        tv2=TexMobject("\\vec a-\\vec b",color="#FB8C00",plot_depth=10); tv2.next_to(a2.get_center(),UR,buff=0.22)
        vec2=VGroup(a2,tv2)
        a3=Arrow(np.array([-4,-2+mnt,0]),np.array([4,1.5+mnt,0]),color="#00FBA5",buff=0,plot_depth=0,tip_length=ttll)
        tv3=TexMobject("\\vec a",color="#00FBA5",plot_depth=10); tv3.next_to(a3.get_center(),DR,buff=0.08)
        vec3=VGroup(a3,tv3)
        vec2.shift(4*LEFT+4*DOWN);
        a4=DashedLine(np.array([0,-2.5+mnt,0]),np.array([4,1.5+mnt,0]),color="#2196F3",buff=0); a4.add_tip(ttll)
        a5=DashedLine(np.array([0,2+mnt,0]),np.array([4,1.5+mnt,0]),color="#FB8C00",buff=0); a5.add_tip(ttll)
        SC2=VGroup(vec1,vec2,vec3,a4,a5)
        return SC2

    def sscc3(self):
        a1=Arrow(np.array([-4,-1.5,0]),np.array([-2,-0.75,0]),color="#2196F3",buff=5)
        tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10); tv1.next_to(a1.get_center(),UL,buff=0.03);
        vec1=VGroup(a1,tv1)
        a5=Arrow(np.array([-4,-1.5,0]),np.array([-2+3*(-2+4),-0.75+3*(-0.75+1.5),0]),color="#FB8C00",buff=0,plot_depth=0)
        tv5=TexMobject("4\\vec a",color="#FB8C00",plot_depth=10); tv5.next_to(a5.get_center(),DR,buff=0.06)
        vec5=VGroup(a5,tv5)
        SC3=VGroup(vec5,vec1)
        return SC3

    text=Text(
        "向量的线性运算",
        font="Microsoft YaHei",
        color="#2196F3",
        stroke_width=1.5,
    ).scale(0.4*txtsc)
    text.to_corner(UL,buff=0.5)
    line=Line(
        np.array([-7,0,0]),
        np.array([4,0,0]),
        color="#2196F3",
        stroke_width=3.0,
    )
    line.next_to(text,DOWN*0.45,aligned_edge=LEFT)
    v1=VGroup(text,line); VIP=VGroup(v1)

    dot=[Dot()]*4
    tit=["","向量的加法","向量的减法","向量的数乘"]
    tt=[Text("",font="Microsoft YaHei",)]*4
    Vt=[VGroup()]*4
    Orz=[VGroup()]*4
    
    Orz[1]=sscc1(self).scale(0.42); Orz[1].move_to(DOWN*1.7+LEFT*4.2)
    Orz[2]=sscc2(self).scale(0.42); Orz[2].move_to(DOWN*1.7)
    Orz[3]=sscc3(self).scale(0.42); Orz[3].move_to(DOWN*1.7+RIGHT*4.2)
    for i in range(1,4):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc)
        if(i==1): dot[i].move_to(6*LEFT+2.3*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        tt[i].next_to(dot[i],RIGHT*0.8); Vt[i]=VGroup(dot[i],tt[i])
        self.play(FadeInFrom(Vt[i],LEFT),FadeInFrom(Orz[i],LEFT),runtime=1); self.wait(0.5); VIP.add(Vt[i],Orz[i])

    self.play(FadeInFrom(v1,LEFT),runtime=1); self.wait(1)
    DownTime(self,5,moving=UP*4.5+RIGHT*3)
    self.play(FadeOutAndShift(VIP,RIGHT))

def sc6(self): # 平面向量基本定理
    def jbdl(self):
        text=Text(
            "平面向量基本定理",
            font="Microsoft YaHei",
            color="#2196F3",
            stroke_width=1.5,
        ).scale(0.4*txtsc)
        text.to_corner(UL,buff=0.5)
        line=Line(
            np.array([-7,0,0]),
            np.array([4,0,0]),
            color="#2196F3",
            stroke_width=3.0,
        )
        line.next_to(text,DOWN*0.45,aligned_edge=LEFT)
        v1=VGroup(text,line); return v1

    def GetPoint(self,p1,p2,p3,typ):
        line=Line(p1,p2)
        if(typ==1):
            return np.array([p1[0]+(p3[1]-p1[1])/line.get_slope(),p3[1],0])
        if(typ==2):
            return np.array([p3[0]-(p3[1]-p1[1])/line.get_slope(),p1[1],0])
    
    sc6sc=0.61; sc6bf=0.1
    dot=Dot(color=BLUE,); dot.move_to(6.25*LEFT+2.5*UP)
    t1=Text("如果",font="Microsoft YaHei",).scale(sc6sc); t1.next_to(dot,RIGHT*0.8)
    t2=TexMobject("\\vec e_1,\\vec e_2").scale(sc6sc); t2.next_to(t1,RIGHT,buff=sc6bf)
    t3=Text("是同一平面内的两个不共线向量,",font="Microsoft YaHei",).scale(sc6sc); t3.next_to(t2,RIGHT,buff=sc6bf)
    t31=Text("那么对于这一平面的",font="Microsoft YaHei",).scale(sc6sc); t31.next_to(t3,RIGHT)
    t4=Text("任意向量",font="Microsoft YaHei",).scale(sc6sc); t4.next_to(t1,DOWN,aligned_edge=LEFT)
    t41=TexMobject("\\vec a").scale(sc6sc); t41.next_to(t4,RIGHT,buff=sc6bf)
    t5=Text(", 有且只有一对实数",font="Microsoft YaHei",).scale(sc6sc); t5.next_to(t41,RIGHT,buff=sc6bf)
    t6=TexMobject("\\lambda_1,\\lambda_2").scale(sc6sc); t6.next_to(t5,RIGHT,buff=sc6bf)
    t7=Text("使得",font="Microsoft YaHei",).scale(sc6sc); t7.next_to(t6,RIGHT,buff=sc6bf)
    t8=TexMobject("\\vec a=\\lambda_1\\vec e_1+\\lambda_2\\vec e_2 .").scale(sc6sc); t8.next_to(t7,RIGHT,buff=sc6bf)
    alg=VGroup(dot,t1,t2,t3,t31,t4,t41,t5,t6,t7,t8)
    pretx=jbdl(self); self.play(FadeInFrom(pretx,LEFT)); self.wait(0.5)

    a1=Arrow(np.array([-3,-1,0]),np.array([-2.2,0.3,0]),color="#2196F3",plot_depth=5,buff=0)
    a2=Arrow(np.array([-3,-1,0]),np.array([-1.7,-1 ,0]),color="#2196F3",plot_depth=5,buff=0)
    e1=TexMobject("\\vec e_1",color="#2196F3",plot_depth=10,).scale(0.6); e1.next_to(a1.get_center(),UL,buff=0.1)
    e2=TexMobject("\\vec e_2",color="#2196F3",plot_depth=10,).scale(0.6); e2.next_to(a2.get_center(),DOWN,buff=0.1)
    aa=Arrow(np.array([-3,-1,0]),np.array([1,1.25,0]),color="#FB8C00",plot_depth=5,buff=0)
    tva=TexMobject("\\vec a",color="#FB8C00",plot_depth=10).scale(0.6); tva.next_to(aa.get_center(),DR,buff=0.1)
    ds1=DashedLine(np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),np.array([1,1.25,0]),1),color="#2196F3",plot_depth=-1,)
    ds2=DashedLine(GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),np.array([1,1.25,0]),1),np.array([1,1.25,0]),color="#2196F3",plot_depth=-1,)
    ds3=DashedLine(np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),np.array([1,1.25,0]),2),color="#2196F3",plot_depth=-1,)
    ds4=DashedLine(GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),np.array([1,1.25,0]),2),np.array([1,1.25,0]),color="#2196F3",plot_depth=-1,)

    self.play(Write(VGroup(dot,t1,t2,t3,a1,a2,e1,e2))); self.wait(1)
    self.play(Write(VGroup(t31,t4,t41,aa,tva))); self.wait(1)
    self.play(Write(VGroup(t5,t6,t7,t8)),Write(ds1),Write(ds2),Write(ds3),Write(ds4)); self.wait(1)
    tva.add_updater(lambda d: d.next_to(aa.get_center(),DR,buff=0.1))
    aend=np.array([1.5,0,0])
    self.play(
        aa.put_start_and_end_on,np.array([-3,-1,0]),aend,
        ds1.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),
        ds2.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),aend,
        ds3.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),
        ds4.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),aend,
        ); self.wait(1)
    aend=np.array([-4,1,0])
    self.play(
        aa.put_start_and_end_on,np.array([-3,-1,0]),aend,
        ds1.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),
        ds2.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),aend,
        ds3.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),
        ds4.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),aend,
        ); self.wait(1)
    aend=np.array([-5.5,-2.5,0])
    self.play(
        aa.put_start_and_end_on,np.array([-3,-1,0]),aend,
        ds1.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),
        ds2.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),aend,
        ds3.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),
        ds4.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),aend,
        ); self.wait(1)
    aend=np.array([1,-3,0])
    self.play(
        aa.put_start_and_end_on,np.array([-3,-1,0]),aend,
        ds1.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),
        ds2.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),aend,
        ds3.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),
        ds4.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),aend,
        ); self.wait(1)
    aend=np.array([1,1.25,0])
    self.play(
        aa.put_start_and_end_on,np.array([-3,-1,0]),aend,
        ds1.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),
        ds2.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,1),aend,
        ds3.put_start_and_end_on,np.array([-3,-1,0]),GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),
        ds4.put_start_and_end_on,GetPoint(self,np.array([-3,-1,0]),np.array([-2.2,0.3,0]),aend,2),aend,
        ); self.wait(1)
    DownTime(self,3)
    self.play(FadeOut(VGroup(alg,a1,a2,e1,e2,aa,tva,ds1,ds2,ds3,ds4,pretx)))

def sc7(self): # 平面向量的坐标表示
    nbp=NumberPlane(plot_depth=-100,); nbp.add_coordinates(); 
    odot=Dot(radius=0.1,plot_depth=100,color=BLUE,); odot.move_to(ORIGIN)
    otv=TexMobject("O",plot_depth=100,).scale(0.5); otv.move_to(DL*0.2)
    VNP=VGroup(nbp,nbp.get_axis_labels(),odot,otv).set_plot_depth(-100)
    self.play(FadeIn(nbp),FadeIn(odot),FadeIn(otv),FadeIn(VNP[1])); self.wait(1.2)
    
    a1=Arrow(np.array([2,1,0]),np.array([5,3,0]),buff=0,color="#2196F3",plot_depth=1,)
    tA=TexMobject("A(3,2)",plot_depth=10,).scale(0.5); tA.move_to(np.array([3,2,0]),aligned_edge=DL)
    a2=Arrow(np.array([0,0,0]),np.array([2,-3,0]),buff=0,color="#FB8C00",plot_depth=1,)
    tB=TexMobject("B(2,-3)",plot_depth=10,).scale(0.5); tB.move_to(np.array([2,-3,0]),aligned_edge=UL)
    ds1=DashedLine(np.array([2,-3,0]),np.array([5,-1,0]),buff=0,color="#2196F3",plot_depth=0.5,)
    ds2=DashedLine(np.array([3,2,0]),np.array([5,-1,0]),buff=0,color="#FB8C00",plot_depth=0.5,)
    a3=Arrow(np.array([0,0,0]),np.array([5,-1,0]),buff=0,color="#00FBA5",plot_depth=1,)
    tC=TexMobject("C(5,-1)",plot_depth=10,).scale(0.5); tC.move_to(np.array([5,-1,0]),aligned_edge=UL)
    e1=Arrow(np.array([0,0,0]),np.array([1,0,0]),buff=0,color=RED,plot_depth=1,)
    te1=TexMobject("\\vec e_1",plot_depth=10,).scale(0.5); te1.next_to(e1.get_center(),DOWN,buff=0.1)
    e2=Arrow(np.array([0,0,0]),np.array([0,1,0]),buff=0,color=RED,plot_depth=1,)
    te2=TexMobject("\\vec e_2",plot_depth=10,).scale(0.5); te2.next_to(e2.get_center(),LEFT,buff=0.1)
    dse1=DashedLine(np.array([0,0,0]),np.array([0,2,0]),buff=0,color=RED,plot_depth=0.5,)
    dse2=DashedLine(np.array([0,2,0]),np.array([3,2,0]),buff=0,color=RED,plot_depth=0.5,)
    dse3=DashedLine(np.array([0,0,0]),np.array([3,0,0]),buff=0,color=RED,plot_depth=0.5,)
    dse4=DashedLine(np.array([3,0,0]),np.array([3,2,0]),buff=0,color=RED,plot_depth=0.5,)
    self.play(Write(a1)); self.wait(1.2)
    self.play(a1.put_start_and_end_on,ORIGIN,np.array([3,2,0])); self.wait(1.2)
    self.play(Write(e1),Write(te1),Write(e2),Write(te2)); self.wait(1.2)
    self.play(Write(dse1),Write(dse2),Write(dse3),Write(dse4)); self.wait(4)
    self.play(FadeOut(VGroup(e1,te1,e2,te2,dse1,dse2,dse3,dse4))); self.wait(1)
    self.play(FadeIn(tA)); self.wait(1.2)    
    self.play(Write(a2),Write(tB)); self.wait(1.2)
    self.play(TransformFromCopy(a1,ds1),TransformFromCopy(a2,ds2)); self.wait(0.5)
    self.play(Write(a3),Write(tC)); self.wait(0.8)
    
    algsc=0.65
    alg1=TexMobject(
        "\\overrightarrow{OA} &=","(3,2)","\\\\",
        "\\overrightarrow{OB} &=","(2,-3)","\\\\",
        "\\overrightarrow{OC} &=","(3+2,2-3)","\\\\",
        plot_depth=100,
        ).scale(algsc); alg1[0:2].set_color("#2196F3"); alg1[3:5].set_color("#FB8C00"); alg1[6:8].set_color("#00FBA5")
    alg1.move_to(UP*2+LEFT*4.5);  self.wait(1.5)
    anims=AnimationGroup(*[FadeInFrom(mob,LEFT) for mob in VGroup(alg1[0:3],alg1[3:6],alg1[6:9]).set_plot_depth(100)],lag_ratio=0.2); self.play(anims); self.wait(1)
    self.play(
        Transform(tA,TexMobject("A(x_A,y_A)",plot_depth=10,).scale(0.5).move_to(np.array([3,2 ,0]),aligned_edge=DL)),
        Transform(tB,TexMobject("B(x_B,y_B)",plot_depth=10,).scale(0.5).move_to(np.array([2,-3,0]),aligned_edge=UL)),
        Transform(tC,TexMobject("C(x_C,y_C)",plot_depth=10,).scale(0.5).move_to(np.array([5,-1,0]),aligned_edge=UL)),
        Transform(alg1[1],TexMobject("(x_A,y_A)",plot_depth=100,).scale(algsc).set_color("#2196F3").move_to(alg1[1].get_center()+RIGHT*0.15)),
        Transform(alg1[4],TexMobject("(x_B,y_B)",plot_depth=100,).scale(algsc).set_color("#FB8C00").move_to(alg1[4].get_center()+RIGHT*0.05)),
        Transform(alg1[7],TexMobject("(x_A+x_B,y_A+y_B)",plot_depth=100,).scale(algsc).set_color("#00FBA5").move_to(alg1[7].get_center()+RIGHT*0.4)),
        ); self.wait(2)
    self.play(
        Transform(alg1[4],TexMobject("(x_C-x_A,y_C-y_A)",plot_depth=100,).scale(algsc).set_color("#FB8C00").move_to(alg1[4].get_center()+RIGHT*0.8)),
        Transform(alg1[7],TexMobject("(x_C,y_C)",plot_depth=100,).scale(algsc).set_color("#00FBA5").move_to(alg1[7].get_center()+LEFT*0.85)),
        ); self.wait(2)
    DownTime(self,3)
    self.play(FadeOut(VGroup(alg1,a2,tB,a3,tC,ds1,ds2)),Transform(tA,TexMobject("A(3,2)",plot_depth=10,).scale(0.5).move_to(np.array([3,2 ,0]),aligned_edge=DL)),); self.wait(0.5)
    
    a2=Arrow(np.array([0,0,0]),np.array([5,10/3,0]),buff=0,color="#FB8C00",plot_depth=0,)
    tB=TexMobject("B(5,\\frac{10}{3})",plot_depth=10,).scale(0.5); tB.move_to(np.array([5,10/3,0]),aligned_edge=UL)
    a3=Arrow(np.array([0,0,0]),np.array([1.5,1,0]),buff=0,color="#00FBA5",plot_depth=2,)
    tC=TexMobject("C(\\frac{3}{2},1)",plot_depth=10,).scale(0.5); tC.move_to(np.array([1.5,1,0]),aligned_edge=UL)
    a4=Arrow(np.array([0,0,0]),np.array([-3,-2,0]),buff=0,color="#536DFE",plot_depth=1,)
    tD=TexMobject("D(-3,-2)",plot_depth=10,).scale(0.5); tD.move_to(np.array([-3,-2,0]),aligned_edge=UR)
    alg1=TexMobject(
        "\\vec a &=","(x_1,x_2)","\\\\",
        "\\lambda\\vec a &=","(\\lambda x_1,\\lambda x_2)","\\\\",
        plot_depth=100,
        ).scale(algsc); alg1[0:2].set_color("#2196F3"); alg1[3:5].set_color("#FB8C00");
    alg1.move_to(UP*2+LEFT*4.5);  # bgalg1=BackgroundRectangle(alg1,fill_opacity=1,plot_depth=-1,)
    self.play(TransformFromCopy(a1,a2),TransformFromCopy(a1,a3),TransformFromCopy(a1,a4),Write(tB),Write(tC),Write(tD)); self.wait(1.2)
    self.play(FadeIn(alg1)); self.wait(1.5)
    DownTime(self,3)
    self.play(FadeOut(VGroup(a1,tA,a2,tB,a3,tC,a4,tD,alg1,VNP)))

def sc8(self): # 向量的点积
    car=Car(self).scale(0.7).move_to(LEFT*3).set_plot_depth(-100)
    a1=Arrow(car.get_center()+UP*0.2,RIGHT*3+UP*0.2,buff=0,color="#2196F3",plot_depth=1,)
    tv1=TexMobject("l",color="#2196F3",plot_depth=10).next_to(a1.get_center(),DOWN,buff=0.1)
    a2=Arrow(car.get_center()+UP*0.2,UP*1.7,buff=0,color="#FB8C00",plot_depth=1,)
    tv2=TexMobject("F",color="#FB8C00",plot_depth=10).next_to(a2.get_center(),UL,buff=0.02)
    dot=Dot(radius=0.08,color=BLUE,plot_depth=5).move_to(car.get_center()+UP*0.2)
    ang1=Sector(radius=1,angle=27*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=3.2,stroke_color=BLUE,plot_depth=0,).scale(0.7).move_to(dot.get_center(),aligned_edge=DL)
    tvg1=TexMobject("\\theta",color=BLUE,plot_depth=10,).next_to(ang1.get_center(),RIGHT,buff=0.4).scale(0.7)
    self.play(FadeIn(car)); self.wait(1.2)
    self.play(Write(a1),Write(tv1),Write(a2),Write(tv2),Write(dot)); self.wait(2.5)
    self.play(Write(ang1),Write(tvg1)); self.wait(1)

    ds1=DashedLine(UP*1.7,UP*0.2,plot_depth=0.5,)
    a3=Arrow(car.get_center()+UP*0.2,UP*0.2,buff=0,color="#00FBA5",plot_depth=2,)
    tv3=TexMobject("F_1",color="#00FBA5",plot_depth=10).next_to(a3.get_center(),DOWN,buff=0.1)
    self.play(Write(ds1)); self.wait(1)
    self.play(TransformFromCopy(a2,a3),Write(tv3)); self.wait(1.2)

    alg1=TexMobject("W=","F_1\\times l").scale(0.7).move_to(DOWN*1+RIGHT*0.5)
    self.play(Write(alg1)); self.wait(1.2)
    self.play(Transform(alg1[1],TexMobject("Fl\\cos\\theta").scale(0.7).next_to(alg1[0],RIGHT,buff=0.15))); self.wait(1.5)
    self.play(Transform(alg1[1],TexMobject("F\\cdot l").scale(0.7).next_to(alg1[0],RIGHT,buff=0.15))); self.wait(1.2)
    alg2=TexMobject("\\vec a \\cdot \\vec b = | \\vec a | | \\vec b | \\cos \\langle \\vec a , \\vec b \\rangle").scale(0.7).next_to(alg1,DOWN*0.2).shift(RIGHT*0.6)
    self.play(Write(alg2)); self.wait(2.5)
    DownTime(self,3)
    self.play(FadeOut(VGroup(car,alg1,alg2,a1,tv1,a2,tv2,dot,ang1,tvg1,ds1,a3,tv3)))

def sc9(self): # 向量的叉积与总结
    dot=Dot(color=BLUE,plot_depth=5,radius=0.08,).move_to(np.array([-4,-1,0]))
    a1=Arrow(np.array([-4,-1,0]),np.array([-1,2,0]),buff=0,color="#2196F3",plot_depth=1,)
    tv1=TexMobject("\\vec a",color="#2196F3",plot_depth=10,).scale(0.7).next_to(a1.get_center(),UL,buff=0.06)
    a2=Arrow(np.array([-4,-1,0]),np.array([0,-1,0]),buff=0,color="#FB8C00",plot_depth=1,)
    tv2=TexMobject("\\vec b",color="#FB8C00",plot_depth=10,).scale(0.7).next_to(a2,DOWN,buff=0.01)
    ds1=DashedLine(np.array([0,-1,0]),np.array([3,2,0]),plot_depth=0.5,color="#2196F3",)
    ds2=DashedLine(np.array([-1,2,0]),np.array([3,2,0]),plot_depth=0.5,color="#FB8C00",)
    ds3=DashedLine(np.array([-1,2,0]),np.array([-1,-1,0]),plot_depth=0,)
    tvh=TexMobject("h",plot_depth=10,).scale(0.7).next_to(ds3,RIGHT,buff=0.1)
    ang1=Sector(radius=1,angle=45.2*DEGREES,color=BLUE,fill_color=BLUE,fill_opacity=0.2,stroke_width=4.5,stroke_color=BLUE,plot_depth=0,).scale(0.7).move_to(np.array([-4,-1,0]),aligned_edge=DL)
    tvg1=TexMobject("\\theta",color=BLUE,plot_depth=10,).next_to(ang1.get_center(),RIGHT,buff=0.42).scale(0.7)
    self.play(Write(a1),Write(tv1),Write(a2),Write(tv2),Write(dot)); self.wait(1.2)
    self.play(TransformFromCopy(a1,ds1),TransformFromCopy(a2,ds2)); self.wait(2.5)
    self.play(Write(ds3),Write(tvh),Write(ang1),Write(tvg1)); self.wait(1.5)
    
    alg1=TexMobject("S=","|\\vec b|\\times h").scale(0.7).move_to(DOWN*2+RIGHT*0.5)
    self.play(Write(alg1)); self.wait(1.2)
    self.play(Transform(alg1[1],TexMobject("|\\vec a| |\\vec b| |\\sin \\theta|").scale(0.7).next_to(alg1[0],RIGHT,buff=0.15))); self.wait(1.5)
    self.play(Transform(alg1[1],TexMobject("|\\vec a\\times \\vec b|").scale(0.7).next_to(alg1[0],RIGHT,buff=0.15))); self.wait(1.2)
    alg2=TexMobject("\\vec a \\times \\vec b = | \\vec a | | \\vec b | \\sin \\langle \\vec a , \\vec b \\rangle").scale(0.7).next_to(alg1,DOWN*0.2).shift(RIGHT*0.25)
    self.play(Write(alg2)); self.wait(2.5)
    DownTime(self,3,moving=UP*3+RIGHT*4)
    self.play(FadeOut(VGroup(dot,a1,tv1,a2,tv2,ds1,ds2,ds3,tvh,ang1,tvg1,alg1,alg2)))
    
    l1=Line(LEFT*20+UP*2.7,RIGHT*20+UP*2.7,color=TEAL_C,stroke_width=6)
    l2=Line(UP*20,DOWN*20,color=TEAL_C,stroke_width=6); prel=VGroup(l1,l2)
    self.play(Write(prel)); self.wait(1.2)
    tit1=Text("Dot Product 点积",font="Microsoft YaHei",color="#2196F3",stroke_width=0,).scale(0.525*txtsc); tit1.move_to(np.array([-3.55,3.35,0]))
    tit2=Text("Cross Product 叉积",font="Microsoft YaHei",color="#2196F3",stroke_width=0,).scale(0.525*txtsc); tit2.move_to(np.array([ 3.55,3.35,0]))
    self.play(FadeInFrom(VGroup(tit1,tit2),LEFT)); self.wait(1.2)
    
    dot=[Dot()]*7
    tit=["","","钝负锐正","力和距离所做的功","","顺负逆正","有向平行四边形面积"]
    sgn=["","\\vec a \\cdot \\vec b = | \\vec a | | \\vec b | \\cos \\langle \\vec a , \\vec b \\rangle","","","\\vec a \\times \\vec b = | \\vec a | | \\vec b | \\sin \\langle \\vec a , \\vec b \\rangle","",""]
    tt=[Text("",font="Microsoft YaHei",)]*7
    ttt=[TexMobject("")]*7
    Vt=[VGroup()]*7; VIP=VGroup()
    for i in range(1,4):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc); ttt[i]=TexMobject(sgn[i]).scale(0.7)
        if(i==1): dot[i].move_to(6*LEFT+2*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        if(i>1): tt[i].next_to(dot[i],RIGHT*0.8); ttt[i].next_to(tt[i],RIGHT,buff=0.15); Vt[i]=VGroup(dot[i],tt[i],ttt[i]);
        if(i==1): ttt[i].next_to(dot[i],RIGHT*0.8); Vt[i]=VGroup(dot[i],ttt[i]); 
        VIP.add(Vt[i])
    for i in range(4,7):
        dot[i]=Dot(color=BLUE,); tt[i]=Text(tit[i],font="Microsoft YaHei",stroke_width=0,).scale(0.35*txtsc); ttt[i]=TexMobject(sgn[i]).scale(0.7)
        if(i==4): dot[i].move_to(1.2*RIGHT+2*UP)
        else: dot[i].next_to(dot[i-1],DOWN*1.5)
        if(i>4): tt[i].next_to(dot[i],RIGHT*0.8); ttt[i].next_to(tt[i],RIGHT,buff=0.15); Vt[i]=VGroup(dot[i],tt[i],ttt[i]);
        if(i==4): ttt[i].next_to(dot[i],RIGHT*0.8); Vt[i]=VGroup(dot[i],ttt[i]); 
        VIP.add(Vt[i])
    for i in range(1,4):
        self.play(FadeInFrom(VGroup(Vt[i],Vt[i+3]),LEFT)); self.wait(1.2)
    self.play(l2.put_start_and_end_on,UP*20,DOWN*2); DownTime(self,3); self.play(l2.put_start_and_end_on,UP*20,DOWN*20)
    self.play(FadeOutAndShift(VGroup(VIP,l1,l2,tit1,tit2),RIGHT))

class Part1(GraphScene):
    def construct(self):
        title_of_video(self)
        cont(self)
        turnin(self,"向量的定义和性质")
        sc1(self)
        sc2(self)
        turnout(self,"向量的定义和性质")
        turnin(self,"向量的线性运算")
        sc3(self)
        sc4(self)
        sc5(self)
        turnout(self,"向量的线性运算")
        turnin(self,"平面向量的坐标表示")
        sc6(self)
        sc7(self)
        turnout(self,"平面向量的坐标表示")
        turnin(self,"向量的点积和叉积")
        sc8(self)
        sc9(self)
        turnout(self,"向量的点积和叉积")
        thanks(self)

# python -m manim pmjh2.py Part1 -p

# "#2196F3"
# "#FB8C00"
# "#00FBA5"