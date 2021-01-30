# 爬取豆瓣读书Top250读书榜单，并将数据可视化

## 一、项目介绍

1、爬取[豆瓣读书](https://book.douban.com/top250?start=")榜单数据，数据包含：排名、图书名、图书链接、封面链接、作者/译者、出版社、出版时间、图书售价、评分、评价人数、简要介绍，这11个数据。

2、将爬取的数据保存到sqlite数据库中。

3、可视化爬取的数据。

## 二、项目实现

1、爬取实现：**test01.py**实现爬取数据并保存到sqlite数据库，通过[beautifulsoup4](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)实现解析网页，通过[re](https://www.runoob.com/regexp/regexp-syntax.html)正则表达式提取网页数据，编写sql语句创建sqlite数据库，并将数据保存到该数据库中。

2、运行**test01.py**生成**book.db**数据库以及**豆瓣读书Top250.xls**数据表。

3、**templates**文件夹下包含几个html文件，**static文件夹**中包含前面所述网页的样式及内容图片、图标。

4、**app.py**是网页页面服务的实现，**book_worcloud.py**实现词云的生成。

5、页面的实现应用了[Flask框架](https://flask.palletsprojects.com/en/1.1.x/)、[Echarts图表](https://echarts.apache.org/zh/index.html)、wordcloud词云等。
