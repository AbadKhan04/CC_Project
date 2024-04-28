from lexer import lex
from parse import Parser

def interpret(code):
    variables = {}
    tokens = lex(code)
    print("Tokens: ",tokens)    # Print out the tokens for debugging
    parser = Parser(tokens, variables)
    parser.parse()

if __name__ == "__main__":
    with open("sample.math", "r") as file:
        code = file.read()
    interpret(code)
