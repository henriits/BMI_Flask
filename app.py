from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    bmi = round(weight / ((height / 100) ** 2), 2)

    if bmi < 18.5:
        bmi_description = "underweight"
    elif bmi < 25:
        bmi_description = "normal weight"
    elif bmi < 30:
        bmi_description = "overweight"
    else:
        bmi_description = "obese"

    return render_template('index.html', bmi=bmi, bmi_description=bmi_description)

if __name__ == '__main__':
    app.run(debug=True)
