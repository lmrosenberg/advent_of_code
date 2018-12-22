initial_state = "#..#.#..##......###...###"

rules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""


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


rules_dict = dict()
for single_rule in rules.splitlines():
    single_rule = single_rule.split(' ')
    rules_dict[single_rule[0]] = single_rule[2]

pots, pot_numbers = initialize(initial_state)
numbered_pots = zip(pots, pot_numbers)
gen_total = sum(i[1] for i in numbered_pots if i[0] == '#')

next_gen = ''
total_plants = len([i for i in pots if i == '#'])

for iteration in range(21):
    print(iteration,[i for i in numbered_pots if i[1] == 0], gen_total)
    #print(iteration, len([i for i in pots if i == '#']), pots)
    for index, pot in enumerate(pots):
        if index == 0:
            pot_context = '..' + pots[index:index+3]
        elif index == 1:
            pot_context = '.' + pot[index-1:index+3]
        elif index >= 2 and index < len(pots)-1:
            pot_context = pots[index-2:index+3]
        elif index <= len(pots)-2:
            pot_context = pots[index-2:index+1] + '..'

        try:
            next_gen = next_gen + rules_dict[pot_context]
        except KeyError:
            next_gen = next_gen + '.'

    numbered_pots = zip(next_gen, pot_numbers)
    gen_total = sum(i[1] for i in numbered_pots if i[0] == '#')

    #print([i for i in numbered_pots if i[1] == 0])

    pots = '..' + next_gen + '..'
    for i in range(2):
        pot_numbers.insert(0, min(pot_numbers) -1)
    for i in range(2):
        pot_numbers.append(max(pot_numbers) + 1)
    next_gen = ''
    total_plants += len([i for i in pots if i == '#'])

#print(20, len([i for i in pots if i == '#']), pots)
#print(total_plants + len([i for i in pots if i == '#']))
#print(gen_total)
