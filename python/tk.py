# -*- coding: UTF-8 -*-
from tkinter import *
root = Tk()
root.title('我是计算机')
root.geometry('320x420')

result = Entry(root)               # 用来显示结果的可变文本
result.pack()
print(result)
# equation = Tk().StringVar( )             # 用来显示算式的可变文本
# result.set(' ')                        # 赋初始值
# equation.set('0') 
# show_uresult = Tk().Label(root,bg='white',fg = 'black',font =('Arail','15'),bd='0',textvariable =equation,anchor='se')       
# show_dresult = Tk().Label(root,bg='white',fg = 'black',font = ('Arail','30'),bd='0',textvariable=result,anchor='se')
root.mainloop()