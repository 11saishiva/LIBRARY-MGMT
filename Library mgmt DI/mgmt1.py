import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

host_name = "127.0.0.1"
user_name = "root"
user_password = "Sql@1234"
db_name = "library"
conn = create_connection(host_name, user_name, user_password, db_name)
cursor = conn.cursor()

def add_book(title, author, genre, year_published):
    sql = "INSERT INTO BOOKS(TITLE, AUTHOR, GENRE, YEAR_PUBLISHED) VALUES (%s, %s, %s, %s)"
    val = (title, author, genre, year_published)
    cursor.execute(sql, val)
    conn.commit()

def add_member(name, email, phone):
    sql = "INSERT INTO MEMBERS(MEMBER_NAME,EMAIL,PHONE) VALUES (%s, %s, %s)"
    val = (name, email, phone)
    cursor.execute(sql, val)
    conn.commit()

def borrow_book(member_id, book_id):
    sql = "UPDATE books SET AVAILABILITY = 'BORROWED' WHERE BOOK_ID = %s"
    cursor.execute(sql, (book_id,))
    sql = "INSERT INTO BORROWING_RECORDS(MEMBER_ID,BOOK_ID,BORROW_DATE) VALUES (%s, %s, CURDATE())"
    cursor.execute(sql, (member_id, book_id))
    conn.commit()

def return_book(book_id):
    sql = "UPDATE books SET AVAILABILITY = 'AVAILABLE' WHERE BOOK_ID = %s"
    cursor.execute(sql, (book_id,))
    sql = "UPDATE BORROWING_RECORDS SET RETURN_DATE = CURDATE() WHERE BOOK_ID = %s AND RETURN_DATE IS NULL"
    cursor.execute(sql, (book_id,))
    conn.commit()

def get_books():
    connection = create_connection(host_name, user_name, user_password, db_name)
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT BOOK_ID, TITLE, AUTHOR, GENRE, YEAR_PUBLISHED, AVAILABILITY FROM BOOKS")
            books = cursor.fetchall()
            return books
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()

def get_members():
    connection = create_connection(host_name, user_name, user_password, db_name)
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT MEMBER_ID,MEMBER_NAME,EMAIL,PHONE FROM members")
            books = cursor.fetchall()
            return books
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()
def remove_book(book_id):
    connection = create_connection(host_name, user_name, user_password, db_name)
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM BOOKS WHERE BOOK_ID = %s", (book_id,))
            connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()

def remove_member(member_id):
    connection = create_connection(host_name, user_name, user_password, db_name)
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM MEMBERS WHERE MEMBER_ID = %s", (member_id,))
            connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()
