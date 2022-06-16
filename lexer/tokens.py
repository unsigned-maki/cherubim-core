TOKENS = {
    ":=": "OP_DEFINE",
    "IF": "OP_IF",
    "IFF": "OP_IFF",
    "NOT": "OP_NOT",
    "AND": "OP_AND",
    "NAND": "OP_NAND",
    "OR": "OP_OR",
    "XOR": "OP_XOR",
    "NOR": "OP_NOR",
    "XNOR": "OP_XNOR",
    "TRUE": "LTRL_TRUE",
    "FALSE": "LTRL_FALSE",
    "T": "LTRL_TRUE",
    "F": "LTRL_FALSE",
    "1": "LTRL_TRUE",
    "0": "LTRL_FALSE",
    "(": "SYN_BRACE_OPEN",
    "[": "SYN_BRACE_OPEN",
    "{": "SYN_BRACE_OPEN",
    ")": "SYN_BRACE_CLOSE",
    "]": "SYN_BRACE_CLOSE",
    "}": "SYN_BRACE_CLOSE",
    ";": "SYN_SEPERATOR"
}

COMPLEX_TOKENS = [
    (":", "=")
]

SYN_TOKENS = [
    "(",
    "[",
    "{",
    ")",
    "]",
    "}",
    ";"
]

TOKEN = {
    "OP_DEFINE": 0,
    "OP_IF": 1,
    "OP_IFF": 2,
    "OP_NOT": 3,
    "OP_AND": 4,
    "OP_NAND": 5,
    "OP_OR": 6,
    "OP_XOR": 7,
    "OP_NOR": 8,
    "OP_XNOR": 9,
    "ID_IDENTIFIER": 10,
    "SYN_SEPERATOR": 11,
    "SYN_BRACE_OPEN": 12,
    "SYN_BRACE_CLOSE": 13,
    "LTRL_TRUE": 14,
    "LTRL_FALSE": 15,
    "NIL": 16
}


class Token:

    def __init__(self, id, type, literal):
        self.id = id
        self.literal = literal

        if type in TOKEN:
            self.type = type
        else:
            self.type = "NIL"
