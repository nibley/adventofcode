from collections import deque

class FlipFlop:
    def __init__(self):
        self.state = False

    def handle(self, pulse, _):
        if pulse:
            return None

        new_state = not self.state
        self.state = new_state
        return new_state

class Conjunction:
    def __init__(self, inputs):
        self.memory = { an_input : False for an_input in inputs }

    def handle(self, pulse, sender):
        self.memory[sender] = pulse
        return not all(self.memory.values())

module_inputs = {}
module_outputs = {}
prefixes = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    module_name, outputs = line.split(' -> ')

    if module_name[0] in '%&':
        prefix = module_name[0]
        module_name = module_name[ 1 : ]
    else:
        prefix = None
    prefixes[module_name] = prefix

    outputs = outputs.split(', ')
    for output in outputs:
        module_inputs.setdefault(output, [])
        module_inputs[output].append(module_name)

    module_outputs[module_name] = outputs

modules = {}
for module_name in module_outputs:
    prefix = prefixes[module_name]
    if prefix is None:
        assert module_name == 'broadcaster'
        continue
    elif prefix == '%':
        modules[module_name] = FlipFlop()
    elif prefix == '&':
        modules[module_name] = Conjunction(module_inputs[module_name])

total_low_pulses = 0
total_high_pulses = 0
for _ in range(1_000):
    pulse_queue = deque([
        ('broadcaster', False, receiver)
        for receiver in module_outputs['broadcaster']
    ])
    while pulse_queue:
        sender, pulse, receiver = pulse_queue.popleft()
        if pulse:
            total_high_pulses += 1
        else:
            total_low_pulses += 1

        if receiver not in modules:
            continue

        resulting_pulse = modules[receiver].handle(pulse, sender)
        if resulting_pulse is None:
            continue

        for next_receiver in module_outputs[receiver]:
            pulse_queue.append( (receiver, resulting_pulse, next_receiver) )

print(total_low_pulses * total_high_pulses)
