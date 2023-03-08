import ply.lex as lex

tokens = ['LENG_1', 'LENG_2', 'OTRO']

t_LENG_1 = r'1(0|1)+11'
t_LENG_2 = r'11(1|0)*1'
t_OTRO = r'.'

def t_error(t):
    print('Error')

def main():
    aceptador = lex.lex()
    cadena = input('Dame una cadena:')
    aceptador.input(cadena)
    el_token = aceptador.token()
    if el_token.type == 'LENG_1' or el_token.type == 'LENG_2':
        print('Cadena aceptada')
    else:
        print('Cadena rechazada')

if __name__ == '__main__':
	main()