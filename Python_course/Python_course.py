#给友文的文字检索

'''
主要功能：
    从word.txt输入待查单词，输出单词到result.txt
使用方法：
    1，把单词或短语加到word.txt中，运行search.exe,等待查词结束，或使用“Ctrl+C”结束，即可保存
    2，程序为追加写模式，不会删除result中的内容
注意事项：
    以下三个文件要在同一目录
    word.txt,
    search.exe,
    result.txt


参考
	1. Python爬虫之自制英汉字典
<https://blog.csdn.net/jclian91/article/details/80433163> 
    2.
    mooc ，Python语言程序设计 ，嵩天、黄天羽、礼欣

'''

import requests
from bs4 import BeautifulSoup


#定义全局变量
result=[]#结果

#-------------------------【网络词典搜索 】------------------------------------------------------
def web_search(word):
    result=open("result.txt","at")
    str1='\n'+word
    try:
        #判断是否为特殊格式，比如2008-Text1
        if '20' in str1:
            str1+='-'*60
        else:                    
            # 利用GET获取输入单词的网页信息
            r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%word)
            # 利用BeautifulSoup将获取到的文本解析成HTML
            soup = BeautifulSoup(r.text, "lxml")
            # 获取字典的标签内容
            s = soup.find(class_='trans-container')('ul')[0]('li')
            # 输出字典的具体内容
            for item in s:
                if item.text:
                    str1=str1+'\t'+item.text
    except Exception:
        str1=str1+"error!是不是拼错了\n"    
    print(str1)            
    result.write(str1)
    result.close()
#-------------------------【获取要查的单词列表 】--------------------------------------------
def getText():  
    txt=open("word.txt","rt")
    datals=txt.readlines()
    return datals
#-------------------------【主函数 】------------------------------------------------------

def main():
    datals=getText()
    for i in datals:
        web_search(i)

main()
