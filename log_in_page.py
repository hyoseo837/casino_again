import PySimpleGUI as sg
from database_operations import check_password

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
            pw_status = check_password(values['-EMAIL-'],values['-PASSWORD-'])
            if pw_status == 'LoggedIn':
                sg.popup("successfully logged in!")
                window.close()
                return values['-EMAIL-']
            else:
                sg.popup(pw_status)
                
        

    window.close()

if __name__ == '__main__':
    main()