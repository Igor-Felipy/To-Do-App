from flask import Flask, request, render_template, redirect, url_for
import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def toDoApp():
        data = db.GetAssignments()
        return render_template('index.html', data=data) 


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        value = str(request.form['name'])
        db.PostAssignmet(str(value))
        print(value)
        return redirect(url_for('toDoApp'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        value = str(request.form['data'])
        db.PutAssignment(id, value)
        return redirect(url_for('toDoApp'))

    else:
        data = tuple(db.Assignment(id))
        return render_template("edit.html", data=data)


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
        db.DeleteAssignment(id)
        return redirect(url_for('toDoApp'))


app.run(debug=True)