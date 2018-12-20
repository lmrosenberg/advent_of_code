sample_text = """Step C must be finished before Step A can begin.
Step C must be finished before Step F can begin.
Step A must be finished before Step B can begin.
Step A must be finished before Step D can begin.
Step B must be finished before Step E can begin.
Step D must be finished before Step E can begin.
Step F must be finished before Step E can begin."""

with open('inputs/day_7.txt') as file:
    input_text = file.read()


def input_processing(input_string):
    actions_list = []

    for line in input_string.splitlines():
        prev_action = line[5]
        next_action = line[36]
        actions_list.append((prev_action,next_action))

    all_befores = {i[0] for i in actions_list}
    all_afters = {i[1] for i in actions_list}
    all_actions = all_befores.union(all_afters)

    first_actions = {i for i in all_actions if i not in all_afters}
    final_action = [i for i in all_actions if i not in all_befores]

    prereqs = dict()
    for i in all_afters:
        out = set()
        for action in actions_list:
            if action[1]==i:
                out.add(action[0])
        prereqs[i] = out

    for i in first_actions:
        prereqs[i] = set()

    return(actions_list, first_actions, final_action[0], prereqs)

def actions_unlocked(current_action, actions_list):
    unlocked = []
    for action in actions_list:
        if action[0] == current_action:
            unlocked.append(action[1])
    return unlocked


def main():
    actions_list, available_actions, final_action, prereqs = input_processing(input_text)

    available_actions_as_a_list = sorted(list(available_actions))
    current_action = available_actions_as_a_list.pop(0)
    actions_string = ''
    completed_actions = set()

    while current_action != final_action:
        actions_string = actions_string+current_action

        new_actions = actions_unlocked(current_action, actions_list)

        available_actions_as_a_list.extend(new_actions)
        available_actions_as_a_list = sorted(list(set(available_actions_as_a_list)))

        completed_actions.add(current_action)
        actions_list = [i for i in actions_list if i[1]!=current_action]

        current_action = available_actions_as_a_list.pop(0)
        put_it_back = []

        while not prereqs[current_action].issubset(completed_actions):
            put_it_back.append(current_action)
            current_action = available_actions_as_a_list.pop(0)

        available_actions_as_a_list.extend(put_it_back)
        available_actions_as_a_list = sorted(set(available_actions_as_a_list))

        #available_actions = set(sorted(available_actions_as_a_list))

    actions_string = actions_string+final_action[0]
    print (actions_string)


if __name__ == "__main__":
    main()
