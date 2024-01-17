from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shh its a secret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submission():
    # stores session in request form
    session['yourname'] = request.form['yourname']
    session['selectlocation'] = request.form['selectlocation']
    session['selectlanguage'] = request.form['selectlanguage']
    session['comments'] = request.form['comments']
    session['time'] = request.form['time']
    session['checkbox'] = request.form['checkbox']
    # prints values in session in our terminal
    print(session['yourname'])
    print(session['selectlocation'])
    print(session['selectlanguage'])
    print(session['time'])
    print(session['checkbox'])
    print(session['comments'])
    return redirect("/result")

@app.route('/result')
def show_submission():
    return render_template('show.html',
    yourname_on_template = session['yourname'],
    selectlocation_on_template = session['selectlocation'],
    selectlanguage_on_template = session['selectlanguage'],
    time_on_template = session['time'],
    checkbox = session['checkbox'],
    comments_on_template = session['comments'])














if __name__=="__main__":  
    # app.run(debug=True)
    app.run(debug=True, host="localhost", port=8000)