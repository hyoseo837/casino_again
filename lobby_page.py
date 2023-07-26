import PySimpleGUI as sg
from database_operations import fetch_data_by_email

def main(email):
    user_data = fetch_data_by_email(email)[0]

    layout = [
        [sg.Text("WELCOME TO CASINO AGAIN!")],
        [sg.Text(f"your name is {user_data[3]}",)]
    ]

    window = sg.Window("CASINO AGAIN!.exe",layout= layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main('example@gmail.com')