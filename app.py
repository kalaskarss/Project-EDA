# S1 - importing flask module

from flask import Flask, render_template, request

# S2 - init flask object

app = Flask(__name__)
# S3 - create route
notes = []
@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

# S4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)