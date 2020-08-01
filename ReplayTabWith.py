import re
import os
#print os.getcwd() #打印出当前工作路径
f = open('D://MyFolders/Developments/Bookmark-Format/catalogue.txt',encoding='UTF-8')
g = open('D://MyFolders/Developments/Bookmark-Format/output.txt','a',encoding='UTF-8')
# show cata

#   替换章节的 Tab 为空格
k = 1
for line in f:
    #去除 Tab 制表符
    ClassNumber = re.findall(r'\d\t',line)
    if(len(ClassNumber)>0):
        for reg in ClassNumber:
            reg_new_temp =  re.findall(r'\d',reg)
            reg_new = reg_new_temp[0] + " "
            line = re.sub(reg,reg_new,line)

    #写入txt
    #g.write(line+"\n")
    g.write(line)

    print (line)
    if ( k>10000):
        break
    k = k + 1
f.close()
g.close()
