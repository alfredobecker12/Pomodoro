import PySimpleGUI as sg

"""
abaixo, o layout define como será a janela em que esse será aplicado.
A estruturação das janelas se baseam em rows(linhas).
No layout acima, cada linha representa uma área horizontal da janela que será aberta.

Pelo motivo de sempre que as telas são fechadas elas precisam ser abertas novamente, são criadas dentro de uma função.
Dessa forma, é só criar a window toda vez que for usar no fluxo principal.
"""

def start_interface():
    start_layout = [[sg.Text('Pomodorão')],
                    [sg.Text('Login', size=(5,1)), sg.Input()],
                    [sg.Text('Senha', size=(5,1)), sg.Input(password_char='*')],
                    [sg.Submit(button_text='Entrar')],
                    [sg.Text('Esqueci a senha', enable_events=True, )],
                    [sg.Text('Cadastrar', enable_events=True)]]
    
    return sg.Window(title='First page', size=(500,200), element_justification='center', grab_anywhere=True, element_padding=(5,5), finalize=True,layout=start_layout)


def register_interface():
    register_layout = [[sg.Text('Cadastro')],
                       [sg.Text('Nome', pad=(20,0)), sg.Input()],
                       [sg.Text('Email', pad=(20,0)), sg.Input()],
                       [sg.Text('Username', pad=(7, 0)), sg.Input()],
                       [sg.Text('Senha', pad=(18,0)), sg.Input(password_char='*')],
                       [sg.Submit(button_text='Cadastrar')],
                       [sg.Submit(button_text='Voltar')]]

    return sg.Window(title='Register page', size=(600,250), element_justification='center', grab_anywhere=True, element_padding=(5,5), layout=register_layout)


def username_suggestion_interface(suggestions):
    suggestion_layout = [[sg.Text('Username já utilizado. Selecione uma das opções abaixo')],
                         [sg.Combo(suggestions)],
                         [sg.Submit(button_text='Ok')]]

    return sg.Window(title='Username suggestions page', size=(380,250), element_justification='center', grab_anywhere=True, element_padding=(5,30), layout=suggestion_layout)


def register_success_interface():
    success_registration_layout = [[sg.Text('A conta foi criada com sucesso!')],
                                   [sg.Submit(button_text='Voltar')]]

    return sg.Window(title='Success Registration page', size=(300,200), element_justification='center', grab_anywhere=True, element_padding=(5,25),layout=success_registration_layout)


def forgot_password_interface():
    forgot_pass_layout = [[sg.Text('Informe o username que uma mensagem será enviada ao email cadastrado.')],
                          [sg.Input(default_text='Email')],
                          [sg.Submit(button_text='Enviar')]]

    return sg.Window(title='Forgot pass page', size=(500,150), element_justification='center', grab_anywhere=True, element_padding=(5,5), layout=forgot_pass_layout)


def forgot_password_success_interface():
    success_forgot_pass_layout = [[sg.Text('Uma mensagem foi enviada ao email registrado!')],
                                  [sg.Submit(button_text='Voltar')]]

    return sg.Window(title='Success forgot pass page', size=(300,200), element_justification='center', grab_anywhere=True, element_padding=(5,25), layout=success_forgot_pass_layout)


def menu_interface():
    menu_layout = [[sg.Submit(button_text=('Pomodoro'), size=(10,3))],
                   [sg.Submit(button_text='Sair', size=(5,2))]]

    return sg.Window(title='Menu page', size=(250,200), element_justification='center', grab_anywhere=True, element_padding=(5,20), layout=menu_layout)


def pomodoro_menu_interface():
    pomodoro_menu_layout = [[sg.Input(default_text='Tempo em minutos (mínimo 1)')], 
                            [sg.Submit(button_text='Iniciar')],
                            [sg.Submit(button_text='Sair')]]

    return sg.Window(title='Pomodoro menu page', size=(300, 200), element_justification='center', grab_anywhere=True, element_padding=(5,20), layout=pomodoro_menu_layout)


def pomodoro_running_interface(time):
    pomodoro_running_layout = [[sg.Text(time, text_color='black', background_color='light blue', key='timer')],
                               [sg.Submit(button_text='Pausar')]]

    return sg.Window(title='Pomodoro running page', size=(350, 250), element_justification='center', grab_anywhere=True, element_padding=(5,30), background_color='light blue', finalize=True, layout=pomodoro_running_layout)


def pomodoro_stopped_interface(time):
    pomodoro_stoped_layout = [[sg.Text(time, text_color='black', background_color='tomato')],
                              [sg.Submit(button_text='Continuar'), sg.Submit(button_text='Voltar')]]

    return sg.Window(title='Pomodoro stopped page', size=(350, 250), element_justification='center', grab_anywhere=True, element_padding=(5,30), background_color='tomato',layout=pomodoro_stoped_layout)


def pomodoro_break_interface(time):
    pomodo_break_layout = [[sg.Text(time, text_color='black', background_color='light green', key='timer')],
                           [sg.Submit(button_text='Voltar')]]

    return sg.Window(title='Pomodoro break page', size=(350,250), element_justification='center', grab_anywhere=True, element_padding=(5,30), background_color='light green', layout=pomodo_break_layout)


if __name__=='__main__':
    register = username_suggestion(['dfdd', 'ddd', 'sair'])
    
    event, values = register.read()
    print(event)
    print(values)
