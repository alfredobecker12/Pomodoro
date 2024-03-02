from interfaces import *
from playsound import *


def running(time):
    """Recebe o tempo do ciclo em segundos e executa um loop de tempo até que encerre ou seja interrompido"""
    
    while True:
        """Loop para controlar os ciclos do pomodoro"""
        pomodoro_running_window = pomodoro_running_interface(time_formatter(time))
        
        for current_time in range(time-1, -1, -1):
            pomodoro_running_event, values = pomodoro_running_window.read(timeout=1000)

            if pomodoro_running_event == 'Pausar':
                pomodoro_running_window.close()
                stop_aux = stopped(current_time+1)
                
                if not stop_aux:
                    return 'Voltar'
                
                elif stop_aux == 'win_closed':
                    return 'win_closed'

                else:
                    pomodoro_running_window = pomodoro_running_interface(time_formatter(current_time))

            elif pomodoro_running_event == sg.WIN_CLOSED:
                pomodoro_running_window.close()
                return 'win_closed'
            
            pomodoro_running_window['timer'].update(time_formatter(current_time))
            pomodoro_running_window.refresh()

        playsound('./Sounds/bells2.wav')
        pomodoro_running_window.close()
        break_time_result = break_time()

        if break_time_result == False:
            pomodoro_running_window.close()
            return 'Voltar'
            
        elif break_time_result == 'win_closed':
            pomodoro_running_window.close()
            return 'win_closed'


def stopped(current_time):
    """Pausa a execução do ciclo e abre uma interface de pausa, guardando o tempo restante do ciclo e oferencendo opção de continuar ou sair"""
    pomodoro_stopped_window = pomodoro_stopped_interface(time_formatter(current_time))
    pomodoro_stopped_event, values = pomodoro_stopped_window.read()

    if pomodoro_stopped_event == 'Continuar':
        pomodoro_stopped_window.close()
        return True

    elif pomodoro_stopped_event == 'Voltar':
        pomodoro_stopped_window.close()
        return False

    elif pomodoro_stopped_event == sg.WIN_CLOSED:
        pomodoro_stopped_window.close()
        return 'win_closed'


def break_time():
    """Após o fim do ciclo, chama a função de breaktime. Ao final do intervalo, ocorre um aviso sonoro"""
    pomodoro_break_window = pomodoro_break_interface(time_formatter(300))

    for i in range(299, -1, -1):
        pomodoro_break_event, values = pomodoro_break_window.read(timeout=1000)

        if pomodoro_break_event == 'Voltar':
            pomodoro_break_window.close()
            return False

        elif pomodoro_break_event == sg.WIN_CLOSED:
            pomodoro_break_window.close()
            return 'win_closed'

        pomodoro_break_window['timer'].update(time_formatter(i))
        pomodoro_break_window.refresh()
    
    playsound('./Sounds/bells.wav')
    pomodoro_break_window.close()
    
    return


def time_formatter(time):
    """Recebe um valor representado em segundos de tipo inteiro e converte em uma string formatada 00:00 - minutos:segundos"""
    minutes = time // 60
    seconds = time - 60*minutes
    
    string_minutes = str(minutes)
    string_seconds = str(seconds)

    if len(string_minutes) == 1:
        string_minutes = '0' + string_minutes
    
    if len(string_seconds) == 1:
        string_seconds = '0' + string_seconds

    return string_minutes+':'+string_seconds


if __name__ == '__main__':
    running(5)
