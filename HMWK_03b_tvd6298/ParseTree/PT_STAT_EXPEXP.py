from .common import *
class PT_STAT_EXPEXP() :
    def __init__( self, exp1, exp2 ) :
        self.m_exp1 = exp1
        self.m_exp2 = exp2
    def dump( self, indent = 0 ) :
        # print((INDENTSTR*indent) + 'ASSIGN')
        # print( (INDENTSTR*(indent+1)) + f"LITERAL {self.m_kind}  '{self.m_value}' " )
        self.m_exp1.dump( indent+1 )
        self.m_exp2.dump( indent+1 )
