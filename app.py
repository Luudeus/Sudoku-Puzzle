import re
import numpy as np
from cs50 import SQL
import json
from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    jsonify,
    request,
    session,
)
from flask_session import Session
from functions import login_required
from sudoku_generator import sudoku_generator
from sudoku import clear_cells_for_difficulty
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///sudoku.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show sudoku's homepage"""
    return redirect("/sudoku")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username", "warning")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "warning")
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username and/or password", "warning")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/sudoku")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username", "warning")
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "warning")
            return render_template("register.html")

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            flash("Must re-enter password", "warning")
            return render_template("register.html")

        # Check if passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            flash("Password and confirmation password don't match", "warning")
            return render_template("register.html")

        # Ensure password has at least two digits and three letters
        password = request.form.get("password")
        digits = re.findall(r"\d", password)
        letters = re.findall(r"[A-Za-z]", password)

        if not (len(digits) >= 2 and len(letters) >= 3):
            flash("Password must contain at least 3 letters and 2 digits", "warning")
            return render_template("register.html")

        # Check is username's is available
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        if len(rows) != 0:
            flash("Username already exists", "warning")
            return render_template("register.html")

        # Insert the user into the users table
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )

        return redirect("/sudoku")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/sudoku")


@app.route("/sudoku", methods=["GET", "POST"])
@login_required
def sudoku():
    grid_populated = False
    if request.method == "POST":
        # If the route is accessed via POST request, generate a new Sudoku.
        solved_sudoku = sudoku_generator()
        # Get selected difficulty
        difficulty = request.form.get("difficulty")
        # Cleared sudoku for the user to solve
        cleared_sudoku = clear_cells_for_difficulty(solved_sudoku.copy(), difficulty)
        # Set the flag to True since the grid will now have values
        grid_populated = True
        # Serialize the solved_sudoku to JSON here
        solved_sudoku_json = json.dumps(solved_sudoku.tolist())
        # Serialize the cleared_sudoku to JSON here
        cleared_sudoku_json = json.dumps(cleared_sudoku.tolist())
        # Pass the Sudoku grid to the front-end.
        print(solved_sudoku_json)

        return render_template(
            "sudoku.html",
            solved_sudoku=solved_sudoku_json,
            cleared_sudoku=cleared_sudoku,
            grid_populated=grid_populated,
        )
    else:
        # Else, show an easy grid.
        return render_template("sudoku.html", grid_populated=grid_populated)


@app.route("/add-points", methods=["POST"])
@login_required
def add_points():
    data = request.get_json()
    points = data["points"]
    user_id = session["user_id"]

    # Update points in database
    db.execute("UPDATE users SET points = points + ? WHERE id = ?", points, user_id)

    return jsonify({"success": True})

@app.route("/leaderboard")
def leaderboard():
    """Show top 10 users based on points"""

    # SQL query to select top 10 users ordered by points in descending order
    top_users = db.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT 10")

    return render_template("leaderboard.html", users=top_users)

