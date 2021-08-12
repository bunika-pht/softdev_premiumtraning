import PySimpleGUI as sg

layout = [  [sg.Text('Resizable Multiline Element Example')],
            [sg.Multiline(size=(20,10), key='-ML-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Resizable Multiline Example', layout, resizable=True,  finalize=True)

window['-ML-'].expand(expand_x=True, expand_y=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()