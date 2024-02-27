from pomodoro_mechanic import *
from sql_operations import *
from register_functions import *


control = True
while control:
    """Controla o programa (True=rodando/False=finaliza)."""
    while True:
        start_window = start_interface() #Cria a interface
        start_window_event, values = start_window.read()
        
        if start_window_event == 'Entrar':
            
            if check_Login(values[0], values[1]):
                """Verifica se as credenciais batem com alguma no banco de dados"""
                start_window.close() # Fecha a interface 
                menu_window = menu_interface() #Cria a interface 
                menu_window_event, values = menu_window.read()
                
                if menu_window_event == sg.WIN_CLOSED: #Finaliza o programa
                    menu_window.close()   
                    control = False
                    break
                
                elif menu_window_event == 'Sair':
                    menu_window.close()
                
                elif menu_window_event == 'Pomodoro':
                    menu_window.close()

                    while control:
                        pomodoro_menu_window = pomodoro_menu_interface() #Cria a interface
                        pomodoro_window_event, values = pomodoro_menu_window.read()
                        
                        if pomodoro_window_event == 'Iniciar':
                            
                            if values[0] is None or not values[0].isnumeric() or int(values[0]) < 1 or int(values[0]) > 60:
                                sg.popup('Insira o tempo de ciclo em segundos (mín: 1 / máx: 60)')
                                pomodoro_menu_window.close()

                            else:
                                time = int(values[0]) * 60 # Tempo em segundos
                                pomodoro_menu_window.close()
                                
                                while True:
                                    running_event = running(time)
                                    
                                    if running_event == 'win_closed':
                                        control = False
                                        break
                                    
                                    elif running_event == 'Voltar':
                                        break

                        elif pomodoro_window_event == 'Sair':
                            pomodoro_menu_window.close()
                            break

                        elif pomodoro_window_event == sg.WIN_CLOSED:
                            pomodoro_menu_window.close()
                            control = False

                        if control == False:
                            break

            else:
                sg.popup('Credenciais incorretas. Tente novamente.')
                start_window.close() # Fecha a interface 

        elif start_window_event == 'Esqueci a senha':
            start_window.close() # Fecha a interface
            
            forgot_pass_window = forgot_password_interface() #Cria a interface
            forgot_password_event, values = forgot_pass_window.read()

        elif start_window_event == 'Cadastrar':
            start_window.close() # Fecha a interface 

            while True:
                register_success_window = register_success_interface()
                register_window = register_interface()
                register_window_event, values = register_window.read()


                if register_window_event == 'Cadastrar':
                    register_window.close()
                    user_check_result = user_check(values[2])

                    if user_check_result:
                        
                        if password_check(values[3]):
                            create_user(values[0], values[1], values[2], values[3])
                            register_window.close()

                        else:
                            sg.popup('A senha informada não atende os padrões de segurança.')
                            register_window.close()
                            continue

                    elif not user_check_result:
                        register_window.close()
                        continue

                    else:
                        
                        if password_check(values[3]):
                            create_user(values[0], values[1], user_check_result, values[3])
                            register_window.close()

                        else:
                            register_window.close()
                            continue
                    
                    register_success_event, values = register_success_window.read()
                    
                    if register_success_event == 'Voltar' or register_success_event == sg.WIN_CLOSED:
                        register_success_window.close()
                        break
                
                elif register_window_event == 'Voltar':
                    register_window.close()
                    break
                
                elif register_window_event == sg.WIN_CLOSED: #Finaliza o programa
                    control = False # Define o fim do loop principal
                    break

        elif start_window_event == sg.WIN_CLOSED: #Finaliza o programa
            control = False # Define o fim do loop principal
            break
        
        if control == False:
            break

if __name__ == '__main__':
    pass
    