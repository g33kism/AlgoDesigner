from flask import Flask, render_template,request,make_response
import urllib 
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/open')
def open():
    return render_template('open.html')


@app.route('/save',methods=['POST'])
def save():
    _xml=urllib.unquote(request.form['xml']).decode('utf8') 
    _filename=request.form['filename']
    response = make_response(_xml)
    response.headers["Content-Disposition"] = "attachment; filename="+_filename
    return response

if __name__=='__main__':
    app.run()