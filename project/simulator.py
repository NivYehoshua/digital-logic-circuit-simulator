import circuit_builder

# Get circuit specifications
num_of_inputs = int(input('Enter number of inputs: '))
op_gates = ['NOT', 'AND', 'OR']
other_options = ['(', ' ', ')']

# Input validation loop (Defensive programming against bad user input)
check_input = True
while check_input:
    try:
        bool_func = input('Enter your boolean function: ')
        bool_func_split = bool_func.split()
        for elem in bool_func_split:
            if (not (elem.upper() in op_gates)) and (not (elem in other_options) and (not (len(elem) == 1 and elem.isalpha()))):
                raise ValueError
        check_input = False

    except ValueError:
        print('Please enter a valid boolean function')

# Build the physical circuit and populate the symbol table (inputs_dict)
inputs_dict = {}
final_circuit = circuit_builder.circuit_builder(bool_func, inputs_dict)

# Sanity check: Verify declared inputs match the actual variables used in the function
if len(inputs_dict) != num_of_inputs:
    raise ValueError

print("-" * 30)

# Generate and evaluate truth table for all possible states
for i in range(2**num_of_inputs):
    # Create binary string with leading zeros
    curr_inputs = (bin(i)[2:].zfill(num_of_inputs))
    j = 0
    # Feed the binary vector into the circuit's input pins
    for key in inputs_dict:
        inputs_dict[key].set_state(int(curr_inputs[j]))
        j += 1
    print(f"Inputs: {curr_inputs} | Output: {final_circuit.output()}")

