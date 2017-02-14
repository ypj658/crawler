# coding:utf-8

from flask import Flask, request, make_response, render_template, redirect, url_for

from flask_bootstrap import Bootstrap

from dbhelpler.dbHelper import dbHelper

app = Flask(__name__)
bootstrap = Bootstrap(app)

db = dbHelper()


@app.route("/hello")
def test():
    return make_response("this is an test page for test the sever is or not ready")


@app.route('/')
def index():
    return redirect(url_for("gxb"))


###
def notice_to_artices(days, source):
    '''
    查询数据库，检索最近days来自source发布的文章，以便用于微信Message输出
    :param days: 最近days
    :param source: 发布者
    :return: 可以用于微信News Message输出的列表
    '''
    notices = db.lately_notice(days, source)
    articles = []
    for notice in notices:
        articles.append({
            'title': notice.title,
            'url': notice.url,
            'picurl': '',
            'description': ''
        })
    return articles


@app.route("/gxb/", methods=['GET', 'POST'])
def gxb():
    notices = db.lately_notice(10, "工信部")

    return render_template("notice.html", items=notices, name="近十日工信部发通知")


@app.route("/fgw/", methods=['GET', 'POST'])
def fgw():
    return render_template("notice.html", name="近十日发改委发通知")


@app.route("/kjb/", methods=['GET', 'POST'])
def kjb():
    notices = db.lately_notice(10, "科技部")
    return render_template("notice.html", items=notices, name="近十日科技部发通知")


@app.route("/sxgxt/", methods=['GET', 'POST'])
def sxgxt():
    notices = db.lately_notice(90, "陕西省工信厅")
    return render_template("notice.html", items=notices, name="近十日省工信厅发通知")


if __name__ == '__main__':
    app.run(debug=True)
