
from prep import *
import PySimpleGUI as sg
main = Main()
pp = DataPreprocess()
window_main = sg.Window("AI.EXE", main.Layout, resizable=True, finalize=True)
window_main.maximize()
window_main.TKroot.minsize(550, 200)
window_insert_active = False

if __name__ == "__main__":
    while True:
        try:
            event, value = window_main.read()
            if event == WIN_CLOSED:
                break
        except Exception as e:
            print(e)
            break
