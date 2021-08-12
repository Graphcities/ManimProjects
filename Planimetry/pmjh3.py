from numpy import tri
from manimlib.imports import *
from manim_sandbox.utils.imports import *
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
        "Chapter 3 - 单位圆的性质和应用",
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
    orz=0.1
    text=Text(
        "Thanks!",
        font="Microsoft YaHei",
        t2c={"a":"#00FBA5","T":"#536DFE","h":"#EF5350","n":"#FB8C00","s":"#2196F3","k":"#00B8D4","!":"#FFD600"},
        stroke_width=0.5,
    ).scale(1.4*txtsc)
    text2=Text(
        "工具: Manim - 3Blue1Brown",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc)
    text3=Text(
        "BGM1: Intimate - Rhythm Doctor",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text3.next_to(text2,DOWN,aligned_edge=LEFT,buff=orz)
    text31=Text(
        "BGM2: Puff Piece - Rhythm Doctor",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text31.next_to(text3,DOWN,aligned_edge=LEFT,buff=orz)
    text32=Text(
        "BGM3: Song of the Sea - Rhythm Doctor",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text32.next_to(text31,DOWN,aligned_edge=LEFT,buff=orz)
    text4=Text(
        "字幕: Arctime",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text4.next_to(text32,DOWN,aligned_edge=LEFT,buff=orz)
    text5=Text(
        "剪辑: DaVinci Resolve 17",
        font="Microsoft YaHei",
        color=GRAY,
        stroke_width=0,
    ).scale(0.24*txtsc); text5.next_to(text4,DOWN,aligned_edge=LEFT,buff=orz)
    Vtext=VGroup(text2,text3,text31,text32,text4,text5)
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

    dot=[Dot()]*5
    tit=["","三角函数的扩展","诱导公式","和角公式与差角公式","和差化积公式"]
    tt=[Text("",font="Microsoft YaHei",)]*5
    Vt=[VGroup()]*5

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

def sc1(self): # 三角函数的扩展
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
    d=Dot(color=WHITE,plot_depth=10); p=Dot(color=BLUE,plot_depth=10)
    p.move_to(axes.c2p(math.cos(50*DEGREES),math.sin(50*DEGREES)))
    l1=Line(d.get_center(),p.get_center(),color="#FB8C00")
    l2=DashedLine(np.array([p.get_center()[0],0,0]),p.get_center())
    tP=TexMobject("P(x,y)",color=WHITE).scale(0.6); tP.next_to(p.get_center(),UR,buff=0.06); tP[0][2].set_color("#00FBA5"); tP[0][4].set_color("#FB8C00")
    tO=TexMobject("O").scale(0.6); tO.next_to(ORIGIN,DL,buff=0.1)
    tA=TexMobject("A").scale(0.6); tA.next_to(axes.c2p(1,0),UR,buff=0.1)
    VA=VGroup(axes,axes.get_axis_labels(),circ,l1,l2,d,p,tO,tP,tA)

    self.play(
        FadeIn(axes),FadeIn(VA[1]),
        FadeIn(l1),FadeIn(l2),FadeIn(tP),FadeIn(tA),
        Write(circ),Write(d),Write(tO),FadeIn(p),
        ); self.wait(1.5)
    self.play(
        axes.shift,LEFT*3,VA[1].shift,LEFT*3,l1.shift,LEFT*3,l2.shift,LEFT*3,tP.shift,LEFT*3,
        tA.shift,LEFT*3,circ.shift,LEFT*3,d.shift,LEFT*3,tO.shift,LEFT*3,p.shift,LEFT*3,
        )

    text=TexMobject(
        "\\angle AOP= \\\\",
        "\\sin \\angle AOP=y= \\\\",
        "\\cos \\angle AOP=x= \\\\",
        "\\tan \\angle AOP=\\frac{y}{x}= \\\\",
        "\\csc \\angle AOP=\\frac{1}{y}= \\\\",
        "\\sec \\angle AOP=\\frac{1}{x}= \\\\",
        "\\cot \\angle AOP=\\frac{x}{y}= \\\\",
    );
    text[1][8].set_color("#FB8C00"); text[2][8].set_color("#00FBA5"); text[3][8:11].set_color("#EF5350")
    text[4][8:11].set_color("#FB8C00"); text[5][8:11].set_color("#00FBA5"); text[6][8:11].set_color("#EF5350")
    text[1][0:3].set_color("#FB8C00"); text[2][0:3].set_color("#00FBA5"); text[3][0:3].set_color("#EF5350")
    text[4][0:3].set_color("#FB8C00"); text[5][0:3].set_color("#00FBA5"); text[6][0:3].set_color("#EF5350")
    nsin=DecimalNumber(0,color="#FB8C00"); nsin.add_updater(lambda t: t.next_to(text[1],RIGHT,buff=0.3))
    ncos=DecimalNumber(0,color="#00FBA5"); ncos.add_updater(lambda t: t.next_to(text[2],RIGHT,buff=0.3))
    ntan=DecimalNumber(0,color="#EF5350"); ntan.add_updater(lambda t: t.next_to(text[3],RIGHT,buff=0.3));
    ncsc=DecimalNumber(0,color="#FB8C00"); ncsc.add_updater(lambda t: t.next_to(text[4],RIGHT,buff=0.3))
    nsec=DecimalNumber(0,color="#00FBA5"); nsec.add_updater(lambda t: t.next_to(text[5],RIGHT,buff=0.3))
    ncot=DecimalNumber(0,color="#EF5350"); ncot.add_updater(lambda t: t.next_to(text[6],RIGHT,buff=0.3));
    nang=DecimalNumber(0); nang.add_updater(lambda t: t.next_to(text[0],RIGHT,buff=0.3))
    ang=TexMobject("^\\circ"); ang.add_updater(lambda t: t.next_to(nang,UR,buff=0.03))
    VT=VGroup(text,nang,ang,nsin,ncos,ntan,ncsc,nsec,ncot).scale(0.8); VT.move_to(RIGHT*3)

    nang.add_updater(lambda t: t.set_value(cdot1.get_center()[0]))
    nsin.add_updater(lambda t: t.set_value(math.sin(cdot1.get_center()[0]*DEGREES)))
    ncos.add_updater(lambda t: t.set_value(math.cos(cdot1.get_center()[0]*DEGREES)))
    ntan.add_updater(lambda t: t.set_value(math.sin(cdot1.get_center()[0]*DEGREES)/math.cos(cdot1.get_center()[0]*DEGREES)))
    ncsc.add_updater(lambda t: t.set_value(1.0/math.sin(cdot1.get_center()[0]*DEGREES)))
    nsec.add_updater(lambda t: t.set_value(1.0/math.cos(cdot1.get_center()[0]*DEGREES)))
    ncot.add_updater(lambda t: t.set_value(math.cos(cdot1.get_center()[0]*DEGREES)/math.sin(cdot1.get_center()[0]*DEGREES)))
    p.add_updater(lambda t: t.move_to(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l1.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(0,0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l2.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    tP.add_updater(lambda t: t.next_to(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES)),UR,buff=0.06))

    self.play(
        Write(VT[0][0]),Write(VT[1]),Write(VT[2]),
        Write(VT[0][1]),Write(VT[3]),
        Write(VT[0][2]),Write(VT[4]),
        Write(VT[0][3]),Write(VT[5]),
        ); self.wait(2)
    self.play(Write(VT[0][4]),Write(VT[6])); self.wait(1.5)
    self.play(Write(VT[0][5]),Write(VT[7])); self.wait(1.5)
    self.play(Write(VT[0][6]),Write(VT[8])); self.wait(1.5)

    self.play(cdot1.move_to,30*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,60*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,45*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,135*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,315*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,765*RIGHT+30*UP,run_time=2); self.wait(1)
    self.play(cdot1.move_to,50*RIGHT+30*UP,run_time=2); self.wait(1)
    DownTime(self,5,moving=LEFT*0.3)
    p.clear_updaters()
    l1.clear_updaters()
    l2.clear_updaters()
    tP.clear_updaters()
    self.play(FadeOut(VT),
        axes.shift,RIGHT*3,VA[1].shift,RIGHT*3,l1.shift,RIGHT*3,l2.shift,RIGHT*3,tP.shift,RIGHT*3,
        tA.shift,RIGHT*3,circ.shift,RIGHT*3,d.shift,RIGHT*3,tO.shift,RIGHT*3,p.shift,RIGHT*3,
        ); self.wait(1);

    numsin=math.sin(50*DEGREES); numcos=math.cos(50*DEGREES)
    a1=Arrow(np.array([2*numcos,0,0]),np.array([2*numcos,2*numsin,0]),color="#2196F3",buff=0,tip_length=0.2,plot_depth=1)
    a2=Arrow(np.array([0,0,0]),np.array([2*numcos,0,0]),color="#00FBA5",buff=0,tip_length=0.2,plot_depth=1)
    a3=Arrow(np.array([2,0,0]),np.array([2,2*numsin/numcos,0]),color="#EF5350",buff=0,tip_length=0.2)
    ds=DashedLine(p.get_center(),np.array([2,2*numsin/numcos,0]))

    self.play(Write(a1),Write(a2)); self.wait(2)
    self.play(Write(ds),Write(a3)); self.wait(2)
    DownTime(self,3,moving=UP*3+RIGHT*4.5)
    self.play(FadeOut(VGroup(a1,a2,a3,ds,axes,VA[1],l1,l2,tP,tA,circ,d,tO,p)))

def sc2(self): # 诱导公式
    cdot1=Dot(); cdot1.move_to(50*RIGHT+30*UP)
    cdot2=Dot(); cdot2.move_to(230*RIGHT+30*UP)

    axes=Axes(
        x_min=-1.6,x_max=1.6,y_min=-1.6,y_max=1.6,
        axis_config={
            "tick_frequency": 1,
            "unit_size": 2,
        },
    )
    axes.add_coordinates()
    circ=Circle(stroke_color="#2196F3",stroke_width=4,radius=2)
    d=Dot(color=WHITE,plot_depth=10); p=Dot(color=BLUE,plot_depth=10)
    p.move_to(axes.c2p(math.cos(50*DEGREES),math.sin(50*DEGREES)))
    l1=Line(d.get_center(),p.get_center(),color="#FB8C00")
    l2=DashedLine(np.array([p.get_center()[0],0,0]),p.get_center())
    tP=TexMobject("P",color=WHITE).scale(0.6); tP.next_to(p.get_center(),UR,buff=0.06);
    tO=TexMobject("O").scale(0.6); tO.next_to(ORIGIN,DL,buff=0.1)
    tA=TexMobject("A").scale(0.6); tA.next_to(axes.c2p(1,0),UR,buff=0.1)
    VA=VGroup(axes,axes.get_axis_labels(),circ,l1,l2,d,p,tO,tP,tA)

    self.play(
        FadeIn(axes),FadeIn(VA[1]),
        FadeIn(l1),FadeIn(l2),FadeIn(tP),FadeIn(tA),
        Write(circ),Write(d),Write(tO),FadeIn(p),
        ); self.wait(1.5)
    
    p.add_updater(lambda t: t.move_to(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l1.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(0,0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    l2.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),0),axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES))))
    tP.add_updater(lambda t: t.next_to(axes.c2p(math.cos(cdot1.get_center()[0]*DEGREES),math.sin(cdot1.get_center()[0]*DEGREES)),UR,buff=0.06))

    text=TexMobject(
        "\\sin (a+k\\cdot 2\\pi) &= \\sin a \\\\",
        "\\cos (a+k\\cdot 2\\pi) &= \\cos a \\\\",
        "\\tan (a+k\\cdot 2\\pi) &= \\tan a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[0][12:15].set_color("#2196F3")
    text[1][0:3].set_color("#00FBA5"); text[1][12:15].set_color("#00FBA5")
    text[2][0:3].set_color("#EF5350"); text[2][12:15].set_color("#EF5350")
    text[0][6:10].set_color("#FFA000"); text[1][6:10].set_color("#FFA000"); text[2][6:10].set_color("#FFA000"); 

    self.play(cdot1.move_to,410*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,-310*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,50*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(
        axes.shift,LEFT*3,VA[1].shift,LEFT*3,l1.shift,LEFT*3,l2.shift,LEFT*3,tP.shift,LEFT*3,
        tA.shift,LEFT*3,circ.shift,LEFT*3,d.shift,LEFT*3,tO.shift,LEFT*3,p.shift,LEFT*3,FadeInFrom(text,LEFT)); self.wait(2)
    self.play(FadeOutAndShift(text,RIGHT))

    q=Dot(color=BLUE,plot_depth=10); q.move_to(axes.c2p(math.cos(230*DEGREES),math.sin(230*DEGREES)))
    l3=Line(d.get_center(),q.get_center(),color="#536DFE")
    l4=DashedLine(np.array([q.get_center()[0],0,0]),q.get_center())
    tQ=TexMobject("Q",color=WHITE).scale(0.6); tQ.next_to(q.get_center(),UR,buff=0.06);
    q.add_updater(lambda t: t.move_to(axes.c2p(math.cos(cdot2.get_center()[0]*DEGREES),math.sin(cdot2.get_center()[0]*DEGREES))))
    l3.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(0,0),axes.c2p(math.cos(cdot2.get_center()[0]*DEGREES),math.sin(cdot2.get_center()[0]*DEGREES))))
    l4.add_updater(lambda t: t.put_start_and_end_on(axes.c2p(math.cos(cdot2.get_center()[0]*DEGREES),0),axes.c2p(math.cos(cdot2.get_center()[0]*DEGREES),math.sin(cdot2.get_center()[0]*DEGREES))))
    tQ.add_updater(lambda t: t.next_to(axes.c2p(math.cos(cdot2.get_center()[0]*DEGREES),math.sin(cdot2.get_center()[0]*DEGREES)),UR,buff=0.06))
    self.play(TransformFromCopy(p,q),TransformFromCopy(l1,l3),TransformFromCopy(l2,l4),TransformFromCopy(tP,tQ)); self.wait(1.5)

    text=TexMobject(
        "\\sin (a+\\pi) &= -\\sin a \\\\",
        "\\cos (a+\\pi) &= -\\cos a \\\\",
        "\\tan (a+\\pi) &= \\tan a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[0][10:13].set_color("#2196F3");
    text[1][0:3].set_color("#00FBA5"); text[1][10:13].set_color("#00FBA5");
    text[2][0:3].set_color("#EF5350"); text[2][9:12].set_color("#EF5350");
    text[0][6].set_color("#FFA000"); text[1][6].set_color("#FFA000"); text[2][6].set_color("#FFA000");
    text[0][9].set_color("#FFA000"); text[1][9].set_color("#FFA000");
    self.play(cdot1.move_to,20*RIGHT+30*UP,cdot2.move_to,200*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,140*RIGHT+30*UP,cdot2.move_to,320*RIGHT+30*UP,FadeInFrom(text,LEFT),run_time=2); self.wait(2)
    self.play(FadeOutAndShift(text,RIGHT))
    
    text=TexMobject(
        "\\sin (-a) &= -\\sin a \\\\",
        "\\cos (-a) &= \\cos a \\\\",
        "\\tan (-a) &= -\\tan a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[0][9:12].set_color("#2196F3");
    text[1][0:3].set_color("#00FBA5"); text[1][8:11].set_color("#00FBA5");
    text[2][0:3].set_color("#EF5350"); text[2][9:12].set_color("#EF5350");
    text[0][4].set_color("#FFA000"); text[1][4].set_color("#FFA000"); text[2][4].set_color("#FFA000");
    text[0][8].set_color("#FFA000"); text[2][8].set_color("#FFA000");
    self.play(cdot2.move_to,220*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,30*RIGHT+30*UP,cdot2.move_to,-30*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,-50*RIGHT+30*UP,cdot2.move_to,50*RIGHT+30*UP,FadeInFrom(text,LEFT),run_time=2); self.wait(2)
    self.play(FadeOutAndShift(text,RIGHT))
    
    text=TexMobject(
        "\\sin (\\pi -a) &= \\sin a \\\\",
        "\\cos (\\pi -a) &= -\\cos a \\\\",
        "\\tan (\\pi -a) &= -\\tan a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[0][9:12].set_color("#2196F3");
    text[1][0:3].set_color("#00FBA5"); text[1][10:13].set_color("#00FBA5");
    text[2][0:3].set_color("#EF5350"); text[2][10:13].set_color("#EF5350");
    text[0][4:6].set_color("#FFA000"); text[1][4:6].set_color("#FFA000"); text[2][4:6].set_color("#FFA000");
    text[1][9].set_color("#FFA000"); text[2][9].set_color("#FFA000");
    self.play(cdot2.move_to,230*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,40*RIGHT+30*UP,cdot2.move_to,140*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,300*RIGHT+30*UP,cdot2.move_to,-120*RIGHT+30*UP,FadeInFrom(text,LEFT),run_time=2); self.wait(2)
    self.play(FadeOutAndShift(text,RIGHT))
    
    text=TexMobject(
        "\\sin (\\frac{\\pi}{2} -a) &= \\cos a \\\\",
        "\\cos (\\frac{\\pi}{2} -a) &= \\sin a \\\\",
        "\\tan (\\frac{\\pi}{2} -a) &= \\cot a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[1][11:14].set_color("#2196F3");
    text[1][0:3].set_color("#00FBA5"); text[0][11:14].set_color("#00FBA5");
    text[2][0:3].set_color("#EF5350"); text[2][11:14].set_color("#EF5350");
    text[0][4:8].set_color("#FFA000"); text[1][4:8].set_color("#FFA000"); text[2][4:8].set_color("#FFA000");
    self.play(cdot2.move_to,-210*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,60*RIGHT+30*UP,cdot2.move_to,30*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,25*RIGHT+30*UP,cdot2.move_to,65*RIGHT+30*UP,FadeInFrom(text,LEFT),run_time=2); self.wait(2)
    self.play(FadeOutAndShift(text,RIGHT))
    
    text=TexMobject(
        "\\sin (\\frac{\\pi}{2} +a) &= \\cos a \\\\",
        "\\cos (\\frac{\\pi}{2} +a) &= -\\sin a \\\\",
        "\\tan (\\frac{\\pi}{2} +a) &= -\\cot a \\\\",
        plot_depth=10,
        ).scale(0.75).move_to(RIGHT*3);
    text[0][0:3].set_color("#2196F3"); text[1][12:15].set_color("#2196F3");
    text[1][0:3].set_color("#00FBA5"); text[0][11:14].set_color("#00FBA5");
    text[2][0:3].set_color("#EF5350"); text[2][12:15].set_color("#EF5350");
    text[0][4:8].set_color("#FFA000"); text[1][4:8].set_color("#FFA000"); text[2][4:8].set_color("#FFA000"); text[1][11].set_color("#FFA000"); text[2][11].set_color("#FFA000");
    self.play(cdot2.move_to,115*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,150*RIGHT+30*UP,cdot2.move_to,240*RIGHT+30*UP,run_time=2); self.wait(1.5)
    self.play(cdot1.move_to,-40*RIGHT+30*UP,cdot2.move_to,50*RIGHT+30*UP,FadeInFrom(text,LEFT),run_time=2); self.wait(2)
    self.play(FadeOutAndShift(VGroup(text,VA,q,l3,l4,tQ),RIGHT))

def sc3(self): # 诱导公式总结
    def alg1(self):
        text=TexMobject(
            "\\sin (a+k\\cdot 2\\pi) &= \\sin a \\\\",
            "\\cos (a+k\\cdot 2\\pi) &= \\cos a \\\\",
            "\\tan (a+k\\cdot 2\\pi) &= \\tan a \\\\",
            plot_depth=10,
            ).scale(0.65);
        text[0][0:3].set_color("#2196F3"); text[0][12:15].set_color("#2196F3")
        text[1][0:3].set_color("#00FBA5"); text[1][12:15].set_color("#00FBA5")
        text[2][0:3].set_color("#EF5350"); text[2][12:15].set_color("#EF5350")
        text[0][6:10].set_color("#FFA000"); text[1][6:10].set_color("#FFA000"); text[2][6:10].set_color("#FFA000");
        squ=Rectangle(height=2.6,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式一",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt
    def alg2(self):
        text=TexMobject(
            "\\sin (a+\\pi) &= -\\sin a \\\\",
            "\\cos (a+\\pi) &= -\\cos a \\\\",
            "\\tan (a+\\pi) &= \\tan a \\\\",
            plot_depth=10,
            ).scale(0.65).move_to(RIGHT*3);
        text[0][0:3].set_color("#2196F3"); text[0][10:13].set_color("#2196F3");
        text[1][0:3].set_color("#00FBA5"); text[1][10:13].set_color("#00FBA5");
        text[2][0:3].set_color("#EF5350"); text[2][9:12].set_color("#EF5350");
        text[0][6].set_color("#FFA000"); text[1][6].set_color("#FFA000"); text[2][6].set_color("#FFA000");
        text[0][9].set_color("#FFA000"); text[1][9].set_color("#FFA000");
        squ=Rectangle(height=2.6,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式二",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt
    def alg3(self):
        text=TexMobject(
            "\\sin (-a) &= -\\sin a \\\\",
            "\\cos (-a) &= \\cos a \\\\",
            "\\tan (-a) &= -\\tan a \\\\",
            plot_depth=10,
            ).scale(0.65).move_to(RIGHT*3);
        text[0][0:3].set_color("#2196F3"); text[0][9:12].set_color("#2196F3");
        text[1][0:3].set_color("#00FBA5"); text[1][8:11].set_color("#00FBA5");
        text[2][0:3].set_color("#EF5350"); text[2][9:12].set_color("#EF5350");
        text[0][4].set_color("#FFA000"); text[1][4].set_color("#FFA000"); text[2][4].set_color("#FFA000");
        text[0][8].set_color("#FFA000"); text[2][8].set_color("#FFA000");
        squ=Rectangle(height=2.6,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式三",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt
    def alg4(self):
        text=TexMobject(
            "\\sin (\\pi -a) &= \\sin a \\\\",
            "\\cos (\\pi -a) &= -\\cos a \\\\",
            "\\tan (\\pi -a) &= -\\tan a \\\\",
            plot_depth=10,
            ).scale(0.65).move_to(RIGHT*3);
        text[0][0:3].set_color("#2196F3"); text[0][9:12].set_color("#2196F3");
        text[1][0:3].set_color("#00FBA5"); text[1][10:13].set_color("#00FBA5");
        text[2][0:3].set_color("#EF5350"); text[2][10:13].set_color("#EF5350");
        text[0][4:6].set_color("#FFA000"); text[1][4:6].set_color("#FFA000"); text[2][4:6].set_color("#FFA000");
        text[1][9].set_color("#FFA000"); text[2][9].set_color("#FFA000");
        squ=Rectangle(height=3.5,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式四",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt
    def alg5(self):
        text=TexMobject(
            "\\sin (\\frac{\\pi}{2} -a) &= \\cos a \\\\",
            "\\cos (\\frac{\\pi}{2} -a) &= \\sin a \\\\",
            "\\tan (\\frac{\\pi}{2} -a) &= \\cot a \\\\",
            plot_depth=10,
            ).scale(0.65).move_to(RIGHT*3);
        text[0][0:3].set_color("#2196F3"); text[1][11:14].set_color("#2196F3");
        text[1][0:3].set_color("#00FBA5"); text[0][11:14].set_color("#00FBA5");
        text[2][0:3].set_color("#EF5350"); text[2][11:14].set_color("#EF5350");
        text[0][4:8].set_color("#FFA000"); text[1][4:8].set_color("#FFA000"); text[2][4:8].set_color("#FFA000");
        squ=Rectangle(height=3.5,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式五",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt
    def alg6(self):
        text=TexMobject(
            "\\sin (\\frac{\\pi}{2} +a) &= \\cos a \\\\",
            "\\cos (\\frac{\\pi}{2} +a) &= -\\sin a \\\\",
            "\\tan (\\frac{\\pi}{2} +a) &= -\\cot a \\\\",
            plot_depth=10,
            ).scale(0.65).move_to(RIGHT*3);
        text[0][0:3].set_color("#2196F3"); text[1][12:15].set_color("#2196F3");
        text[1][0:3].set_color("#00FBA5"); text[0][11:14].set_color("#00FBA5");
        text[2][0:3].set_color("#EF5350"); text[2][12:15].set_color("#EF5350");
        text[0][4:8].set_color("#FFA000"); text[1][4:8].set_color("#FFA000"); text[2][4:8].set_color("#FFA000"); text[1][11].set_color("#FFA000"); text[2][11].set_color("#FFA000");
        squ=Rectangle(height=3.5,weight=3.25,color="#FFD600",stroke_width=5)
        line=Line(LEFT*1,RIGHT*2.35,color=BLUE).next_to(text,UP,aligned_edge=LEFT,buff=0.2)
        tit=Text("公式六",font="Microsoft YaHei",stroke_width=2,color=BLUE).scale(0.75).next_to(text,UP,aligned_edge=LEFT,buff=0.4)
        ttt=VGroup(line,text,tit); squ.move_to(ttt.get_center()); ttt.add(squ)
        return ttt

    a1=alg1(self).move_to(LEFT*4.5+UP*2)
    a2=alg2(self).move_to(UP*2)
    a3=alg3(self).move_to(RIGHT*4.5+UP*2)
    a4=alg4(self).move_to(LEFT*4.5+DOWN*1.4)
    a5=alg5(self).move_to(DOWN*1.4)
    a6=alg6(self).move_to(RIGHT*4.5+DOWN*1.4)
    VIP=VGroup(a1,a2,a3,a4,a5,a6)
    anims=AnimationGroup(*[Write(mob) for mob in VIP],lag_ratio=0.08); self.play(anims); self.wait(1)

    dot=[Dot()]*6; bdot=[Dot()]*6
    for i in range(1,6):
        dot[i]=Dot(radius=0.1,color=RED); bdot[i]=Dot(radius=0.1,color=RED,fill_opacity=0,stroke_width=3)
        if(i>1): dot[i].next_to(dot[i-1],RIGHT,buff=0.35); bdot[i].next_to(bdot[i-1],RIGHT,buff=0.35)
    DVIP=VGroup(dot[1],dot[2],dot[3],dot[4],dot[5]); DVIP.move_to(DOWN*3.61)
    BDVIP=VGroup(bdot[1],bdot[2],bdot[3],bdot[4],bdot[5]); BDVIP.move_to(DOWN*3.61)
    self.play(FadeIn(DVIP))
    for i in range(1,6):
        self.wait(1)
        self.play(Transform(dot[i],bdot[i]))
    self.play(FadeOut(DVIP))
    self.play(FadeOut(VIP))

def sc4(self): # 和角公式与差角公式
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
    d=Dot(color=WHITE,plot_depth=10); a=Dot(color=BLUE,plot_depth=10)
    a.move_to(axes.c2p(math.cos(80*DEGREES),math.sin(80*DEGREES)))
    l1=Line(d.get_center(),a.get_center(),color="#FB8C00")
    tA=TexMobject("A",color=WHITE).scale(0.6).next_to(a.get_center(),UR,buff=0.06);
    b=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(math.cos(50*DEGREES),math.sin(50*DEGREES)))
    tB=TexMobject("B",color=WHITE).scale(0.6).next_to(b.get_center(),UR,buff=0.06)
    l2=Line(d.get_center(),b.get_center(),color="#00FBA5")
    c=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(math.cos(30*DEGREES),math.sin(30*DEGREES)))
    tC=TexMobject("C",color=WHITE).scale(0.6).next_to(c.get_center(),UR,buff=0.06)
    l3=Line(d.get_center(),c.get_center(),color="#03A9F4")
    tO=TexMobject("O").scale(0.6); tO.next_to(ORIGIN,DL,buff=0.1)
    p=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(1,0))
    tP=TexMobject("P").scale(0.6); tP.next_to(axes.c2p(1,0),UR,buff=0.1)
    l4=Line(a.get_center(),b.get_center(),color=WHITE)
    l5=Line(c.get_center(),p.get_center(),color=WHITE)
    anga=Angle(Dot().move_to(axes.c2p(1,0)),d,a,color="#FB8C00",stroke_width=4.5,radius=0.4); taa=TexMobject("a",color="#FB8C00",plot_depth=10,).scale(0.6).next_to(anga.get_center(),UR,buff=0.1)
    angb=Angle(Dot().move_to(axes.c2p(1,0)),d,b,color="#00FBA5",stroke_width=4.5,radius=0.55); tab=TexMobject("b",color="#00FBA5",plot_depth=10,).scale(0.6).next_to(angb.get_center(),RIGHT,buff=0.14)
    angc=Angle(Dot().move_to(axes.c2p(1,0)),d,c,color="#03A9F4",stroke_width=4.5,radius=0.75); tac=TexMobject("a-b",color="#03A9F4",plot_depth=10,).scale(0.6).next_to(angc.get_center(),RIGHT,buff=0.14)
    VA=VGroup(axes,axes.get_axis_labels(),circ,l1,d,a,tO,tP,tA,anga,taa,b,tB,l2,angb,tab,c,tC,l3,angc,tac,p)

    self.play(FadeIn(axes),FadeIn(VA[1]),Write(circ),Write(d),Write(tO),Write(tP),Write(p)); self.wait(1.5)
    self.play(Write(l1),Write(tA),Write(a),Write(anga),Write(taa),Write(b),Write(tB),Write(l2),Write(angb),Write(tab)); self.wait(1.5)
    self.play(TransformFromCopy(VGroup(anga,angb),angc),TransformFromCopy(VGroup(taa,tab),tac),TransformFromCopy(VGroup(a,b),c),TransformFromCopy(VGroup(tA,tB),tC),TransformFromCopy(VGroup(l1,l2),l3)); self.wait(1.5)
    self.play(Write(l4),Write(l5)); self.wait(1.5)
    self.play(
        axes.shift,LEFT*3,VA[1].shift,LEFT*3,circ.shift,LEFT*3,d.shift,LEFT*3,tO.shift,LEFT*3,tP.shift,LEFT*3,p.shift,LEFT*3,
        l1.shift,LEFT*3,tA.shift,LEFT*3,a.shift,LEFT*3,anga.shift,LEFT*3,taa.shift,LEFT*3,b.shift,LEFT*3,tB.shift,LEFT*3,l2.shift,LEFT*3,angb.shift,LEFT*3,tab.shift,LEFT*3,
        angc.shift,LEFT*3,tac.shift,LEFT*3,c.shift,LEFT*3,tC.shift,LEFT*3,l3.shift,LEFT*3,l4.shift,LEFT*3,l5.shift,LEFT*3,
        ); self.wait(1)

    text=TexMobject("AB=CP"); text.move_to(RIGHT*3)
    text2=TexMobject("\\cos(a-b) = \\cos a\\cos b+\\sin a\\sin b").move_to(0.36249982*UP)
    text3=TexMobject("\\cos(a-b) = \\cos a\\cos b+\\sin a\\sin b").move_to(np.array([0,-3.62499820e-01,0]))
    text4=TexMobject("\\cos(a+b) = \\cos a\\cos b-\\sin a\\sin b").move_to(np.array([0,-1.08749947e+00,0]))
    self.play(TransformFromCopy(VGroup(tA,tB,tC,tP),text)); self.wait(1.5)
    self.play(
        Transform(tA,TexMobject("A(\\cos a,\\sin a)",color=WHITE).scale(0.6).next_to(a.get_center(),UR,buff=0.04)),
        Transform(tB,TexMobject("B(\\cos b,\\sin b)",color=WHITE).scale(0.6).next_to(b.get_center(),UR,buff=0.04)),
        Transform(tC,TexMobject("C(\\cos (a-b),\\sin (a-b))",color=WHITE).scale(0.6).next_to(c.get_center(),UR,buff=0.04)),
        Transform(tP,TexMobject("P(1,0)").scale(0.6).next_to(axes.c2p(1,0),UR,buff=0.08)),
        ); self.wait(2)
    self.play(
        Transform(text,TexMobject("&(\\cos a-\\cos b)^2+(\\sin a-\\sin b)^2 \\\\=\\ &[\\cos(a-b)-1]^2+\\sin^2(a-b)").scale(0.7).move_to(RIGHT*3+DOWN*2)),
        ); self.wait(2)
    self.play(
        Transform(text,TexMobject("&-2\\sin a\\sin b-2\\cos a\\cos b+2 \\\\=\\ &-2\\cos(a-b)+2").scale(0.7).move_to(RIGHT*3+DOWN*2)),
        ); self.wait(2)
    self.play(
        Transform(text,TexMobject("&\\cos(a-b) \\\\=\\ &\\cos a\\cos b+\\sin a\\sin b").scale(0.7).move_to(RIGHT*3+DOWN*2)),
        ); self.wait(2)
    DownTime(self,3,moving=UP*4.5+RIGHT*4.5)
    self.play(
        FadeOutAndShift(axes,LEFT),FadeOutAndShift(VA[1],LEFT),FadeOutAndShift(circ,LEFT),FadeOutAndShift(d,LEFT),FadeOutAndShift(tO,LEFT),FadeOutAndShift(tP,LEFT),FadeOutAndShift(p,LEFT),
        FadeOutAndShift(l1,LEFT),FadeOutAndShift(tA,LEFT),FadeOutAndShift(a,LEFT),FadeOutAndShift(taa,LEFT),FadeOutAndShift(anga,LEFT),
        FadeOutAndShift(l2,LEFT),FadeOutAndShift(tB,LEFT),FadeOutAndShift(b,LEFT),FadeOutAndShift(tab,LEFT),FadeOutAndShift(angb,LEFT),
        FadeOutAndShift(l3,LEFT),FadeOutAndShift(tC,LEFT),FadeOutAndShift(c,LEFT),FadeOutAndShift(tac,LEFT),FadeOutAndShift(angc,LEFT),FadeOutAndShift(l4,LEFT),FadeOutAndShift(l5,LEFT),
        Transform(text,TexMobject("\\cos(a-b) = \\cos a\\cos b+\\sin a\\sin b").scale(1)),
        ); self.wait(1)
    self.play(text.move_to,0.36249982*DOWN,TransformFromCopy(text,text2)); self.wait(1.5)
    self.play(Transform(text2,TexMobject("\\cos(a-(-b)) = \\cos a\\cos (-b)+\\sin a\\sin (-b)").move_to(0.36249982*UP))); self.wait(1.5)
    self.play(Transform(text2,TexMobject("\\cos(a+b) = \\cos a\\cos b-\\sin a\\sin b").move_to(0.36249982*UP))); self.wait(1.5)
    self.play(
        text.move_to,np.array([0,3.62499830e-01,0]),
        text2.move_to,np.array([0,1.08749947e+00,0]),
        TransformFromCopy(text2,text4),TransformFromCopy(text,text3)
        ); self.wait(1.5)
    self.play(
        Transform(text3,TexMobject("\\cos(90^\\circ-a-b) = \\cos (90^\\circ-a)\\cos b+\\sin (90^\\circ-a)\\sin b").move_to(np.array([0,-3.62499820e-01,0]))),
        Transform(text4,TexMobject("\\cos(90^\\circ-a+b) = \\cos (90^\\circ-a)\\cos b-\\sin (90^\\circ-a)\\sin b").move_to(np.array([0,-1.08749947e+00,0]))),
        ); self.wait(2)
    self.play(
        Transform(text3,TexMobject("\\sin(a+b) = \\sin a\\cos b+\\sin b\\cos a").move_to(np.array([0.01,-3.62499820e-01,0]))),
        Transform(text4,TexMobject("\\sin(a-b) = \\sin a\\cos b-\\sin b\\cos a").move_to(np.array([0.01,-1.08749947e+00,0]))),
        ); self.wait(2)
    
    dot=[Dot()]*6; bdot=[Dot()]*6
    for i in range(1,6):
        dot[i]=Dot(radius=0.1,color=RED); bdot[i]=Dot(radius=0.1,color=RED,fill_opacity=0,stroke_width=3)
        if(i>1): dot[i].next_to(dot[i-1],RIGHT,buff=0.35); bdot[i].next_to(bdot[i-1],RIGHT,buff=0.35)
    DVIP=VGroup(dot[1],dot[2],dot[3],dot[4],dot[5]); DVIP.move_to(DOWN*3.61)
    BDVIP=VGroup(bdot[1],bdot[2],bdot[3],bdot[4],bdot[5]); BDVIP.move_to(DOWN*3.61)
    self.play(FadeIn(DVIP))
    for i in range(1,6):
        self.wait(1)
        self.play(Transform(dot[i],bdot[i]))
    self.play(FadeOut(DVIP))
    self.play(
        FadeOutAndShift(text,RIGHT),FadeOutAndShift(text2,RIGHT),FadeOutAndShift(text3,RIGHT),FadeOutAndShift(text4,RIGHT),
        FadeInFrom(axes,LEFT),FadeInFrom(VA[1],LEFT),FadeInFrom(circ,LEFT),FadeInFrom(d,LEFT),FadeInFrom(tO,LEFT),
        FadeInFrom(l1,LEFT),FadeInFrom(tA,LEFT),FadeInFrom(a,LEFT),FadeInFrom(taa,LEFT),FadeInFrom(anga,LEFT),
        FadeInFrom(l2,LEFT),FadeInFrom(tB,LEFT),FadeInFrom(b,LEFT),FadeInFrom(tab,LEFT),FadeInFrom(angb,LEFT),
        ); self.wait(1)

    self.play(l1.add_tip,0.22,l2.add_tip,0.22,); self.wait(1.5)
    text=TexMobject(
        "& \\overrightarrow{OB}\\cdot\\overrightarrow{OA} \\\\",
        "=\\ & \\cos(a-b) \\\\",
        "=\\ & \\cos a\\cos b+\\sin a\\sin b",
        ).scale(0.7).move_to(RIGHT*3+DOWN*2)
    self.play(TransformFromCopy(VGroup(tO,tA,tB),text)); self.wait(2)
    self.play(Transform(text,
        TexMobject(
        "& \\overrightarrow{OB}\\times\\overrightarrow{OA} \\\\",
        "=\\ & \\sin(a-b) \\\\",
        "=\\ & \\sin a\\cos b-\\sin b\\cos a",
        ).scale(0.7).move_to(RIGHT*3+DOWN*2)
        )); self.wait(2)
    DownTime(self,3,moving=UP*4.5+RIGHT*4.5)
    self.play(
        FadeOutAndShift(axes,LEFT),FadeOutAndShift(VA[1],LEFT),FadeOutAndShift(circ,LEFT),FadeOutAndShift(d,LEFT),FadeOutAndShift(tO,LEFT),FadeOutAndShift(text,LEFT),
        FadeOutAndShift(l1,LEFT),FadeOutAndShift(tA,LEFT),FadeOutAndShift(a,LEFT),FadeOutAndShift(taa,LEFT),FadeOutAndShift(anga,LEFT),
        FadeOutAndShift(l2,LEFT),FadeOutAndShift(tB,LEFT),FadeOutAndShift(b,LEFT),FadeOutAndShift(tab,LEFT),FadeOutAndShift(angb,LEFT),
        )

def sc5(self): # 和差化积公式
    axes=Axes(
        x_min=-1.6,x_max=1.6,y_min=-1.6,y_max=1.6,
        axis_config={
            "tick_frequency": 1,
            "unit_size": 2,
        },
    )
    axes.add_coordinates()
    circ=Circle(stroke_color="#2196F3",stroke_width=4,radius=2)
    d=Dot(color=WHITE,plot_depth=10); a=Dot(color=BLUE,plot_depth=10)
    a.move_to(axes.c2p(math.cos(70*DEGREES),math.sin(70*DEGREES)))
    l1=Line(d.get_center(),a.get_center(),color="#FB8C00")
    ds1=DashedLine(a.get_center(),np.array([a.get_center()[0],0,0]),color="#FB8C00")
    tA=TexMobject("A",color=WHITE,plot_depth=100,).scale(0.6).next_to(a.get_center(),UR,buff=0.06);
    b=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(math.cos(30*DEGREES),math.sin(30*DEGREES)))
    tB=TexMobject("B",color=WHITE,plot_depth=100,).scale(0.6).next_to(b.get_center(),UR,buff=0.06)
    l2=Line(d.get_center(),b.get_center(),color="#00FBA5")
    ds2=DashedLine(b.get_center(),np.array([b.get_center()[0],0,0]),color="#00FBA5")
    tO=TexMobject("O").scale(0.6); tO.next_to(ORIGIN,DL,buff=0.1)
    p=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(1,0))
    tP=TexMobject("P").scale(0.6); tP.next_to(axes.c2p(1,0),UR,buff=0.1)
    c=Dot(color=BLUE,plot_depth=10).move_to(axes.c2p(math.cos(70*DEGREES)+math.cos(30*DEGREES),math.sin(70*DEGREES)+math.sin(30*DEGREES)))
    tC=TexMobject("C").scale(0.6); tC.next_to(axes.c2p(math.cos(70*DEGREES)+math.cos(30*DEGREES),math.sin(70*DEGREES)+math.sin(30*DEGREES)),UR,buff=0.1)
    l3=Line(a.get_center(),c.get_center(),color="#00FBA5")
    l4=Line(b.get_center(),c.get_center(),color="#FB8C00")
    ds3=DashedLine(b.get_center(),np.array([c.get_center()[0],b.get_center()[1],0]))
    ds4=DashedLine(c.get_center(),np.array([c.get_center()[0],b.get_center()[1],0]),color="#FB8C00")
    ds5=DashedLine(np.array([c.get_center()[0],b.get_center()[1],0]),np.array([c.get_center()[0],0,0]),color="#00FBA5")
    l5=Line(d.get_center(),c.get_center(),color="#03A9F4")
    ds6=DashedLine(a.get_center(),b.get_center())
    e=Dot(color=BLUE,plot_depth=10).move_to(np.array([c.get_center()[0],0,0]))
    tE=TexMobject("D").scale(0.6); tE.next_to(e.get_center(),UR,buff=0.1)
    anga=Angle(Dot().move_to(axes.c2p(1,0)),d,a,color="#FB8C00",stroke_width=4.5,radius=0.4); taa=TexMobject("a",color="#FB8C00",plot_depth=10,).scale(0.6).next_to(anga.get_center(),UR,buff=0.1)
    angb=Angle(Dot().move_to(axes.c2p(1,0)),d,b,color="#00FBA5",stroke_width=4.5,radius=0.55); tab=TexMobject("b",color="#00FBA5",plot_depth=10,).scale(0.6).next_to(angb.get_center(),RIGHT,buff=0.125)
    angc=Angle(p,d,c,color="#03A9F4",stroke_width=4.5,radius=0.8); tac=TexMobject("(a+b)/2",color="#03A9F4",plot_depth=10).scale(0.4).next_to(angc.get_center(),UR,buff=0.1)
    angd=Angle(c,d,a,color="#536DFE",stroke_width=4.5,radius=0.8); tad=TexMobject("(a-b)/2",color="#536DFE",plot_depth=10).scale(0.4).next_to(angd.get_center(),UR,buff=0.05)
    VA=VGroup(axes,axes.get_axis_labels(),circ,l1,ds1,d,a,tO,tP,tA,anga,taa,b,tB,l2,ds2,angb,tab,p,c,tC)

    self.play(FadeIn(axes),FadeIn(VA[1]),Write(circ),Write(d),Write(tO)); self.wait(1)
    self.play(Write(l1),Write(tA),Write(a),Write(ds1),Write(anga),Write(taa),Write(b),Write(tB),Write(ds2),Write(l2),Write(angb),Write(tab)); self.wait(1)
    self.play(Write(c),Write(tC),TransformFromCopy(l1,l4),TransformFromCopy(l2,l3)); self.wait(1.5)
    self.play(Write(ds3),TransformFromCopy(ds1,ds4),TransformFromCopy(ds2,ds5),Write(e),Write(tE)); self.wait(1.5)
    self.play(Write(l5),Write(ds6)); self.wait(1.5)
    self.play(Write(angc),Write(tac),Write(angd),Write(tad)); self.wait(1.5)
    self.play(
        axes.shift,LEFT*3,VA[1].shift,LEFT*3,circ.shift,LEFT*3,d.shift,LEFT*3,tO.shift,LEFT*3,
        l1.shift,LEFT*3,tA.shift,LEFT*3,a.shift,LEFT*3,ds1.shift,LEFT*3,anga.shift,LEFT*3,taa.shift,LEFT*3,b.shift,LEFT*3,tB.shift,LEFT*3,ds2.shift,LEFT*3,l2.shift,LEFT*3,angb.shift,LEFT*3,tab.shift,LEFT*3,
        c.shift,LEFT*3,tC.shift,LEFT*3,l3.shift,LEFT*3,l4.shift,LEFT*3,
        ds3.shift,LEFT*3,ds4.shift,LEFT*3,ds5.shift,LEFT*3,e.shift,LEFT*3,tE.shift,LEFT*3,
        l5.shift,LEFT*3,ds6.shift,LEFT*3,angc.shift,LEFT*3,tac.shift,LEFT*3,angd.shift,LEFT*3,tad.shift,LEFT*3,
        ); self.wait(1)

    text=TexMobject("OC=2\\cos \\frac{a-b}{2}").scale(0.7).move_to(RIGHT*3)
    text[0][0:2].set_color("#03A9F4"); text[0][4:12].set_color("#536DFE")
    text2=TexMobject("OC\\times \\sin \\frac{a+b}{2}=CD").scale(0.7).move_to(np.array([3,-0.47787372,0]))
    text2[0][0:2].set_color("#03A9F4"); text2[0][3:11].set_color("#03A9F4"); text2[0][12:14].set_color(["#FB8C00","#00FBA5"])
    text3=TexMobject("CD=\\sin a+\\sin b").scale(0.7).move_to(np.array([3,-2*0.47787372,0]))
    text3[0][0:2].set_color(["#FB8C00","#00FBA5"]); text3[0][3:7].set_color("#FB8C00"); text3[0][8:12].set_color("#00FBA5")
    text4=TexMobject("\\sin a+\\sin b=2\\sin \\frac{a+b}{2}\\cos \\frac{a-b}{2}").scale(0.7).move_to(RIGHT*3+DOWN*2)
    text4[0][0:4].set_color("#FB8C00"); text4[0][5:9].set_color("#00FBA5"); text4[0][11:19].set_color("#03A9F4"); text4[0][19:27].set_color("#536DFE")
    self.play(Write(text)); self.wait(1.5)
    self.play(text.move_to,np.array([3,0.47787372,0]),Write(text2)); self.wait(1.5)
    self.play(text.shift,UP*0.47787372,text2.shift,UP*0.47787372,Write(text3)); self.wait(1.5)
    self.play(ReplacementTransform(VGroup(text,text2,text3),text4)); self.wait(1.5)
    DownTime(self,3,moving=UP*4.5+RIGHT*4)
    self.play(FadeOut(VGroup(
        axes,VA[1],circ,d,tO,l1,tA,a,ds1,anga,taa,b,tB,ds2,l2,angb,tab,c,tC,l3,l4,
        ds3,ds4,ds5,e,tE,l5,ds6,angc,tac,angd,tad,text4
        )))

class Part1(GraphScene):
    def construct(self):
        title_of_video(self)
        cont(self)
        turnin(self,"三角函数的扩展")
        sc1(self)
        turnout(self,"三角函数的扩展")
        turnin(self,"诱导公式")
        sc2(self)
        sc3(self)
        turnout(self,"诱导公式")
        turnin(self,"和角公式与差角公式")
        sc4(self)
        turnout(self,"和角公式与差角公式")
        turnin(self,"和差化积公式")
        sc5(self)
        turnout(self,"和差化积公式")
        thanks(self)

# python -m manim pmjh3.py Part1 -p