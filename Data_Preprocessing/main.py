
from prep import *
import PySimpleGUI as sg
main = Main()
pp = DataPreprocess()
window_main = sg.Window("AI.EXE", pp.Layout_InserDataset,
                        resizable=True, finalize=True)
window_main.maximize()
window_main.TKroot.minsize(550, 200)
window_insert_active = False

if __name__ == "__main__":
    while True:
        try:
            event, value = window_main.read()
            if event == WIN_CLOSED:
                break
            elif event == '-FOLDER-':
                folder = value['-FOLDER-']
                print(folder)
                try:
                    # ? Get list of files in folder
                    file_list = os.listdir(folder)
                    # print("filelist"+str(file_list))
                except:
                    file_list = []
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".jpg", ".jpeg"))
                ]
                F_classname = value["-CLASS TYPE-"]
                isFile = os.path.isfile(os.path.join("Class", F_classname))
                print(isFile)
                if isFile == False:
                    os.makedirs(os.path.join("Class", F_classname))

                window_main['-FILE LIST-'].update(fnames)
        except Exception as e:
            print(str(e))
            break
