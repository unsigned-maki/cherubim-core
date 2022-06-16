SYMBOL = {
    "SYM_FUNCTION": 0,
    "SYM_LITERAL": 1,
    "SYM_NIL": 2
}


class Symbol:

    def __init__(self, type):
        if type not in SYMBOL:
            self.type = "SYM_NIL"
        else:
            self.type = type


class SymbolLiteral(Symbol):

    def __init__(self, literal):
        self.literal = literal
        super().__init__("SYM_LITERAL")

    def get(self):
        return self.literal

    def set(self, literal):
        self.literal = literal


class SymbolFunction(Symbol):

    def __init__(self, chain, arg_list):
        self.chain = chain
        self.arg_list = arg_list
        super().__init__("SYM_FUNCTION")

    def call(self, args):
        if len(args) == len(arg_list):
            #  TODO: implement resolving of chain
        else:
            #  TODO: implement error


class SymbolTable:

    def __init__(self):
        self.table = {}

    def __getitem__(self, key):
        return self.read(key)

    def __setitem__(self, key, value):
        return self.write(key, value)

    def read(self, key):
        if not key in self.table:
            return False
        else:
            return self.table[key]

    def write(self, key, value):
        if not isinstance(key, str) or not isinstance(value, Symbol):
            return False
        else:
            self.type[key] = value
            return True
