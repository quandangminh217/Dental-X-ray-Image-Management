from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Đọc dữ liệu bệnh nhân từ file JSON
def load_patient_data():
    with open('data/patients.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        patients = load_patient_data()
        patient_info = next((p for p in patients if p['id'] == patient_id), None)
        if patient_info:
            return render_template('result.html', patient=patient_info)
        else:
            return render_template('index.html', error="Không tìm thấy bệnh nhân.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
