import io
from os import path
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
# window_main = sg.Window("AI.EXE", pp.Layout_InserDataset,
#                         resizable=True, finalize=True)
window_main.maximize()
window_main.TKroot.minsize(550, 200)
window_insert_active = False


def controller(img, brightness=255,
               contrast=127):

    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv.addWeighted(img, al_pha,
                             img, 0, ga_mma)

    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv.addWeighted(cal, Alpha,
                             cal, 0, Gamma)

    # putText renders the specified text string in the image.
    # cv.putText(cal, 'B:{},C:{}'.format(brightness,
    #                                     contrast), (10, 30),
    #             cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cal


if __name__ == "__main__":
    class_list = []
    while True:
        class_combo = os.listdir(r"Class")
        try:
            event, value = window_main.read()
            window_main["-CLASS COMBO-"].update(values=class_combo)
            if event == WIN_CLOSED:
                break
            elif event == '-CLASS COMBO-':
                selected_class = value["-CLASS COMBO-"]
                window_main["-CLASS NAME-"].Update(selected_class)
                path_image = os.path.join(r"Class/", selected_class+"/")
                img_list = os.listdir(path_image)
                window_main["-FILE LIST-"].update(img_list)
            elif event == '-FILE LIST-':
                try:
                    filename = value["-FILE LIST-"][0]
                    name, ext = os.path.splitext(filename)
                    img = cv.imread(os.path.join(path_image, filename))
                    window_main['-IN HIGH-'].update(img.shape[0])
                    window_main['-IN WIDTH-'].update(img.shape[1])
                    data = Image.fromarray(img)
                    data.thumbnail((600, 300))
                    bio = io.BytesIO()
                    b, g, r = data.split()
                    data = Image.merge("RGB", (r, g, b))
                    data.save(bio, format="PNG")
                    window_main['-IMAGE-'].update(data=bio.getvalue(),
                                                  size=(600, 300))
                except Exception as e:
                    print("error:"+str(e))
            elif event == '-CL-':
                img = cv.imread(os.path.join(path_image, filename))
                window_main['-IN HIGH-'].update(img.shape[0])
                window_main['-IN WIDTH-'].update(img.shape[1])
                data = Image.fromarray(img)
                data.thumbnail((600, 300))
                bio = io.BytesIO()
                b, g, r = data.split()
                data = Image.merge("RGB", (r, g, b))
                data.save(bio, format="PNG")
                window_main['-IMAGE-'].update(
                    data=bio.getvalue(), size=(600, 300))
            elif event == '-RZ-':
                try:
                    dim = (int(value['-IN WIDTH-']), int(value['-IN HIGH-']))
                    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
                    data = Image.fromarray(resized)
                    data.thumbnail((600, 300))
                    bio = io.BytesIO()
                    b, g, r = data.split()
                    data = Image.merge("RGB", (r, g, b))
                    data.save(bio, format="PNG")
                    window_main['-IMAGE-'].update(
                        data=bio.getvalue(), size=(600, 300))
                except Exception as e:
                    print(str(e))

            elif event == '-TL-':
                img = cv.rotate(
                    img, cv.ROTATE_90_COUNTERCLOCKWISE)
                data = Image.fromarray(img)
                data.thumbnail((600, 300))
                bio = io.BytesIO()
                b, g, r = data.split()
                data = Image.merge("RGB", (r, g, b))
                data.save(bio, format="PNG")
                window_main['-IMAGE-'].update(
                    data=bio.getvalue(), size=(600, 300))
            elif event == '-TR-':
                img = cv.rotate(
                    img, cv.ROTATE_90_CLOCKWISE)
                data = Image.fromarray(img)
                data.thumbnail((600, 300))
                bio = io.BytesIO()
                b, g, r = data.split()
                data = Image.merge("RGB", (r, g, b))
                data.save(bio, format="PNG")
                window_main['-IMAGE-'].update(
                    data=bio.getvalue(), size=(600, 300))
            elif event == '-SLIDER BRIGHT-':
                try:
                    # convert it to hsv
                    defualt_b = 0
                    slide_value_b = int(value["-SLIDER BRIGHT-"])
                    slide_value_c = int(value["-SLIDER CONTRAST-"])

                    img = controller(img, slide_value_b,
                                     slide_value_c)
                    data = Image.fromarray(img)
                    data.thumbnail((600, 300))
                    bio = io.BytesIO()
                    b, g, r = data.split()
                    data = Image.merge("RGB", (r, g, b))
                    data.save(bio, format="PNG")
                    window_main['-IMAGE-'].update(
                        data=bio.getvalue(), size=(600, 300))

                except Exception as e:
                    print(str(e))
            # elif event == '-ADD CLASS-':
            #     folder = value['-FOLDER-']
            #     try:
            #         file_list = os.listdir(folder)
            #     except Exception as e:
            #         print(str(e))
            #         file_list = []
            #     fnames = [
            #         f
            #         for f in file_list
            #         if os.path.isfile(os.path.join(folder, f))
            #         and f.lower().endswith((".png", ".jpg", ".jpeg"))
            #     ]
            #     F_classname = value["-CLASS TYPE-"]
            #     Class_path = os.path.join(r"Class", F_classname)
            #     isFolder = os.path.exists(Class_path)

            #     if isFolder == False:
            #         try:
            #             os.makedirs(Class_path)
            #             for i in fnames:
            #                 shutil.copy2(os.path.join(folder, i), os.path.join(
            #                     Class_path, i))
            #         except Exception as e:
            #             print(str(e))
            #         class_list.append(F_classname)
            #     elif isFolder == True:
            #         try:
            #             for i in fnames:
            #                 shutil.copy2(os.path.join(folder, i), os.path.join(
            #                     Class_path, i))
            #         except Exception as e:
            #             print(str(e))
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
            # elif event == "-FILE LIST-":
            #     try:
            #         filename = value["-FILE LIST-"][0]
            #         name, ext = os.path.splitext(filename)
            #         img = cv.imread(os.path.join(
            #             os.path.join(Class_path), filename))

            #         data = Image.fromarray(img)
            #         data.thumbnail((600, 300))
            #         bio = io.BytesIO()
            #         b, g, r = data.split()
            #         data = Image.merge("RGB", (r, g, b))
            #         data.save(bio, format="PNG")
            #         window_main['-IMAGE-'].update(data=bio.getvalue(),
            #                                       size=(600, 300))
            #     except Exception as e:
            #         print("error:"+str(e))
            # elif event == "-DEL IMG-":
            #     try:
            #         path_del = os.path.join(
            #             "Class", value["-CLASS LIST-"][0])
            #         os.remove(os.path.join(path_del, filename))
            #     except:
            #         pass
            #     file_list = os.listdir(path_del)
            #     fnames = [
            #         f
            #         for f in file_list
            #         if os.path.isfile(os.path.join(folder, f))
            #         and f.lower().endswith((".png", ".jpg", ".jpeg"))]
            #     window_main["-FILE LIST-"].update(fnames)
        except Exception as e:
            print(str(e))
            break
