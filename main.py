from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import write_block, check


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        whom = request.form['whom']
        write_block(name=name, amount=amount, to_whom=whom)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def checkk():
    result = check()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)