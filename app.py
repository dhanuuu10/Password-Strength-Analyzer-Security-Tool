from flask import Flask, render_template, request

from analyzer.engine import run_analysis


app = Flask(__name__)

COMMON_PASSWORD_FILE = "data/common_passwords.txt"


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        password = request.form.get("password", "")

        # Basic input validation
        if not password:
            error = "Please enter a password to analyze."

        elif len(password) > 128:
            error = "Password must not exceed 128 characters."

        else:
            result = run_analysis(
                password,
                COMMON_PASSWORD_FILE
            )

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(
        debug=False,
        host="127.0.0.1",
        port=5000
    )