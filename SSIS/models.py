from SSIS import mysql


class students():
    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM students ORDER BY id_number")
        data = cur.fetchall()
        return data
    
    @staticmethod
    def addStudent(form, gender, course):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO students
                        VALUES ('{form["idNumber"]}',
                                '{form["lastName"]}',
                                '{form["firstName"]}',
                                '{course}',
                                {form["yearLevel"]},
                                '{gender}')
                        ''')
            mysql.connection.commit()
            status = [1, form["firstName"], form["lastName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status

    @staticmethod
    def updateStudent(form, gender, course):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        UPDATE students
                        SET id_number='{form["idNumber"]}',
                            last_name='{form["lastName"]}',
                            first_name='{form["firstName"]}',
                            course='{course}',
                            year_level={form["yearLevel"]},
                            gender='{gender}'
                        WHERE id_number='{form["referID"]}'
                        ''')
            mysql.connection.commit()
            status = [1, form["firstName"], form["lastName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status
    
    @staticmethod
    def removeStudent(idNumber):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        DELETE FROM students
                        WHERE id_number='{idNumber}'
                        ''')
            mysql.connection.commit()
            status = [1, idNumber]
            return status
        
        except Exception as e:
            status = [0, e]
            return status


class courses(object):
    
    def __init__(self, courseCode=None,
                 courseName=None, collegeCode=None):
        self.courseCode     = courseCode
        self.courseName     = courseName
        self.collegeCode    = collegeCode
        
    def addCourse(self):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO courses
                        VALUES ('{self.courseCode}', '{self.courseName}',
                                '{self.collegeCode}')
                        ''')
            mysql.connection.commit()
            return "Success"
            
        except Exception as e:
            print(e)
            return e
    
    @staticmethod
    def removeCourse(courseCode):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    DELETE FROM courses
                    WHERE course_code='{courseCode}'
                    ''')
        mysql.connection.commit()
        
    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM courses")
        data = cur.fetchall()
        return data


class colleges(object):
    
    def __init__(self, collegeCode=None, collegeName=None):
        self.collegeCode = collegeCode
        self.collegeName = collegeName
        
    def addCollege(self):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO colleges
                        VALUES ('{self.collegeCode}', '{self.collegeName}')
                        ''')
            mysql.connection.commit()
            return "Success"
            
        except Exception as e:
            print(e)
            return e
    
    @staticmethod
    def removeCollege(collegeCode):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        DELETE FROM colleges
                        WHERE college_code='{collegeCode}'
                        ''')
            mysql.connetion.commit()
            return 1
        
        except:
            return 0

    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM colleges")
        data = cur.fetchall()
        return data
    