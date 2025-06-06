grammar Sci;

// Entry point for parsing
program
  : expression* EOF
  ;

expression
  : LPAREN ( expression | atom | statement '?'? )+ RPAREN
  | LPAREN (return_statement '?'?)+ RPAREN
  ;

return_statement
  : method_call
  | assignment
  | procedure_call
  | property_access
  ;


statement
  : module
  | include
  | public_
  | local
  | define
  | procedures
  | switch
  | class
  | enum
  | instance
  | if
  | for
  | not
  | math
  | bit_math
  | logic
  | RETURN
  ;

atom : STRING | NUMBER | TRUE | FALSE;

module: MODULE SYMBOL;
public_: PUBLIC (SYMBOL NUMBER)+;
local: LOCAL (SYMBOL (EQ NUMBER)?)+;
include: INCLUDE STRING;
definition: (SYMBOL (SYMBOL | atom | expression));
define: DEFINE definition*;


procedures: procedure_declaration | procedure_definition;

procedure_declaration: PROCEDURE SYMBOL+;
procedure_definition: PROCEDURE procedure_signature expression*;
procedure_signature: LPAREN SYMBOL (TMP | SYMBOL)* RPAREN;


switch_case: LPAREN (ELSE | SYMBOL) (atom | expression) RPAREN;
switch_expression: (SYMBOL | expression);
switch: SWITCH switch_expression switch_case*;

for: FOR expression expression expression expression*;

not: NOT (atom | SYMBOL | statement | expression);
if: IF (atom |SYMBOL | statement | expression) expression* else?;
else: ELSE expression*;



property_access: SYMBOL SYMBOL;
named_parameter: SYMBOL ':' parameter;
parameter: (SYMBOL | REFERENCE | statement | atom | expression);

method_call:
  (expression | SYMBOL)
  (SYMBOL ':'
    (parameter* | parameter? (',' named_parameter)* ','?)
  )+
  ;

assignment: EQ SYMBOL (SYMBOL| atom | statement | expression);

bit_math
  : (BITOR | BITAND | BITXOR) (statement | atom | SYMBOL | expression)+
  | (SLEFT | SRIGHT) (statement | atom | SYMBOL | expression) (statement | atom | SYMBOL | expression)
  ;
math
  : decrement
  | increment
  | plus_assign
  | minus_assign
  | add
  | subtract
  | multiply
  | divide
  ;

increment: INC (SYMBOL | NUMBER | expression);
decrement: DEC (SYMBOL | NUMBER | expression);
minus_assign: MINUS_EQ SYMBOL (SYMBOL | NUMBER | expression);
plus_assign: PLUS_EQ SYMBOL (SYMBOL | NUMBER | expression);
add: PLUS (NUMBER | SYMBOL | expression) (NUMBER | SYMBOL | expression);
subtract: MINUS (NUMBER | SYMBOL | expression) (NUMBER | SYMBOL | expression);
multiply: MUL (NUMBER | SYMBOL | expression) (NUMBER | SYMBOL | expression);
divide: DIV (NUMBER | SYMBOL | expression) (NUMBER | SYMBOL | expression);

logic
  : greater_or_equal
  | greater
  | less_than_or_equal
  | less_than
  | equals
  | not_equals
  ;

greater_or_equal: GE (SYMBOL | NUMBER | expression) (SYMBOL | NUMBER | expression)+ ;
greater: GT (SYMBOL | NUMBER | expression) (SYMBOL | NUMBER | expression)+ ;
less_than_or_equal: LE (SYMBOL | NUMBER | expression) (SYMBOL | NUMBER | expression)+ ;
less_than: LT (SYMBOL | NUMBER | expression) (SYMBOL | NUMBER | expression)+ ;
equals: EQ2 (SYMBOL | atom | expression) (SYMBOL | atom | expression)+ ;
not_equals: NE (SYMBOL | NUMBER) (SYMBOL | NUMBER)+ ;


