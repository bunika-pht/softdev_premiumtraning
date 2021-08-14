
from typing import Text
import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'
ModelTrainingBarSlid = 50

head_text = 30
content_text = 10
sg.theme('Reddit')


class Code_generate():
    Layout = [
        [sg.Button("generate code", font=("Helvetica"))],
        [sg.Output( key='-CODE-')],
    ]


class MODEL_TRANING():

    def collapse(layout, key):
        return sg.pin(sg.Column(layout, key=key))

    MODEL_1 = [
        [sg.Text("this is parameter model1")],
    ]
    MODEL_2 = [
        [sg.Text("this is parameter model2")],
    ]
    MODEL_3 = [
        [sg.Text("this is parameter model3")],
    ]
    MODEL_4 = [
        [sg.Text("this is parameter model4")],
    ]
    MODEL_5 = [
        [sg.Text("this is parameter model5")],
    ]

    LIST_MODEL = [
        [
            sg.Text("Import CVS File"),
            sg.In(size=(ModelTrainingBarSlid, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Data spilt : Test size "),
            sg.Input(key='-TEST SIZE-', enable_events=True, size=(ModelTrainingBarSlid, 1)),
            # sg.Button("Add", key="-ADD TRAIN SIZE-"),
        ],
        [
            sg.Checkbox("Data Validation")
        ],
        [
            sg.Text("n split"),
            sg.Input(key='-N SPLIT-',enable_events=True,size=(ModelTrainingBarSlid,1))
        ],
        [
            sg.Text("Select Model"), sg.InputCombo(('Linear Model', 'SVM', 'Nearest Neighbor ',
                                                   'Decision Trees', 'Neural network'), size=(ModelTrainingBarSlid, 1)),
        ],
        [collapse(MODEL_1, '-M1-')
         ],
        [collapse(MODEL_2, '-M2-')
         ],
        [collapse(MODEL_3, '-M3-')
         ],
        [collapse(MODEL_4, '-M4-')
         ],
        [collapse(MODEL_5, '-M5-')
         ],
        [
            sg.Text("Class list From Csv")
        ],

        [
            sg.Listbox(values=[], enable_events=True,
                       size=(ModelTrainingBarSlid, 5), key="-CLASS LIST-")
        ],

    ]
    Frame_layout1 = [
        [sg.Text("confusion metrix", size=(70, 10), key="-TRAINM-")],
        [sg.Text("accuracy", key="-AC TRAIN-")],
    ]
    Frame_layout2 = [

        [sg.Text("confusion metrix", size=(70, 10), key="-TESTM-")],
        [sg.Text("accuracy", key="-AC TEST-")]

    ]
    TRAIN_COLUMN = [
        [sg.Frame('Train set', Frame_layout1, font='Any 12',size=(700,100))]
    ]

    TEST_COLUMN = [
        [sg.Frame('Test set', Frame_layout2, font='Any 12',size=(700,100))]
    ]


    PAGE_LAYOUT_MATRIX = [
        [sg.Text("Result", font=("Helvetica", head_text))],
        [sg.Text("Model Description"), sg.Text(key="-MD-")],
        [sg.Column([[sg.Column(TRAIN_COLUMN,element_justification='left'), sg.Column(TEST_COLUMN,element_justification='right')]],size=(2000,700),element_justification='center')],
        [sg.Button("Save Model", key="-SAVE MD-")]
    ]
    PAGE_LAYOUT_SELECT_MODEL = [
        [sg.Text('MAKE MODEL',font=("Helvetica", head_text))],
        [sg.Column(LIST_MODEL, key= '-TRAIN-')],
        [sg.Button("Back", key="-BACK-"),
         sg.Button("Train Model", key="-TRAIN-")],
        Code_generate.Layout,
    ]



class MODEL_PREDICTION():

    RESULT_LAYOUT = [
        [sg.Text("Result : Accuracy : Class prediction" , size=(40, 10), key="-RESULT-")],
        [sg.Text("%", key="-AC TEST-")]
    ]
    
    RESULT_LAYOUT1 = [
        [sg.Text("Result : Accuracy : Class prediction" , size=(40, 10), key="-RESULT1-")],
        [sg.Text("%", key="-AC TEST1-")]
    ]
    
    IMAGE_VIEW = [
            [sg.Text("View",font=("Helvetica", content_text))],
            [sg.Image(key="-PREDICT IMG-")],
    ]

    DATASET_CONFIG = [
        [sg.Text("Image file  "),
         sg.In(size=(30, 1), enable_events=True, key="-IMG FILE-"),
         sg.FilesBrowse()],

        [sg.Text("Data config"),
         sg.In(size=(30, 1), enable_events=True, key="-CONFIG FILE-"),
         sg.FileBrowse()],

        [sg.Text("Model file   "),
         sg.In(size=(30, 1), enable_events=True, key="-MODEL FILE-"),
         sg.FileBrowse()],

        [sg.Text("File List")],
        [sg.Listbox(values=[], enable_events=True, size=(50, content_text), key="-FILE LIST-")],
        [sg.Frame('Result', RESULT_LAYOUT, font='Any 12',size=(50,1))],
        [sg.Button("Predict", key="-PREDICT-", size=(50,1))],
    ]

    CAMERA_CONFIG =[
        [sg.Text('Camera'),sg.InputCombo(("USB CAMERA 3.0","Webcam"),size=(50,1))],
        [sg.Text("Data config"),
         sg.In(size=(30, 1), enable_events=True, key="-CONFIG FILE1-"),
         sg.FileBrowse()],
        [sg.Text("Model file   "),
         sg.In(size=(30, 1), enable_events=True, key="-MODEL FILE1-"),
         sg.FileBrowse()],
        [sg.Text("File List")],
        [sg.Listbox(values=[], enable_events=True,size=(50, content_text), key="-FILE LIST1-")],
        [sg.Frame('Result', RESULT_LAYOUT1, font='Any 12',size=(50,1))],
        [sg.Button("Predict", key="-PREDICT1-", size=(50,1))],
    ]

    DATA_IN_LAYOUT = [
        [sg.Column(DATASET_CONFIG)],
    ]

    CAMERA_IN_LAYOUT = [
        [sg.Column(CAMERA_CONFIG)],
    ]

    PAGE_LAYOUT = [
        [sg.Text("Model prediction",font=("Helvetica", head_text))],
        [sg.Column(IMAGE_VIEW,key='-TREE1-',size=(500,500),background_color='red'),
        [sg.Text()],
        sg.TabGroup([[  sg.Tab('Dataset Input', DATA_IN_LAYOUT,element_justification='right'),
                        sg.Tab('Camera Input', CAMERA_IN_LAYOUT,element_justification='right')]] ,
                        size=(400,700), key='-TREE-')],
        Code_generate.Layout,
    ]



# MLT = MODEL_TRANING()
# window_MLT = sg.Window("AI.EXE", MLT.PAGE_LAYOUT_SELECT_MODEL,resizable=True,finalize=True)
# window_MLT["-TRAIN-"].expand(True,True)
# window_MLT["-CODE-"].expand(True,True)


MLP = MODEL_PREDICTION()
window_MLP = sg.Window("AI.EXE", MLP.PAGE_LAYOUT,resizable=True,finalize=True)
window_MLP.bind('<Configure>', "Configure")
window_MLP["-TREE1-"].expand(True,True)
window_MLP["-CODE-"].expand(True,True)

while True:
    event, values = window_MLP.read()
    if event == sg.WINDOW_CLOSED:
        break
    # elif event == 'Configure':
    #     if window.TKroot.state() == 'zoomed':
    #         status.update(value='Window zoomed and maximized !')
    #     else:
    #         status.update(value='Window normal')

window_MLP.close()

# window.close()
# import PySimpleGUI as sg

# layout = [[sg.Text('Window normal', size=(30, 1), key='Status')]]
# window = sg.Window('Title', layout, resizable=True, finalize=True)
# window.bind('<Configure>', "Configure")
# status = window['Status']

# while True:

#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     elif event == 'Configure':
#         if window.TKroot.state() == 'zoomed':
#             status.update(value='Window zoomed and maximized !')
#         else:
#             status.update(value='Window normal')

# window.close()