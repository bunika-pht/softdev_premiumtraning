
import PySimpleGUI as sg
import os
import glob
import fnmatch
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import cv2 as cv
SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'


head_text = 30
content_text = 15
sg.theme('Reddit')

''' https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-collapsible-sections-visible-invisible-elements'''


class Code_generate():
    Layout = [
        [sg.Button("generate code", font=("Helvetica"))],
        [sg.Output(size=(600, 10), key='-CODE-')]
    ]


class Main():
    Layout = [
        [sg.Text("AI Premium Training", auto_size_text=True,
                 font=("Helvetica", head_text),)],
        [sg.Text(size=(1, 1))],
        [sg.Button("Data Pre-Processing", font=("Helvetica", content_text), key="-PREP-",  tooltip="Topic1: description"),
         sg.Button("Model Training", font=("Helvetica", content_text),
                   key="-TRAINING-", tooltip="Topic2: description"),
         sg.Button("Model Prediction", font=("Helvetica", content_text), key="-PREDICT-", tooltip="Topic3: description")],

    ]


class DataPreprocess():

    def collapse(layout, key):
        return sg.pin(sg.Column(layout, key=key))

    file_list_colum = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(70, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),

        ],
        [
            sg.Text("Class       "),
            sg.Input(key='-CLASS TYPE-', enable_events=True, size=(70, 20)),
            sg.Button("Add", key="-ADD CLASS-"),
        ],
        [
            sg.Listbox(values=[], enable_events=True,
                       size=(70, content_text), key="-FILE LIST-")
        ],
        [
            sg.Button("Delete", key="-DEL IMG-")
        ],
        [
            sg.Text("Class list")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(70, 10), key="-CLASS LIST-")
        ],
        [sg.Column([[sg.Button("Back", key="-BACK-")]], element_justification='left'), sg.Text(
            size=(70, 1)), sg.Column([[sg.Button("Next", key="-NEXT-")]], element_justification='right')],
    ]

    image_viewer_colum = [
        [sg.Text("choose an image from the list on the left")],
        [sg.Text(size=(70, 1), key="-IMG NAME-")],
        [sg.Image(key="-IMAGE1-", size=(70, 500))],

        [sg.Text("1/299", key="-N IMG-", size=(70, 1), justification="right")],

    ]

    Layout_InserDataset = [
        [sg.Text('Insert Data')],
        [sg.Column(file_list_colum, element_justification='left', key="-CL1-"), sg.VSeparator(),
         sg.Column(image_viewer_colum, element_justification='center', key="-CL2-")],
    ]

    resize_section = [[sg.Input('width', key='-IN WIDTH-', size=(10, 1)), sg.Input('high', key='-IN HIGH-', size=(10, 1))]

                      ]

    rotation_section = [
        [sg.Button('Left', key='-TL-'), sg.Button('Right', key='-TR-')]]

    bright_and_contrast_section = [
        [sg.Text('  brightness'), sg.Text('', key='-TEXT BRIGHT-')],
        [sg.T(' 0', size=(4, 1), key='-MIN BRIGHT-'),
         sg.Slider((0, 100), key='-SLIDER BRIGHT-', orientation='h',
                   enable_events=True, disable_number_display=True),
         sg.T(' 100', size=(4, 1), key='-MAX BRIGHT-')],
        [sg.Text('  contrast'), sg.Text('', key='-TEXT CONTRAST')],
        [sg.T(' 0', size=(4, 1), key='-MIN CONTRAST-'),
         sg.Slider((0, 100), key='-SLIDER CONTRAST-', orientation='h',
                   enable_events=True, disable_number_display=True),
         sg.T(' 100', size=(4, 1), key='-MAX CONTRAST-')]
    ]

    # '''Blur () [ Gaussian, Median, Blur ]'''
    blur_section = [
        [sg.Text('  Noise'), sg.Text('', key='-OUTPUT_N-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT3-'),
         sg.Slider((0, 100), key='-SLIDER_N-', orientation='h',
                   enable_events=True, disable_number_display=True, tooltip="description"),
         sg.T(' 100', size=(4, 1), key='-RIGHT3-')],

        [sg.Text('  Gaussian'), sg.Text('', key='-OUTPUT_G-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT4-'),
         sg.Slider((0, 100), key='-SLIDER_G-', orientation='h',
                   enable_events=True, disable_number_display=True, tooltip="description"),
         sg.T(' 100', size=(4, 1), key='-RIGHT4-')],

        [sg.Text('  Median'), sg.Text('', key='-OUTPUT_M-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT5-'),
         sg.Slider((0, 100), key='-SLIDER_M-', orientation='h',
                   enable_events=True, disable_number_display=True, tooltip="description"),
         sg.T(' 100', size=(4, 1), key='-RIGHT5-')],
    ]

    section_column_tab1 = [
        #### Section 1 part ####
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='black'),
         sg.T('Resize', enable_events=True, text_color='black', k='-OPEN SEC1-TEXT')],
        [collapse(resize_section, '-SEC1-')],
        #### Section 2 part ####
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='black'),
         sg.T('Rotaion', enable_events=True, text_color='black', k='-OPEN SEC2-TEXT')],
        [collapse(rotation_section, '-SEC2-')],
        #### Section 3 part ####
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC3-', text_color='black'),
         sg.T('Brightness and Contrast', enable_events=True, text_color='black', k='-OPEN SEC3-TEXT')],
        [collapse(bright_and_contrast_section, '-SEC3-')],
        #### Section 4 part ####
        [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC4-', text_color='black'),
         sg.T('Blur', enable_events=True, text_color='black', k='-OPEN SEC4-TEXT')],
        [collapse(blur_section, '-SEC4-')],
    ]

    feature_extraction_tab2 = [
        [sg.T("Edge Detection ()")],
        [sg.T("Thresholding()")],
        [sg.T("Gray Scale ()")],
    ]
    layout_tab = [
        [sg.TabGroup([[sg.Tab('Pre-process', section_column_tab1),
                     sg.Tab('Feature Extraction', feature_extraction_tab2)]], size=(500, 400))],
        [sg.Button("Export CSV", key="-CSV-")],
    ]

    image_viewer_colum_pp = [
        [sg.Image(key="-IMAGE-", size=(100, 300))],
        [
            sg.Listbox(values=[], enable_events=True,
                       size=(100, 5), key="-FILE LIST-")
        ],
    ]
    Layout_Data_Preprocess = [
        [sg.Text("Data Preprocessing")],
        [sg.Column(image_viewer_colum_pp, element_justification='left'),
         sg.VSeperator(), sg.Column(layout_tab, element_justification='right')],
        Code_generate.Layout,

    ]


