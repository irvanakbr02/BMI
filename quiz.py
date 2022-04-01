from flask import Flask, jsonify, request
from flask import Flask

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    berat = float(request.form.get('berat'))
    tinggi = float(request.form.get('tinggi'))
    BMI = berat/(tinggi/100)**2
    if BMI < 18.5:
        keterangan = "Kurus"
    elif BMI > 18.5 and BMI < 25:
        keterangan = "Normal"
    elif BMI > 25 and BMI < 40:
        keterangan = "Berlebih"
    else:
        keterangan = "Bahaya"
    data = {'Hasil BMI': keterangan}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, port=4000)    