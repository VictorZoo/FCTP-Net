#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:11:41 2017

@author: hunhpc, victor
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

imgfile=GetFileList('train_before/train_A') 
for img in imgfile:  
    str1=img+' '+'0'+'\n'        
    train_txt.writelines(str1)
    
imgfile=GetFileList('train_before/train_DW')
for img in imgfile:  
    str2=img+' '+'1'+'\n'          
    train_txt.writelines(str2)
    
imgfile=GetFileList('train_before/train_PE')  
for img in imgfile:  
    str3=img+' '+'2'+'\n'          
    train_txt.writelines(str3)
      
imgfile=GetFileList('train_before/train_RL')  
for img in imgfile:  
    str4=img+' '+'3'+'\n'           
    train_txt.writelines(str4)

imgfile=GetFileList('train_before/train_UL') 
for img in imgfile:  
    str5=img+' '+'4'+'\n'         
    train_txt.writelines(str5)  
    
imgfile=GetFileList('train_before/train_W') 
for img in imgfile:  
    str6=img+' '+'5'+'\n'         
    train_txt.writelines(str6) 

train_txt.close()  
  
  
  
test_txt=open('FPval1.txt','w')  

imgfile=GetFileList('val/test_A')
for img in imgfile:  
    str7=img+' '+'0'+'\n'  
    test_txt.writelines(str7)  
    
imgfile=GetFileList('val/test_DW')
for img in imgfile:  
    str8=img+' '+'1'+'\n'  
    test_txt.writelines(str8)  
    
imgfile=GetFileList('val/test_PE')
for img in imgfile:  
    str9=img+' '+'2'+'\n'  
    test_txt.writelines(str9)
    
imgfile=GetFileList('val/test_RL')  
for img in imgfile:  
    str10=img+' '+'3'+'\n'  
    test_txt.writelines(str10)
    
imgfile=GetFileList('val/test_UL') 
for img in imgfile:  
    str11=img+' '+'4'+'\n'  
    test_txt.writelines(str11)
    
imgfile=GetFileList('val/test_W') 
for img in imgfile:  
    str12=img+' '+'5'+'\n'  
    test_txt.writelines(str12) 

test_txt.close()  
  
print("succeed")  
