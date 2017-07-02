# Generated from TemporalLogic.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\25@\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\5\2\13\n\2\3\2\3")
        buf.write(u"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\3\3")
        buf.write(u"\7\3\33\n\3\f\3\16\3\36\13\3\3\3\3\3\5\3\"\n\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\5\3*\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\7\38\n\3\f\3\16\3;\13\3\3\4\3")
        buf.write(u"\4\3\4\3\4\2\3\4\5\2\4\6\2\3\3\2\17\20H\2\n\3\2\2\2\4")
        buf.write(u")\3\2\2\2\6<\3\2\2\2\b\t\7\21\2\2\t\13\7\16\2\2\n\b\3")
        buf.write(u"\2\2\2\n\13\3\2\2\2\13\f\3\2\2\2\f\r\7\22\2\2\r\3\3\2")
        buf.write(u"\2\2\16\17\b\3\1\2\17\20\7\t\2\2\20*\5\4\3\7\21*\7\7")
        buf.write(u"\2\2\22*\7\b\2\2\23*\7\22\2\2\24\26\t\2\2\2\25\24\3\2")
        buf.write(u"\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\34\5\2\2\2\30\31")
        buf.write(u"\t\2\2\2\31\33\5\2\2\2\32\30\3\2\2\2\33\36\3\2\2\2\34")
        buf.write(u"\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2")
        buf.write(u"\37!\7\6\2\2 \"\t\2\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2")
        buf.write(u"\2#$\7\21\2\2$*\3\2\2\2%&\7\f\2\2&\'\5\4\3\2\'(\7\r\2")
        buf.write(u"\2(*\3\2\2\2)\16\3\2\2\2)\21\3\2\2\2)\22\3\2\2\2)\23")
        buf.write(u"\3\2\2\2)\25\3\2\2\2)%\3\2\2\2*9\3\2\2\2+,\f\6\2\2,-")
        buf.write(u"\7\n\2\2-8\5\4\3\7./\f\5\2\2/\60\7\13\2\2\608\5\4\3\6")
        buf.write(u"\61\62\f\4\2\2\62\63\7\3\2\2\63\64\7\4\2\2\64\65\7\21")
        buf.write(u"\2\2\65\66\7\5\2\2\668\5\4\3\5\67+\3\2\2\2\67.\3\2\2")
        buf.write(u"\2\67\61\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\5\3")
        buf.write(u"\2\2\2;9\3\2\2\2<=\5\4\3\2=>\7\2\2\3>\7\3\2\2\2\t\n\25")
        buf.write(u"\34!)\679")
        return buf.getvalue()


