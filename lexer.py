import re

token_patterns = [
    (r"VAR", "VAR"),
    (r"ADD", "ADD"),
    (r"SUB", "SUB"),
    (r"MULTIPLY", "MULTIPLY"),
    (r"DIVIDE", "DIVIDE"),
    (r"SQUARE", "SQUARE"),
    (r"WRITE", "WRITE"),
    (r"READ", "READ"),
    (r"AND", "AND"),
    (r"OR", "OR"),
    (r"XOR", "XOR"),
    (r"NOT", "NOT"),
    (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER"),
    (r"[0-9]+", "NUMBER"),
    (r"=", "="),
    (r"\+", "+"),
    (r"-", "-"),
    (r"\*", "*"),
    (r"/", "/"),
    (r"\^", "^"),
    (r"==", "=="),
    (r"!=", "!="),
    (r">=", ">="),
    (r">", ">"),
    (r"<=", "<="),
    (r"<", "<"),
    (r"=", "="),
    (r"\(", "("),
    (r"\)", ")"),
    (r":", ":"),
    (r",", ","),
    (r"#.*", "COMMENT"),
    (r"\s+", None),  # Ignore whitespace
]

def lex(code):
    tokens = []
    while code:
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append((token_type, value))
                code = code[len(value):].lstrip()
                break
        else:
            raise SyntaxError("Invalid token: {}".format(code))
    return tokens
