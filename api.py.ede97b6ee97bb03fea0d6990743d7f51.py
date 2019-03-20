from flask import Flask, jsonify, render_template, Response, request
import json
import pymysql

# 实例化app对象
app = Flask(__name__)

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     password='232824Liu!', database='test')


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# 添加工作数据
def insertData(data):
    cursor = db.cursor()

    sql = 'INSERT INTO `test`.`work` (`id`, `item`, `solution`, `done`, `date`) VALUES (%(id)s, %(item)s, %(solution)s, %(done)s,  %(date)s)'

    # 执行SQL语句
    cursor.execute(sql, data)
    db.commit()

    # 关闭数据库连接
    cursor.close()


def deleteData(data):
    cursor = db.cursor()

    sql = 'DELETE FROM `test`.`work` WHERE (`id`=%(id)s)'

    # 执行SQL语句
    cursor.execute(sql, data)
    db.commit()

    # 关闭数据库连接
    cursor.close()


def updateData(data):
    cursor = db.cursor()
    sql = 'UPDATE `test`.`work` SET `item` = %(item)s, `solution` = %(solution)s, `done` = %(done)s, `date` = %(date)s WHERE (`id` = %(id)s)'
    # 执行SQL语句
    cursor.execute(sql, data)
    db.commit()

    # 关闭数据库连接
    cursor.close()


# 获取工作数据
def getData():
    testInfo = []

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT * FROM `test`.`work`"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 使用 fetchall() 方法获取所有数据.
        data = cursor.fetchall()
        for row in data:
            jsonp = {}
            jsonp['id'] = row[0]
            jsonp['item'] = row[1]
            jsonp['solution'] = row[2]
            jsonp['done'] = row[3]
            jsonp['date'] = row[4]
            testInfo.append(jsonp)
        return testInfo
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    cursor.close()
    # db.close()


@app.route('/v1/work', methods=['GET'])
def test_data():
    # page = int(request.args.get("page")) * 6
    # pageEnd = page + 5
    # print(pageEnd)
    # testInfo = getData({'page': page, 'pageEnd': pageEnd})
    testInfo = getData()
    content = json.dumps(testInfo)
    resp = Response_headers(content)
    return resp


@app.route('/v1/addWork', methods=['POST'])
def test_post():
    print(request.method)
    if request.method == 'POST':
            # Request.form获得所有post参数放在一个类似dict类中
        datax = dict(request.form)

        print(datax)

        insertData(datax)
        resp = Response_headers('200 ok')
        return resp
    else:
        content = json.dumps({"error_code": "1001"})
        resp = Response_headers(content)
        return resp


@app.route('/v1/deletework', methods=['POST'])
def deleteWork():
    if request.method == 'POST':
        # Request.form获得所有post参数放在一个类似dict类中
        datax = dict(request.form)

        deleteData(datax)
        resp = Response_headers('200 ok')
        return resp
    else:
        content = json.dumps({"error_code": "1001"})
        resp = Response_headers(content)
        return resp


@app.route('/v1/updateWork', methods=['POST'])
def updateWork():
    if request.method == 'POST':
        # Request.form获得所有post参数放在一个类似dict类中
        datax = dict(request.form)

        print(datax)

        updateData(datax)
        resp = Response_headers('200 ok')
        return resp
    else:
        content = json.dumps({"error_code": "1001"})
        resp = Response_headers(content)
        return resp


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html')


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp
    # return "error_code:400"


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=7777,
            debug=True
            )
