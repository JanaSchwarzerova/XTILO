class State:
    def __init__(self, name, start=False, end=False):
        """
        Initialize a state for the Turing machine.

        Args:
        - name (str): The identifier for the state.
        - start (bool): Indicates whether the state is the starting state.
        - end (bool): Indicates whether the state is an accepting (ending) state.
        """
        self.name = name
        self.start = start
        self.end = end

class Tape:
    def __init__(self, symbols):
        """
        Initialize the tape for the Turing machine.

        Args:
        - symbols (list): List of symbols on the tape.
        """
        self.symbols = symbols

class Rule:
    def __init__(self, current_state, read_symbol, next_state, write_symbol, operation):
        """
        Initialize a transition rule for the Turing machine.

        Args:
        - current_state (State): Current state.
        - read_symbol (str): Symbol to be read.
        - next_state (State): Next state.
        - write_symbol (str): Symbol to be written on the tape.
        - operation (str): Tape head movement direction ('R' for right, 'L' for left).
        """
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.operation = operation

class Machine:
    def __init__(self, rules, tape, head):
        """
        Initialize the Turing machine.

        Args:
        - rules (list): List of transition rules.
        - tape (Tape): Initial tape configuration.
        - head (int): Initial position of the tape head.
        """
        self.rules = rules
        self.tape = tape
        self.head = head

    def simulate(self):
        """
        Simulate the Turing machine on the given input.

        Returns:
        - str: Resulting tape content after simulation.
        """
        current_state = next(rule.current_state for rule in self.rules if rule.current_state.start)

        while current_state not in [rule.current_state for rule in self.rules if rule.current_state.end]:
            current_symbol = self.tape.symbols[self.head]

            rule = next((r for r in self.rules if r.current_state == current_state and r.read_symbol == current_symbol), None)

            if rule is None:
                break

            self.tape.symbols[self.head] = rule.write_symbol

            if rule.operation == 'R':
                self.head += 1
            elif rule.operation == 'L':
                self.head -= 1

            current_state = rule.next_state

            # Extend the tape if needed
            if self.head == len(self.tape.symbols):
                self.tape.symbols.append('_')
            # Avoid moving the head to the left beyond the tape
            elif self.head == -1:
                self.head = 0

        return ''.join(self.tape.symbols)


# Example usage:
states = [State('q0', start=True), State('q1'), State('q2', end=True)]
tape = Tape(['1', '0', '0', '1', '0', '0', '0'])
rules = [
    Rule(states[0], '0', states[1], '1', 'R'),
    Rule(states[0], '1', states[1], '0', 'R'),
    Rule(states[1], '0', states[2], '1', 'R'),
    Rule(states[1], '1', states[2], '0', 'R')
]
machine = Machine(rules, tape, 0)

result = machine.simulate()

# Output
print(f"Original tape: {''.join(tape.symbols)}")
print(f"Result: {result}")

if __name__ == '__main__':
    # Example usage:
    states = [State('q0', start=True), State('q1'), State('q2', end=True)]
    tape = Tape(['1', '0', '0', '1', '0', '0', '0'])
    rules = [
        Rule(states[0], '0', states[1], '1', 'R'),
        Rule(states[0], '1', states[1], '0', 'R'),
        Rule(states[1], '0', states[2], '1', 'R'),
        Rule(states[1], '1', states[2], '0', 'R')
    ]
    machine = Machine(rules, tape, 0)

    result = machine.simulate()

    # Output
    print(f"Original tape: {''.join(tape.symbols)}")
    print(f"Result: {result}")

