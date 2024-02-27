# Verificar imports


"""
while True:
    event, values = start_window.read()
    if event == sg.WIN_CLOSED:
        start_window.close()  
        break
    elif event == 'Entrar':
        start_window.close()
        break

while True:
    event, values = register_window.read()
    if event == sg.WIN_CLOSED:
        register_window.close()
        break
    elif event == 'Voltar':
        register_window.close()
        break
    elif event == 'Cadastrar':
        register_window.close()
        break

while True:
    event, values = success_registration_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Voltar':
        success_registration_window.close()
        break
        
while True:
    event, values = forgot_pass_window.read()
    if event == sg.WIN_CLOSED:
        forgot_pass_window.close()
        break
    elif event == 'Enviar':
        forgot_pass_window.close()
        break 

while True:
    event, values = success_forgot_pass_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Voltar':
        success_forgot_pass_window.close()
        break 

while True:
    event, values = menu_window.read()
    if event == sg.WIN_CLOSED:
        menu_window.close()
        break
    elif event == 'Pomodoro':
        menu_window.close()
        break 
    elif event == 'Sair':
        menu_window.close()        

while True:
    event, values = pomodoro_menu_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Iniciar':
        pomodoro_menu_window.close()
        break 
    elif event == 'Sair':
        pomodoro_menu_window.close()
        break        

while True:
    event, values = pomodoro_stoped_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Parar':
        pomodoro_stoped_window.close()
        break 
    elif event == 'Pausar':
        pomodoro_stoped_window.close()
        break        

A variável event captura a ação de apertar algum botão. O botão de submit(), por não ter uma chave específica, retorna sue texto, que nesse caso é 'Entrar'.
A variável values captura os dados de input em um dicionário.  
"""

