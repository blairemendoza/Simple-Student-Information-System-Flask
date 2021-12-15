from flask import render_template, redirect, url_for, request, flash
from . import college
from SSIS.models import colleges
from SSIS.college.forms import collegeForm

@college.route('/')
@college.route('/index')
def index():
    data = colleges.retrieveAll()
    form = collegeForm()
    title = 'Colleges'

    return render_template('college/index.html', colleges=data,
                           form=form, title=title)
    

@college.route('/add', methods=['GET', 'POST'])
def addCollege():
    if request.method == 'POST':
        form = collegeForm()
        status = colleges.addCollege(form.data)
        
        if 1 in status:
            flash(f"'{status[1]}' has been successfully added.", "success")
        else:
            flash(f"{status[1]}", "error")
            
        return redirect(url_for('college.index'))
    
    else:
        flash("You are trying to access a forbidden URL. Maybe try adding a college first.", "error")
        return redirect(url_for('college.index'))
    
@college.route('/update', methods=['GET', 'POST'])
def updateCollege():
    if request.method == 'POST':
        form = collegeForm()
        status = colleges.updateCollege(form.data)
        
        if 1 in status:
            flash(f"'{status[1]}' has been successfully updated.", "success")
        else:
            flash(f"{status[1]}", "error")

        return redirect(url_for('college.index'))
        
    else:
        flash("You are trying to access a forbidden URL. Maybe try updating a college first.", "error")
        return redirect(url_for('college.index'))
    
@college.route('/remove/<string:collegeCode>')
def removeCollege(collegeCode):
    status = colleges.removeCollege(collegeCode)

    if 1 in status:
        flash(f"'{status[1]}' has been successfully removed.", "success")
    else:
        flash(f"{status[1]}", "error")
    
    return redirect(url_for('college.index'))