
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEASSIGN DIVIDE ELSE EQUAL GREATER ID IF LESS LPAREN MINUS NUMBER PLUS RPAREN TIMES WHILEprogram : statement_liststatement_list : statement\n                      | statement_list statementstatement : expression_statement\n                 | conditional_statement\n                 | loop_statementexpression_statement : ID ASSIGN expressionexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : IDfactor : LPAREN expression RPARENexpression : expression LESS term\n                  | expression GREATER term\n                  | expression EQUAL termconditional_statement : IF expression statement ELSE statement\n                             | IF expression statement %prec IFXloop_statement : WHILE expression statement'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,],[7,7,-2,-4,-5,-6,16,16,-3,16,7,-10,-13,-14,-15,16,7,-7,-21,16,16,16,16,16,16,16,-22,7,-8,-9,-17,-18,-19,-11,-12,-16,-20,]),'IF':([0,2,3,4,5,6,10,12,13,14,15,16,18,19,20,29,30,31,32,33,34,35,36,37,38,39,],[8,8,-2,-4,-5,-6,-3,8,-10,-13,-14,-15,8,-7,-21,-22,8,-8,-9,-17,-18,-19,-11,-12,-16,-20,]),'WHILE':([0,2,3,4,5,6,10,12,13,14,15,16,18,19,20,29,30,31,32,33,34,35,36,37,38,39,],[9,9,-2,-4,-5,-6,-3,9,-10,-13,-14,-15,9,-7,-21,-22,9,-8,-9,-17,-18,-19,-11,-12,-16,-20,]),'$end':([1,2,3,4,5,6,10,13,14,15,16,19,20,29,31,32,33,34,35,36,37,38,39,],[0,-1,-2,-4,-5,-6,-3,-10,-13,-14,-15,-7,-21,-22,-8,-9,-17,-18,-19,-11,-12,-16,-20,]),'ELSE':([4,5,6,13,14,15,16,19,20,29,31,32,33,34,35,36,37,38,39,],[-4,-5,-6,-10,-13,-14,-15,-7,30,-22,-8,-9,-17,-18,-19,-11,-12,-16,-20,]),'ASSIGN':([7,],[11,]),'NUMBER':([8,9,11,17,21,22,23,24,25,26,27,],[15,15,15,15,15,15,15,15,15,15,15,]),'LPAREN':([8,9,11,17,21,22,23,24,25,26,27,],[17,17,17,17,17,17,17,17,17,17,17,]),'PLUS':([12,13,14,15,16,18,19,28,31,32,33,34,35,36,37,38,],[21,-10,-13,-14,-15,21,21,21,-8,-9,-17,-18,-19,-11,-12,-16,]),'MINUS':([12,13,14,15,16,18,19,28,31,32,33,34,35,36,37,38,],[22,-10,-13,-14,-15,22,22,22,-8,-9,-17,-18,-19,-11,-12,-16,]),'LESS':([12,13,14,15,16,18,19,28,31,32,33,34,35,36,37,38,],[23,-10,-13,-14,-15,23,23,23,-8,-9,-17,-18,-19,-11,-12,-16,]),'GREATER':([12,13,14,15,16,18,19,28,31,32,33,34,35,36,37,38,],[24,-10,-13,-14,-15,24,24,24,-8,-9,-17,-18,-19,-11,-12,-16,]),'EQUAL':([12,13,14,15,16,18,19,28,31,32,33,34,35,36,37,38,],[25,-10,-13,-14,-15,25,25,25,-8,-9,-17,-18,-19,-11,-12,-16,]),'RPAREN':([13,14,15,16,28,31,32,33,34,35,36,37,38,],[-10,-13,-14,-15,38,-8,-9,-17,-18,-19,-11,-12,-16,]),'TIMES':([13,14,15,16,31,32,33,34,35,36,37,38,],[26,-13,-14,-15,26,26,26,26,26,-11,-12,-16,]),'DIVIDE':([13,14,15,16,31,32,33,34,35,36,37,38,],[27,-13,-14,-15,27,27,27,27,27,-11,-12,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,12,18,30,],[3,10,20,29,39,]),'expression_statement':([0,2,12,18,30,],[4,4,4,4,4,]),'conditional_statement':([0,2,12,18,30,],[5,5,5,5,5,]),'loop_statement':([0,2,12,18,30,],[6,6,6,6,6,]),'expression':([8,9,11,17,],[12,18,19,28,]),'term':([8,9,11,17,21,22,23,24,25,],[13,13,13,13,31,32,33,34,35,]),'factor':([8,9,11,17,21,22,23,24,25,26,27,],[14,14,14,14,14,14,14,14,14,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','zara_parser.py',8),
  ('statement_list -> statement','statement_list',1,'p_statement_list','zara_parser.py',12),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','zara_parser.py',13),
  ('statement -> expression_statement','statement',1,'p_statement','zara_parser.py',20),
  ('statement -> conditional_statement','statement',1,'p_statement','zara_parser.py',21),
  ('statement -> loop_statement','statement',1,'p_statement','zara_parser.py',22),
  ('expression_statement -> ID ASSIGN expression','expression_statement',3,'p_expression_statement','zara_parser.py',26),
  ('expression -> expression PLUS term','expression',3,'p_expression','zara_parser.py',31),
  ('expression -> expression MINUS term','expression',3,'p_expression','zara_parser.py',32),
  ('expression -> term','expression',1,'p_expression_term','zara_parser.py',36),
  ('term -> term TIMES factor','term',3,'p_term','zara_parser.py',40),
  ('term -> term DIVIDE factor','term',3,'p_term','zara_parser.py',41),
  ('term -> factor','term',1,'p_term_factor','zara_parser.py',45),
  ('factor -> NUMBER','factor',1,'p_factor_number','zara_parser.py',49),
  ('factor -> ID','factor',1,'p_factor_id','zara_parser.py',53),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expression','zara_parser.py',58),
  ('expression -> expression LESS term','expression',3,'p_comparison_expression','zara_parser.py',63),
  ('expression -> expression GREATER term','expression',3,'p_comparison_expression','zara_parser.py',64),
  ('expression -> expression EQUAL term','expression',3,'p_comparison_expression','zara_parser.py',65),
  ('conditional_statement -> IF expression statement ELSE statement','conditional_statement',5,'p_conditional_statement','zara_parser.py',70),
  ('conditional_statement -> IF expression statement','conditional_statement',3,'p_conditional_statement','zara_parser.py',71),
  ('loop_statement -> WHILE expression statement','loop_statement',3,'p_loop_statement','zara_parser.py',85),
]
