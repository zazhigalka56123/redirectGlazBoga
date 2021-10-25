from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://t.me/BillGates_officialbot?start=396447633")


if __name__ == '__main__':
    app.run()