property_definition: SYMBOL (SYMBOL | SYMBOL ':'? (atom | expression));
string_prop: SYMBOL STRING;
var_prop: SYMBOL SYMBOL (atom | SYMBOL);
property_init: string_prop | var_prop;

class_properties: LPAREN PROPERTIES property_definition* RPAREN;
properties: LPAREN PROPERTIES property_init+ RPAREN;

methods_definition: LPAREN METHODS SYMBOL* RPAREN;
method_parameters: (TMP | SYMBOL)+;
method_signature: LPAREN SYMBOL method_parameters? RPAREN;
method: LPAREN METHOD method_signature expression* RPAREN;

procedure_call: SYMBOL SYMBOL (SYMBOL | atom)*;

enum: ENUM SYMBOL+;
class: CLASS SYMBOL (OF | KINDOF | KINDOF_ALT) SYMBOL
  (class_properties | methods_definition | method)*
  ;

instance: INSTANCE SYMBOL (OF | KINDOF | KINDOF_ALT) SYMBOL
  (properties | method)+
  ;


COMMENT: ';' ~[\r\n]* -> skip;
WS: [ \t\n\r]+ -> skip;

// Keywords
INCLUDE : 'include' ;
PUBLIC : 'public' ;
EXTERN : 'extern' ;
GLOBAL : 'global' ;
LOCAL : 'local' ;
DEFINE : 'define' ;
ENUM : 'enum' ;
PROCEDURE : 'procedure' ;
SELECTORS : 'selectors' ;
CLASSDEF : 'class-def' ;
CLASSDEF_ALT : 'classdef' ;
MODULE : 'module#' ;
SCRIPTNUM : 'script#' ;
CLASSNUM : 'class#' ;
SUPER : 'super#' ;
CLASS : 'class' ;
PROPERTIES : 'properties' ;
METHODS : 'methods' ;
METHOD : 'method' ;
INSTANCE : 'instance' ;
OF : 'of' ;
KINDOF : 'kindof' ;
KINDOF_ALT : 'kind-of' ;
TMP : '&tmp' ;
RETURN : 'return' ;
BREAK : 'break' ;
BREAKIF : 'breakif' ;
CONTINUE : 'continue' ;
CONTIF : 'contif' ;
WHILE : 'while' ;
REPEAT : 'repeat' ;
FOR : 'for' ;
IF : 'if' ;
ELSE : 'else' ;
COND : 'cond' ;
SWITCH : 'switch' ;
FILE : 'file#' ;
SWITCHTO : 'switchto' ;

// Operators
INC : '++' ;
DEC : '--' ;
REST : '&rest' ;
PLUS : '+' ;
MUL : '*' ;
BITXOR : '^' ;
BITAND : '&' ;
BITOR : '|' ;
MINUS : '-' ;
DIV : '/' ;
MOD : 'mod' ;
SLEFT : '<<' ;
SRIGHT : '>>' ;
EQ : '=' ;
PLUS_EQ : '+=' ;
MUL_EQ : '*=' ;
MINUS_EQ : '-=' ;
DIV_EQ : '/=' ;
SLEFT_EQ : '<<=' ;
SRIGHT_EQ : '>>=' ;
XOR_EQ : '^=' ;
AND_EQ : '&=' ;
OR_EQ : '|=' ;
BNOT : '~' ;
NOT : 'not' ;
NEG : 'neg' ;
GT : '>' ;
GE : '>=' ;
LT : '<' ;
LE : '<=' ;
UGT : 'u>' ;
UGE : 'u>=' ;
ULT : 'u<' ;
ULE : 'u<=' ;
EQ2 : '==' ;
NE : '!=' ;
AND : 'and' ;
OR : 'or' ;
TRUE : 'TRUE' ;
FALSE : 'FALSE' ;
ARGC : 'argc' ;

STRING: '"' (~[\\"\r\n])* '"' ;
NUMBER: [0-9]+ ;
SYMBOL: [a-zA-Z0-9_+-/*=!$%&|<>@]+ ;
REFERENCE: '#' SYMBOL ':'?;

LPAREN: '(';
RPAREN: ')';
