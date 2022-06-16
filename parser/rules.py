CHAIN_RULES = {
    "LTRL": {
        "previous": [
            "OP_DEFINE",
            "OP_IF",
            "OP_IFF",
            "OP_NOT",
            "OP_AND",
            "OP_NAND",
            "OP_OR",
            "OP_XOR",
            "OP_NOR",
            "OP_XNOR",
            "ID_IDENTIFIER",
            "SYN_SEPERATOR",
            "NIL"
        ],
        "next": [
            "OP_DEFINE",
            "OP_IF",
            "OP_IFF",
            "OP_NOT",
            "OP_AND",
            "OP_NAND",
            "OP_OR",
            "OP_XOR",
            "OP_NOR",
            "OP_XNOR",
            "ID_IDENTIFIER",
            "SYN_BRACE_CLOSE",
            "NIL"
        ]
    },
    "OP": {
        "previous": [
            "ID_IDENTIFIER",
            "SYN_BRACE_CLOSE",
            "LTRL_TRUE",
            "LTRL_FALSE",
            "NIL"
        ],
        "next": [
            "ID_IDENTIFIER",
            "SYN_BRACE_OPEN",
            "LTRL_TRUE",
            "LTRL_FALSE",
            "NIL"
        ]
    },
    "OP_NOT": {
        "previous": [
            "OP_DEFINE",
            "OP_IF",
            "OP_IFF",
            "OP_NOT",
            "OP_AND",
            "OP_NAND",
            "OP_OR",
            "OP_XOR",
            "OP_NOR",
            "OP_XNOR",
            "SYN_BRACE_OPEN"
        ],
        "next": [
            "ID_IDENTIFIER",
            "LTRL_TRUE",
            "LTRL_FALSE",
            "SYN_BRACE_OPEN"
        ]
    },
    "ID": {
        "previous": [
            "OP_DEFINE",
            "OP_IF",
            "OP_IFF",
            "OP_NOT",
            "OP_AND",
            "OP_NAND",
            "OP_OR",
            "OP_XOR",
            "OP_NOR",
            "OP_XNOR",
            "SYN_BRACE_OPEN"
        ],
        "next": [
            "OP_DEFINE",
            "OP_IF",
            "OP_IFF",
            "OP_NOT",
            "OP_AND",
            "OP_NAND",
            "OP_OR",
            "OP_XOR",
            "OP_NOR",
            "OP_XNOR",
            "SYN_BRACE_OPEN",
            "SYN_BRACE_CLOSE"
        ]
    }
}