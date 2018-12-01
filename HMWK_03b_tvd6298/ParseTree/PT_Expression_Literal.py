from .common import *
import sys
class PT_Expression_Literal() :
    Stringcount = 0
    Realcount = 0
    Intcount = 0
    def __init__( self, kind, value ) :
        self.m_kind = kind
        self.m_value = value
    def dump( self, indent = 0 , fp = sys.stdout) :
        print((INDENTSTR*indent) + 'ARG' , file = fp)
        print( (INDENTSTR*(indent+1)) + f"LITERAL {self.m_kind}  '{self.m_value}' " , file = fp )

    def codeGen(self , fp=sys.stdout  ) :
        if self.m_kind == "STRING" :
            print( file = fp )
            print( '.data', file = fp )
            print( f"STRLIT{PT_Expression_Literal.Stringcount}: .asciz \"{self.m_value}\" ", file = fp )
            print( '.text', file = fp )
            print( f"movq $STRLIT{PT_Expression_Literal.Stringcount}, %rdi", file = fp )
            PT_Expression_Literal.Stringcount = PT_Expression_Literal.Stringcount + 1
            print( 'call  writeString', file = fp )
            print( 'call  writeNewLine', file = fp )
            print( file = fp )
        if self.m_kind == "INTEGER" :
            print( '.data', file = fp )
            print( '.align 4', file = fp )
            print( f"INTLIT{PT_Expression_Literal.Intcount}: .int {self.m_value} ", file = fp )
            print( '.text', file = fp )
            print( f"movq $INTLIT{PT_Expression_Literal.Intcount}, %edi", file = fp )
            PT_Expression_Literal.Intcount = PT_Expression_Literal.Intcount + 1
            print( 'call  writeInteger', file = fp )
            print( 'call  writeNewLine', file = fp )
            print( file = fp )
        if self.m_kind == "REAL":
            print( '.data', file = fp )
            print( '.align 8', file = fp )
            print( f"REALIT{PT_Expression_Literal.Realcount}: .double {self.m_value} ", file = fp )
            print( '.text', file = fp )
            print( f"movq $REALIT{PT_Expression_Literal.Realcount}, %xmm0", file = fp )
            PT_Expression_Literal.Realcount = PT_Expression_Literal.Realcount + 1 
            print( 'call  writeReal', file = fp )
            print( 'call  writeNewLine', file = fp )
            print( file = fp )

    def semanticCheack(self) :
           #self.m_block.semanticCheack()
            if self.m_kind == "REAL" :
               m = float(self.m_value)
               if float(self.m_value) != m :
                   raise ValueError('value of float exceeded')

            if self.m_kind == "STRING":
                for a in self.m_value:
                    if  ord(a) <=127 :
                        pass
                    else :
                        raise ValueError('String value is not in unicode')

            if self.m_kind == "INTEGER" :
                m = int(self.m_value)
                if  m > 2**31 - 1:
                    raise ValueError('value of Integer exceeded')
