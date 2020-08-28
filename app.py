import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# import object ID
from bson.objectid import ObjectId
# import password security
from werkzeug.security import generate_password_hash, check_password_hash
# cloudinary imports
import cloudinary
from cloudinary.uploader import upload, destroy

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Environmental variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# cloudinary configs
cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET')
)


# Home page
@app.route("/")
@app.route("/experiences_home")
def experiences_home():
    experiences = mongo.db.experiences.find()
    return render_template("experiences_home.html", experiences=experiences)


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    experiences = list(mongo.db.experiences.find(
        {"$text": {"$search": query}}))
    return render_template("experiences_home.html", experiences=experiences)


# Sorter
@app.route("/sorter", methods=["GET", "POST"])
def sorter():
    sorter = request.form.get("sorter")
    experiences = mongo.db.experiences.find()
    # Sorting criteria
    if sorter == "country":
        experiences = mongo.db.experiences.find().sort("country_name", 1)
    elif sorter == "user":
        experiences = mongo.db.experiences.find().sort("created_by", 1)
    else:
        experiences = mongo.db.experiences.find().sort("recommendation", 1)

    return render_template(
        "experiences_home.html", experiences=experiences)


# Register user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user name already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User name already exists. Please try again.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # make new user active for the session
        session["user"] = request.form.get("username").lower()
        flash("Registration succesful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log in functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks for correct password:
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # password doesn't match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Users experience page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets the session username from db
    experiences = mongo.db.experiences.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, experiences=experiences)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("experiences_home"))


# More info about experience
@app.route("/moreinfo/<experience_id>")
def moreinfo(experience_id):
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    return render_template("moreinfo.html", experience=experience)


# Image upload
@app.route("/imageupload", methods=["GET", "POST"])
def imageupload():
    upload_result = None
    if request.method == "POST":
        file_to_upload = request.files.get("image")
        # Checks if user added the image
        if file_to_upload:
            upload_result = upload(file_to_upload)
        else:
            flash("You have to upload an image first to create experience")
            return redirect(url_for('imageupload'))

        # Sets the variables for the next step
        imagelink = upload_result['secure_url']
        public_id = upload_result['public_id']
        return render_template(
            'addxp.html', imagelink=imagelink, public_id=public_id)

    return render_template("imageupload.html")


# Add experience
@app.route("/addxp", methods=["GET", "POST"])
def addxp():
    if request.method == "POST":
        experience = {
            "title": request.form.get("title"),
            "country_name": request.form.get("country_name"),
            "location": request.form.get("city"),
            "recommendation": request.form.get("recommendation"),
            "duration": request.form.get("duration"),
            "tips": request.form.get("tips"),
            "travel_arrangements": request.form.get("traveling"),
            "description": request.form.get("description"),
            "created_by": session["user"],
            "imagelink": request.form.get("imagelink"),
            "public_id": request.form.get("public-id")
        }

        mongo.db.experiences.insert_one(experience)
        flash("You have succesfully added your experience")
        return redirect(url_for(
                        "profile", username=session["user"]))
    return render_template("addxp.html")


# Edit experience image
@app.route("/imgedit/<experience_id>", methods=["GET", "POST"])
def imgedit(experience_id):
    upload_result = None
    experience_id = experience_id
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})

    if request.method == "POST":
        # Gets the image for upload
        file_to_upload = request.files.get("image")
        # If there's a new image
        if file_to_upload:
            # Delete the previous one
            destroy(experience['public_id'], invalidate=True)
            # And continue with the new one
            upload_result = upload(file_to_upload)
            imagelink = upload_result['secure_url']
            public_id = upload_result['public_id']

            flash("Image updated succesfully")
            return render_template(
                'editxp.html',
                experience=experience,
                imagelink=imagelink,
                experience_id=experience_id,
                public_id=public_id)
        # If user didn't change the image
        else:
            imagelink = experience['imagelink']
            public_id = experience['public_id']
            return render_template(
                'editxp.html',
                experience=experience,
                imagelink=imagelink,
                experience_id=experience_id,
                public_id=public_id)

    return render_template(
        "imgedit.html", experience_id=experience_id, experience=experience)


# Edit experience details
@app.route("/editxp/<experience_id>", methods=["GET", "POST"])
def editxp(experience_id):
    experience_id = experience_id
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    if request.method == "POST":
        submit = {
            "title": request.form.get("title"),
            "country_name": request.form.get("country_name"),
            "location": request.form.get("city"),
            "recommendation": request.form.get("recommendation"),
            "duration": request.form.get("duration"),
            "tips": request.form.get("tips"),
            "travel_arrangements": request.form.get("traveling"),
            "description": request.form.get("description"),
            "created_by": session["user"],
            "imagelink": request.form.get("imagelink"),
            "public_id": request.form.get("public-id")
        }
        mongo.db.experiences.update(
            {"_id": ObjectId(experience_id)}, submit)
        flash("You have succesfully edited details")
        return redirect(url_for(
                        "profile", username=session["user"]))

    return render_template(
                'editxp.html',
                experience=experience,
                experience_id=experience_id)


# Delete experience
@app.route("/deletexp/<experience_id>")
def deletexp(experience_id):
    # find public_id of experience and delete the image on cloudinary
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    destroy(experience['public_id'], invalidate=True)
    # then delete the experience from DB
    experiences = mongo.db.experiences.find()
    mongo.db.experiences.remove({"_id": ObjectId(experience_id)})
    flash("You have succesfully removed your experience")

    return render_template(
            "profile.html",
            username=session["user"],
            experiences=experiences)


# Error handling
# Good old Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Forbidden - when pressing back after logged out
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(500)
def server_err(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))
