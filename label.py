#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:11:41 2017

@author: hunhpc
"""


#<pre class="python" name="code"></pre>#coding:utf-8  
''''' 
Created on Jul 29, 2016 
 
@author: sgg 
'''  
  
"<span style=""font-family:Arial;font-size:18px;"">"  
"<span style=""font-size:18px;"">"  
"<span style=""font-size:18px;"">"   
import os  
  
def IsSubString(SubStrList,Str):  
    flag=True  
    for substr in SubStrList:  
        if not(substr in Str):  
            flag=False  
      
    return flag  
  
#扫面文件  
def GetFileList(FindPath,FlagStr=[]):  
    FileList=[]  
    FileNames=os.listdir(FindPath)  
    if len(FileNames)>0:  
        for fn in FileNames:  
            if len(FlagStr)>0:  
                if IsSubString(FlagStr,fn):  
                    fullfilename=os.path.join(FindPath,fn)  
                    FileList.append(fullfilename)  
            else:  
                fullfilename=os.path.join(FindPath,fn)  
                FileList.append(fullfilename)  
      
    if len(FileList)>0:  
        FileList.sort()  
          
    return FileList  
  
  
  
train_txt=open('FPtrain1.txt','w')  
#制作标签数据，如果是A的，标签设置为0，如果是DW的标签为1.  
imgfile=GetFileList('train_before/train_A')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str1=img+' '+'0'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str1)
    
imgfile=GetFileList('train_before/train_DW')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str2=img+' '+'1'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str2)
    
imgfile=GetFileList('train_before/train_PE')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str3=img+' '+'2'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str3)
      
imgfile=GetFileList('train_before/train_RL')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str4=img+' '+'3'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str4)

imgfile=GetFileList('train_before/train_UL')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str5=img+' '+'4'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str5)  
    
imgfile=GetFileList('train_before/train_W')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str6=img+' '+'5'+'\n'        #用空格代替转义字符 \t   
    train_txt.writelines(str6) 

train_txt.close()  
  
  
#测试集文件列表  
test_txt=open('FPval1.txt','w')  
#制作标签数据，如果是男的，标签设置为0，如果是女的标签为1  
imgfile=GetFileList('val/test_A')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str7=img+' '+'0'+'\n'  
    test_txt.writelines(str7)  
    
imgfile=GetFileList('val/test_DW')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str8=img+' '+'1'+'\n'  
    test_txt.writelines(str8)  
    
imgfile=GetFileList('val/test_PE')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str9=img+' '+'2'+'\n'  
    test_txt.writelines(str9)
    
imgfile=GetFileList('val/test_RL')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str10=img+' '+'3'+'\n'  
    test_txt.writelines(str10)
    
imgfile=GetFileList('val/test_UL')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str11=img+' '+'4'+'\n'  
    test_txt.writelines(str11)
    
imgfile=GetFileList('val/test_W')#将数据集放在与.py文件相同目录下  
for img in imgfile:  
    str12=img+' '+'5'+'\n'  
    test_txt.writelines(str12) 

test_txt.close()  
  
print("成功生成文件列表")  
