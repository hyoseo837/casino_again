import psycopg2
import PySimpleGUI as sg
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
        sg.popup("Database connection error:", str(e))
        return None

def is_email_available(email):
    if not('@' in email and '.' in email):
        return False
    else:
        connection = create_database_connection()

        cursor_obj = connection.cursor()
        quary = "SELECT * FROM users WHERE email = '" + email + "';"
        cursor_obj.execute(quary)
        result = cursor_obj.fetchall()
        cursor_obj.close()
        connection.close()
        if result == []:
            return True
        else:
            return False
     
def add_to_database(name, email,hashed_pw):
    connection = create_database_connection()
    cursor_obj = connection.cursor()
    quary = f"INSERT INTO users (nickname, email, pw_hash, account, sign_in_date) VALUES ('{name}','{email}','{hashed_pw}', 500, NOW()::DATE);"
    cursor_obj.execute(quary)
    connection.commit()
    cursor_obj.close()
    connection.close()

def register_user(isAvailable,name, email, password):
    if not isAvailable:
        sg.popup('The email is not available or invalid.', text_color='red')
        return False
    if len(name)>50:
        sg.popup('your nickname is too long', text_color='red')
        return False

    hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest()
    add_to_database(name,email, hashed_pw);
    return True


def main():
    isAvailable = False;
    layout = [
        [sg.Text('Enter your email'),sg.InputText(key = '-EMAIL-')],
        [sg.Button('Check Available', key = '-CHECK_AVAIL-'),sg.Text('enter your email',key = '-READY_TEXT-')],
        [sg.Text('Enter your name'), sg.InputText(key = '-NAME-')],
        [sg.Text('Enter your password  '), sg.InputText(key = '-PASSWORD-')],
        [sg.Text('Reenter your password'), sg.InputText(key = '-PASSWORD_CHECK-')],
        [sg.Button('Submit', key='-SUBMIT-'),sg.Button('CANCEL')]

    ]
    window = sg.Window("Sign In",layout= layout)

    email_add = 'example@gmail.com'
    pw1 = 0;
    pw2 = 1;

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'CANCEL':
            break
        elif event == '-CHECK_AVAIL-':
            email = values['-EMAIL-']
            if is_email_available(email):
                window['-READY_TEXT-'].update('you can use this email', text_color = 'Green')
                isAvailable = True
                email_add = email
            else:
                window['-READY_TEXT-'].update('enter another email', text_color = 'Red')
                isAvailable = False
        elif event == '-SUBMIT-':
            pw1 = values['-PASSWORD-']
            pw2 = values['-PASSWORD_CHECK-']
            if pw1 == pw2:
                if register_user(isAvailable, values['-NAME-'],email_add,pw1):
                    sg.popup("User registered successfully!")
                    break
            else:
                sg.popup("Please Recheck the passwords")

    window.close()

if __name__ == '__main__':
    main()