import re
import os
#print os.getcwd() #打印出当前工作路径
f = open('D://MyFolders/Developments/Bookmark-Format/catalogue.txt',encoding='UTF-8')
g = open('D://MyFolders/Developments/Bookmark-Format/output.txt','a',encoding='UTF-8')
# show cata

#   change cata with reg
k = 1
for line in f:
    #去除空格
    line = ''.join(line.split())
    #[\u4e00-\u9fa5]
    
    # 处理两位/三位页码换行
    ClassNumber = re.findall(r'\d{3,3}',line)
    for reg in ClassNumber:
        reg_new =  reg+"\n"
        line = re.sub(reg,reg_new,line)

    #写入txt
    g.write(line+"\n")

    print (line)
    if ( k>10000):
        break
    k = k + 1
f.close()
g.close()
