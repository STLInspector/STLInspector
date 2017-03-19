grammar TemporalLogic;

@header {
from core.temporallogic import *
import re as regex


def parse_ap_tuple(string):
    t = []
    if string is not None:
        t = tuple(string.strip('(').strip(')^T').split(','))
    return None if t == [] else tuple([x.strip(' ') for x in t])


def parse_ap_operator(string):
    o = {
        '==': eq,
        '!=': ne,
        '<': lt,
        '<=': le,
        '>': gt,
        '>=': ge
    }
    return o[string]


def parse_conjunction(l):
    """
    Receives a list of temporal logic formulae and returns a conjunction
    containing all the formulae. For example:
    parse_conjunction([AP("a"), AP("b"), AP("c")]) --> AND(AP("a"), AND(AP("b"), AP("c")))
    """
    if len(l) == 1:
        return l[0]
    else:
        return AND(l[0], parse_conjunction(l[1:]))


def parse_disjunction(l):
    """
    Receives a list of temporal logic formulae and returns a disjunction
    containing all the formulae. For example:
    parse_disjunction([AP("a"), AP("b"), AP("c")]) --> OR(AP("a"), OR(AP("b"), AP("c")))
    """
    if len(l) == 1:
        return l[0]
    else:
        return OR(l[0], parse_disjunction(l[1:]))


def parse_c(string):
    res = regex.search('((^\d+(\.\d+)?)|(^\+\d+(\.\d+)?)|(^\-\d+(\.\d+)?))\ *', string)
    return None if res == None else [res.group()]
}

constant returns [Clause c]
        : ANTLR_TRUE {$c = ap_true}
        | ANTLR_FALSE {$c = ap_false}
        ;

ap returns [Clause c]
		: ANTLR_VARIABLE ANTLR_WS* ANTLR_OPERATOR ANTLR_WS*ANTLR_B {$c = AP(None, parse_c($ANTLR_VARIABLE.text), parse_ap_operator($ANTLR_OPERATOR.text), float($ANTLR_B.text), [regex.sub("((^\d+(\.\d+)?)|(^\+\d+(\.\d+)?)|(^\-\d+(\.\d+)?))\ *", '', $ANTLR_VARIABLE.text)])}
		| ANTLR_C ANTLR_WS* ANTLR_VARIABLE ANTLR_WS* ANTLR_OPERATOR ANTLR_WS*ANTLR_B {$c = AP(None, parse_ap_tuple($ANTLR_C.text), parse_ap_operator($ANTLR_OPERATOR.text), float($ANTLR_B.text), parse_ap_tuple($ANTLR_VARIABLE.text))}
		;
		
simp returns [Clause c]
        : ANTLR_VARIABLE {$c = AP($ANTLR_VARIABLE.text)}
		| ap {$c = $ap.c}
        | constant {$c = $constant.c}
        ;

literal returns [Clause c]
        : ANTLR_NOT literal {$c = NOT($literal.c)}
        | simp {$c = $simp.c}
		| ANTLR_LBR release ANTLR_RBR {$c = $release.c}
        ;

conjunction returns [Clause c]
		@init{thelist = list()}
		: literal {$c = $literal.c}
		| a = literal {thelist.append($a.c);} (ANTLR_AND b = literal {thelist.append($b.c)})* {$c = parse_conjunction(thelist)}
        ;
		
disjunction returns [Clause c]
		@init{thelist = list()}
		: conjunction {$c = $conjunction.c}
		| a = literal {thelist.append($a.c);} (ANTLR_OR b = literal {thelist.append($b.c)})* {$c = parse_disjunction(thelist)}
        ;
		
implication returns [Clause c]
		: disjunction {$c = $disjunction.c}
        | a = implication ANTLR_IMPLIES b = implication {$c = IMPLIES($a.c, $b.c)}
        ;
		
