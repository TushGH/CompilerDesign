from .common import *

class PT_UNIOP_EXP() :
    def __init__( self, uniop , exp ) :
        self.m_uniop = uniop
        self.m_exp = exp

    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + f"UNIOP '{self.m_uniop}'")
        self.m_exp.dump( indent+1 )
        
