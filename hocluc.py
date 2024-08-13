# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:58:22 2024

@author: Nguyễn Minh Nhựt
"""

gpa=float(input("Anh/chị nhâp điểm trung bình (GPA):"))
if gpa<3.5:
    print("Học lực kém")
elif gpa>=3.5 and gpa<5.0:
    print("Học lực yếu")
elif gpa>=5.0 and gpa<7.0:
    print("Hoc lực trung bình")
elif gpa>=7.0 and gpa<8.0:
    print("Học lực khá")
elif gpa>=8.0 and gpa<9.0:
    print("Học lực giỏi")
elif gpa>=9.0 and gpa<=10:
    print("Học lực xuất sắc")
else:
    print("Không xác định")