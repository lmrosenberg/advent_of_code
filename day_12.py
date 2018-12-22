initial_state = """.##..#.#..##..##..##...#####.#.....#..#..##.###.#.####......#.......#..###.#.#.##.#.#.###...##.###.#"""

rules = """.##.# => #
##.#. => #
##... => #
#.... => .
.#..# => .
#.##. => .
.##.. => .
.#.## => .
###.. => .
..##. => #
##### => #
#...# => #
.#... => #
###.# => #
#.### => #
##..# => .
.###. => #
...## => .
..#.# => .
##.## => #
....# => .
#.#.# => #
#.#.. => .
.#### => .
...#. => #
..### => .
..#.. => #
..... => .
####. => .
#..## => #
.#.#. => .
#..#. => #"""


def process_string(string):
    processed = [i for i in string]
    return processed


def initialize(string):
    pots = string
    pot_numbers = range(len(pots))
    pots = '..' + pots + '..'
    pot_numbers.insert(0, -1)
    pot_numbers.insert(0, -2)
    for i in range(2):
        pot_numbers.append(max(pot_numbers) + 1)
    return pots, pot_numbers


def prepare_next_gen(next_gen, pot_numbers):
    pots = '..' + next_gen + '..'
    for i in range(2):
        pot_numbers.insert(0, min(pot_numbers) - 1)
        pot_numbers.append(max(pot_numbers) + 1)
    if pots[:6] == '.....':
        pots = pots[2:]
        pot_numbers = pot_numbers[2:]
    if pots[-5:] == '.....':
        pots = pots[:-2]
        pot_numbers = pot_numbers[:-2]
    return pots, pot_numbers

rules_dict = dict()
for single_rule in rules.splitlines():
    single_rule = single_rule.split(' ')
    rules_dict[single_rule[0]] = single_rule[2]

pots, pot_numbers = initialize(initial_state)
numbered_pots = zip(pots, pot_numbers)
gen_total = sum(i[1] for i in numbered_pots if i[0] == '#')

next_gen = ''
print('pre_print',0, [i for i in numbered_pots if i[1] == 0], gen_total)

for iteration in range(50000000000):
    #print('pre_print',iteration, [i for i in numbered_pots if i[1] == 0], gen_total)
    #print(pots)
    #print(iteration, len([i for i in pots if i == '#']), pots)
    for index, pot in enumerate(pots):
        pot_context = ''
        if index == 0:
            pot_context = '..' + pots[index:index+3]
        elif index == 1:
            pot_context = '.' + pots[index-1:index+3]
        elif index >= 2 and index < len(pots)-2:
            pot_context = pots[index-2:index+3]
        elif index == len(pots)-2:
            pot_context = pots[index-2:index+2] + '.'
        elif index == len(pots)-1:
            pot_context = pots[index-2:index+1] + '..'

        try:
            next_gen = next_gen + rules_dict[pot_context]
        except KeyError:
            next_gen = next_gen + '.'

    numbered_pots = zip(next_gen, pot_numbers)
    gen_total = sum(i[1] for i in numbered_pots if i[0] == '#')

    #print([i for i in numbered_pots if i[1] == 0])

    pots, pot_numbers = prepare_next_gen(next_gen, pot_numbers)
    next_gen = ''
    #print('post_print',iteration + 1, [i for i in numbered_pots if i[1] == 0], gen_total)

print("total is:", gen_total)
