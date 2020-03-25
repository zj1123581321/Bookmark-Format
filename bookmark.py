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
    #三级目录+@，然后处理二级目录 \d\.\d[\u4e00-\u9fa5]然后处理3级目录

    # 处理三级目录
    ClassNumber = re.findall(r"\d{1,2}\.\d{1,2}\.\d{1,2}",line)
    if (len(ClassNumber)>0):
        ClassNumber_new = ClassNumber[0]+"temp"
        line = re.sub(ClassNumber[0],ClassNumber_new,line)

    # 处理二级目录
        # 后面是空格
    ClassNumber = re.findall(r'\d{1,2}\.\d{1,2} ',line)
    if(len(ClassNumber)>0):
        ClassNumber_new = "\t" + ClassNumber[0]
        line = re.sub(ClassNumber[0],ClassNumber_new,line)

        # 后面是汉字
    ClassNumber = re.findall(r'\d{1,2}\.\d{1,2}[\u4e00-\u9fa5]',line)
    if(len(ClassNumber)>0):
        NumberTemp = re.findall(r'\d{1,2}\.\d{1,2}',ClassNumber[0])
        ClassNumber_new = "\t" + NumberTemp[0]+" "
        line = re.sub(NumberTemp[0],ClassNumber_new,line)

    # 返回处理三级目录
    ClassNumber = re.findall(r"\d{1,2}\.\d{1,2}\.\d{1,2}",line)
    if (len(ClassNumber)>0):
        ClassNumber_new = "\t\t" + ClassNumber[0]
        line = re.sub('temp',' ',line)
        line = re.sub(ClassNumber[0],ClassNumber_new,line)
    
    # 处理习题(归属于每一章)
    ClassNumber = re.findall('习题',line)
    if (len(ClassNumber)>0):
        ClassNumber_new = "\t" + ClassNumber[0]
        line = re.sub(ClassNumber[0],ClassNumber_new,line)
    
    # 处理小结(归属于每一章)
    ClassNumber = re.findall('小结',line)
    if (len(ClassNumber)>0):
        ClassNumber_new = "\t" + ClassNumber[0]
        line = re.sub(ClassNumber[0],ClassNumber_new,line)

    # 处理参考文献(归属于每一章)
    ClassNumber = re.findall('参考文献',line)
    if (len(ClassNumber)>0):
        ClassNumber_new = "\t" + ClassNumber[0]
        line = re.sub(ClassNumber[0],ClassNumber_new,line)

    # 处理汉字-页码黏连
    ClassNumber = re.findall(r'[\u2E80-\u9FFF]{1,3}\d{1,4}',line)
    if(len(ClassNumber)>0):
        NumberTemp = re.findall(r'[\u2E80-\u9FFF]{1,3}',ClassNumber[len(ClassNumber)-1])
        ClassNumber_new =  NumberTemp[0]+"\t"
        line = re.sub(NumberTemp[0],ClassNumber_new,line)
    
    # 处理英文-页码黏连
    ClassNumber = re.findall(r'[a-zA-Z]{2,3}\d{1,4}',line)
    if(len(ClassNumber)>0):
        NumberTemp = re.findall(r'[a-zA-Z]{2,3}',ClassNumber[len(ClassNumber)-1])
        ClassNumber_new =  NumberTemp[0]+"\t"
        line = re.sub(NumberTemp[0],ClassNumber_new,line)

    #写入txt
    g.write(line+"\n")

    print (line)
    if ( k>10000):
        break
    k = k + 1
f.close()
g.close()
