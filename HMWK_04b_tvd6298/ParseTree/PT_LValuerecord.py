from .common import *

class PT_LValuerecord() :
    def __init__( self, name1 , name2 ) :
        self.m_name1 = name1
        self.m_name2 = name2

    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + 'LVALUE RECORD COMPONENT')
        print( (INDENTSTR*(indent+ 1 )) + f"LVALUE ID  '{ self.m_name1}'" )
        print( (INDENTSTR*(indent+ 1 )) + f"COMPONENT  '{ self.m_name2}'" )
