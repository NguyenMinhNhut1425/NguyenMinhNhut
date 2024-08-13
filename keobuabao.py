# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:36:48 2024

@author: MINH NHUT
"""
import random
luachon = ["kéo", "búa", "bao"]
ngchoi = input("lựa chọn (kéo-búa-bao):")
may = random.choice(luachon) 
print(f"Bạn chọn: {ngchoi}")
print(f"Máy chon: {may}")
if ngchoi == may:
    print("Hòa")
elif ngchoi == 'kéo' and may == 'bao' or \
     ngchoi == 'búa' and may == 'kéo' or \
     ngchoi == 'bao' and may == 'búa':
    print("Bạn thắng")
else:
    print("Bạn thua")
