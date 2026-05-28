from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    email = request.form.get("email")
    employee_id = request.form.get("employee_id")
    department = request.form.get("department")

    tasks = []

    if department == "Developer":
        tasks = [
            "Create GitHub Account",
            "Install VS Code",
            "Complete Security Training"
        ]

    elif department == "HR":
        tasks = [
            "Employee Policy Training",
            "Recruitment Basics",
            "Payroll Overview"
        ]

    elif department == "Marketing":
        tasks = [
            "Marketing Orientation",
            "Campaign Training",
            "Social Media Basics"
        ]

    return render_template(
        "result.html",
        name=name,
        email=email,
        employee_id=employee_id,
        department=department,
        tasks=tasks
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)