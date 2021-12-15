from flask import render_template, redirect, url_for, request, flash
from . import course
from SSIS.models import courses, colleges
from SSIS.course.forms import courseForm

@course.route('/')
@course.route('/index')
def index():
    data = courses.retrieveAll()
    collegeList = colleges.retrieveAll()
    form = courseForm()
    title = 'Courses'
    
    return render_template('course/index.html', courses=data,
                           colleges=collegeList, form=form, title=title)


@course.route('/add', methods=['GET', 'POST'])
def addCourse():
    if request.method == 'POST':
        form = courseForm()
        collegeCode = request.form['collegeAdd']
        status = courses.addCourse(form.data, collegeCode)
        
        if 1 in status:
            flash(f"'{status[1]}' has been successfully added.", "success")
        else:
            flash(f"{status[1]}", "error")
        
        return redirect(url_for('course.index'))
    
    else:
        flash("You are trying to access a forbidden URL. Maybe try adding a course first.", "error")
        return redirect(url_for('course.index'))
    

@course.route('/update', methods=['GET', 'POST'])
def updateCourse():
    if request.method == 'POST':
        form = courseForm()
        collegeCode = request.form['collegeUpdate']
        status = courses.updateCourse(form.data, collegeCode)
        
        if 1 in status:
            flash(f"'{status[1]}' has been successfully updated.", "success")
        else:
            flash(f"{status[1]}", "error")
            
        return redirect(url_for('course.index'))
    
    else:
        flash("You are trying to access a forbidden URL. Maybe try updating a course first.", "error")
        return redirect(url_for('course.index'))
    
    
@course.route('/remove/<string:courseCode>')
def removeCourse(courseCode):
    status = courses.removeCourse(courseCode)

    if 1 in status:
        flash(f"'{status[1]}' has been successfully removed.", "success")
    else:
        flash(f"{status[1]}", "error")
    
    return redirect(url_for('course.index'))