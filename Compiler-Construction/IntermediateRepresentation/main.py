from tac_generator import TACGenerator

# Zara program in a simple format with assignments, expressions, control structures, and method calls
zara_code = """
x = 5
y = 10
z = x + y
if x > y
max = x
end_if
result = add(x, y)
"""

# Instantiate the TAC generator
tac_generator = TACGenerator()
tac_generator.generate_tac(zara_code)

# Print generated TAC code
print("Generated Intermediate Representation (TAC):")
for line, comment in tac_generator.get_code():
    if comment:
        print(f"{line} // {comment}")
    else:
        print(line)
