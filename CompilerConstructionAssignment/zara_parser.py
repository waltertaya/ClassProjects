# zara_parser.py
import ply.yacc as yacc
from zara_lexer import tokens

# Grammar rules

# Define a program structure
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_statement
                 | conditional_statement
                 | loop_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = (p[2], p[1], p[3])

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = (p[2], p[1], p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = p[1]

def p_factor_id(p):
    '''factor : ID'''
    p[0] = ('var', p[1])

def p_conditional_statement(p):
    '''conditional_statement : IF expression statement ELSE statement
                             | IF expression statement'''
    if len(p) == 6:
        p[0] = ('if_else', p[2], p[3], p[5])
    else:
        p[0] = ('if', p[2], p[3])

def p_loop_statement(p):
    '''loop_statement : WHILE expression statement'''
    p[0] = ('while', p[2], p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
