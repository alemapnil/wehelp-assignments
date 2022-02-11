from flask import Flask, request, redirect, render_template,session
from numpy import record
import mysql.connector
## connect to database
connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='123456',
    database='loginout'
)
cursor = connection.cursor()



#建立 Application 物件
app = Flask (
    __name__,
    static_folder='static', #staic holder name
    static_url_path='/static', #static route
    ) 
app.secret_key = 'you\'ll never know.'

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

        cursor.execute(f"insert into member values('{account}','{name}','{password}');")
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
        
        a_n_p = cursor.fetchall()
        if a_n_p !=[]:
            session['user'] = a_n_p[0][1]
            return redirect('/member')
        errorMessage = 'wronginput'
        return redirect(f'/error?message={errorMessage}')


@app.route('/member')
def member():
    if 'user' in session:
        return render_template("member.html", inputname = session['user'])
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