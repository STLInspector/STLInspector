grammar TemporalLogic;

// the grammar style is inspired by
// https://stackoverflow.com/questions/30976962/nested-boolean-expression-parser-using-antlr


// Variables cannot be named just 'G', 'F', 'N', 'o', 'U' or 'R' since these are keywords of the grammar.
// token should not overlap
TOKEN_OPERATOR	: '==' | '!=' | '<=' | '>=' | '<' | '>';
TOKEN_TRUE     	: 'true';
TOKEN_FALSE    	: 'false';
TOKEN_NOT      	: '!';
TOKEN_AND      	: '&';
TOKEN_OR		: '|';
TOKEN_LB        : '(';
TOKEN_RB        : ')';
TOKEN_DIGIT		: [0-9];
TOKEN_WS		: [ \r\t\n]+ ->skip;

// operators at the top has the highest precedence
formula
    : TOKEN_TRUE # TrueCase
	| TOKEN_FALSE # FalseCase
	| TOKEN_NOT child=formula # NotCase
    | left=formula TOKEN_AND right=formula # AndCase
	| left=formula TOKEN_OR right=formula # OrCase
	| left=formula 'U' '[' TOKEN_DIGIT ']' right=formula # UntilCase
    | TOKEN_LB child=formula TOKEN_RB # BracketCase
    ;

start
    : child=formula EOF
    ;
