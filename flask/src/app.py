from flask import Flask, request
from do_something import do_nothing

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello!</h1>"

# param?var_1=123
@app.route("/param")
def param():
    var_1 = request.args.get("var_1")
    do_nothing()
    return f"{var_1} input!"

@app.route("/hello", methods=["GET", "POST"])
def hello_post():
    var_1 = request.form.get("var_1")
    return f"Hello {var_1}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
