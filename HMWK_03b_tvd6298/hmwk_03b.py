# Deshpande Tushar V.
# tvd6298
# 2018-10-02
#---------#---------#---------#---------#---------#--------#
import ply.yacc
import ply.lex
import os
import sys

# TODO:
# Put your ASL parse tree classes in this package.
# Take a look in the ParseTree/ subdirectory to see how
# the code is structured.
from ParseTree import *

#---------#---------#---------#---------#---------#--------#
# TODO: Put your ASL ply tokenizer from HMWK 03a here.

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'and' : 'AND',
   'by' : 'BY',
   'const' : 'CONST',
   'div' : 'DIV',
   'elif': 'ELIF',
   'exit' : 'EXIT',
   'extends' : 'EXTENDS',
   'fi' : 'FI',
   'for' : 'FOR',
   'func' : 'FUNC',
   'loop' : 'LOOP',
   'mod' : 'MOD',
   'next' : 'NEXT',
   'not' : 'NOT',
   'of' : 'OF',
   'or' : 'OR',
   'read' : 'READ',
   'record' : 'RECORD',
   'return' : 'RETURN',
   'then' : 'THEN',
   'to' : 'TO',
   'var' : 'VAR',
   'write' : 'WRITE',
   'do' : 'DO'
}

tokens = [
 'ID','INTEGER','REAL','STRING','ASSIGN','AT',
'COLON','DIVIDE','EQ','GE','GT','LBRACE',
'LBRACKET','LE','LPAREN','LT','MINUS',
'MULTIPLY','NE','PERIOD','COMMA',
'PLUS','PTR','RBRACE','RBRACKET','RPAREN','SEMICOLON'

] + list(reserved.values())

#Tokens
t_PLUS = r'\+'
t_EQ = r'=='
t_ASSIGN = r'='
t_AT = r'@'
t_COMMA = r','
t_COLON = r':'
t_DIVIDE =r'/'
t_GE = r'>='
t_GT = r'>'
t_LBRACE = r'\{'
t_LBRACKET = r'\['
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_NE = r'<>'
t_PERIOD = r'\.'

t_PTR = r'->'
t_RBRACE = r'\}'
t_RBRACKET = r']'
t_RPAREN = r'\)'
t_SEMICOLON = r';'

t_ignore = " \t"
t_ignore_COMMENT = r'//.*'

def t_REAL( t ) :
    r'\d+\.\d*([eE][-+]?\d+)?'
    return t

def t_INTEGER( t ) :
  r'\d+'
  return t

def t_ID( t ) :
  r'[_a-zA-Z][_a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'ID')
  return t



def t_STRING( t ):
    r' "[^"\n]*"'
    t.value = t.value[1:-1]
    return t ;

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error( t ) :
  print( f'Illegal character "{t.value[0]}" on line {t.lineno}.'  )
  t.lexer.skip( 1 )

#---------#---------#---------#---------#---------#--------#
# TODO: Put your ASL ply parser routines here.

# Below are a few sample kinds of parser routines to give
# you an idea of how your routines could be structured.

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','NOT'),
    ('nonassoc', 'LT', 'LE', 'EQ','NE','GE','GT'),
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE','MOD','DIV'),

    )
# works correctly ****************************************************
def p_program( p ) :
  'program : block'
  p[0] = PT_Program( p[1] )

def p_block(p) :
    'block : LBRACE block_items RBRACE'
    p[0] = PT_Block(p[2])

def p_empty(p):
    'empty :'
    pass

def p_block_items_empty(p):
    'block_items : empty'
    p[0] = []

def p_block_items(p):
    'block_items : x_prefix block_item'
    p[1].append(p[2])
    p[0] = p[1]

def p_x_prefix_empty(p):
    'x_prefix : empty'
    p[0] = []

def p_x_prefix(p):
    'x_prefix : x_prefix block_item SEMICOLON'
    p[1].append(p[2])
    p[0] = p[1]

def p_block_item(p):
    'block_item : statement'
    p[0] = p[1]

def p_expression_Real( p ) :
      'expression : REAL'
      p[0] = PT_Expression_Literal('REAL',p[1])

def p_expression_integer( p ) :
      'expression : INTEGER'
      p[0] = PT_Expression_Literal('INTEGER',p[1])




# expression test  function from here **********************
def p_expression_string(p) :
    'expression : STRING '
    p[0] = PT_Expression_Literal('STRING',p[1])