globally returns [Clause c]
		: implication {$c = $implication.c}
		| ANTLR_GLOBALLY ANTLR_LIMIT_1 ANTLR_LIMIT_2 a = literal {$c = GLOBALLY($a.c, int($ANTLR_LIMIT_1.text.strip('[')), int($ANTLR_LIMIT_2.text.strip(',').strip(']')))}
		| ANTLR_GLOBALLY a = literal {$c = GLOBALLY($a.c)}
		;

myfinally returns [Clause c]
		: globally {$c = $globally.c}
		| ANTLR_FINALLY ANTLR_LIMIT_1 ANTLR_LIMIT_2 a = literal {$c = FINALLY($a.c, int($ANTLR_LIMIT_1.text.strip('[')), int($ANTLR_LIMIT_2.text.strip(',').strip(']')))}
		| ANTLR_FINALLY a = literal {$c = FINALLY($a.c)}
		;
		
mynext returns [Clause c]
		: myfinally {$c = $myfinally.c}
		| ANTLR_NEXT ANTLR_LIMIT_1']' a = literal {$c = NEXT($a.c, int($ANTLR_LIMIT_1.text.strip('[')))}
		| ANTLR_NEXT a = literal {$c = NEXT($a.c)}
		;
		
until returns [Clause c]
		: mynext {$c = $mynext.c}
		| a = until (ANTLR_UNTIL ANTLR_LIMIT_1 ANTLR_LIMIT_2) b = until {$c = UNTIL($a.c, $b.c, int($ANTLR_LIMIT_1.text.strip('[')), int($ANTLR_LIMIT_2.text.strip(',').strip(']')))}
		| a = until (ANTLR_UNTIL) b = until {$c = UNTIL($a.c, $b.c)}
		;
		
release returns [Clause c]
		: until {$c = $until.c}
		| a = release (ANTLR_RELEASE ANTLR_LIMIT_1 ANTLR_LIMIT_2) b = release {$c = RELEASE($a.c, $b.c, int($ANTLR_LIMIT_1.text.strip('[')), int($ANTLR_LIMIT_2.text.strip(',').strip(']')))}
		| a = release (ANTLR_RELEASE) d = until {$c = RELEASE($a.c, $d.c)}
		;
		
start returns [Clause c]
		: EOF {$c = ap_true}
		| a = release EOF {$c = $a.c}
		;

// Variables cannot be named just 'G', 'F', 'N', 'o', 'U' or 'R' since these are keywords of the grammar.
fragment F_NUM	: ('-'|'+')?((('0'..'9')*'.'('0'..'9')+)|('0'..'9')+);
ANTLR_B			: F_NUM;
ANTLR_C			: ('('(F_NUM','ANTLR_WS*)+F_NUM')^T');
fragment F_VAR 	: [A-EH-MO-QS-TV-Za-np-z_@][A-Za-z0-9_]*;
ANTLR_VARIABLE	: ('('(F_VAR','ANTLR_WS*)+F_VAR')' | F_NUM ANTLR_WS* F_VAR | F_VAR);
ANTLR_OPERATOR	: '==' | '!=' | '<=' | '>=' | '<' | '>';
ANTLR_TRUE     	: 'true';
ANTLR_FALSE    	: 'false';
ANTLR_LBR      	: '(';
ANTLR_RBR      	: ')';
ANTLR_NOT      	: '!';
ANTLR_AND      	: '&';
ANTLR_OR		: '|';
ANTLR_IMPLIES	: '->';
ANTLR_LIMIT_1	: '['F_NUM;
ANTLR_LIMIT_2	: ','ANTLR_WS*F_NUM']';
ANTLR_GLOBALLY 	: '[]' | 'G';
ANTLR_FINALLY	: '<>' | 'F';
ANTLR_NEXT		: 'o' | 'N';
ANTLR_UNTIL		: 'U';
ANTLR_RELEASE	: 'R';
ANTLR_WS       	: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
