#GovRptWordcloudv1.py
import jieba
import wordcloud
f=open("新建文本文档.txt","r")

t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
#w=wordcloud.WordCloud(font_path="msyh.ttc",\
#    width=1000,height=700,background_color="white",\
#    )
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("grwordcloud.png")

