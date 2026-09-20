import sqlite3

conn = sqlite3.connect('test.db')
# cursor --> act as a messanger ==> python --> cursor --> database
cursor = conn.cursor()

# cursor.execute("""DROP TABLE IF EXISTS students""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               Name TEXT PRIMARY KEY, 
               Age INTEGER,
               City TEXT
)
""")

conn.commit() ## Insert/Delete/Update

# # cursor.execute("""
# # SELECT name FROM sqlite_master WHERE type='table'
# #                """)

# print(cursor.fetchall())

# cursor.execute("""SELECT * FROM students
#                """)

# print(cursor.fetchall())

# # cursor.execute(""" ALTER TABLE students RENAME TO Pupil1""")

# # cursor.execute("""
# # SELECT name FROM sqlite_master WHERE type='table'
# #                """)

# cursor.execute("""DROP TABLE students
#                """)



# cursor.execute("""
# SELECT name FROM sqlite_master WHERE type='table'
#                """)

# cursor.execute("""INSERT INTO students VALUES('Dipanshu', 99, 'Pune')""")

cursor.execute("""UPDATE students SET City = 'Los Angeles' WHERE Name = 'John'""")

cursor.execute("""DELETE FROM students WHERE Name = 'John'""")

conn.commit()

cursor.execute("""select * from students""")

print(cursor.fetchall())

cursor.close()
conn.close()


#CRUD --> Create, Read, Update, Delete