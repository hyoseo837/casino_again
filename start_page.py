import PySimpleGUI as sg
import sign_in_page, log_in_page

islogged = False

sg.theme('dark grey 9')
layout = [
    [sg.Text("WELCOME TO CASINO AGAIN!")],
    [sg.Button('Log in',key='-LOG_IN-'),sg.Button('Sign in',key='-SIGN_IN-')]
]

window = sg.Window("CASINO AGAIN!.exe",layout= layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-SIGN_IN-':
        sign_in_page.main()
    elif event == '-LOG_IN-':
        log_in_page.main()

window.close()