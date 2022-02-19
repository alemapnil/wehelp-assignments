from flask import Flask, request, redirect, render_template,session
from flask import jsonify
import mysql.connector


## connect to database

connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='123456',
    database='week7'
)
cursor = connection.cursor()


#建立 Application 物件
app = Flask (
    __name__,
    static_folder='static', #staic holder name
    static_url_path='/static', #static route
    ) 
app.secret_key = 'you\'ll never know.'
app.config["JSON_AS_ASCII"] = False

@app.route("/api/members")
def api_get():
    account = request.args.get('username','其他錯誤')
    sql = """SELECT * FROM `member`
                WHERE `username` = %s
            """
    cursor.execute(sql, (account,))

    u_p_n = cursor.fetchone()
    if u_p_n is not None:
        data={
            'data':{
                'id':u_p_n[0],
                'name':u_p_n[1],
                'username':u_p_n[2]
                }
        }
    else:
        data={'data':u_p_n}
    return jsonify(data)




@app.route('/api/member')
def postJson():
    return render_template('postJson.html')



@app.route('/apiResult',methods=['POST'])
def change():
    if 'user' in session:
        newname = request.get_json()['name']
        data = {"ok":True}

        sql = """ update `member`
                set `name` = %s
                where `username`=%s
            """
        cursor.execute(sql, (newname,session['user']))
        connection.commit()

    else:
        data = {"error":True}
    return jsonify(data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/error')
def error():
    message = request.args.get('message','其他錯誤')
    if message =='empty':
        EM = '請輸入帳號、密碼'
        return render_template('fail.html', EM = EM)
    elif message == 'wronginput':
        EM = '帳號或密碼輸入錯誤'
        return render_template('fail.html', EM = EM)
    elif message == 'duplicate':
        EM = '帳號已經被註冊'
        return render_template('fail.html', EM = EM)
    else:
        return redirect('/')

@app.route("/register", methods=['POST'])
def register():
    name, account, password = request.form['name'], request.form['account'], request.form['password'], 

    if account == '' or password =='':
        errorMessage = 'empty'
        return redirect(f'/error?message={errorMessage}')

    else:

        sql = """SELECT * FROM `member`
                WHERE `username` = %s
            """
        cursor.execute(sql, (account,))

        u_p_n = cursor.fetchall()
        if u_p_n != []:
            errorMessage = 'duplicate'
            return redirect(f'/error?message={errorMessage}')

        cursor.execute(f"insert into member (`username`, `name`, `password`) values('{account}','{name}','{password}');")
        connection.commit()
        return redirect('/')



@app.route("/signin", methods=['POST'])
def signin():
    account, password = request.form['account'], request.form['password']

    if account == '' or password =='':
        errorMessage = 'empty'
        return redirect(f'/error?message={errorMessage}')

    else:
        sql = """SELECT * FROM `member`
                WHERE `username` = %s and  `password` = %s 
            """
        cursor.execute(sql, (account,password))
        
        a_n_p = cursor.fetchone()
        if a_n_p is not None:
            session['user'] = a_n_p[2]
            return redirect('/member')
        errorMessage = 'wronginput'
        return redirect(f'/error?message={errorMessage}')


@app.route('/member')
def member():
    if 'user' in session:
        sql = """SELECT * FROM `member`
                WHERE `username` = %s 
            """
        cursor.execute(sql, (session['user'],))
        a_n_p = cursor.fetchone()

        return render_template("member.html", inputname = a_n_p[1])

    else:
        return redirect('/')

@app.route('/signout')
def signout():
    if 'user' in session:
        del session['user']
    return redirect('/')


app.run(port=3000)
cursor.close()
connection.close()