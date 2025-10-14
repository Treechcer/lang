class TokenType():
    Number = "NUMBER"
    Identifier = "IDENTIFIER"
    Equals = "EQUALS"
    OpenParam = "OPENPARAM"
    CloseParam = "CLOSEPARAM"
    BinaryOperator = "BINARYOPERATOR"
    Let = "LET"

class Token():
    def __init__(self, value : str, type : TokenType):
        self.value = value
        self.type = type

KEYWORDS = {
    "let" : TokenType.Let,
}

def token(value : str, type : TokenType):
    return Token(value, type)

def isalpha(src : str):
    return src.upper() != src.lower()

def isint(src : str):
    c = ord(src)
    bounds = [ord("0"), ord("9")]
    return (c >= bounds[0] and c <= bounds[1])

def isskipable(src : str):
    return src == " " or src == "\n" or src == "\t"

def tokenise(source : str) -> token:
    token = []
    src = list(source)

    while (len(src) > 0):
        if (src[0] == "("):
            token.append(Token(src.pop(0), TokenType.OpenParam))
        elif (src[0] == ")"):
            token.append(Token(src.pop(0), TokenType.CloseParam))
        elif (src[0] == "+" or src[0] == "-" or src[0] == "*" or src[0] == "/"):
            token.append(Token(src.pop(0), TokenType.BinaryOperator))
        elif (src[0] == "="):
            token.append(Token(src.pop(0), TokenType.Equals))
        else:
            #number token
            if (isint(src[0])):
                num = ""
                while len(src) > 0 and isint(src[0]):
                    num += src.pop(0)
                token.append(Token(num, TokenType.Number))
            elif (isalpha(src[0])):
                id = ""
                while len(src) > 0 and isalpha(src[0]):
                    id += src.pop(0)
                
                reserved = KEYWORDS.get(id, None)

                if reserved is not None:
                    token.append(Token(id, TokenType.Identifier))
                else:
                    token.append(Token(id, reserved))
            elif (isskipable(src[0])):
                src.pop(0)
            else:
                print("Unrecognised character found in src", src[0])
                exit

    print(token[0].value, token[1].value, token[2].value)
    return token

tokenise("hello = 5")