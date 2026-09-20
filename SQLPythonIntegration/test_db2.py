import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments(
    enroll_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id)
        REFERENCES students(student_id),
    FOREIGN KEY(course_id)
        REFERENCES courses(course_id)
)
""")

cursor.execute("""
INSERT OR IGNORE INTO students(student_id, name)
VALUES
(1, 'Dipanshu'),
(2, 'Priya'),
(3, 'Rahul'),
(4, 'Amit')
""")

cursor.execute("""
INSERT OR IGNORE INTO courses(course_id, course_name)
VALUES
(101, 'Python'),
(102, 'SQL'),
(103, 'AWS')
""")

cursor.execute("""
INSERT OR IGNORE INTO enrollments(
    enroll_id,
    student_id,
    course_id
)
VALUES
(1,1,101),
(2,1,102),
(3,2,101),
(4,3,103)
""")
print("INNER JOIN RESULT")
cursor.execute("""
select s.name, c.course_name from students s inner join enrollments e ON s.student_id = e.student_id
               inner join courses c on e.course_id = c.course_id
""")

print(cursor.fetchall())

cursor.execute("""
select s.name, c.course_name from students s LEFT JOIN enrollments e ON s.student_id = e.student_id
               LEFT JOIN courses c on e.course_id = c.course_id
""")

print("LEFT JOIN RESULT")
print(cursor.fetchall())

cursor.execute("""select s.name, c.course_name from students s RIGHT JOIN enrollments e ON s.student_id = e.student_id
               RIGHT JOIN courses c on e.course_id = c.course_id""")

print("RIGHT JOIN RESULT")
print(cursor.fetchall())

cursor.execute("""select s.name, c.course_name from students s FULL OUTER JOIN enrollments e ON s.student_id = e.student_id
               FULL OUTER JOIN courses c on e.course_id = c.course_id""")

print("FULL OUTER JOIN RESULT")
print(cursor.fetchall())

cursor.execute("""select s.name, c.course_name from students s 
               CROSS JOIN courses c""")

print("CROSS JOIN RESULT")
print(cursor.fetchall())

conn.commit()
conn.close()

try: 
    print("new connection")
    conn = sqlite3.connect('school.db')
    print("new connection created")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO enrollments(enroll_id, student_id, course_id) VALUES(4, 10, 101)""")
    conn.commit()

except Exception as e:
    conn.rollback()
    print("Error occurred: ", e)