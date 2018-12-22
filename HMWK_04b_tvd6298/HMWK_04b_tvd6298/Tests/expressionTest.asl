// --- Expression test
// At least one of everything that can appear in an expression.
// Not meant to do anything.  Just a test for the scanner/parser.
// Syntactically correct, but semantically meaningless.

// expression	⟶	literal
// 	⟶	lvalue
// 	⟶	'(' expression ')'
// 	⟶	unary_op expression
// 	⟶	expression binary_op expression
// 	⟶	expression '(' expressions ')'
// ****************remaining to code*****************  //
// 	⟶	ID '{' [ record_inits ] '}'
// 	⟶	'@' type_expr '{' [ array_inits ] '}'
//****************************************************
// literal	⟶	INTEGER | REAL | STRING

// lvalue	⟶	ID
// 	⟶	lvalue '[' expression ']'
// 	⟶	lvalue '.' ID

// unary_op	⟶	'-' | not

// binary_op	⟶	'+' | '-' | '*' | '/' | div | mod | or | and
// 	⟶	'<' | '<=' | '>=' | '>' | '==' | '<>'

// array_init	⟶	[ expression of ] expression
// array_inits	⟶	array_init { ',' array_init }

// record_init	⟶	ID '=' expression
// record_inits	⟶	record_init { ',' record_init }

{
  // INTEGER literals
  a = 0123;
  b = 00;
  c = 999;

  // REAL literals
  a = 0.0;
  b = 0.;
  c = 9.e-12;
  d = 8.7E+4;
  e = 6.54e3;

  // STRING literals
  a = "";
  b = "abc";

  // LValues
  a = b;
  c = d[e];
  f = g.h;
  i = j.k[l].m.n;

  // Nested expression.
  a = (b);
  c = ((d));
  e = (((f)));
  a = 1+(2+b);
  a = 1+2+b;
  c = 2+(3+(4+d));
  c = 2+3+4+d;
  e = 3+(4+(5+(6+f)));
  e = 3+4+5+6+f;

  // Unary operators
  a = -b;
  a = --b;
  c = not d;
  c = not not d;

  // Binary operators
  a = b+c;
  d = e-f;
  g = h*j;
  k = l/m;
  n = o div p;
  q = r mod s;

  t = -u * v;
  t = -u / v;
  t = -u mod v;
  t = -u div v;

  w = x + y * z;
  w = x + y / z;
  w = x + y mod z;
  w = x + y div z;
  w = x - y * z;
  w = x - y / z;
  w = x - y mod z;
  w = x - y div z;

  a = b + c < d - e;
  a = b + c <= d - e;
  a = b + c == d - e;
  a = b + c <> d - e;
  a = b + c >= d - e;
  a = b + c > d - e;

  f = not g - h < i + j and k - l > m + n or o + p <= q - r and s + t >= u - v;

  // FUNC CALLS
  a = b( c, d, e );
  f = (g(h(i(k))))( 1, 2, 3.4 );

  // ARRAY CONSTRUCTORS
  l = @integer{ 10 of m, n - o of p + q };

  // RECORD CONSTRUCTOR
  r = rectype{ s = t, u = v+w*z }
}
