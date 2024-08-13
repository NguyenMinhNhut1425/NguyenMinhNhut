# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:08:45 2024

@author: MINH NHUT
"""

a=float(input("Nhập vào số a:"))
b=float(input("Nhập vào số b:"))
c=float(input("Nhập vào số c:"))

if a + b > c and a + c > b and b + c > a:
    print(f"{a}, {b}, {c} là ba cạnh của tam giác")
else:
    print(f"{a}, {b}, {c} không phải là ba cạnh của tam giác")