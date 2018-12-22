from .common import *

class PT_LValue() :
    def __init__( self, name  ) :
        self.m_name = name

    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + 'LVALUE')
        print( (INDENTSTR*(indent+ 1 )) + f"LVALUE ID  '{ self.m_name}'" )
      #self.m_name.dump( indent+1 )
