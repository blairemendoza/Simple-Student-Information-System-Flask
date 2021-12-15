from SSIS import mysql


class students(object):
    
    def __init__(self, idNumber=None, lastName=None, firstName=None,
                 course=None, yearLevel=None, gender=None):
        self.idNumber   = idNumber
        self.lastName   = lastName
        self.firstName  = firstName
        self.course     = course
        self.yearLevel  = yearLevel
        self.gender     = gender
        
    def addStudent(self):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    INSERT INTO students
                    VALUES ('{self.idNumber}', '{self.lastName}', '{self.firstName}',
                            '{self.course}', '{self.yearLevel}', {self.gender})
                    ''')
        mysql.connection.commit()
    
    @staticmethod
    def removeStudent(idNumber):
        try:
            cur = mysql.connetion.cursor()
            cur.execute(f'''
                        DELETE FROM students
                        WHERE id_number='{idNumber}'
                        ''')
            mysql.connection.commit()
            return 1
        
        except:
            return 0

    @staticmethod
    def retrieveAll():
        cur = mysql.connetion.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        return data
    

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
        cur = mysql.connection.cursor()
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
    