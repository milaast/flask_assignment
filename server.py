from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Takes user to application form."""

    return render_template("application-form.html",
                            first_name="firstname",
                            last_name="lastname",
                            title="desired_position",
                            salary="salary")

@app.route("/application-success", method=["POST"])
def application_success():
    """Acknowledge that users job application was received"""

    name = request.form.get("name")
    title = request.form.get("title")
    salary = request.form.get("salary")

    return render_template("application_response.html")

if __name__ == "__main__":
# We have to set debug=True here, since it has to be True at the
# point that we invoke the DebugToolbarExtension
    app.debug = True

# Use the DebugToolbar
    DebugToolbarExtension(app)

app.run(host="0.0.0.0")
