from typing import Text
import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

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
        [sg.Text(size=(1,1))],    
        [sg.Button("Data Pre-Processing",font=("Helvetica", content_text), key="-PP1-",  tooltip="Topic1: description"),
         sg.Button("Model Training", font=("Helvetica", content_text),
                   key="-PP2-" , tooltip="Topic2: description"),
         sg.Button("Model Prediction", font=("Helvetica", content_text), key="-PP3-", tooltip="Topic3: description")],
 
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
            sg.Input(key='-CLASS TYPE-', enable_events=True, size=(70,20)),
            sg.Button("Add", key="-ADD CLASS-"),
        ],
        [
         sg.Listbox(values=["1.png","2.png","3.png"], enable_events=True,
                       size=(70, content_text), key="-FILE LIST-",select_mode='extended')
        ],
        [
            sg.Button("Delete", key="-DEL IMG-")
        ],
        [
            sg.Text("Class list")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(70,10), key="-CLASS LIST-")
        ],
         [sg.Column([[sg.Button("Back", key="-BACK-")]],element_justification='left'),sg.Text(size=(70,1)),sg.Column([[sg.Button("Next", key="-NEXT-")]],element_justification='right')],
    ]
    
    image_viewer_colum = [
        [sg.Text("choose an image from the list on the left")],
        [sg.Text(size=(70,1), key="-TOUT1-")],
        [sg.Image(key="-IMAGE1-",size=(70,500))],
        
          [sg.Text("1/299",key="-N IMG-",size=(70,1),justification="right")],
        
    ]

    Layout_InserDataset = [
        [sg.Text('Insert Data')],
        [sg.Column(file_list_colum,element_justification='left',key="-CL1-"), sg.VSeparator(),
        sg.Column(image_viewer_colum,element_justification='center',key="-CL2-")],
    ]

    resize_section = [[sg.Input('Input sec 1', key='-IN1-')],
                      # [sg.Input(key='-IN11-')],
                      # [sg.Button('Button section 1',  button_color='yellow on green'),
                      #  sg.Button('Button2 section 1', button_color='yellow on green'),
                      #  sg.Button('Button3 section 1', button_color='yellow on green')]
                      ]

    rotation_section = [[sg.Button('Left'), sg.Button('Right')]]

    bright_and_contrast_section = [
        [sg.Text('  brightness'), sg.Text('', key='-OUTPUT_B-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT1-'),
         sg.Slider((0, 100), key='-SLIDER_Bri-', orientation='h',
                   enable_events=True, disable_number_display=True),
         sg.T(' 100', size=(4, 1), key='-RIGHT1-')],
        [sg.Text('  contrast'), sg.Text('', key='-OUTPUT_C-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT2-'),
         sg.Slider((0, 100), key='-SLIDER_Con-', orientation='h',
                   enable_events=True, disable_number_display=True),
         sg.T(' 100', size=(4, 1), key='-RIGHT2-')]
    ]

    # '''Blur () [ Gaussian, Median, Blur ]'''
    blur_section = [
        [sg.Text('  Noise'), sg.Text('', key='-OUTPUT_N-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT3-'),
         sg.Slider((0, 100), key='-SLIDER_N-', orientation='h',
                   enable_events=True, disable_number_display=True,tooltip="description"),
         sg.T(' 100', size=(4, 1), key='-RIGHT3-')],

        [sg.Text('  Gaussian'), sg.Text('', key='-OUTPUT_G-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT4-'),
         sg.Slider((0, 100), key='-SLIDER_G-', orientation='h',
                   enable_events=True, disable_number_display=True,tooltip="description"),
         sg.T(' 100', size=(4, 1), key='-RIGHT4-')],

        [sg.Text('  Median'), sg.Text('', key='-OUTPUT_M-')],
        [sg.T(' 0', size=(4, 1), key='-LEFT5-'),
         sg.Slider((0, 100), key='-SLIDER_M-', orientation='h',
                   enable_events=True, disable_number_display=True,tooltip="description"),
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
                     sg.Tab('Feature Extraction', feature_extraction_tab2)]],size=(500,400))],
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
        [sg.Column(image_viewer_colum_pp,element_justification='left'),
         sg.VSeperator(), sg.Column(layout_tab,element_justification='right')],
        Code_generate.Layout,

    ]


