# Generated from TemporalLogic.g4 by ANTLR 4.6
from antlr4 import *

from ..temporallogic import *
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


# This class defines a complete listener for a parse tree produced by TemporalLogicParser.
class TemporalLogicListener(ParseTreeListener):

    # Enter a parse tree produced by TemporalLogicParser#constant.
    def enterConstant(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#constant.
    def exitConstant(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#ap.
    def enterAp(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#ap.
    def exitAp(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#simp.
    def enterSimp(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#simp.
    def exitSimp(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#literal.
    def enterLiteral(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#literal.
    def exitLiteral(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#conjunction.
    def enterConjunction(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#conjunction.
    def exitConjunction(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#disjunction.
    def enterDisjunction(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#disjunction.
    def exitDisjunction(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#implication.
    def enterImplication(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#implication.
    def exitImplication(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#globally.
    def enterGlobally(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#globally.
    def exitGlobally(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#myfinally.
    def enterMyfinally(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#myfinally.
    def exitMyfinally(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#mynext.
    def enterMynext(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#mynext.
    def exitMynext(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#until.
    def enterUntil(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#until.
    def exitUntil(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#release.
    def enterRelease(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#release.
    def exitRelease(self, ctx):
        pass


    # Enter a parse tree produced by TemporalLogicParser#start.
    def enterStart(self, ctx):
        pass

    # Exit a parse tree produced by TemporalLogicParser#start.
    def exitStart(self, ctx):
        pass


