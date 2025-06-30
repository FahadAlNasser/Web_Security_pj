from flask import Blueprint, render_template, request, redirect, flash, current_app
from werkzeug.utils import secure_filename
from .scanner import virustotal_scanningurl, virustotal_scanningfile
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    url_conclusion = None
    file_conclusion = None
    if request.method == 'POST':
        if 'url' in request.form and request.form['url']:
            url_conclusion = virustotal_scanningurl(request.form['url'])
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filename = secure_filename(file.filename)   
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                file_conclusion = virustotal_scanningfile(filepath)
    return render_template('index.html', url_conclusion=url_conclusion, file_conclusion=file_conclusion)