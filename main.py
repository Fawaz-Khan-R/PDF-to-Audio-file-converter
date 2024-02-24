from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pyttsx3
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_audio_from_pdf(pdf_path, start_page, end_page, keyword, output_file):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    speaker = pyttsx3.init()

    audio_text = ''
    if keyword:
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if keyword in text:
                audio_text += text + ' '
    else:
        for page_num in range(start_page - 1, end_page):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            audio_text += text + ' '

    speaker.save_to_file(audio_text, output_file)
    speaker.runAndWait()

    pdf_file.close()
    speaker.stop()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        scanning_option = request.form['scanning_option']
        file = request.files['file']
        keyword = request.form.get('keyword')
        start_page = int(request.form.get('start_page', 1))
        end_page = int(request.form.get('end_page', 1))

        # Save uploaded file
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract audio
        output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        extract_audio_from_pdf(file_path, start_page, end_page, keyword, output_file)

        return redirect(url_for('download', filename='output.mp3'))
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
