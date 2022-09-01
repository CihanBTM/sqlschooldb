import mysql.connector
from datetime import datetime
from connection import connection

import mysql.connector

'''connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="???????",
        database="schooldb")'''

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname,birthday,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthday,Gender) VALUES(%s, %s, %s, %s, %s)"
        value = (self.studentNumber,self.name,self.surname,self.birthday,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit eklendi.')

        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()




#ahmet = Student("202","ahmet","yilmaz",datetime(2005, 5, 17), "E")
#ahmet.saveStudent()



    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthday,Gender) VALUES(%s, %s, %s, %s, %s)"
        value = students
        Student.mycursor.executemany(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayit eklendi.')

        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

ogrenciler = [("301", "Ahmet", "Yilmaz", datetime(2005, 5, 17), "E"),
              ("302", "Ali", "Can", datetime(2005, 6, 17), "E"),
              ("303", "Canan", "Tan", datetime(2005, 7, 17), "K"),
              ("304", "Ayse", "Taner", datetime(2005, 9, 23), "K"),
              ("305", "Bahadir", "Tokoz", datetime(2004, 7, 27), "E"),
              ("306", "Ali", "Cenk", datetime(2003, 8, 25), "E")
              ]

Student.saveStudents(ogrenciler)


##############################################################

    @staticmethod

    def StudentInfo():
        sql = "select * from student"

        Student.mycursor.execute(sql)

        try:
            result = Student.mycursor.fetchall()
            print(result)
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

Student.StudentInfo()












##
