from .common import *

class PT_LVALUE_ARRAY() :
    def __init__( self, name1 , exp ) :
        self.m_name1 = name1
        self.m_exp= exp

    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + 'LVALUE ARRAY SUBSCRIPT')
        self.m_exp.dump( indent+1 )
