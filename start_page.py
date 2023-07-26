import PySimpleGUI as sg
import sign_in_page, log_in_page, lobby_page


def main():
    layout = [
        [sg.Text("WELCOME TO CASINO AGAIN!",size=400,justification='center')],
        [sg.Button('Log in',key='-LOG_IN-'),sg.Button('Sign in',key='-SIGN_IN-')]
    ]

    window = sg.Window("CASINO AGAIN!.exe",layout= layout,size=(400,200),finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-SIGN_IN-':
            sign_in_page.main()
        elif event == '-LOG_IN-':
            user_id = log_in_page.main()
            if user_id:
                window.close()
                lobby_page.main(user_id)

    window.close()

if __name__ == "__main__":
    main()