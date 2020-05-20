# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:30:45 2020

@author: HP
"""


import unittest
from Max_Area import circle
from Max_Area import search

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = circle(0.5,0.5,0.5)
        self.c2 = circle(-0.5,-0.5,0.5)
        self.c3 = circle(0.5,0,0.5)
        self.c4 = circle(-0.5,0.5,0.5)

    def test_search(self):
        c_list = []
        c_list.append(self.c1)
        c_list.append(self.c2)
        c_list.append(self.c3)
        #在已有c1，c2，c3的情况下寻找能塞入盒子中的最大圆
        search(c_list)
        #search得到的新的最大圆应为c4
        #对两圆的参数进行比较
        self.assertEqual(c_list[3].x ,self.c4.x)
        self.assertEqual(c_list[3].y, self.c4.y)
        self.assertEqual(c_list[3].r, self.c4.r)

if __name__ == '__main__':
    unittest.main(verbosity=2)