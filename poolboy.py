import os
import sys
import re
import zipfile
from flask import Flask, render_template, request

app = Flask(__name__)

def extract_zip(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def zip_entire_path(extract_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(extract_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, extract_path))

def replace_text_in_file(file_path):
    old_text_pattern = re.compile(rb'<bbmd_questiontype>Multiple Answer</bbmd_questiontype>', re.IGNORECASE)
    new_text = b"<bbmd_questiontype>Multiple Choice</bbmd_questiontype>"

    with open(file_path, 'rb') as file:
        file_content = file.read()

    modified_content = old_text_pattern.sub(new_text, file_content)

    if modified_content != file_content:
        with open(file_path, 'wb') as file:
            file.write(modified_content)
        return True

    return False

def remove_text_in_file(file_path):
    text_to_remove_pattern = re.compile(rb'<not>.+?</not>', re.IGNORECASE | re.DOTALL)

    with open(file_path, 'rb') as file:
        file_content_before = file.read()

    modified_content = text_to_remove_pattern.sub(b'', file_content_before)

    if modified_content != file_content_before:
        with open(file_path, 'wb') as file:
            file.write(modified_content)
        return True

    return False

def remove_and_text_in_file(file_path):
    and_text_pattern = re.compile(rb'<and>|</and>', re.IGNORECASE)

    with open(file_path, 'rb') as file:
        file_content_before = file.read()

    modified_content = and_text_pattern.sub(b'', file_content_before)

    if modified_content != file_content_before:
        with open(file_path, 'wb') as file:
            file.write(modified_content)
        return True

    return False

def process_files(directory_path):
    modified_files_replace = []
    modified_files_remove_not = []
    modified_files_remove_and = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if replace_text_in_file(file_path):
                modified_files_replace.append(file_path)

            if remove_text_in_file(file_path):
                modified_files_remove_not.append(file_path)

            if remove_and_text_in_file(file_path):
                modified_files_remove_and.append(file_path)

    return modified_files_replace, modified_files_remove_not, modified_files_remove_and

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        zip_file = request.files['zip_file']
        extract_path = request.form['extract_path']

        zip_file.save(zip_file.filename)
        extract_zip(zip_file.filename, extract_path)

        modified_files_replace, _, _ = process_files(extract_path)

        # Zip the entire extract path
        output_zip_path = os.path.join(os.path.dirname(zip_file.filename), f'{os.path.basename(extract_path)}.zip')
        zip_entire_path(extract_path, output_zip_path)

        return render_template('result.html', files=modified_files_replace, output_zip_path=output_zip_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
