from flask import Flask, make_response, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '60ff22b9bd3b402fabbeebcd323afadd890ce5b35cce4270'


@app.route('/')
def set_cookie():
    session['logged_in'] = True
    session['username'] = "admin"
    return ""


if __name__ == '__main__':
    app.run(port=5001, debug=True)