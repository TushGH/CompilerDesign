# Dalio, Brian A.
# dalioba
# 2018-10-02
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Footer() :
  def __init__( self, value ) :
    self.m_Value = value

  def dump( self, indent = 0 ) :
    print( (INDENTSTR*indent) + 'FOOTER' )
    print( ((INDENTSTR*(indent+1))) + f'{self.m_Value!r}' )

#---------#---------#---------#---------#---------#--------#
