import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash,Markup


data = [{'title':'python3 dict','text':'python dictionary object'},
        {'title':'selenium python','text':'selenium python library and robotframework'}
        ]

user = {'USERNAME':"fengguangke",'PASSWORD':'123456'}
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def show_entries():
    entries = data
    return render_template('show_entries.html',entries=entries)

@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    data.append({'title':request.form['title'],'text':request.form['text']})
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != user['USERNAME']:
            error = 'invalid username'
        elif request.form['password'] != user['PASSWORD']:
            error = 'invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.errorhandler(404)
def error_handle(error):
    return render_template('pageNotFound.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


