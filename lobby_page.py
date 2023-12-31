import PySimpleGUI as sg
from database_operations import fetch_data_by_email,update_money
import slot_machine

def main(email):
    user_data = fetch_data_by_email(email)[0]
    nickname = user_data[3]
    money = user_data[4]

    # Define the list of games available in the lobby
    game_list = [
        "Slot Machine",
        "Roulette",
        "Blackjack",
        "Poker",
        "Craps",
        "Baccarat",
        "Keno",
        "Video Poker",
    ]

    # Define the layout of the lobby page
    layout = [
        [sg.Text("Welcome to the Casino Game Lobby!", font=("Helvetica", 20),justification='center')],
        [sg.Text(f"your name is {nickname}",size=50), sg.Text(f"{money} $",justification='right',key='-BALANCE-')],
        [sg.Text("Please choose a game to play:", font=("Helvetica", 16))],
    ]

    # Create buttons for each game and add them to the layout
    for game in game_list:
        layout.append([sg.Button(game, key=game, size=(15, 2))])


    window = sg.Window("CASINO AGAIN!.exe",layout= layout,finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            update_money(email,money)
            break
        elif event == 'Slot Machine':
            money = slot_machine.main(money)
            window['-BALANCE-'].update(f"{money} $")
        elif event == 'Keno':
            money += 100
            window['-BALANCE-'].update(f"{money} $")


    window.close()

#abc

if __name__ == "__main__":
    main('example@gmail.com')