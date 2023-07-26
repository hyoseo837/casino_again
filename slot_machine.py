import PySimpleGUI as sg

def main():
        
    layout = [
        [sg.Column([[sg.Text("cherry", justification='aaa')],[sg.Text("bbb")]], element_justification='center'),
        sg.Column([[sg.Text("Centered Text 2", justification='center')]], element_justification='center')]
    ]

    window = sg.Window("Slot Machine",layout= layout,size=(300,500),finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'CANCEL':
            break
                
        

    window.close()

if __name__ == '__main__':
    main()