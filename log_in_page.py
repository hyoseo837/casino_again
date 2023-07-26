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
    
def check_password(email,password):
    connection = create_database_connection()

    cursor_obj = connection.cursor()
    quary = "SELECT pw_hash FROM users WHERE email = '" + email + "';"
    cursor_obj.execute(quary)
    result = cursor_obj.fetchall()
    cursor_obj.close()
    connection.close()

    if result == []:
        sg.popup("Unknown email: check your email address again");
        return False
    else:
        hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest()
        if hashed_pw == result[0][0]:
            sg.popup("Successfully logged in!")
            return True
        else:
            sg.popup("Wrong Password: check your password again")
            return False

def main():
    layout = [
        [sg.Text('enter your email'), sg.InputText(key='-EMAIL-')],
        [sg.Text('enter your password'), sg.InputText(key='-PASSWORD-')],
        [sg.Button('OK',key='-SUBMIT-'),sg.Button('CANCEL')]
    ]

    window = sg.Window("log in",layout= layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'CANCEL':
            break
        elif event == '-SUBMIT-':
            if check_password(values['-EMAIL-'], values['-PASSWORD-']):
                break
        

    window.close()

if __name__ == '__main__':
    main()