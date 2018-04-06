import ply.lex as lex


t_WORD = r'[A-Za-z]+'
t_NUMBER = r'[0-9]+'


tokens = ('WORD',
          'NUMBER',
          )

lexer = lex.lex()


lexer.input("Hello World 9")

print(lexer.token())





