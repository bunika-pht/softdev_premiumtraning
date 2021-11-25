
from PySimpleGUI.PySimpleGUI import I
from prep import *
import PySimpleGUI as sg
import shutil
main = Main()
pp = DataPreprocess()
window_main = sg.Window("AI.EXE", pp.Layout_InserDataset,
                        resizable=True, finalize=True)
window_main.maximize()
window_main.TKroot.minsize(550, 200)
window_insert_active = False

if __name__ == "__main__":
    class_list = []
    while True:
        try:
            event, value = window_main.read()
            if event == WIN_CLOSED:
                break
            elif event == '-ADD CLASS-':
                folder = value['-FOLDER-']

                try:
                    file_list = os.listdir(folder)
                except:
                    file_list = []
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".jpg", ".jpeg"))
                ]
                F_classname = value["-CLASS TYPE-"]
                isFolder = os.path.isfile(os.path.join("Class", F_classname))
                if isFolder == False:
                    try:
                        os.makedirs(os.path.join("Class", F_classname))
                        path = os.path.join("Class", F_classname)
                        for i in fnames:
                            shutil.copyfile(os.path.join(folder, i), os.path.join(
                                path, i))
                    except Exception as e:
                        print(str(e))
                if isFolder == True:
                    try:
                        pass
                    except Exception as e:
                        print(str(e))
                class_list.append(F_classname)
                print(class_list)
                window_main['-CLASS LIST-'].update(class_list)
            elif event == "-CLASS LIST-":  # A file was chosen from the listbox
                try:
                    file_list = os.listdir(os.path.join(
                        "Class", value["-CLASS LIST-"][0]))
                    fnames = [
                        f
                        for f in file_list
                    ]
                    window_main['-FILE LIST-'].update(fnames)

                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))
            break
