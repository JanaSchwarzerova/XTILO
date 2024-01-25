class TuringMachine:
    def __init__(self, states, alphabet, tape_alphabet, blank_symbol, rules, start_state, accept_state, reject_state):
        self.states = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.blank_symbol = blank_symbol
        self.rules = rules
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

    def execute(self, input_str):
        tape = [self.blank_symbol] + list(input_str) + [self.blank_symbol]
        head = 1  # Head starts at the first symbol of the input
        current_state = self.start_state

        while current_state != self.accept_state and current_state != self.reject_state:
            current_symbol = tape[head]
            rule = next((r for r in self.rules if r.current_state == current_state and r.read_symbol == current_symbol), None)

            if rule is None:
                current_state = self.reject_state
                break

            tape[head] = rule.write_symbol

            if rule.operation == 'R':
                head += 1
            elif rule.operation == 'L':
                head -= 1

            current_state = rule.next_state

        result = ''.join(tape[1:-1])  # Exclude the blank symbols
        return result, current_state

# Množina stavů
states = ['q0', 'q1', 'q2', 'q_accept', 'q_reject']

# Abeceda
alphabet = ['0', '1']

# Abeceda pásky
tape_alphabet = ['0', '1', '_']

# Symbol pro prázdné pole na páskové abecedě
blank_symbol = '_'

# Pravidla přechodu
rules = [
    Rule(states[0], '0', states[1], '1', 'R'),
    Rule(states[0], '1', states[1], '0', 'R'),
    Rule(states[1], '0', states[2], '1', 'R'),
    Rule(states[1], '1', states[2], '0', 'R')
]

# Počáteční a koncový stav
start_state = 'q0'
accept_state = 'q_accept'
reject_state = 'q_reject'

# Inicializace Turingova stroje
tm = TuringMachine(states, alphabet, tape_alphabet, blank_symbol, rules, start_state, accept_state, reject_state)

# Simulace Turingova stroje s daným vstupem
input_str = '1001000'
result, final_state = tm.execute(input_str)

# Výstup
print(f"Input: {input_str}")
print(f"Result: {result}")
print(f"Final State: {final_state}")
