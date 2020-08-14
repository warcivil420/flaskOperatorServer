from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/admin")
def hello_main():
    return "kuggk"

@app.route("/sign")
def sign():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run()
