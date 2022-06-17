import memory
from . import chain


def resolve_braces(braces, brace_table):
    for i in range(0, len(braces)):
        if braces[i][1] == "SYN_BRACE_OPEN" and braces[i + 1][1] == "SYN_BRACE_CLOSE":
            brace_table[braces[i][0]] = braces[i + 1][0]

    for k in brace_table:
        if (k, "SYN_BRACE_OPEN") in braces:
            braces.remove((k, "SYN_BRACE_OPEN"))
        if (brace_table[k], "SYN_BRACE_CLOSE") in braces:
            braces.remove((brace_table[k], "SYN_BRACE_CLOSE"))

    if len(braces) == 0:
        return True
    else:
        return resolve_braces(braces, brace_table)


def parse(tokens):
    braces = []

    for token in tokens:
        if token.type == "SYN_BRACE_OPEN":
            braces.append((token.id, "SYN_BRACE_OPEN"))
        elif token.type == "SYN_BRACE_CLOSE":
            braces.append((token.id, "SYN_BRACE_CLOSE"))

    brace_table = {}

    resolve_braces(braces, brace_table)

    return chain.Chain(tokens, 0, len(tokens) - 1, brace_table, memory.SymbolTable())
