"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    titles_grades = hackbright.get_grades_by_github(github)



    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github,
                            titles_grades=titles_grades)

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    html = render_template("student_search.html")

    return html


@app.route("/student-add")
def student_add():
    """Add a student."""

    

    return render_template("student_add.html")




@app.route("/new-student", methods=['POST'])
def new_student():
    """Shows new student information."""

    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name,last_name,github)

    return render_template("new_student.html", 
                            first_name=first_name, 
                            last_name=last_name, 
                            github=github)

@app.route("/project")
def project_info():
    """Shows project info."""

    link_title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(link_title)

    students_grades = hackbright.get_grades_by_title(link_title)

    return render_template("project.html", 
                            title=title,
                            description=description,
                            maximum_grade=max_grade,
                            students_grades=students_grades)


@app.route("/")
def homepage():
    """Displays list of students and projects."""

    projects = hackbright.get_grades_by_github(github)

    students = hackbright.get_grades_by_title(title)

    return render_template("homepage.html",
                            projects=projects,
                            students=students)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)



