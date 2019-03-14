# correct answer for sample input: (20, [('.', 0)], 325)
# correct answer for 20 generations: 3738

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

#    print('l',pots[:5], rules_dict[pots[:5]])
#    while rules_dict[pots[:5]] == '.' and pots[:2] == '..':
#        pots = pots[1:]
#        pot_numbers = pot_numbers[1:]
#        print('l',pots[:5], rules_dict[pots[:5]])
#    print('r',pots[-5:], rules_dict[pots[-5:]])
#    while rules_dict[pots[-5:]] == '.' and pots[-2:] == '..':
#        pots = pots[:-1]
#        pot_numbers = pot_numbers[:-1]
#        print('r',pots[-5:], rules_dict[pots[-5:]])
    for j in range(2):
        if pots[:5] == '.....':
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

for outer_iteration in range(1000):
    for inner_iteration in range(50000000000/1000):
        previous_iteration_pots = pots
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
        if pots == previous_iteration_pots:
            print("total is:", gen_total)
            print(pots)
            exit()
        if inner_iteration % 1000 == 0:
            print(inner_iteration, pots)
            print('next', next_gen)
        next_gen = ''
    if outer_iteration % 10 == 0:
        print(outer_iteration, pots)

    #    print('post_print',iteration + 1, [i for i in numbered_pots if i[1] == 0], gen_total)

print("total is:", gen_total)
print(pots)
