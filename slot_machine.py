import PySimpleGUI as sg
import random
import lobby_page

def earning(slots):
    if slots.count('🍒') == 3:
        return 5000
    elif slots.count('🍒') == 2:
        return 100
    elif slots.count('🍒') == 1:
        return 50
    elif slots.count('1') == 3:
        return 1000
    elif slots.count('2') == 3:
        return 1200
    elif slots.count('3') == 3:
        return 1400
    elif slots.count('4') == 3:
        return 1600
    elif slots.count('5') == 3:
        return 1800
    elif slots.count('6') == 3:
        return 2000
    elif slots.count('7') == 3:
        return 3000
    else:
        return 0

def main(account):
    money = account
    symbols = ['1','2','3','4','5','6','7','🍒']
    slots = ['1','1','1']

    layout = [
        [sg.Text(f'your balance : {money}',justification='right',key='-BALANCE-')],
        [sg.Text('🍒',key='-SLOT1-'),sg.Text('🍒',key='-SLOT2-'),sg.Text('🍒',key='-SLOT3-')],
        [sg.Button('roll',key='-ROLL-')]
    ]

    window = sg.Window("Slot Machine",layout= layout,size=(200,300),finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'CANCEL':
            sg.popup('going to lobby...')
            break
        elif event == '-ROLL-':
            if money > 49:
                money -= 50
                for i in range(3):
                    slots[i] = random.choice(symbols)
                window['-SLOT1-'].update(slots[0])
                window['-SLOT2-'].update(slots[1])
                window['-SLOT3-'].update(slots[2])
                bonus = earning(slots)
                money += bonus
                window['-BALANCE-'].update(f'your balance : {money}')
                if bonus > 999:
                    sg.popup(f"Congratulation!\nyou got {bonus} $")
            else:
                sg.popup('not enough money')
                

    window.close()
    return money

if __name__ == '__main__':
    main(5000)