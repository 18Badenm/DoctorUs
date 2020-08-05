TITLE = "DoctorUS"

START_TEXT = "Hola a tod@s! Bienvenid@s a DoctorUS \n\n" \
             "Este bot entregará un riesgo de tener COVID19 \n" \
             "y los pasos a seguir \n" \
             "\n" \
             "Por favor ingrese los datos que se pediran \n" \
             "para crear su perfil \n" \
             "\n" \
             "Siga las instrucciones \n"
#removed the newlines so speech can be better
START_TEXT_AUDIO = "Hola a tod@s! Bienvenid@s a DoctorUS "\
             "Este bot entregará un riesgo de tener COVID19 " \
             "y los pasos a seguir " \
             "" \
             "Por favor ingrese los datos que se pediran " \
             "para crear su perfil " \
             "" \
             "Siga las instrucciones "
			 
LEGAL_INFO = "Por favor leer y firmar si está de acuerdo\n" \
             "...\n...\n...\n" \
             "¿Está de acuerdo? "
LEGAL_INFO_AUDIO = "Por favor leer y firmar si está de acuerdo" \
             "¿Está de acuerdo? "
# User info
name = 'Nombre'
age = 'Edad'
rut = 'Rut'
legal_state = 'Estado civil'
sex = 'Sexo'
commune = 'Comuna'
medical_insurance = 'Previsión de salud'
salary = 'Ingreso familiar'
n_team_members = 'Numero integrantes en grupo familiar'
job = 'Area trabajo'
job_type = 'Tipo contrato'
job_state = 'Estado laboral'

# Questions to get user info
dict_info_questions = {name: "Ingrese su nombre ",      #string
                       age: "Ingrese su edad ",         #number
                       rut: "Ingrese su rut ",          #string
                       legal_state: "¿Cuál es su estado civil? ", #string
                       sex: "Ingrese su sexo",          #charachter (F)
                       commune: "Ingrese su comuna ",   #string
                       medical_insurance: "¿Cual es su prevision? ", #string
                       salary: "¿Cual es su ingreso familiar ? ", #number
                       n_team_members: "¿N° integrantes en grupo familiar ? ", #number
                       job: "¿En que área trabaja ? ", #string
                       job_type: "¿Tiene contrato ? ",  #string
                       job_state: "¿Cuál es su estado laboral ? "} #string
list_info_questions = ["Ingrese su nombre ",
                       "Ingrese su edad ",
                       "Ingrese su rut ",
                       "¿Cuál es su estado civil? ",
                       "Ingrese su sexo",
                       "Ingrese su comuna ",
                       "¿Cual es su prevision? ",
                       "¿Cual es su ingreso familiar ? ",
                       "¿N° integrantes en grupo familiar ? ",
                       "¿En que área trabaja ? ",
                       "¿Tiene contrato ? ",
                       "¿Cuál es su estado laboral ? "]