from flask import Flask, request, redirect, render_template,session


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
        EM = '帳號、或密碼輸入錯誤'
        return render_template('fail.html', EM = EM)
    else:
        return redirect('/')

@app.route("/signin", methods=['POST'])
def signin():
    account, password = request.form['account'], request.form['password']

    if account == '' or password =='':
        errorMessage = 'empty'
        return redirect(f'/error?message={errorMessage}')

    elif account =='test' and password =='test':

        session['user'] = f'{account}_{password}'
        return redirect('/member')
    else:
        errorMessage = 'wronginput'
        return redirect(f'/error?message={errorMessage}')


@app.route('/member')
def member():
    if 'user' in session:
        return render_template("member.html")
    else:
        return redirect('/')

@app.route('/signout')
def signout():
    if 'user' in session:
        del session['user']
    return redirect('/')


app.run(port=3000)
