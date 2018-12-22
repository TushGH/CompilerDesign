# CompilerDesign
This is a complier designed for ASL languale using  Python Ply library<br>
you can find the ply documentation here - : https://www.dabeaz.com/ply/ <br><br><br>
<h1>This project follows the following steps</h1><br>
1] Tokenizer(Lexical analysis)<br>
2] Syntax Analysis<br>
3] Semantic Analysis<br>
4] Code generation ( Assembly language X86 )<br>
<br><br><br>
Note: <br>
1]This Compiler is used to print 3 types of literals 1) String 2) Integer 3)float <br>
2] The file extension for the program is .asl<br>
3] It requires <b>Python3</b> working environment<br>
4] It requires gcc compiler<br>
5] It generates the parse tree in hmwk_04b.parse file<br>
6] The Code (Assembly code generated) is in hmwk_04b.s file<br>

<br><br>
<h4>Command for execution </h4><br><pre>
1] Generate parse tree and assembly language<br>
   python hmwk_04b.py <filename>.asl   ( use python3 environment python3 hmwk_04b.py <filename>.asl)
2] gcc -static -o test useful_libc.s <filename>.s (To compile library and generated code with test executable file)
3] ./test   
</pre>

<h4> Example of abc.asl </h4><br><pre>
{
  write( "simpleWrite" );
  write( 1 );
  write( 2.3 );
  write( "Integer : ", 4 );
  write( "Real    : ", 5.6 )
}
</pre><br><br>
<h4> The Parse Tree Generated for abc.asl file </h4><br><pre>
Parse returns ...
PROGRAM
  {
    WRITE
      ARG
        LITERAL STRING  'simpleWrite' 
    WRITE
      ARG
        LITERAL INTEGER  '1' 
    WRITE
      ARG
        LITERAL REAL  '2.3' 
    WRITE
      ARG
        LITERAL STRING  'Integer : ' 
      ARG
        LITERAL INTEGER  '4' 
    WRITE
      ARG
        LITERAL STRING  'Real    : ' 
      ARG
        LITERAL REAL  '5.6' 
  }
  </pre><br><br>
 <h4> The Assembly code Generated for abc.asl file </h4><br><pre>
.global main
.text
main:

# Prologue
pushq   %rbp
movq    %rsp, %rbp

.data
STRLIT0: .asciz "simpleWrite" 
.text
movq $STRLIT0, %rdi
call  writeString
call  writeNewLine

.data
.align 4
INTLIT0: .int 1 
.text
movl INTLIT0, %edi
call  writeInteger
call  writeNewLine

.data
.align 8
REALIT0: .double 2.3 
.text
movq REALIT0, %xmm0
call  writeReal
call  writeNewLine


.data
STRLIT1: .asciz "Integer : " 
.text
movq $STRLIT1, %rdi
call  writeString
.data
.align 4
INTLIT1: .int 4 
.text
movl INTLIT1, %edi
call  writeInteger
call  writeNewLine


.data
STRLIT2: .asciz "Real    : " 
.text
movq $STRLIT2, %rdi
call  writeString
.data
.align 8
REALIT1: .double 5.6 
.text
movq REALIT1, %xmm0
call  writeReal
call  writeNewLine


# exit value
movl    $0, %eax

# Epilogue
leave
ret
</pre><br><br>
<h4> The Out Generatedput for abc.asl file </h4><br><pre>
simpleWrite
1
2.3
Integer : 4
Real    : 5.6
</pre>
<br> This Project is completed as a part of course Compiler Design at University of Texas at Arlington(CSE 4305 / CSE 5317 )
Under the guidance of Prof brian a dalio.
  

