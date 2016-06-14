# -*- coding:utf-8 -*-
from PIL import Image
import pdb
#from collection 
im=Image.open('mozart.gif')
im_new=im.copy()
w,h=im.size
L=[]
for y in range(h):
    for x in range(w):
        L.append(im.getpixel((x,y)))
    pink=L.index(195)
    L=L[pink:]+L[:pink]

    #print(L)
    #pdb.set_trace()
    for x,value in enumerate(L):
        im_new.putpixel((x,y),value)
    L=[]

im_new.show()