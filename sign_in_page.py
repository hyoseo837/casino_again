import PySimpleGUI as sg
from database_operations import register_user
from check_validity import *

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
            if is_email_valid(values['-EMAIL-']):
                window['-READY_TEXT-'].update('you can use this email', text_color = 'Green')
                isAvailable = True
                email_add = values['-EMAIL-']
            else:
                window['-READY_TEXT-'].update('enter another email', text_color = 'Red')
                isAvailable = False
        elif event == '-SUBMIT-':
            pw1, pw2 = values['-PASSWORD-'],values['-PASSWORD_CHECK-']
            if is_password_valid(pw1,pw2):
                if isAvailable:
                    name = values['-NAME-']
                    if not is_name_valid:
                        sg.popup('invalid nickname')
                    else:
                        register_user(name,email_add,pw1)
                        sg.popup("User registered successfully!")
                        break
                else:
                    sg.popup("invalid email")
            else:
                sg.popup("invalid password")

    window.close()

if __name__ == '__main__':
    main()