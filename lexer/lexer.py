from . import tokens


def post_process(input):
    ignore_next = False
    tmp = " "
    chars = list(input)

    for i in range(0, len(chars)):
        if ignore_next:
            ignore_next = False
            continue

        if chars[i] in tokens.SYN_TOKENS:
            tmp += f" {chars[i]} "
            continue

        if i == len(chars) - 1:
            continue

        if (chars[i], chars[i + 1]) in tokens.COMPLEX_TOKENS:
            tmp += f" {chars[i]}{chars[i+1]} "
            ignore_next = True
            continue

        tmp += chars[i]

    return tmp


def split(input):
    split = []
    tmp = ""

    for i in input:
        if i in ['', ' ', '\n', '\t', '\b', '\r']:
            split.append(tmp)
            tmp = ""
            continue

        tmp += i.upper()

        if not len(split):
            continue

    return split


def lex(input):
    id_counter = 0
    new_tokens = []

    input = post_process(input)
    split_input = split(input)

    for i in split_input:
        if i not in ['', ' ', '\n', '\t', '\b', '\r']:
            if i in tokens.TOKENS:
                new_tokens.append(tokens.Token(id_counter, tokens.TOKENS[i], i))
            else:
                new_tokens.append(tokens.Token(id_counter, "ID_IDENTIFIER", i))

            id_counter += 1

    return new_tokens
