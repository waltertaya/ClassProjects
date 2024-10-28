class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.types = {}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Variable '{name}' already declared.")
        self.symbols[name] = True  # Mark variable as declared
        self.types[name] = var_type  # Store variable type

    def assign(self, name, value_type):
        if name not in self.symbols:
            raise Exception(f"Variable '{name}' not declared.")
        if self.types[name] != value_type:
            raise Exception(f"Type mismatch: cannot assign {value_type} to {self.types[name]}.")

    def get_type(self, name):
        return self.types.get(name, None)

# Initialize the symbol table
symbol_table = SymbolTable()
