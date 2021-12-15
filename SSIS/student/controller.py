from flask import render_template, redirect, request, flash
from flask.helpers import url_for
from . import student
from SSIS.models import students, courses
from SSIS.student.forms import studentForm

@student.route('/')
@student.route('/index')
def index():
    data = students.retrieveAll()
    courseList = courses.retrieveAll()
    form = studentForm()
    title = 'Home'
    
    return render_template('student/index.html', students=data,
                           courses=courseList, form=form, title=title)


@student.route('/student/add', methods=['GET', 'POST'])
def addStudent():
    if request.method == 'POST':
        form = studentForm()
        gender = request.form['genderAdd']
        course = request.form['courseAdd']
        status = students.addStudent(form.data, gender, course)
        
        if 1 in status:
            flash(f"'{status[1]} {status[2]}' has been successfully added.", "success")
        else:
            flash(f"{status[1]}", "error")
        
        return redirect(url_for('student.index'))
    
    else:
        flash("You are trying to access a forbidden URL. Maybe try adding a student first.", "error")
        return redirect(url_for('student.index'))


@student.route('/student/update', methods=['GET', 'POST'])
def updateStudent():
    if request.method == 'POST':
        form = studentForm()
        gender = request.form['genderUpdate']
        course = request.form['courseUpdate']
        status = students.updateStudent(form.data, gender, course)
        
        if 1 in status:
            flash(f"'{status[1]} {status[2]}' has been successfully updated.", "success")
        else:
            flash(f"{status[1]}", "error")
        
        return redirect(url_for('student.index'))
    
    else:
        flash("You are trying to access a forbidden URL. Maybe try updating a student first.", "error")
        return redirect(url_for('student.index'))


@student.route('/student/remove/<string:idNumber>')
def removeStudent(idNumber):
    status = students.removeStudent(idNumber)
    
    if 1 in status:
        flash(f"'{status[1]}' has been successfully removed.", "success")
    else:
        flash(f"{status[1]}", "error")
    
    return redirect(url_for('student.index'))