## Turing Machine Simulator
This Python script provides a simple implementation of a Turing machine simulator. The Turing machine is defined using three main classes: State, Tape, and Rule, and the simulation is performed by the Machine class.

Classes
State
Represents a state in the Turing machine.

__init__(self, name, start=False, end=False): Initializes a state with a given name, and flags indicating whether it is the starting or ending state.
Tape
Represents the tape of the Turing machine.

__init__(self, symbols): Initializes the tape with a list of symbols.
Rule
Represents a transition rule in the Turing machine.

__init__(self, current_state, read_symbol, next_state, write_symbol, operation): Initializes a transition rule with the current state, symbol to be read, next state, symbol to be written, and tape head movement direction.
Machine
Represents the Turing machine.

__init__(self, rules, tape, head): Initializes the Turing machine with a list of transition rules, initial tape configuration, and the initial position of the tape head.

simulate(self) -> str: Simulates the Turing machine on the given input, returning the resulting tape content after simulation.

## How to Run:

Ensure you have Python installed on your system.
Open the script in a Python environment (IDE or terminal).
Run the script, and the simulation result will be printed.
