from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from utils.functions import update_parameters, generate_extract, update_attributes

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this for security reasons
app.DEBUG = True
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'xlsx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('html/index.html')


@app.route('/update_platform')
def update_platform_page():
    return render_template('html/update_platform.html')


@app.route('/update_parameters', methods=['GET', 'POST'])
def update_parameters_page():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            # Your function to process the parameters excel file
            update_parameters(filename)
            flash('Parameters updated successfully')
            return redirect(url_for('update_parameters_page'))
    return render_template('html/update_parameters.html')


@app.route('/update_attributes', methods=['GET', 'POST'])
def update_attributes_page():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            # Your function to process the attributes excel file
            # update_attributes(filename)
            flash('Attributes updated successfully')
            return redirect(url_for('update_attributes_page'))
    return render_template('html/update_attributes.html')


@app.route('/get_extract', methods=['GET', 'POST'])
def get_extract():
    if request.method == 'POST':
        extract_type = request.form['extract_type']
        tickers = request.form['tickers'].split(',')
        if extract_type in ['parameters', 'indicators']:
            names = request.form['names'].split(',')
        else:
            names = None
        # Commenting out the actual function call and replacing with flash message
        # output_file = generate_extract(extract_type, tickers, names)
        flash(f'The extract for {extract_type} would be generated here!')
        return redirect(url_for('get_extract'))
    return render_template('html/get_extract.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
