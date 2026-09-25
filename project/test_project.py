import logic_gates, circuit_builder

def test_logic_gates():
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    and_outputs = [0, 0, 0, 1]
    or_outputs = [0, 1, 1, 1]
    and_gate = logic_gates.AndGate()
    not_gate = logic_gates.NotGate()
    or_gate = logic_gates.OrGate()
    for i in range(4):
        and_gate.inputs = inputs[i]
        assert and_gate.output() == and_outputs[i]
        or_gate.inputs = inputs[i]
        assert or_gate.output() == or_outputs[i]

    not_gate.inputs = [1]
    assert not_gate.output() == 0
    not_gate.inputs = [0]
    assert not_gate.output() == 1


def test_circuit_builder():
    assert circuit_builder.shunting_yard('A or B'.split()) == ['A', 'B', 'OR']
    assert circuit_builder.shunting_yard('( not A or B ) and C'.split()) == ['A', 'NOT', 'B', 'OR', 'C', 'AND']
    assert circuit_builder.shunting_yard(' ( ( A or not B ) and ( not C or D and not E ) )  or F'.split()) == \
           ['A', 'B', 'NOT', 'OR', 'C', 'NOT', 'D', 'E', 'NOT', 'AND', 'OR', 'AND', 'F', 'OR']

def test_simulator():
    inputs_dict = {}
    final_circuit = circuit_builder.circuit_builder("A or not B and C", inputs_dict)
    print(inputs_dict)
    inputs_dict['A'].set_state(0)
    inputs_dict['B'].set_state(1)
    inputs_dict['C'].set_state(1)
    assert final_circuit.output() == 0
    inputs_dict['A'].set_state(1)
    assert final_circuit.output() == 1





