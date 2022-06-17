from .block import Block
from lexer.tokens import Token, TOKEN
from .rules import CHAIN_RULES as cr


class Chain:

    def __init__(self, tokens, from_, to, braces, memory):
        self.inner = []

        i = from_

        while i <= to:

            current = tokens[i]
            previous = tokens[i - 1] if i > from_ else Token(-1, "NIL", "NIL")
            next = tokens[i + 1] if i < to else Token(-1, "NIL", "NIL")

            match current.type:
                case "SYN_BRACE_OPEN":
                    if braces.get(current.id, False):
                        self.inner.append(
                            Block(
                                "BLOCK_CHAIN",
                                Chain(tokens, current.id + 1, braces[current.id] - 1, braces, memory)
                            )
                        )
                        i = braces[current.id]
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "SYN_BRACE_CLOSE":
                    continue
                case "LTRL_TRUE" | "LTRL_FALSE":
                    if previous.type in cr["LTRL"]["previous"] and next.type in cr["LTRL"]["next"]:
                        self.inner.append(Block(current.type, current.literal))
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "OP_IF" | "OP_IFF" | "OP_AND" | "OP_NAND" | "OP_OR" | "OP_XOR" | "OP_NOR" | "OP_XNOR":
                    if previous.type in cr["OP"]["previous"] and next.type in cr["OP"]["next"]:
                        self.inner.append(Block(current.type, current.literal))
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "OP_NOT":
                    if previous.type in cr["OP_NOT"]["previous"] and next.type in cr["OP_NOT"]["next"]:
                        self.inner.append(Block(current.type, current.literal))
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "OP_DEFINE":
                    if previous.type in cr["OP_DEFINE"]["previous"] and next.type in cr["OP_DEFINE"]["next"]:
                        self.inner.append(Block(current.type, current.literal))
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "ID_IDENTIFIER":
                    if previous.type in cr["ID"]["previous"] and next.type in cr["ID"]["next"]:
                        self.inner.append(Block(current.type, current.literal))
                    else:
                        raise ValueError("Error")
                        #  TODO: raise error
                case "NIL":
                    continue
                case _:
                    raise ValueError("Error")
                    #  TODO: raise error

            i += 1