def p_expression_lvalue(p):
    'expression : lvalue'
    p[0] = p[1]

def p_expression_exp(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_uniop(p):
    'expression : uniop expression'
    p[0] = PT_UNIOP_EXP(p[1],p[2])
#
# def p_expression_expexp(p):
#     'expression : expression LPAREN expression RPAREN'





#  write statement ########

def p_statement_write(p) :
    'statement : WRITE LPAREN expressions RPAREN '
    p[0] = PT_Statement_write(p[1],p[3])


def p_expressions_empty(p):
    'expressions : empty '
    p[0] = []

def p_expressions(p):
    'expressions : x_preff  expression'
    p[1].append(p[2])
    p[0] = p[1]

def p_x_preff_empty(p):
    'x_preff : empty'
    p[0] = []

def p_x_preff(p):
    'x_preff : x_preff expression COMMA'
    p[1].append(p[2])
    p[0] = p[1]





########################################################



def p_uniop(p):
    '''uniop : MINUS
             | NOT'''
    if p[1] == '-'  : p[0] = p[1]
    elif p[1] == 'not': p[0] = p[1]

# function for LVALUE start from here
def p_lvalue_id(p) :
    'lvalue : ID'
    p[0] = PT_LValue(p[1])

def p_lvalue_array(p):
    'lvalue : lvalue LBRACKET expression RBRACKET'
    p[0] = PT_LVALUE_ARRAY(p[1],p[3])

def p_lvalue_record(p):
    'lvalue : lvalue PERIOD ID'
    p[0] = PT_LValuerecord(p[1],p[3])

#**************for binary operator***************
def p_binaryop(p) :
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression OR expression
                  | expression AND expression
                  | expression LT expression
                  | expression LE expression
                  | expression GE expression
                  | expression GT expression
                  | expression EQ expression
                  | expression NE expression
                  '''
    if p[2] == '+'  : p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '-': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '*': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '/': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == 'div': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == 'mod': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == 'or': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == 'and': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '<': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '<=': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '>=': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '>': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '==': p[0] = PT_BINARYOP(p[2],p[1],p[3])
    elif p[2] == '<>': p[0] = PT_BINARYOP(p[2],p[1],p[3])

# ****************Statement functions from here************************

def p_statement_single(p):
    '''expression : EXIT
                  | NEXT '''
    if p[0] == 'exit' : p[0]= PT_STAT_SING(p[1])
    elif p[0] == 'next' : p[0] = PT_STAT_SING(p[1])


def p_statement_block(p):
    'statement : block'
    p[0] = PT_Block(p[1])

def p_statement_lvalueAExp(p):
    'statement : lvalue ASSIGN expression'
    p[0] = PT_STAT_EXP(p[1] , p[3])

def p_statement_expexp(p):
    'statement : expression LBRACKET expression RBRACKET '
    p[0] = PT_STAT_EXPEXP(p[1],p[3])


def p_error( p ) :
  if p is None :
    print( 'Syntax error!' )

  else :
    print( f'Syntax error at "{p.value}", line {p.lineno}' )

  raise ValueError( 'Syntactic error' )
#---------#---------#---------#---------#---------#--------#
def _main( inputFile ) :
  with open( inputFile, 'r' ) as fp :
    data = fp.read()
  a = os.path.basename(sys.argv[0]) # getting the file name
  #print(a[:-3]) # getting rid of etension
  parseFile = a[:-3] + ".parse"
  codeFile = a[:-3] + ".s"
  #print(parseFile)
  #print(codeFile)
  try :
    _  = ply.lex.lex()
    parser = ply.yacc.yacc()
    value = parser.parse( data )


    with open(parseFile, 'w') as fp:
        print( 'Parse returns ...' , file = fp )
        value.dump(fp = fp)

    try :
        value.semanticCheack();

    except Exception as e:
        print("caught an exception")
        print(str(e))
        raise

    with open(codeFile, 'w') as fp:

        value.codeGen(fp = fp)



  except ValueError :
    print( 'Error during processing.  Abort.' )

#---------#---------#---------#
if __name__ == '__main__' :
  import sys

  if len( sys.argv ) > 1 :
    _main( sys.argv[ 1 ] )

  else :
    print( 'Input file name required.' )

#---------#---------#---------#---------#---------#--------#
