import ply.yacc as yacc
from zara_lexer import tokens
from symbol_table import symbol_table

# Define grammar rules with semantic actions

def p_statement_assign(p):
    'statement : ID EQUAL expression SEMICOLON'
    var_name = p[1]
    value_type = p[3]  # Type of the expression on the right side
    symbol_table.assign(var_name, value_type)  # Check for correct assignment

def p_statement_decl(p):
    'statement : type ID EQUAL expression SEMICOLON'
    var_type = p[1]
    var_name = p[2]
    value_type = p[4]  # Type of the expression on the right side
    symbol_table.declare(var_name, var_type)  # Declare variable
    symbol_table.assign(var_name, value_type)  # Check for correct assignment

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING
            | stack'''
    p[0] = p[1]  # Return the type as the value for semantic checking

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    # Here we can check the types of both operands and return a type
    left_type = p[1]  # Type of the left operand
    right_type = p[3]  # Type of the right operand
    # Example type-checking logic (you may want to expand this based on your requirements)
    if left_type != right_type:
        raise Exception(f"Type error: cannot operate on {left_type} and {right_type}")
    p[0] = left_type  # The result type is the same as the operands for simplicity

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = 'int'  # Assuming NUMBER is an integer

def p_expression_id(p):
    'expression : ID'
    p[0] = symbol_table.get_type(p[1])  # Get the type of the variable from the symbol table
    if p[0] is None:
        raise Exception(f"Variable '{p[1]}' not declared.")

def p_expression_bool(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = 'bool'  # Both true and false are boolean types

def p_expression_string(p):
    'expression : STRING'
    p[0] = 'string'  # STRING tokens are strings

def p_expression_array(p):
    'expression : ID LBRACKET expression RBRACKET'
    var_name = p[1]
    if symbol_table.get_type(var_name) is None:
        raise Exception(f"Variable '{var_name}' not declared.")
    p[0] = symbol_table.get_type(var_name)  # Return the type of the array element

def p_expression_stack(p):
    'expression : ID DOT PUSH LPAREN expression RPAREN'
    var_name = p[1]
    value_type = p[5]  # Type of the value being pushed
    # Check if it's a valid stack type
    if symbol_table.get_type(var_name) != 'stack':
        raise Exception(f"Variable '{var_name}' is not a stack.")
    p[0] = 'void'  # Push operation returns nothing

def p_expression_pop(p):
    'expression : ID DOT POP LPAREN RPAREN'
    var_name = p[1]
    # Check if it's a valid stack type
    if symbol_table.get_type(var_name) != 'stack':
        raise Exception(f"Variable '{var_name}' is not a stack.")
    p[0] = 'int'  # Assuming the pop returns an int for simplicity

def p_error(p):
    print(f"Syntax error at '{p.value if p else 'EOF'}'")

# Build the parser
parser = yacc.yacc()