class TemporalLogicParser ( Parser ):

    grammarFileName = "TemporalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'U'", u"'['", u"']'", u"<INVALID>", 
                     u"'true'", u"'false'", u"'!'", u"'&'", u"'|'", u"'('", 
                     u"')'", u"'*'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"TOKEN_OPERATOR", u"TOKEN_TRUE", u"TOKEN_FALSE", 
                      u"TOKEN_NOT", u"TOKEN_AND", u"TOKEN_OR", u"TOKEN_LB", 
                      u"TOKEN_RB", u"TOKEN_MULT", u"TOKEN_ADD", u"TOKEN_SUB", 
                      u"TOKEN_POSNUMBER", u"TOKEN_VARIABLE", u"TOKEN_GLOBALLY", 
                      u"TOKEN_FINALLY", u"TOKEN_WS" ]

    RULE_pos_scaled_variable = 0
    RULE_formula = 1
    RULE_start = 2

    ruleNames =  [ u"pos_scaled_variable", u"formula", u"start" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TOKEN_OPERATOR=4
    TOKEN_TRUE=5
    TOKEN_FALSE=6
    TOKEN_NOT=7
    TOKEN_AND=8
    TOKEN_OR=9
    TOKEN_LB=10
    TOKEN_RB=11
    TOKEN_MULT=12
    TOKEN_ADD=13
    TOKEN_SUB=14
    TOKEN_POSNUMBER=15
    TOKEN_VARIABLE=16
    TOKEN_GLOBALLY=17
    TOKEN_FINALLY=18
    TOKEN_WS=19

    def __init__(self, input):
        super(TemporalLogicParser, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Pos_scaled_variableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.Pos_scaled_variableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_VARIABLE(self):
            return self.getToken(TemporalLogicParser.TOKEN_VARIABLE, 0)

        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)

        def TOKEN_MULT(self):
            return self.getToken(TemporalLogicParser.TOKEN_MULT, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_pos_scaled_variable

        def enterRule(self, listener):
            if hasattr(listener, "enterPos_scaled_variable"):
                listener.enterPos_scaled_variable(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPos_scaled_variable"):
                listener.exitPos_scaled_variable(self)




    def pos_scaled_variable(self):

        localctx = TemporalLogicParser.Pos_scaled_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pos_scaled_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            _la = self._input.LA(1)
            if _la==TemporalLogicParser.TOKEN_POSNUMBER:
                self.state = 6
                self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 7
                self.match(TemporalLogicParser.TOKEN_MULT)


            self.state = 10
            self.match(TemporalLogicParser.TOKEN_VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.FormulaContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_formula

     
        def copyFrom(self, ctx):
            super(TemporalLogicParser.FormulaContext, self).copyFrom(ctx)


    class NotCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.NotCaseContext, self).__init__(parser)
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_NOT(self):
            return self.getToken(TemporalLogicParser.TOKEN_NOT, 0)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotCase"):
                listener.enterNotCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotCase"):
                listener.exitNotCase(self)


    class TrueCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.TrueCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_TRUE(self):
            return self.getToken(TemporalLogicParser.TOKEN_TRUE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTrueCase"):
                listener.enterTrueCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTrueCase"):
                listener.exitTrueCase(self)


    class BooleanVarCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.BooleanVarCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_VARIABLE(self):
            return self.getToken(TemporalLogicParser.TOKEN_VARIABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanVarCase"):
                listener.enterBooleanVarCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanVarCase"):
                listener.exitBooleanVarCase(self)


    class UntilCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.UntilCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterUntilCase"):
                listener.enterUntilCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUntilCase"):
                listener.exitUntilCase(self)


    class FalseCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.FalseCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_FALSE(self):
            return self.getToken(TemporalLogicParser.TOKEN_FALSE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterFalseCase"):
                listener.enterFalseCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFalseCase"):
                listener.exitFalseCase(self)


    class OrCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.OrCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_OR(self):
            return self.getToken(TemporalLogicParser.TOKEN_OR, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrCase"):
                listener.enterOrCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrCase"):
                listener.exitOrCase(self)


    class BracketCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.BracketCaseContext, self).__init__(parser)
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_LB(self):
            return self.getToken(TemporalLogicParser.TOKEN_LB, 0)
        def TOKEN_RB(self):
            return self.getToken(TemporalLogicParser.TOKEN_RB, 0)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBracketCase"):
                listener.enterBracketCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBracketCase"):
                listener.exitBracketCase(self)


    class AndCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.AndCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_AND(self):
            return self.getToken(TemporalLogicParser.TOKEN_AND, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndCase"):
                listener.enterAndCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndCase"):
                listener.exitAndCase(self)


    class APCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.APCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def pos_scaled_variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.Pos_scaled_variableContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.Pos_scaled_variableContext,i)

        def TOKEN_OPERATOR(self):
            return self.getToken(TemporalLogicParser.TOKEN_OPERATOR, 0)
        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)
        def TOKEN_ADD(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_ADD)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_ADD, i)
        def TOKEN_SUB(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_SUB)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_SUB, i)

        def enterRule(self, listener):
            if hasattr(listener, "enterAPCase"):
                listener.enterAPCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAPCase"):
                listener.exitAPCase(self)



    def formula(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = TemporalLogicParser.NotCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(TemporalLogicParser.TOKEN_NOT)
                self.state = 14
                localctx.child = self.formula(5)
                pass

            elif la_ == 2:
                localctx = TemporalLogicParser.TrueCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(TemporalLogicParser.TOKEN_TRUE)
                pass

            elif la_ == 3:
                localctx = TemporalLogicParser.FalseCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(TemporalLogicParser.TOKEN_FALSE)
                pass

            elif la_ == 4:
                localctx = TemporalLogicParser.BooleanVarCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(TemporalLogicParser.TOKEN_VARIABLE)
                pass

            elif la_ == 5:
                localctx = TemporalLogicParser.APCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                _la = self._input.LA(1)
                if _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 18
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 21
                self.pos_scaled_variable()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 22
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 23
                    self.pos_scaled_variable()
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 29
                self.match(TemporalLogicParser.TOKEN_OPERATOR)
                self.state = 31
                _la = self._input.LA(1)
                if _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 30
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 33
                self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                pass

            elif la_ == 6:
                localctx = TemporalLogicParser.BracketCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(TemporalLogicParser.TOKEN_LB)
                self.state = 36
                localctx.child = self.formula(0)
                self.state = 37
                self.match(TemporalLogicParser.TOKEN_RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = TemporalLogicParser.AndCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        self.match(TemporalLogicParser.TOKEN_AND)
                        self.state = 43
                        localctx.right = self.formula(5)
                        pass

                    elif la_ == 2:
                        localctx = TemporalLogicParser.OrCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(TemporalLogicParser.TOKEN_OR)
                        self.state = 46
                        localctx.right = self.formula(4)
                        pass

                    elif la_ == 3:
                        localctx = TemporalLogicParser.UntilCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        self.match(TemporalLogicParser.T__0)
                        self.state = 49
                        self.match(TemporalLogicParser.T__1)
                        self.state = 50
                        self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                        self.state = 51
                        self.match(TemporalLogicParser.T__2)
                        self.state = 52
                        localctx.right = self.formula(3)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.StartContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.child = None # FormulaContext

        def EOF(self):
            return self.getToken(TemporalLogicParser.EOF, 0)

        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_start

        def enterRule(self, listener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)




    def start(self):

        localctx = TemporalLogicParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.child = self.formula(0)
            self.state = 59
            self.match(TemporalLogicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




