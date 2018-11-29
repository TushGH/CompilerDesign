# Deshpande Tushar.
# tvd6298
# 2018-10-02
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Program() :
  def __init__( self, block ) :
    self.m_block = block


  def dump( self, indent = 0 ) :
    print( (INDENTSTR*indent) + 'PROGRAM' )
    # for a in self.m_block :
    #     a.dump(indent+1)
    self.m_block.dump( indent+1 )

#---------#---------#---------#---------#---------#--------#
