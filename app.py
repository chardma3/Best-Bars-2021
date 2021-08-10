import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# ------------------------------------------------------------- CONFIG  #
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------------------------------------------------------------- HOMEPAGE  #
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get_reviews")
# Render reviews
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
# Search functionality
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
# Render register page
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_reviews", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
# Render login page
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"],
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hi, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "get_reviews", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect User Details")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect User Details")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
# Logout Functionality
def logout():
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/write_review", methods=["GET", "POST"])
# Render write review page
def write_review():
    if request.method == "POST":
        review = {
            "bar_name": request.form.get("bar_name"),
            "review": request.form.get("review"),
            "picture": request.form.get("picture"),
            "fav_drink": request.form.get("fav_drink"),
            "location": request.form.get("location"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added!")
        return redirect(url_for("get_reviews"))

    bars = mongo.db.bars.find().sort("bar_name", 1)
    return render_template("write_review.html", bars=bars)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
# Render edit review page
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "bar_name": request.form.get("bar_name"),
            "review": request.form.get("review"),
            "picture": request.form.get("picture"),
            "fav_drink": request.form.get("fav_drink"),
            "location": request.form.get("location"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated!")
        return redirect(url_for("get_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    bars = mongo.db.bars.find().sort("bar_name", 1)
    return render_template("edit_review.html", review=review, bars=bars)


@app.route("/delete_review/<review_id>")
# Delete functionality
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted!")
    return redirect(url_for("get_reviews"))


# ---------------------------------------------------------- ERROR HANDLERS #
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


# ---------------------------------------------------------- RUN THE APP  #
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
