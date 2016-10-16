from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("/index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_page():
    """Go to application page."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def save_info():
    """To save info from form submission."""
# the session variable saved 'name' and whole_name' and I tried switching both names during testing
# and I already forgot which name is from where
# and somehow the 'name' variable is still there after I cleaned up the function

    # whole_name = request.form.get("f_name") + " " + request.form.get("l_name")

    # name_list = []
    # if 'salary' in session:
    #     session['salary'] += 1
    # else:
    #     session['salary'] = 1
    #     session['whole_name'] = name_list[whole_name]
    # else:
    #     name_list.append(whole_name)

    session['whole_name'] = request.form.get("f_name") + " " + request.form.get("l_name")

    session['salary'] = request.form.get("salary")

    session['job'] = request.form.get("job")


    # name = request.form.get("f_name") + " " + request.form.get("l_name")

# How can I access the "current" value of the session from form submission?
# Below code returns the entire list of the values in a session key.
    # if "whole_name" not in session:
    #     session['whole_name'] = session.get('name', 'name') + 1

    # if "salary" not in session:
    #     session['salary'] = [salary]
    # else:
    #     session['salary'].append(salary) *it keep saying the value is unicode which has no attribute to append

    # if "job" not in session:
    #     session['job'] = [job]
    # else:
    #     session['job'].append(job)

    return render_template("/application-response.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
