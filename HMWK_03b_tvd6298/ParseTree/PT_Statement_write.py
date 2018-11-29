from .common import *

class PT_Statement_write() :
    def __init__( self, write1 , exp ) :
        self.write1 = write1
        self.m_exp= exp

    def dump( self, indent = 0 ) :
        print((INDENTSTR*indent) + 'WRITE')
        for e in self.m_exp :
            e.dump(indent + 1 )
        
