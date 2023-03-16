from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def bmi():
    return render_template('bmi.html')

@app.route('/', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = round(weight / (height ** 2), 2)
    return render_template('bmi.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
