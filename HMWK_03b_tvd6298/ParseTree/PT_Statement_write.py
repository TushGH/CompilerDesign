from .common import *
import sys

class PT_Statement_write() :

    def __init__( self, write1 , exp ) :
        self.write1 = write1
        self.m_exp= exp

    def codeGen(self , fp=sys.stdout):
        for e in self.m_exp :
            e.codeGen(fp = fp)



    def dump( self, indent = 0 , fp=sys.stdout) :
        print((INDENTSTR*indent) + 'WRITE' , file = fp)
        for e in self.m_exp :
            e.dump(indent + 1 , fp )

    def semanticCheack(self) :
           for e in self.m_exp :
               e.semanticCheack()
