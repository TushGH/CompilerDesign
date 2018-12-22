// --- Statement test
// At least one of every kind of statement.
// Not meant to do anything.  Just a test for the scanner/parser.
// Syntactically correct, but semantically meaningless.

// statement ⟶ block
//   | lvalue '=' expression
//   | expression '(' expressions ')'
//   | 'read' '(' lvalue { ',' lvalue } ')'
//   | 'write' '(' write_params ')'
//   | 'if' expression 'then' statement
//     { 'elif' expression 'then' statement }
//     [ 'else' statement ] 'fi'
//   | 'while' expression 'do' statement
//   | 'loop' statement
//   | 'for' lvalue '=' expression 'to' expression [ 'by' expression ]
//     'do' statement
//   | 'exit'
//   | 'next'
//   | 'return' [ expression ]

{
  {
    // A block, which has to have something in it.

    // lvalue = expression
    a[b].c[3].whatever = 1 + 2 + 12.34
  };

  // Function call!
  someFunction( arg0 );
  (fctReturningFct())( arg1, arg2, arg3 );

  // Read and write!
  read( lvalue1, lvalue2[1+2*3], lvalue3.component, lvalue4[a].component );
  write( "A string", 56.78 + 90.12 * 34.56 );

  // If!
  if expr then exit fi;

  if expr1 then if expr2 then foo() else bar() fi fi;

  if expr then {
    doSomething = true
  } elif anotherExpr then {
    doSomethingElse()
  } elif yetAnotherExpr then {
    doAnotherSomethingElse()
  } else
    thatsAllFolks()
  fi;

  // While!
  while expr do
    something();

  // Loop!
  loop {
    yadaYadaYada()
  };

  // For!
  for lvalue = 1 to 100 by 2 do {
    a = a + lvalue;
    if a < b then
      next
    else
      exit
    fi
  };

  // Return!
  return expr+expr*expr-expr/expr;
  return        // Returning 'void'.
}
