# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:29:36 2024

@author: MINH NHUT
"""
import math

a=float(input("Nhập giá trị của a:"))
b=float(input("Nhập giá trị của b:"))
c=float(input("Nhập giá trị của c:"))

delta = b**2 - (4*a*c)

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Pt có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Pt có nghiệm kép: x1 = x2 = {x}")
else:
    print("Pt vô nghiệm")