# if __name__ == main:
#     try:
#         pass
#     except:
#         pass
# while True:
#     # * menu page
#     event1, values1 = window_main.read()
#     if event1 == WIN_CLOSED:
#         break
#     elif event1 == '-PREP-' and not window_insert_active:
#         window_insert_active = True
#         window_main.Hide()
#         window_insert_data = sg.Window(
#             "AI.EXE", pp.Layout_InserDataset, resizable=True, finalize=True)
#         window_prep_active = False
#         while True:
#             # * insert data page
#             event2, values2 = window_insert_data.Read()
#             if event2 == sg.WIN_CLOSED:
#                 window_insert_active = False
#                 break
#             elif event2 == '-FOLDER-':
#                 folder = values2['-FOLDER-']
#                 try:
#                     # ? Get list of files in folder
#                     file_list = os.listdir(folder)
#                 except:
#                     file_list = []
#                 fnames = [
#                     f
#                     for f in file_list
#                     if os.path.isfile(os.path.join(folder, f))
#                     and f.lower().endswith((".png", ".jpg", ".jpeg"))
#                 ]
#                 window_insert_data['-FILE LIST-'].update(fnames)
#             elif event2 == "-FILE LIST-":  # A file was chosen from the listbox
#                 try:
#                     filename = os.path.join(
#                         values2["-FOLDER-"], values2["-FILE LIST-"][0])
#                     window_insert_data["-TOUT1-"].update(filename)
#                     window_insert_data["-IMAGE1-"].update(filename=filename)
#                 except:
#                     pass
#             elif event2 == "-DEL IMG-":
#                 try:
#                     os.remove(filename)
#                 except:
#                     pass
#                 file_list = os.listdir(folder)
#                 fnames = [
#                     f
#                     for f in file_list
#                     if os.path.isfile(os.path.join(folder, f))
#                     and f.lower().endswith((".png", ".jpg", ".jpeg"))]
#                 window_insert_data["-FILE LIST-"].update(fnames)

#             elif event2 == '-NEXT-' and not window_prep_active:
#                 window_insert_active = False
#                 window_prep_active = True
#                 window_insert_data.Hide()
#                 window_prep = sg.Window(
#                     "AI.EXE", pp.Layout_Data_Preprocess, resizable=True, finalize=True)
#                 while True:
#                     # * pre-sprocess page
#                     event3, values3 = window_prep.read()
#                     window_prep['-FILE LIST-'].update(fnames)

#                     if event3 == sg.WIN_CLOSED:
#                         window_prep_active = False
#                         break
#                     elif event3 == "-FILE LIST-":  # A file was chosen from the listbox
#                         try:
#                             filename = os.path.join(
#                                 values2["-FOLDER-"], values3["-FILE LIST-"][0])
#                             window_prep["-IMAGE-"].update(
#                                 filename=filename, size=(500, 300))
#                         except:
#                             pass
