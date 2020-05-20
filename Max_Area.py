# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#定义圆类
class circle:
    #定义构造函数
    def __init__ (self,x=0,y=0,r=0): 
        self.x=x
        self.y=y
        self.r=abs(r)
    
    #输出圆的半径和圆心坐标    
    def print_circle(self):
        print('radius={}, coordinate=({},{})'.format(self.r, self.x, self.y))
    
#定义search函数，寻找list中符合条件的最大圆
def search(list):
    max_x=0
    max_y=0
    max_r=0
    
    state=1#初始状态设置为1
    #在-1到1这个范围内以0.01为步长逐点扫描作为圆心，range中必须为整数类型，所以整体扩大100倍再缩小
    for x in range(-100,100,1):
        x=x/100
        for y in range(-100,100,1):
            y=y/100
            for c in list:
                if (x-c.x)**2 + (y-c.y)**2 < c.r**2:
                    state=0#当发生重叠时状态变为0
            
            if state==0:
                state=1        
                continue
            
            #先使半径为到边界的最短距离
            r=min(abs(x+1),abs(1-x),abs(y+1),abs(y-1))
            
            #找到在不重叠不越界的情况下圆的最大半径
            for c in list:
                if (x-c.x)**2+(y-c.y)**2<(c.r+r)**2:
                    r=((x-c.x)**2+(y-c.y)**2)**0.5-c.r ##若相交，改变r为相切时的半径
            
            #存储得到的最大半径圆的信息
            if r>max_r:
                max_x=x
                max_y=y
                max_r=r
    
    new=circle(max_x,max_y,max_r)
    list.append(new)     
           
def plot(list):
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1,1])
    plt.ylim([-1,1])  
    theta = np.linspace(0,2*np.pi,50)
    for c in list: 
        plt.plot(c.x+c.r*np.cos(theta),c.y+c.r*np.sin(theta),'b') 
    plt.show()
 
if __name__ == "__main__":
    m = 30
    c_list = []   
    RR = 0
    n=m
    
    #利用贪心算法，每次在前一次的基础上，调用search函数得到当前情况下的最优解
    while(n):
        search(c_list)   
        n-=1
        
    for c in c_list:
        RR+=c.r**2
        c.print_circle()
    print('for {} circles, the maximize sum of r^2 = {}'.format(m, RR))

    plot(c_list)    