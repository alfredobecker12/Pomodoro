from interfaces import *
from playsound import playsound


def running(time):
    """Recebe o tempo do ciclo em segundos e executa um loop de tempo até que encerre ou seja interrompido"""
    
    while True:
        """Loop para controlar os ciclos do pomodoro"""
        pomodoro_running = pomodoro_running_interface(time_formatter(time))
        
        for current_time in range(time-1, -1, -1):
            pomodoro_running_event, values = pomodoro_running.read(timeout=1000)

            if pomodoro_running_event == 'Pausar':
                pomodoro_running.close()
                stop_aux = stopped(current_time+1)
                
                if not stop_aux:
                    return 'Voltar'

                else:
                    pomodoro_running = pomodoro_running_interface(time_formatter(current_time))

            elif pomodoro_running_event == sg.WIN_CLOSED:
                pomodoro_running.close()
                return 'win_closed'
            
            pomodoro_running['timer'].update(time_formatter(current_time))
            pomodoro_running.refresh()

        pomodoro_running.close()
        break_time()


def stopped(current_time):
    """Pausa a execução do ciclo e abre uma interface de pausa, guardando o tempo restante do ciclo e oferencendo opção de continuar ou sair"""
    pomodoro_stopped = pomodoro_stopped_interface(time_formatter(current_time))
    pomodoro_stopped_event, values = pomodoro_stopped.read()

    if pomodoro_stopped_event == 'Continuar':
        pomodoro_stopped.close()
        return True

    elif pomodoro_stopped_event == 'Voltar':
        pomodoro_stopped.close()
        return False


def break_time():
    """Após o fim do ciclo, chama a função de breaktime. Ao final do intervalo, ocorre um aviso sonoro"""
    pomodoro_break = pomodoro_break_interface(time_formatter(300))
    for i in range(5, -1, -1):
        pomodoro_break_event, values = pomodoro_break.read(timeout=1000)

        if pomodoro_break_event == 'Voltar':
            pomodoro_break.close()
            return False

        elif pomodoro_break_event == sg.WIN_CLOSED:
            pomodoro_break.close()
            return False

        pomodoro_break['timer'].update(time_formatter(i))
        pomodoro_break.refresh()
    
    playsound('C:\\Users\\Alfredo\\Desktop\\Nerdice\\Git\\Pomodoro\\Sounds\\bell.wav')
    pomodoro_break.close()


def time_formatter(time):
    """Recebe um valor representado em segundos de tipo inteiro e converte em uma string formatada 00:00 - minutos:segundos"""
    minutes = time//60
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

