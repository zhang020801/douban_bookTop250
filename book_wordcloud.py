import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

conn = sqlite3.connect("book.db")
cur = conn.cursor()
sql = "select jieshao from book250 "
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
conn.close()
#分词
cut = jieba.cut(text)
string = ' '.join(cut)
#print(len(string))

img = Image.open(r'.\static\img\book_0.jpg')
img_array = np.array(img)
#print(img_array)
wc = WordCloud(
    background_color='black',
    mask=img_array,
    font_path="STXINWEI"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
#plt.show()
#输出词云图片
plt.savefig(r'.\static\img\book3.jpg')