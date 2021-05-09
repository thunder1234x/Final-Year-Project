from flask import Flask ,request , render_template , redirect ,url_for
from dbConfig import mySql;

app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template('newfirst.html');


@app.route('/SignUpPage',methods=['POST','GET'])
def signUpPage():
    if request.method == 'POST':
        name = request.form['Name'],
        email = request.form['Email'],
        addr = request.form['Address'],
        city = request.form['City'],
        hNo = request.form['House'],
        pin = request.form['Pin'],
        mNo = request.form['Mobile'],
        pas = request.form['Password'],
        typ = request.form['Type']

        return redirect(url_for('newfirst.html'));
    else:
        return render_template('Sighup.html');


@app.route('/logIn')
def loginPage():
    return render_template('newuser.html');


if __name__ == '__main__':
    app.run(debug=True)