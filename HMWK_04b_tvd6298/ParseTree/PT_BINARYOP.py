from .common import *

class PT_BINARYOP() :
    def __init__( self, operator ,exp1, exp2 ) :
        self.m_operator = operator
        self.m_exp1 = exp1
        self.m_exp2 = exp2


    def dump( self, indent = 0 ) :
        
        print((INDENTSTR*indent) + f"BINARYOP '{self.m_operator}'")
        self.m_exp1.dump( indent+1 )
        self.m_exp2.dump( indent+1 )
        #print( (INDENTSTR*(indent+ 1 )) + f"LVALUE ID  '{ self.m_name}'" )
      #self.m_name.dump( indent+1 )