class Model_tranning():
    def collapse(layout, key):
        return sg.pin(sg.Column(layout, key=key))

    model_1 = [
        [sg.Text("this is parameter model1")],
    ]
    model_2 = [
        [sg.Text("this is parameter model2")],
    ]
    model_3 = [
        [sg.Text("this is parameter model3")],
    ]
    model_4 = [
        [sg.Text("this is parameter model4")],
    ]
    model_5 = [
        [sg.Text("this is parameter model5")],
    ]
    list_model = [
        [
            sg.Text("Import CVS File"),
            sg.In(size=(300, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Data spilt : Test size "),
            sg.Input(key='-TEST SIZE-', enable_events=True, size=(300, 1)),
            # sg.Button("Add", key="-ADD TRAIN SIZE-"),
        ],
        [
            sg.Checkbox("Data Validation")
        ],
        [
            sg.Text("n split"),
            sg.Input(key='-N SPLIT-',enable_events=True,size=(30,1))
        ],
        [
            sg.Text("Select Model"), sg.InputCombo(('Linear Model', 'SVM', 'Nearest Neighbor ',
                                                   'Decision Trees', 'Neural network'), size=(300, 1)),
        ],
        [collapse(model_1, '-M1-')
         ],
        [collapse(model_2, '-M2-')
         ],
        [collapse(model_3, '-M3-')
         ],
        [collapse(model_4, '-M4-')
         ],
        [collapse(model_5, '-M5-')
         ],
        [
            sg.Text("Class list From Csv")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(300, 5), key="-CLASS LIST-")
        ],

    ]

    Layout = [
        [sg.Text('Mylayout')],
        [sg.Column(list_model)],
        [sg.Button("Back", key="-BACK-"),
         sg.Button("Train Model", key="-TRAIN-")],
        Code_generate.Layout,
    ]
    Frame_layout1 = [
        [sg.Text("confusion metrix", size=(80, 30), key="-TRAINM-")],
        [sg.Text("accuracy", key="-AC TRAIN-")],
    ]
    Frame_layout2 = [

        [sg.Text("confusion metrix", size=(80, 30), key="-TESTM-")],
        [sg.Text("accuracy", key="-AC TEST-")]

    ]
    train_column = [
        [sg.Frame('Train set', Frame_layout1, font='Any 12',size=(700,100))]
    ]

    test_column = [
        [sg.Frame('Test set', Frame_layout2, font='Any 12',size=(700,100))]


    ]
    Layout_Confusion_Matrix = [
        [sg.Text("Result", font=("Helvetica", head_text))],
        [sg.Text("Model Description"), sg.Text(key="-MD-")],
       [sg.Column(train_column,element_justification='left'), sg.Column(test_column,element_justification='right')],
        [sg.Button("Save Model", key="-SAVE MD-")]


    ]


class Prediction_Model():
    show_img = [
            [sg.Image(key="-PREDICT IMG-",size=(500,100))],
    ]
    result_layout = [

        [sg.Text("Result : Accuracy : Class prediction", size=(40, 10), key="-RESULT-")],
        [sg.Text("%", key="-AC TEST-")]

    ]
    
    brow_config = [
        [sg.Text("Image file"),
         sg.In(size=(25, 1), enable_events=True, key="-IMG FILE-"),
         sg.FilesBrowse()],
        [sg.Text("Pre-processing config"),
         sg.In(size=(25, 1), enable_events=True, key="-CONFIG FILE-"),
         sg.FileBrowse()],
        [sg.Text("Model File"),
         sg.In(size=(25, 1), enable_events=True, key="-MODEL FILE-"),
         sg.FileBrowse()],
        [sg.Button("Predict", key="-PREDICT-")],
        [sg.Text("File List")],
        [
            sg.Listbox(values=[], enable_events=True,
                       size=(40, content_text), key="-FILE LIST-")
        ],
        [sg.Frame('Result', result_layout, font='Any 12')]
    ]

    Layout = [
        [sg.Text("Model prediction",font=("Helvetica", head_text))],
        [sg.Column(show_img),sg.VSeperator(),sg.Column(brow_config)],
    ]


main = Main()
pp = DataPreprocess()
ML = Model_tranning()
PL = Prediction_Model()
window = sg.Window("AI.EXE", ML.Layout_Confusion_Matrix,resizable=True,finalize=True)
window.maximize()
window.TKroot.minsize(550,200)
# window['-CL1-'].expand(expand_x=True, expand_y=True)
# window['-CL2-'].expand(expand_x=True, expand_y=True)
# window['-PP1-'].expand(expand_x=True, expand_y=True)
# window['-PP2-'].expand(expand_x=True, expand_y=True)
# window['-PP3-'].expand(expand_x=True, expand_y=True)
while True:
    event, values = window.read()
    if event == "OK" or event == WIN_CLOSED:
        break

window.close()
