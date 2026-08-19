from abc import ABC, abstractmethod

class LogicGate(ABC):
    """
    Abstract base class for digital logic gates.
    Handles basic wiring (inputs/outputs) and enforces fan-in/fan-out constraints.
    """
    def __init__(self, next_gates: list = None, inputs: list = None, fan_in: int = 2, fan_out: int = 1):
        """
        Initialize the gate with its incoming and outgoing connections.

        Args:
            next_gates: List of gates this gate feeds its output into.
            inputs: List of gates (or literal binary values) feeding into this gate.
            fan_in: Maximum number of allowed inputs.
            fan_out: Maximum number of allowed output connections.
        """
        # Initialize safely to avoid mutable default argument pitfalls
        self.inputs = inputs if inputs is not None else []
        self.next_gates = next_gates if next_gates is not None else []
        self.fan_in = fan_in
        self.fan_out = fan_out

        if not self.validate(self.inputs, self.next_gates):
            raise ValueError(f"Connection limits exceeded. Max fan-in: {self.fan_in}, Max fan-out: {self.fan_out}")

    def validate(self, lst1: list, lst2: list):
        """Verify that the current connections respect the fan-in and fan-out limits."""
        return len(lst1) <= self.fan_in and len(lst2) <= self.fan_out

    @abstractmethod
    def output(self):
        """Calculate and return the logical output of the gate."""
        pass

    def input_next(self):
        """Wire this gate to the inputs of the connected next gates."""
        for gate in self.next_gates:
            gate.inputs.append(self)

class AndGate(LogicGate):
    """Logical AND gate."""
    def output(self):
        for inp in self.inputs:
            # Evaluate connected gates dynamically or read raw binary values
            if isinstance(inp, LogicGate):
                op = inp.output()
                if op == 0:
                    return 0
            elif inp == 0:
                return 0
        return 1

class OrGate(LogicGate):
    """Logical OR gate."""
    def output(self):
        for inp in self.inputs:
            if isinstance(inp, LogicGate):
                op = inp.output()
                if op == 1:
                    return 1
            elif inp == 1:
                return 1
        return 0

class NotGate(LogicGate):
    """Logical NOT gate. Restricted to a single input."""
    def __init__(self, next_gates: list = None, inputs: list = None, fan_in: int = 1, fan_out: int = 1):
        super().__init__(next_gates=next_gates, inputs=inputs, fan_in=fan_in, fan_out=fan_out)

    def output(self):
        if isinstance(self.inputs[0], LogicGate):
            op = self.inputs[0].output()
            if op == 0:
                return 1
        elif self.inputs[0] == 0:
            return 1
        return 0

class InputPin(LogicGate):
    """
    Represents an external input source (pin) to the circuit.
    Has no inputs itself, but holds a state that can be changed externally.
    """
    def __init__(self, name:str, curr_state: int = 0, next_gates: list | None = None):
        # Input pins don't have inputs, but can fan out to many target gates
        super().__init__(next_gates = next_gates, inputs=[], fan_in=0, fan_out=100)
        self.name = name
        self.curr_state = curr_state

    def output(self):
        """Return the current state of the pin."""
        return self.curr_state

    def set_state(self, state: int):
        """Update the pin's state for the next simulation cycle."""
        self.curr_state = state
