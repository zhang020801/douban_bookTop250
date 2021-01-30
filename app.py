from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route("/index")
def index():
    datalist = []
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    sql = "select id,title,score,book_link,Img_link,author,press,time,money,num,jieshao from book250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    score = []
    num = []
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    sql = "select score,count(score) from book250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("index.html",books = datalist,score = score,num = num)
@app.route("/num")
def num():
    datalist = []
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    sql = "select id,title,score,book_link,Img_link,author,press,time,money,num,jieshao from book250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("num.html",books = datalist)
@app.route("/wordcloud")
def wordcloud():
    return render_template("wordcloud.html")
@app.route("/team")
def team():
    return render_template("team.html")
@app.route("/login")
def login():
    return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)