
from . import start_conversation_text
from Sound import speechfile
import PySimpleGUI as sg
from Utils import conversation


class DoctorUsView:

    def __init__(self, controller):
        self.init_program = self.hello_world()
        self.controller = controller

    def hello_world(self):
        
        speechfile.speak(start_conversation_text.START_TEXT_AUDIO)
        event = sg.popup_ok_cancel(start_conversation_text.START_TEXT, title='Doctor US')
        #sg.Popup('clickit', keep_on_top=True)
        if event == 'Cancel':   #quit if exit button
              return False
        elif event == 'OK':
            return True
        
    # Ask for legal conditions
    def accept_legal_info(self):
        speechfile.speak(start_conversation_text.LEGAL_INFO_AUDIO)
        event = sg.popup_scrolled(start_conversation_text.LEGAL_INFO, yes_no=True, title=start_conversation_text.TITLE)
        if event == 'No':  # quit if exit button
            return False
        elif event == 'Yes':
            return True

    # Ask questions in dict_questions. Return answers as a dict of text
    def ask_user_profile(self):
        def audiospeak(number):
            speechfile.speak(start_conversation_text.list_info_questions[number])
			
        layout = []
        i = 0
        for k, v in start_conversation_text.dict_info_questions.items():
            button_name = "Audio" + str(i)
            i += 1
            format_ = [sg.Text(v, size=(25, 1)),
                       sg.InputText(key=k, size=(30, 1)),sg.Button(button_name, bind_return_key=True)]
            layout.append(format_)
        layout.append([sg.Button('ENVIAR', bind_return_key=True),
                       sg.Button('SALIR')])
        window = sg.Window(title='Antecedentes', layout=layout)
        ans = True
        while ans == True:
            event, values = window.read()
            if event == 'SALIR':  # quit if exit button
                ans = False 
                window.close()
                raise Exception
            if event == 'Audio0':
                audiospeak(0)
            if event == 'Audio1':
                audiospeak(1)
            if event == 'Audio2':
                audiospeak(2)
            if event == 'Audio3':
                audiospeak(3)
            if event == 'Audio4':
                audiospeak(4)
            if event == 'Audio5':
                audiospeak(5)
            if event == 'Audio6':
                audiospeak(6)
            if event == 'Audio7':
                audiospeak(7)
            if event == 'Audio8':
                audiospeak(8)
            if event == 'Audio9':
                audiospeak(9)
            if event == 'Audio10':
                audiospeak(10)
            if event == 'Audio11':
                audiospeak(11)
            elif event == 'ENVIAR':
                ans = False
                print(self.controller.save_user_profile(values))
                print(values)
                window.close()
                self.controller.save_user_profile(values)
                print("here")
                
                
    # TODO : hacerlo bonito. Ver como evitar que bloquee la terminal al usar Output, probar logging
    def chatbox(self, age, sex):
        print("Are we here")
        sg.theme('Dark Blue 3')
        layout = [[sg.Text('DoctorUs dice', size=(20, 1))],
                  [sg.Output(size=(70, 20), font=('Helvetica 12'), key='-OUTPUT', )],
                  [sg.Multiline("Presiona PARTIR para empezar", size=(20, 2), font=('Helvetica 10'), key='-IN-',
                                do_not_clear=False, enter_submits=True),
                   sg.Button('PARTIR', bind_return_key=True),
                   sg.Button('LIMPIAR'),
                   sg.Button('SALIR')]]

        window = sg.Window('DoctorUs Chatbot', layout, font=('Helvetica', ' 13'), default_button_element_size=(8, 2))

        event, value = window.read()
        if event == 'SALIR':
            raise NotImplementedError("EXIT PROGRAM")
        elif event == 'LIMPIAR':
            window['-OUTPUT-'].update('')
        elif event == 'PARTIR':
            window['-IN-'].update('')
            try:
                evidence, diagnoses, triage = conversation.conduct_interview_gui(evidence=[], age=age, sex=sex,
                                                                                 windows=window)
                self.controller.save_user_diagnosis(evidence, diagnoses, triage)

            except NotImplementedError:
                raise NotImplementedError("EXIT PROGRAM")
            except Exception as err:
                raise err
            finally:
                window.close()

    #TODO: Doesnt Working
    def show_summary(self, evidence, diagnoses, triage):
        layout = []
        # List of evidences
        if evidence:
            layout.append([sg.Text("Evidencia")])
            cont = 0
            for ev in (evidence):
                if ev['choice_id'] == 'present':
                    output = [sg.Text(f'{cont + 1}. '), sg.Text(ev['name'])]
                    layout.append(output)
                    cont +=1
        if triage:
            layout.append([sg.Text("Resumen"), sg.Text(triage['description'])])
            layout.append([sg.Text("Recomendacion "), sg.Text(triage['label'])])

        window = sg.Window('Resultados', layout, font=('Helvetica', ' 13'), default_button_element_size=(8, 2))

        event, value = window.read()
        if event == 'OK':
            window.close()
