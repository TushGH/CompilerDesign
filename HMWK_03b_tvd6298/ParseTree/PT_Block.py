from .common import *

class PT_Block() :
    def __init__( self, block_items ) :
        self.m_block_items = block_items

    def dump( self, indent = 0 ) :
      print( (INDENTSTR*indent) + '{' )
      for a in self.m_block_items :
          a.dump(indent+1)
      print( (INDENTSTR*indent) + '}' )
     # self.m_block_items.dump( indent+1 )
