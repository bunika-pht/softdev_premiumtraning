
import io
import PIL
from PySimpleGUI.PySimpleGUI import Image
from numpy.core.fromnumeric import size
from prep import *
import PySimpleGUI as sg
import shutil
from PIL import *
from PIL import Image

import base64
main = Main()
pp = DataPreprocess()
window_main = sg.Window("AI.EXE", pp.Layout_Data_Preprocess,
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

            elif event == '-RZ-':
                try:
                    img = cv.imread(r"Class\test113\3.png")
                    dim = (int(value['-IN WIDTH-']), int(value['-IN HIGH-']))
                    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
                    print(type(resized))
                    data = Image.fromarray(resized)
                    bio = io.BytesIO()
                    b, g, r = data.split()
                    data = Image.merge("RGB", (r, g, b))
                    data.save(bio, format="PNG")
                    window_main['-IMAGE-'].update(
                        data=bio.getvalue(), size=dim)
                except Exception as e:
                    print(str(e))
            # elif event == '-ADD CLASS-':
            #     folder = value['-FOLDER-']

            #     try:
            #         file_list = os.listdir(folder)
            #     except:
            #         file_list = []
            #     fnames = [
            #         f
            #         for f in file_list
            #         if os.path.isfile(os.path.join(folder, f))
            #         and f.lower().endswith((".png", ".jpg", ".jpeg"))
            #     ]
            #     F_classname = value["-CLASS TYPE-"]
            #     isFolder = os.path.isfile(os.path.join("Class", F_classname))
            #     if isFolder == False:
            #         try:
            #             os.makedirs(os.path.join("Class", F_classname))
            #             path = os.path.join("Class", F_classname)
            #             for i in fnames:
            #                 shutil.copyfile(os.path.join(folder, i), os.path.join(
            #                     path, i))
            #         except Exception as e:
            #             print(str(e))
            #     if isFolder == True:
            #         try:
            #             pass
            #         except Exception as e:
            #             print(str(e))
            #     class_list.append(F_classname)
            #     print(class_list)
            #     window_main['-CLASS LIST-'].update(class_list)
            # elif event == "-CLASS LIST-":  # A file was chosen from the listbox
            #     try:
            #         file_list = os.listdir(os.path.join(
            #             "Class", value["-CLASS LIST-"][0]))
            #         fnames = [
            #             f
            #             for f in file_list
            #         ]
            #         window_main['-FILE LIST-'].update(fnames)

            #     except Exception as e:
            #         print(str(e))
        except Exception as e:
            print(str(e))
            break
