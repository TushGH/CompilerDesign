from .common import *
class PT_Statement_Assign() :
    def __init__( self, lvalue, expression ) :
        self.m_lvalue = lvalue
        self.m_expression = expression
    def dump( self, indent = 0 ) :
      print( (INDENTSTR*indent) + 'ASSIGN' )
      self.m_lvalue.dump( indent+1 )
      self.m_expression.dump( indent+1 )
