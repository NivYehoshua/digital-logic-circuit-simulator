import logic_gates

def shunting_yard(func_split: list):
    """
        Converts an infix boolean expression into Reverse Polish Notation (RPN)
        based on Dijkstra's Shunting Yard algorithm.
    """
    op_gates = ['NOT', 'AND', 'OR']
    output_queue = []
    operator_stack = []
    for elem in func_split:
        # Operands (variables) go directly to the output queue
        if len(elem) == 1 and elem.isalpha():
            output_queue.append(elem)

        if elem.upper() in op_gates:
            while True:
                if len(operator_stack) == 0 or operator_stack[-1] == '(':
                    operator_stack.append(elem.upper())
                    break
                # Precedence check using list indices (NOT > AND > OR)
                if op_gates.index(elem.upper()) >= op_gates.index(operator_stack[-1]):
                    output_queue.append(operator_stack.pop().upper())
                else:
                    operator_stack.append(elem.upper())
                    break

        if elem == '(':
            operator_stack.append('(')

        if elem == ')':
            while True:
                if operator_stack[-1] == '(':
                    operator_stack.pop()
                    break
                output_queue.append(operator_stack.pop())

    # Flush any remaining operators
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue


def circuit_builder(bool_func: str, inputs_dict: dict | None = None):
    """
        Builds a circuit of LogicGate objects from a boolean expression string.
        Uses inputs_dict as a symbol table to ensure multiple instances of the same
        variable point to the exact same InputPin object in memory.
    """
    if inputs_dict is None:
        inputs_dict = {}
    trans_bool_func = shunting_yard(bool_func.split())
    output_stack = []

    for elem in trans_bool_func:
        # Handle inputs
        if len(elem) == 1:
            # Use existing pin if already created, otherwise create a new one
            if elem in inputs_dict:
                output_stack.append(inputs_dict[elem])
            else:
                new_input_pin = logic_gates.InputPin(elem)
                output_stack.append(new_input_pin)
                inputs_dict[elem] = new_input_pin

        # Handle logic gates (wiring them bottom-up)
        if elem == 'NOT':
            new_not_gate = logic_gates.NotGate()
            inp_1 = output_stack.pop()
            inp_1.next_gates = [new_not_gate]
            inp_1.input_next()
            output_stack.append(new_not_gate)

        if elem == 'AND':
            new_and_gate = logic_gates.AndGate()
            inp_1 = output_stack.pop()
            inp_1.next_gates = [new_and_gate]
            inp_1.input_next()
            inp_2 = output_stack.pop()
            inp_2.next_gates = [new_and_gate]
            inp_2.input_next()
            output_stack.append(new_and_gate)

        if elem == 'OR':
            new_or_gate = logic_gates.OrGate()
            inp_1 = output_stack.pop()
            inp_1.next_gates = [new_or_gate]
            inp_1.input_next()
            inp_2 = output_stack.pop()
            inp_2.next_gates = [new_or_gate]
            inp_2.input_next()
            output_stack.append(new_or_gate)

    # The last remaining item in the stack is the output gate of the circuit
    return output_stack[0]




