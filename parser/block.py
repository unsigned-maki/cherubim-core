BLOCK = {
    "BLOCK_NOP": 0,
    "BLOCK_CHAIN": 1,
    "BLOCK_DEFINE": 2,
    "BLOCK_IF": 3,
    "BLOCK_IFF": 4,
    "BLOCK_NOT": 5,
    "BLOCK_AND": 6,
    "BLOCK_NAND": 7,
    "BLOCK_OR": 8,
    "BLOCK_XOR": 9,
    "BLOCK_NOR": 10,
    "BLOCK_XNOR": 11,
    "BLOCK_IDENTIFIER": 12,
    "BLOCK_STATEMENT": 13
}


class Block:

    def __init__(self, type, inner):
        match type:
            case "OP_DEFINE":
                self.type = "BLOCK_DEFINE"
            case "OP_IF":
                self.type = "BLOCK_IF"
            case "OP_IFF":
                self.type = "BLOCK_IFF"
            case "OP_NOT":
                self.type = "BLOCK_NOT"
            case "OP_AND":
                self.type = "BLOCK_AND"
            case "OP_NAND":
                self.type = "BLOCK_NAND"
            case "OP_OR":
                self.type = "BLOCK_OR"
            case "OP_XOR":
                self.type = "BLOCK_XOR"
            case "OP_NOR":
                self.type = "BLOCK_NOR"
            case "OP_XNOR":
                self.type = "BLOCK_XNOR"
            case "ID_IDENTIFIER":
                self.type = "BLOCK_IDENTIFIER"
            case "LTRL_TRUE":
            case "LTRL_FALSE":
                self.type = "BLOCK_STATEMENT"
            case "BLOCK_CHAIN":
                self.type = "BLOCK_CHAIN"
            case _:
                self.type = "BLOCK_NOP"

        self.inner = inner
