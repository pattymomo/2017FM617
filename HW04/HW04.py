
# coding: utf-8

# In[2]:


def HW04():
    for j in range(1, 10):
        for i in range(1, 10):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()
        
    for i in range(8):                     # 總共有8層
        for j in range(8 - i - 1):     # 在第一個*號出現前，先印出空白
                 print(" ", end = "")
        for k in range(i + 1):         # 印出該層所需要的 *字數量
                 print("* ", end = "" )
        print() #換行
HW04()

