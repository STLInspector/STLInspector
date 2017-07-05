# Generated from TemporalLogic.g4 by ANTLR 4.5.2
from antlr4 import *
from STLInspector.core.temporallogic import *
from TemporalLogicParser import TemporalLogicParser
import operator

# This class defines a complete generic visitor for a parse tree produced by TemporalLogicParser.
# todo: I assume the visitor pattern was not used correctly

class ParseException(Exception):

    def __init__(self, msg, line, column):
        super(ParseException, self).__init__(msg)
        self.input_line = line
        self.input_column = column

class TemporalLogicVisitor(ParseTreeVisitor):

    def visit(self, ctx):
        # hack, visti* attributes are not called otherwise
        classname = ctx.__class__.__name__
        if not classname.endswith('Context'):
            return super(TemporalLogicVisitor, self).visit(ctx)
        fct = 'visit' + classname[:-len('Context')]
        if not hasattr(self, fct):
            return super(TemporalLogicVisitor, self).visit(ctx)
        return getattr(self, fct)(ctx)


    # Visit a parse tree produced by TemporalLogicParser#NotCase.
    def visitNotCase(self, ctx):
        return NOT(self.visit(ctx.child))


    # Visit a parse tree produced by TemporalLogicParser#TrueCase.
    def visitTrueCase(self, ctx):
        return ap_true


    # Visit a parse tree produced by TemporalLogicParser#FalseCase.
    def visitFalseCase(self, ctx):
        return ap_false


    # Visit a parse tree produced by TemporalLogicParser#BooleanVarCase.
    def visitBooleanVarCase(self, ctx):
        return AP(ctx.children[0].getText())


    def visitScaledVariableCase(self, ctx):
        if len(ctx.children) == 1:
            return 1, ctx.children[0].getText()
        elif len(ctx.children) == 3 and ctx.children[1].getText() == '*':
            return float(ctx.children[0].getText()), ctx.children[2].getText()
        else:
            raise ParseException('Format of scaled variable not correct',
                                 ctx.start.line, ctx.start.column)

     # Visit a parse tree produced by TemporalLogicParser#APCase.
    def visitAPCase(self, ctx):
        # children list has to consist of a sign scaled_variable sequence
        factors = []
        variables = []
        # first sign is optional
        factor = 1
        for child in ctx.children[:-2]:
            if isinstance(child, tree.Tree.TerminalNode):
                # + or - sign
                if child.getText() == '+':
                    factor = 1
                elif child.getText() == '-':
                    factor = -1
                else:
                    raise ParseException(
                        'Expected + or - sign, but found "{}"'.format(child.getText()),
                        child.start.line,
                        child.start.column)
            elif isinstance(child, TemporalLogicParser.Pos_scaled_variableContext):
                scale, variable = self.visitScaledVariableCase(child)
                factors.append(factor*scale)
                variables.append(variable)
                factor = 1

        cmpop = {
            '>' : operator.gt,
            '<' : operator.lt,
            '>=' : operator.ge,
            '<=' : operator.le,
            '==' : operator.eq,
            "!=" : operator.ne
        }.get(ctx.children[-2].getText(), None)
        if cmpop is None:
            raise ParseException('Unknown compare operator "{}"'.format(ctx.children[-2].getText()),
                                 ctx.children[-2].start.line,
                                 ctx.children[-2].start.column)
        return AP(None, factors, cmpop, float(ctx.children[-1].getText()), variables)


    # Visit a parse tree produced by TemporalLogicParser#OrCase.
    def visitOrCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return OR(left, right)


    # Visit a parse tree produced by TemporalLogicParser#AndCase.
    def visitAndCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return AND(left, right)


    # Visit a parse tree produced by TemporalLogicParser#ImpliesCase.
    def visitImpliesCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return IMPLIES(left, right)


    # Visit a parse tree produced by TemporalLogicParser#GloballyCase.
    def visitGloballyCase(self, ctx):
        child = self.visit(ctx.child)
        leftlimit = float(ctx.leftlimit.text) if ctx.leftlimit is not None else None
        rightlimit = float(ctx.rightlimit.text) if ctx.rightlimit is not None else None
        return GLOBALLY(child, leftlimit, rightlimit)


    # Visit a parse tree produced by TemporalLogicParser#FinallyCase.
    def visitFinallyCase(self, ctx):
        child = self.visit(ctx.child)
        leftlimit = float(ctx.leftlimit.text) if ctx.leftlimit is not None else None
        rightlimit = float(ctx.rightlimit.text) if ctx.rightlimit is not None else None
        return FINALLY(child, leftlimit, rightlimit)


    # Visit a parse tree produced by TemporalLogicParser#NextCase.
    def visitNextCase(self, ctx):
        child = self.visit(ctx.child)
        offset = float(ctx.offset.text) if ctx.offset is not None else None
        return NEXT(child, offset)


    # Visit a parse tree produced by TemporalLogicParser#UntilCase.
    def visitUntilCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        leftlimit = float(ctx.leftlimit.text) if ctx.leftlimit is not None else None
        rightlimit = float(ctx.rightlimit.text) if ctx.rightlimit is not None else None
        return UNTIL(left, right, leftlimit, rightlimit)


    # Visit a parse tree produced by TemporalLogicParser#ReleaseCase.
    def visitReleaseCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        leftlimit = float(ctx.leftlimit.text) if ctx.leftlimit is not None else None
        rightlimit = float(ctx.rightlimit.text) if ctx.rightlimit is not None else None
        return RELEASE(left, right, leftlimit, rightlimit)

    # Visit a parse tree produced by TemporalLogicParser#ParensCase.
    def visitBracketCase(self, ctx):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TemporalLogicParser#start.
    def visitStart(self, ctx):
        return self.visit(ctx.child)

