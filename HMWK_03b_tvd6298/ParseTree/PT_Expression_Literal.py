from .common import *
class PT_Expression_Literal() :
    def __init__( self, kind, value ) :
        self.m_kind = kind
        self.m_value = value
    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + 'EXPRESSION')
        print( (INDENTSTR*(indent+1)) + f"LITERAL {self.m_kind}  '{self.m_value}' " )
        # self.m_kind.dump( indent+1 )
        # self.m_value.dump( indent+1 )
