from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('static/upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        # TODO This is where we call gpt2
        # process(f.filename, )
        print(f)
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
