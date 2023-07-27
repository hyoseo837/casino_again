import psycopg2
import hashlib

def create_database_connection():
    try:
        connection = psycopg2.connect(
            database="casino_again",
            user="postgres",
            password="14511461",
            host="localhost",
            port='5432'
        )
        return connection
    except psycopg2.OperationalError as e:
        return "Database connection error: "+ str(e)

     
def register_user(name, email, password):

    hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest()
    connection = create_database_connection()
    cursor_obj = connection.cursor()
    quary = f"INSERT INTO users (nickname, email, pw_hash, account, sign_in_date) VALUES ('{name}','{email}','{hashed_pw}', 500, NOW()::DATE);"
    cursor_obj.execute(quary)
    connection.commit()
    cursor_obj.close()
    connection.close()

def update_money(email,money):
    connection = create_database_connection()
    if type(connection) == str:
        return None
    cursor_obj = connection.cursor()
    quary = f"UPDATE users SET account = {money} WHERE email = '{email}';"
    cursor_obj.execute(quary)
    connection.commit()
    cursor_obj.close()
    connection.close()


def check_password(email,password):
    result = fetch_data_by_email(email)
    if result == None:
        return "connectionError"
    elif result == []:
        return "unknownEmail"
    else:
        hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest()
        if hashed_pw == result[0][2]:
            return "LoggedIn"
        else:
            return "wrongPassword"

    
def fetch_data_by_email(email):
    connection=create_database_connection()
    if type(connection) == str:
        return None
    cursor_obj = connection.cursor()
    quary = "SELECT * FROM users WHERE email = '" + email + "';"
    cursor_obj.execute(quary)
    result = cursor_obj.fetchall()
    cursor_obj.close()
    connection.close()
    return result
