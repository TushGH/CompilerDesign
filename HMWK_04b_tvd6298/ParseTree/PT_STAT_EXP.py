from .common import *
class PT_STAT_EXP() :
    def __init__( self, lvalue, exp ) :
        self.m_lvalue = lvalue
        self.m_exp = exp
    def dump( self, indent = 0 ) :
        # print((INDENTSTR*indent) + 'ASSIGN')
        # print( (INDENTSTR*(indent+1)) + f"LITERAL {self.m_kind}  '{self.m_value}' " )
        self.m_lvalue.dump( indent+1 )
        self.m_exp.dump( indent+1 )
