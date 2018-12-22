# Deshpande Tushar.
# tvd6298
# 2018-10-02
#---------#---------#---------#---------#---------#--------#
from .common import *
import sys

#---------#---------#---------#---------#---------#--------#
class PT_Program() :
    def __init__( self, block ) :
        self.m_block = block

    def codeGen(self , fp=sys.stdout) :
        print( '.global main', file = fp )
        print( '.text', file = fp )
        print( 'main:', file = fp )
        print( file = fp )
        print( '# Prologue', file = fp )
        print( 'pushq   %rbp', file = fp )
        print( 'movq    %rsp, %rbp', file = fp )
        self.m_block.codeGen(fp = fp)
        print( file = fp )
        print('# exit value' , file = fp )
        print( 'movl    $0, %eax', file = fp )
        print( file = fp )
        print( '# Epilogue', file = fp )
        print( 'leave', file = fp )
        print( 'ret', file = fp )




    def dump( self, indent = 0 , fp=sys.stdout ) :
        print( (INDENTSTR*indent) + 'PROGRAM' , file = fp )
        # for a in self.m_block :
        #     a.dump(indent+1)
        self.m_block.dump( indent+1 , fp )

    def semanticCheack(self) :
           self.m_block.semanticCheack()






#---------#---------#---------#---------#---------#--------#
