import ply.lex as lex


t_WORD = r'[A-Z][a-z]+'
t_NUMBER = r'[0-9]+'

def t_SPACE(t):
    r'\s+'
    pass

def t_error(t):
    print("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)

tokens = ('WORD',
          'NUMBER')

lexer = lex.lex()
type(lexer)

lexer.input("Hello World 9 ")

for token in lexer:
    print(token)





