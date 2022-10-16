from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__, template_folder='templates')

@app.get('/pointer')
def get_pointer():
    import app
    app.main()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)