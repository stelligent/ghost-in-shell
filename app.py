from flask import render_template, url_for, Flask, request, jsonify

app = Flask(__name__)


# Recursive factorial function
def fact(n):
    return 1 if (n < 1) else n * fact(n - 1)


# Default route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Factorial route for form post
@app.route('/factorial/', methods=['GET', 'POST'])
def factorial():
    n = int(request.json['number'])
    result = fact(n)
    data = {'factorial': result}
    data = jsonify(data)
    return data


# Main func
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
