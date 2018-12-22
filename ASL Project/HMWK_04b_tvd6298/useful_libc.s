# Dalio, Brian A.
# dalioba
# 2018-11-14

# as --gstabs+ -o u.o useful_libc.s     <- Assemble the source code into object code.
#                                          (--gstabs+ includes debugging info for gdb)
# gcc -static -o test u.o useful_test.c <- Make a static executable from the object code,
#                                          linking it with stdlib and a test harness.
# ./test                                <- Run the executable.
# echo $?                               <- Display the exit code from the run.

.global readInteger
.global readReal
.global writeBoolean
.global writeInteger
.global writeNewLine
.global writeReal
.global writeString

.text
#-----------------------------------------------------------
readInteger:
  # Establish stack frame.
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr

  # scanf( fmt, &intVal )
  movq    %rdi, %rsi    # Arg 2: &intVal (from caller)
  movq    $READ_INT_FMT, %rdi # Arg 1: format

  movl    $0, %eax      # Zero args are in the FP registers
  call    scanf         # scanf( const char *fmt, &intVal )

  # After scanf call, %eax will be 1 on success, 0 on failure

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
readReal:
  # Establish stack frame.
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr

  # scanf( fmt, &fpVal )
  movq    %rdi, %rsi    # Arg 2: &fpVal (from caller)
  movq    $READ_REAL_FMT, %rdi # Arg 1: format

  movl    $0, %eax      # Zero args are in the FP registers
  call    scanf         # scanf( const char *fmt, &fpVal )

  # After scanf call, %eax will be 1 on success, 0 on failure

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
writeBoolean:
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr
  subq    $16, %rsp     # Get some space for locals

  cmpq    $0, %rdi      # Printing false?
  je      writeFalse    # Yep!
  movq    $BOOLEAN_TRUE, %rdi # Nope, so Arg 1: true string
  jmp     writeBooleanString # Go write it out

writeFalse:
  movq    $BOOLEAN_FALSE, %rdi # Arg 1: false string

writeBooleanString:
  movl    $0, %eax      # Zero args are in the FP registers
  call    printf        # printf( const char *fmt, int intVal )

  movl    %eax, -4(%rbp) # Remember what printf returned

  # fflush( stdout )
  movq    stdout, %rdi  # Arg 1: stdout
  call    fflush        # fflush( FILE *stream )

  # Return 0 <= return value of printf
  cmpl    $0, -4(%rbp)  # Compare printf result to 0
  setge   %al           # AL = 1 if 0 <= result else 0
  movzbl  %al, %eax     # Ensure rest of EAX is 0

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
writeInteger:
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr
  subq    $16, %rsp     # Get some space for locals

  movq    %rdi, %rsi    # Arg 2: int (from caller)
  movq    $WRITE_INT_FMT, %rdi # Arg 1: format

  movl    $0, %eax      # Zero args are in the FP registers
  call    printf        # printf( const char *fmt, int intVal )

  movl    %eax, -4(%rbp) # Remember what printf returned

  # fflush( stdout )
  movq    stdout, %rdi  # Arg 1: stdout
  call    fflush        # fflush( FILE *stream )

  # Return 0 <= return value of printf
  cmpl    $0, -4(%rbp)  # Compare printf result to 0
  setge   %al           # AL = 1 if 0 <= result else 0
  movzbl  %al, %eax     # Ensure rest of EAX is 0

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
writeNewLine:
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr
  subq    $16, %rsp     # Get some space for locals

  # putchar( '\n' )
  movl    $10, %edi     # Arg 1: newline character
  call    putchar       # putchar( const char c )

  movl    %eax, -4(%rbp) # Remember what putchar returned

  # fflush( stdout )
  movq    stdout, %rdi  # Arg 1: stdout
  call    fflush        # fflush( FILE *stream )

  # Return EOF != return value of putchar
  cmpl    $-1, -4(%rbp) # Compare putchar result to EOF
  setne   %al           # AL = 1 if EOF != result else 0
  movzbl  %al, %eax     # Ensure rest of EAX is 0

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
writeReal:
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr
  subq    $16, %rsp     # Get some space for locals

  movq    $WRITE_REAL_FMT, %rdi # Arg 1: format
  # Arg 2 is already in %xmm0

  movl    $1, %eax      # One arg is in an FP register
  call    printf        # printf( const char *fmt, double fpVal )

  movl    %eax, -4(%rbp) # Remember what printf returned

  # fflush( stdout )
  movq    stdout, %rdi  # Arg 1: stdout
  call    fflush        # fflush( FILE *stream )

  # Return 0 <= return value of printf
  cmpl    $0, -4(%rbp)  # Compare printf result to 0
  setge   %al           # AL = 1 if 0 <= result else 0
  movzbl  %al, %eax     # Ensure rest of EAX is 0

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
writeString:
  pushq   %rbp          # Save old base (frame) ptr
  movq    %rsp, %rbp    # Make the current stack ptr the base (frame) ptr
  subq    $16, %rsp     # Get some space for locals

  movq    %rdi, %rsi    # Arg 2: const char * (from caller)
  movq    $WRITE_STRING_FMT, %rdi # Arg 1: format

  movl    $0, %eax      # Zero args are in the FP registers
  call    printf        # printf( const char *fmt, const char *str )

  movl    %eax, -4(%rbp) # Remember what printf returned

  # fflush( stdout )
  movq    stdout, %rdi  # Arg 1: stdout
  call    fflush        # fflush( FILE *stream )

  # Return 0 <= return value of printf
  cmpl    $0, -4(%rbp)  # Compare printf result to 0
  setge   %al           # AL = 1 if 0 <= result else 0
  movzbl  %al, %eax     # Ensure rest of EAX is 0

  leave                 # Disestablish stack frame
  ret                   # Return to caller;  (integer) result in %eax

#-----------------------------------------------------------
.data
READ_INT_FMT:
  .asciz  " %d"

READ_REAL_FMT:
  .asciz  " %lf"

BOOLEAN_TRUE:
  .asciz  "true"

BOOLEAN_FALSE:
  .asciz  "false"

WRITE_INT_FMT:
  .asciz  "%d"

WRITE_REAL_FMT:
  .asciz  "%lf"

WRITE_STRING_FMT:
  .asciz  "%s"

#-----------------------------------------------------------
