import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# https://www.youtube.com/watch?v=Ij4wXdedRVY SQL Implementation
@app.route("/")
@login_required
def index():

    user_id = session['user_id']
    holdings= []
    grand_total = 0

# Indexing for each share
    rows = db.execute("""
        SELECT symbol, SUM(shares) as totalShares
        FROM transactions
        WHERE user_id = :user_id
        GROUP BY symbol
        HAVING totalShares > 0;
    """, user_id = session['user_id'])

# Appending the values for Jinja implementation
    for row in rows:
        stock = lookup(row['symbol'])
        holdings.append({
            "symbol" : stock['symbol'],
            "name" : stock['name'],
            "price" : stock['price'],
            "shares" : row["totalShares"],
            "total" : stock['price'] * row['totalShares'],


         })
        grand_total += stock["price"] * row["totalShares"]

# Update the Grand Total for the live stock values that might have changed
    rows  = db.execute(
    """SELECT cash
        FROM users
        WHERE id=:user_id""",
        user_id=session['user_id'])

    cash = rows[0]['cash']
    grand_total += cash

    return render_template('index.html', holdings = holdings, cash = cash, grand_total = grand_total)




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

# Getting the form
    if request.method == 'GET':
        return render_template('/buy.html')

# Post the form - setting variables(values)
    if request.method == 'POST':
        user_id = session['user_id']
        rows = db.execute(
        """SELECT * FROM users
            WHERE id = :user_id""",
            user_id = user_id)
        cash_account = rows[0]['cash']

        symbol = request.form.get('symbol')
        stock = lookup(symbol)
        shares = int(request.form.get('shares'))


# Stock does not exist in account
        if stock == None or int(shares) < 1.0:
            return apology('Invalid symbol AND/OR quantity')
## Buying process
        else:
            stock_price = stock['price']

            total_price = stock_price * int(shares)

            if cash_account >= total_price:

# Assigning new cash value
                cash_left = db.execute("""
                SELECT cash
                FROM users
                WHERE id = :user_id""",
                user_id = user_id)

                cash_left = cash_left[0]['cash']
                new_account = cash_left - total_price

# Updating new value into DB
                db.execute("""
                UPDATE users
                SET cash = :new_account
                WHERE id = :user_id""",
                user_id = user_id,
                new_account = new_account)

                db.execute("""
                INSERT INTO transactions
                (user_id, symbol, shares, price)
                VALUES
                (:user_id, :symbol, :shares, :price) """,
                user_id = session["user_id"],
                symbol = stock['symbol'],
                shares = shares,
                price = stock['price']

                )
                flash("Bought!")
                return redirect("/")



        return apology("TODO")


# Implement  Jinja historical representation with stocks, prices and related timestamps
@app.route("/history")
@login_required
def history():

   rows = db.execute("""
   SELECT * FROM transactions
   WHERE user_id =:user_id
   GROUP BY transacted""",
   user_id =  session['user_id'])

   return render_template("history.html", rows = rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
# Quote the stock price value from the API

    hide_form = 'hidden'
    show = 'show'
    if request.method == 'GET':
        return render_template('/quote.html', hide_form = show, show = hide_form)
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        if lookup(symbol) == None:
            return apology('Invalid symbol')
        else:

            stock = lookup(symbol)
            name = stock['name']
            symbol = stock['symbol']
            price = stock['price']

            return render_template('quote.html',  name = name, symbol = symbol, price = price, hide_form = 'hidden',show = 'show')

    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():

    # Get form
    if request.method == 'GET':
        return render_template('register.html')

    #Form request
    if request.method == 'POST':

        #Ensure username and password
        if not request.form.get('username'):
            return apology("invalid userrname", 403)

        elif not request.form.get('password'):
            return apology("invalid passsword", 403)

        elif not request.form.get('password-confirm'):
            return apology("Confirm your password")

        # Query DB for username and password
        rows = db.execute("""
        SELECT * FROM users
        WHERE
        username = :username""",
        username = request.form.get("username"))

        if len(rows) == 1:
            return apology("User already exists", 403)

        # pass check and hashing
        password = request.form.get('password')
        password_confirmation = request.form.get('password-confirm')

        if password == password_confirmation:
            password = generate_password_hash(password)
            username = request.form.get('username')
            db.execute("""
            INSERT INTO users
            (username, hash)
            VALUES (:username, :password""",
            username = username, password = password)

        else:
            return apology("Passwords must be equal")

    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
# Insert options into SELECT form input
    if request.method == "GET":
        stock_list = []
        options = db.execute("""
        SELECT DISTINCT(symbol)
        FROM transactions
        WHERE user_id = :user_id""",
        user_id = session['user_id'])

        for option in options:

            stock_list.append(option['symbol'])

        return render_template('sell.html', options = stock_list)
# Selling process

    elif request.method == "POST":
        symbol = request.form.get('symbol')
        stocks = request.form.get('shares')
        db_symbol = lookup(symbol)
        current_shares = []

        to_sell = db.execute(
        """SELECT SUM(shares) as totalShares
        FROM "transactions"
        WHERE user_id = :user_id
        AND symbol=:symbol """,
        user_id = session['user_id'], symbol=symbol)

        for row in to_sell:
            current_shares.append(row['totalShares'])

        if current_shares[0] < int(stocks):
            return apology("Not enough shares")
        else:

            reduced_value = current_shares[0] - int(stocks)

            rows = db.execute("""
            SELECT cash
            FROM users
            WHERE id=:id """, id=session['user_id'])
            cash = rows[0]['cash']

#Update cash value accordingly
            cash_updated = cash + int(stocks) * db_symbol['price']
            # grand_total += cash_updated
            db.execute("""
            UPDATE users
            SET cash = :cash_updated
            WHERE id=:id""",
            cash_updated = cash_updated,id=session['user_id'])

# Inserting new value after selling process
            db.execute("""INSERT INTO
                transactions (user_id, symbol, shares, price)
                VALUES (:user_id, :symbol, :shares, :price) """,
                user_id = session["user_id"],
                symbol = db_symbol['symbol'],
                shares = -1 * int(stocks),
                price = db_symbol['price']

                )
            flash("Sold!")
            return redirect('/')

    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
