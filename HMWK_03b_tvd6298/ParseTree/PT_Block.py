from .common import *
import sys

class PT_Block() :
    def __init__( self, block_items ) :
        self.m_block_items = block_items

    def semanticCheack(self) :
        for a in self.m_block_items:
            a.semanticCheack()

    def dump( self, indent = 0 , fp=sys.stdout ) :
      print( (INDENTSTR*indent) + '{' , file = fp )
      for a in self.m_block_items :
          a.dump(indent+1 , fp)
      print( (INDENTSTR*indent) + '}' , file = fp )
     # self.m_block_items.dump( indent+1 )
