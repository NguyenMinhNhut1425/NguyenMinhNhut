# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:13:47 2024

@author: MINH NHUT
a=float(input("Nhập giá trị a="))
b=float(input("Nhập giá trị b="))
if a==0:
    if b==0:
       print("Pt có vô số nghiệm")
    else:
        print("Pt vô nghiệm")
else:
    x=-b/a
    print(f"Giá trị cửa x là {x}")        
"""

a=float(input("Nhập giá trị a="))
b=float(input("Nhập giá trị b="))
if a==0:
    if b==0:
       print("Pt có vô số nghiệm")
    else:
        print("Pt vô nghiệm")
else:
    x=-b/a
    print(f"Giá trị của x là {x}")        