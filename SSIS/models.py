from SSIS import mysql


class students():
    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM students ORDER BY id_number")
        data = cur.fetchall()
        return data
    
    @staticmethod
    def addStudent(form, gender, course, imgURL, thumbURL):
        print(imgURL)
        print(thumbURL)
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO students
                        VALUES ('{form["idNumber"]}',
                                '{form["lastName"]}',
                                '{form["firstName"]}',
                                '{course}', '{form["yearLevel"]}',
                                '{gender}', '{imgURL}', '{thumbURL}')
                        ''')
            mysql.connection.commit()
            status = [1, form["firstName"], form["lastName"]]
            return status
        
        except Exception as e:
            print(e)
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
    def updateImage(imgURL, thumbURL, idNumber):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    UPDATE students
                    SET img_url='{imgURL}',
                        thumb_url='{thumbURL}'
                    WHERE id_number='{idNumber}'
                    ''')
        mysql.connection.commit()
        return
    
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


class courses():
    
    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM courses")
        data = cur.fetchall()
        return data
        
    @staticmethod
    def addCourse(form, collegeCode):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO courses
                        VALUES ('{form["courseCode"]}',
                                '{form["courseName"]}',
                                '{collegeCode}')
                        ''')
            mysql.connection.commit()
            status = [1, form["courseName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status
        
    @staticmethod
    def updateCourse(form, collegeCode):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        UPDATE courses
                        SET course_code='{form["courseCode"]}',
                            course_name='{form["courseName"]}',
                            college_code='{collegeCode}'
                        WHERE course_code='{form["referCode"]}'
                        ''')
            mysql.connection.commit()
            status = [1, form["courseName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status
    
    @staticmethod
    def removeCourse(courseCode):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        DELETE FROM courses
                        WHERE course_code='{courseCode}'
                        ''')
            mysql.connection.commit()
            status = [1, courseCode]
            return status
        
        except Exception as e:
            status = [0, e]
            return status


class colleges():
    
    @staticmethod
    def retrieveAll():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM colleges")
        data = cur.fetchall()
        return data

    @staticmethod
    def addCollege(form):
        print(form)
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO colleges
                        VALUES ('{form["collegeCode"]}',
                                '{form["collegeName"]}')
                        ''')
            mysql.connection.commit()
            status = [1, form["collegeName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status

    @staticmethod
    def updateCollege(form):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        UPDATE colleges
                        SET college_code='{form["collegeCode"]}',
                            college_name='{form["collegeName"]}'
                        WHERE college_code='{form["referCode"]}'
                        ''')
            mysql.connection.commit()
            status = [1, form["collegeName"]]
            return status
        
        except Exception as e:
            status = [0, e]
            return status
    
    @staticmethod
    def removeCollege(collegeCode):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        DELETE FROM colleges
                        WHERE college_code='{collegeCode}'
                        ''')
            mysql.connection.commit()
            status = [1, collegeCode]
            return status
        
        except Exception as e:
            status = [0, e]
            return status