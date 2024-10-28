# zara_lexer.py
import ply.lex as lex

# List of token names
tokens = [
    'NUMBER', 'ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'EQUAL', 'LESS', 'GREATER',
    'IF', 'ELSE', 'WHILE', 'ASSIGN'
]

# Regular expressions for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL   = r'=='
t_LESS    = r'<'
t_GREATER = r'>'
t_ASSIGN  = r'='

# Keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Token for identifiers and reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# Token for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
