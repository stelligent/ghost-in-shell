from flask import render_template, url_for, Flask

app = Flask(__name__)

def factorial(n):
    return 1 if (n < 1) else n * factorial(n - 1)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
