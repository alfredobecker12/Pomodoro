from sql_operations import check_user
from random import randrange
from interfaces import *

def password_check(password):
    """Recebe uma string representando uma senha. A partir disso, verifica se possui alguns requisitos de segurança"""
    special_chars = ['!','@','#','$','&','*','(',')','-','_','+','/',';',':','.',',','?','+','=']
    upper = False
    alpha = False
    num = False
    special = False
    
    if (20 >= len(password) >= 8):
        
        for iterator in password:
            
            if iterator.isdigit():
                num = True
            
            elif iterator.isupper():
                upper = True
                alpha = True
            
            elif iterator.isalpha():
                alpha = True
            
            elif iterator in special_chars:
                special = True
        
        if upper and alpha and num and special:
            return True
        
        else:
            return False
    else:
        sg.popup('A senha deve conter de 8 a 20 caracteres e ter um especial, um numérico e um maiúsculo.')
        return False


def user_check(username):
    """Recebe uma string representando um username. Verifica se já está contido no banco de dados e apresenta variações caso esteja"""
    if len(username) < 6:
            sg.popup('O nome deve ser maior que 6 caracteres.')
            return False

    if check_user(username):
        suggestions = []
        
        while len(suggestions) != 3:
            suggestion = username + str(randrange(10, 1000))
            
            if not check_user(suggestion):
                suggestions.append(suggestion)
        suggestions.append('Nenhum')

        username_suggestion_window = username_suggestion_interface(suggestions)
        username_suggestion_event, values = username_suggestion_window.read()

        if username_suggestion_event == 'Ok':
            if values[0] == suggestions[3]:
                username_suggestion_window.close()
                return False
            
            else:
                username_suggestion_window.close()
                return values[0]

        elif username_suggestion_event == sg.WIN_CLOSED:
            username_suggestion_window.close()
            return False

    else:
        return True
    
if __name__ == '__main__':
    pass