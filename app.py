import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# cloudinary imports
import cloudinary
from cloudinary.uploader import upload, destroy

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

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


@app.route("/")
@app.route("/experiences_home")
def experiences_home():
    experiences = mongo.db.experiences.find()
    return render_template("experiences_home.html", experiences=experiences)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    experiences = list(mongo.db.experiences.find(
        {"$text": {"$search": query}}))
    return render_template("experiences_home.html", experiences=experiences)


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


@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("experiences_home"))


@app.route("/moreinfo/<experience_id>")
def moreinfo(experience_id):
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    return render_template("moreinfo.html", experience=experience)


@app.route("/imageupload", methods=["GET", "POST"])
def imageupload():
    # downsized = None
    upload_result = None
    if request.method == "POST":
        file_to_upload = request.files.get("image")
        if file_to_upload:
            upload_result = upload(file_to_upload)
        else:
            flash("You have to upload an image first to create experience")
            return redirect(url_for('imageupload'))

        imagelink = upload_result['secure_url']
        public_id = upload_result['public_id']
        return render_template(
            'addxp.html', imagelink=imagelink, public_id=public_id)

    return render_template("imageupload.html")


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


@app.route("/imgedit/<experience_id>", methods=["GET", "POST"])
def imgedit(experience_id):
    upload_result = None
    experience_id = experience_id
    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    # public_id = experience.public_id

    if request.method == "POST":
        file_to_upload = request.files.get("image")
        if file_to_upload:
            upload_result = upload(file_to_upload)
            imagelink = upload_result['secure_url']
            public_id = experience['public_id']
            # if upload_result['public_id'] != public_id:
                # cloudinary.uploader.destroy(
                    # experience['public_id'], invalidate=True)

            flash("Image updated succesfully")
            return render_template(
                'editxp.html',
                imagelink=imagelink,
                experience_id=experience_id)

        else:
            imagelink = experience['imagelink']
            return render_template(
                'editxp.html',
                experience=experience,
                imagelink=imagelink,
                experience_id=experience_id)

        return render_template(
            'editxp.html',
            imagelink=imagelink,
            experience=experience,
            experience_id=experience_id)

    return render_template(
        "imgedit.html", experience=experience, experience_id=experience_id)


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

    experience = mongo.db.experiences.find_one(
        {"_id": ObjectId(experience_id)})
    return render_template(
        "editxp.html",
        experience=experience,
        experience_id=experience_id)


@app.route("/deletexp/<experience_id>")
def deletexp(experience_id):
    experiences = mongo.db.experiences.find()
    mongo.db.experiences.remove({"_id": ObjectId(experience_id)})
    # destroy(experience['public_id'], invalidate=True)
    flash("You have succesfully removed your experience")

    return render_template(
            "profile.html", username=session["user"])


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # cloud_name=os.environ.get("CLOUD_NAME"),
            debug=True)
