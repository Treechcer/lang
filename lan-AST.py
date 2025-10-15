global NodeType

class Stmt():
    def __init__(self, nodeTypeL):
        if nodeTypeL in NodeType:
            self.nodeType = nodeTypeL

class program(Stmt):
    def __init__(self):
        super().__init__("Program")
        # Stmt array
        self.body

class Expression(Stmt):
    pass

class BinaryExpression(Expression):
    def __init__(self, operator, left, right):
        super().__init__("BinaryExpr")
        self.left = left
        self.right = right
        self.operator = operator

class identifier(Expression):
    def __init__(self, symbol):
        super().__init__("Identifier")
        self.symbol = symbol

class NumericLiteral(Expression):
    def __init__(self, value):
        super().__init__("NumericLiteral")
        self.value = value

NodeType = ["Program", "NumericLiteral", "Identifier", "BinaryExpr"]
