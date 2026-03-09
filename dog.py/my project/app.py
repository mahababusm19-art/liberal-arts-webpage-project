from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "secret"


# DATA
students = [
    {"name":"Sota Matazuki","year":"3"},
    {"name":"Ms. Pranati Narain","year":"3"},
    {"name":"SARANYA BHAKUNI","year":"3"}
]

courses = [
"Political Thought",
"Storytelling",
"Python Programming",
"Design Thinking",
"Sustainability Studies"
]

faculty = [
"Sucheth sir",
"Lal Dina Sir",
"Vipiin sir"
]

placements = [
{"student":"Lakshita","company":"Google"},
{"student":"Yazhini","company":"Deloitte"}
]

timetable = [
{"day":"Monday","course":"Political Thought"},
{"day":"Tuesday","course":"Python Programming"},
{"day":"Wednesday","course":"Design Thinking"},
{"day":"Thursday","course":"Storytelling"},
{"day":"Friday","course":"Sustainability Studies"}
]


# LOGIN PAGE
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "student" and password == "123":

            session["user"] = username
            return redirect(url_for("home"))

    return render_template("login.html")


# HOME PAGE
@app.route("/home")
def home():

    if "user" in session:
        return render_template("index.html")

    return redirect("/")


# COURSES PAGE
@app.route("/courses")
def courses_page():

    if "user" in session:
        return render_template("courses.html", courses=courses)

    return redirect("/")


# STUDENTS PAGE
@app.route("/students")
def students_page():

    if "user" in session:
        return render_template("students.html", students=students)

    return redirect("/")


# FACULTY PAGE
@app.route("/faculty")
def faculty_page():

    if "user" in session:
        return render_template("faculty.html", faculty=faculty)

    return redirect("/")


# PLACEMENTS PAGE
@app.route("/placements")
def placements_page():

    if "user" in session:
        return render_template("placements.html", placements=placements)

    return redirect("/")


# TIMETABLE PAGE
@app.route("/timetable")
def timetable_page():

    if "user" in session:
        return render_template("timetable.html", timetable=timetable)

    return redirect("/")


# LOGOUT
@app.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True)