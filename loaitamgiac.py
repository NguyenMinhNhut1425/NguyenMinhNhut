# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:14:34 2024

@author: MINH NHUT
"""
a = float(input("Nhập giá trị của cạnh a: "))
b = float(input("Nhập giá trị của cạnh b: "))
c = float(input("Nhập giá trị của cạnh c: "))

if a == b == c:
    print("Đây là tam giác đều")
    
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    if a == b or a == c or b == c:
        print("Đây là tam giác vuông cân")
    else:
        print("Đây là tam giác vuông")

elif a == b or a == c or b == c:
    print("Đây là tam giác cân")
        
else:
    print("Đây là tam giác thường")