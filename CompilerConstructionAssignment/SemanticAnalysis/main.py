from zara_parser_with_translation import parser
from symbol_table import symbol_table

def run_test(program_code):
    print("Testing Program:")
    print(program_code)
    print("Output:")
    try:
        parser.parse(program_code)
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 30)

def test_correct_variable_usage():
    program = "int a = 5; int b = 10; a = b + 2;"
    run_test(program)

def test_incorrect_type_assignment():
    program = "float c = 2.5; int d = 3; d = c;"
    run_test(program)

def test_scope_violation():
    program = "if (true) { int e = 4; } e = 5;"
    run_test(program)

def test_array_type_consistency():
    program = "int arr[5]; arr[0] = 5; arr[1] = \"test\";"
    run_test(program)

def test_stack_type_consistency():
    program = "stack<int> s; s.push(5); s.push(\"test\"); int top = s.pop();"
    run_test(program)

if __name__ == "__main__":
    symbol_table.__init__()
    print("Running Semantic Analyzer Tests...\n")
    test_correct_variable_usage()
    test_incorrect_type_assignment()
    test_scope_violation()
    test_array_type_consistency()
    test_stack_type_consistency()
    print("\nAll tests completed.")
