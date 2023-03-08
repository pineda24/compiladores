# Importaciones
import ply.lex as lex

# Definición de tokens
tokens = ['LENG_1', 'LENG_2', 'OTRO']

t_LENG_1 = r'1(0|1)+11'
t_LENG_2 = r'11(1|0)*1'
t_OTRO = r'.'

# Función para manejar errores
def t_error(t):
    print('Error')

# Función para manejar el lexer
def lexer(cadena):
    aceptador = lex.lex()
    aceptador.input(cadena)
    el_token = aceptador.token()
    if el_token.type == 'LENG_1' or el_token.type == 'LENG_2':
        return 'Cadena aceptada'
    else:
        return 'Cadena rechazada'
