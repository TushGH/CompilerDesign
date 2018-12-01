from .common import *
import sys
class PT_Expression_Literal() :
    def __init__( self, kind, value ) :
        self.m_kind = kind
        self.m_value = value
    def dump( self, indent = 0 , fp = sys.stdout) :
        print((INDENTSTR*indent) + 'EXPRESSION' , file = fp)
        print( (INDENTSTR*(indent+1)) + f"LITERAL {self.m_kind}  '{self.m_value}' " , file = fp )
        # self.m_kind.dump( indent+1 )
        # self.m_value.dump( indent+1 )

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
