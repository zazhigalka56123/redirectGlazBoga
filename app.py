from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://www.google.com/search?q=%D0%B2%D0%B0%D0%BD%D1%8E+%D0%B5%D0%B1%D1%83%D1%82+%D0%B2+%D0%B6"
                    "%D0%BE%D0%BF%D1%83")


if __name__ == '__main__':
    app.run()
