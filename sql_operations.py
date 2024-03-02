from db_connection import *


def create_user(nome, email, username, password):
    """Insere os dados do usuários nas tabelas users e userslogin. Dessa forma, cadastra o usuário no sistema."""
    try:
        
        with conn:
            
            with conn.cursor() as creator_curs:
                sql_query = 'INSERT INTO users(nome, email) VALUES(%s, %s)'
                creator_curs.execute(sql_query, (nome, email))
                """Primeiramente, cria esse registro e a primary key ID"""

                sql_query = 'SELECT id FROM users WHERE nome=%s'
                creator_curs.execute(sql_query, (nome,))
                aux = creator_curs.fetchone() # Retorna o resultado do último execute em forma de tuple
                """Procura o id do usuário criado na tabela users para usar na tabela userslogin"""

                sql_query = 'INSERT INTO userslogin(id, username, password) VALUES(%s, %s, %s)'
                creator_curs.execute(sql_query, (aux, username, password))
                """Finalmente, cria o login preenchendo o id_fk com o mesmo valor do id_pk"""

    except Exception as error:
        print('Erro: ', error)        


def check_user(user):
    """Verifica se o usuário em questão está registrado no sistema. Dependendo do caso, retorna um boolean."""
    try:
        
        with conn:
            
            with conn.cursor() as checker_curs:
                sql_query = 'SELECT username FROM userslogin WHERE username=%s'
                checker_curs.execute(sql_query, (user,))
                
                if checker_curs.fetchone() is None:
                    """Usuário não registrado"""
                    return False
                
                else:
                    """Usuário registrado"""
                    return True
    
    except Exception as error:
        print('Erro: ', error)
    

def check_Login(username, password):
    """Verifica as credenciais informadas no banco de dados. Retorna boolean indicando se estão contidas o não."""
    try:
        
        with conn:
            
            with conn.cursor() as login_checker_curs:
                sql_query = 'SELECT id FROM userslogin WHERE username=%s'
                login_checker_curs.execute(sql_query, (username,))
                user_id = login_checker_curs.fetchone()
                
                if user_id == None:
                    """Usuário não cadastrado."""
                    return False
                
                sql_query = 'SELECT password FROM userslogin WHERE id=%s'
                login_checker_curs.execute(sql_query,(user_id,))
                if password != login_checker_curs.fetchone()[0]: # Especificado índice para poder comparar string - string e não string - tuple
                
                    """Usuário encontrado, porém senha incorreta."""   
                    return False
                
                return True

    except Exception as error:
        print(f"SQL error: {error}")


def get_email(username):
    """Busca o email cadastrado no username informado. Pertinente para o envio de mensagem de pseudo-recuperação de senha."""
    try:

        with conn:
            
            with conn.cursor() as email_curs:
                sql_query = 'SELECT email FROM users WHERE id=(SELECT id FROM userslogin WHERE username=%s)'
                email_curs.execute(sql_query, (username,))
                email = email_curs.fetchone()[0]

                if email == None:
                    """Verifica se o email foi encontrado."""
                    return 
                
                else:
                    return email

    except Exception as error:
        print('Erro: ', error)


if __name__ == '__main__':
    get_email('windowsvista60')
    