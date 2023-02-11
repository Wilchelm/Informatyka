#!/usr/bin/python3
# -*- coding: utf-8 -*-

tokens = ( 'OPER', 'NUMBER', 'SIZE', 'COLOR', 'KIND', 'MATERIAL', )

# Tokens

t_OPER = r'((D|d)ostarczono)|((W|w)ydano)'
t_SIZE = r'((M|m)ał(y|ey|ch))|((Ś|ś)redn(i|ie|ich))'
t_COLOR = r'((B|b)iał(y|ych))|((Z|z)ielon(y|e|ych))'
t_KIND = r'((N|n)iezbędni(k|ki|ków))|((Z|z)będni(k|ki|ków))'
t_MATERIAL = r'((P|p)lastikow(y|e|ych))|((A|a)luminiow(y|e|ych))'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
 
# Ignored characters 
t_ignore = " \t" 

def t_newline(t): 
	r'\n+' 
	t.lexer.lineno += t.value.count("\n") 

def t_error(t): 
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

def t_BYE(t):
	r'(bye|BYE|Bye)'
	print ('Bye bye')
	exit()



# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','KIND','MATERIAL'),
    ('right','UOPER'),
)

# dictionary of names
names = { }


def p_uoper(t):
    'uoper : OPER %prec UOPER'

def P_cmd(t):
    '''cmd : OPER NUMBER art'''

def p_art(t):
    '''art : KIND
	   | attr art'''

def p_attr(t):
    '''attr : SIZE 
            | COLOR 
            | MATERIAL'''

def p_error(t):
    print ("Syntax error at '%s'" % t.value)


import ply.yacc as yacc 
parser = yacc.yacc()
while True: 
	try: s = input('Write command > ') # Use raw_input on Python 2
	except EOFError: break
	if parser.parse(s):
		print ("OK")
	else:
		print ("KO")

