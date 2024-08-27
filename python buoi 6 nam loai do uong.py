#!/usr/bin/env python
# coding: utf-8

# In[4]:


mon_1 = 'Tra olong'
mon_2 = 'Tra chanh'
mon_3 = 'Cafe'
mon_4 = 'Tra
mon_5 = 'Tra da'
price_1 = 20
price_2 = 30
price_3 = 40
price_4 = 50
price_5 = 10
print("Menu cua hang: ")
print(mon_1, '---', price_1, 'Bam 1 de goi')
print(mon_2, '---', price_2, 'Bam 2 de goi')
print(mon_3, '---', price_3, 'Bam 3 de goi')
print(mon_4, '---', price_4, 'Bam 4 de goi')
print(mon_5, '---', price_5, 'Bam 5 de goi')
do_uong = int(input("Ban muon uong loai do uong nao? "))
if(do_uong == 1):
    so_luong = int(input('Hay nhap so luong muon mua: '))
    print(f'Ban da mua {so_luong} coc {mon_1}')
    print(f'So tien ban phai tra la: {so_luong * price_1}')
if(do_uong == 2):
    so_luong = int(input('Hay nhap so luong muon mua: '))
    print(f'Ban da mua {so_luong} coc {mon_2}')
    print(f'So tien ban phai tra la: {so_luong * price_2}')
if(do_uong == 3):
    so_luong = int(input('Hay nhap so luong muon mua: '))
    print(f'Ban da mua {so_luong} coc {mon_3}')
    print(f'So tien ban phai tra la: {so_luong * price_3}')
if(do_uong == 4):
    so_luong = int(input('Hay nhap so luong muon mua: '))
    print(f'Ban da mua {so_luong} coc {mon_4}')
    print(f'So tien ban phai tra la: {so_luong * price_4}')
if(do_uong == 5):
    so_luong = int(input('Hay nhap so luong muon mua: '))
    print(f'Ban da mua {so_luong} coc {mon_5}')
    print(f'So tien ban phai tra la: {so_luong * price_5}')


# In[ ]:




