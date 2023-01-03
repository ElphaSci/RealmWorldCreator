grammar sci;
prog:	expr;
expr: '(' 'let' ' ' (VAR ' ' (expr|VAR|INT))+ ' ' (expr|VAR|INT) ')'
	| '(' ('add'|'mult') ' ' (expr|VAR|INT) ' ' (expr|VAR|INT) ')'
        ;
VAR: [a-zA-Z0-9]+ ;
INT: [0-9]+ ;