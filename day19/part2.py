import copy

file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    content = fd.read().split('\n\n')

    string_rules = content[0].splitlines()
    string_items = content[1].splitlines()

rules_map = {}
for string_rule in string_rules:
    aux_split = string_rule.split('{')
    name = aux_split[0]
    aux_rules = aux_split[1].split(',')
    default_rule = aux_rules[-1][:-1]
    aux_rules = [x.split(':') for x in aux_rules[:-1]]
    aux_rules = [(aux_rule[0], aux_rule[1], int(aux_rule[2:]), next_rule) for aux_rule, next_rule in aux_rules]
    rules_map[name] = (aux_rules, default_rule)

items_list = []
for string_item in string_items:
    current_items = string_item[1:-1].split(',')
    current_items = {x.split('=')[0]: int(x.split('=')[1]) for x in current_items}
    items_list.append(current_items)


def traverse_decision_tree(all_rules, ranges, curent_rule):
    if curent_rule == 'A':
        prod = 1
        for low, high in ranges.values():
            prod *= high - low + 1

        return prod

    elif curent_rule == 'R':
        return 0

    rules, starting_default_rule = all_rules[curent_rule]
    res = 0

    for part_category, operation, treshold, next_rule in rules:
        low, high = ranges[part_category]
        if operation == '<':
            if low < treshold:
                aux_ranges = copy.deepcopy(ranges)
                aux_ranges[part_category] = (low, treshold - 1)
                res += traverse_decision_tree(all_rules, aux_ranges, next_rule)
            ranges[part_category] = (max(treshold,low), high)
        elif operation == '>':
            if high > treshold:
                aux_ranges = copy.deepcopy(ranges)
                aux_ranges[part_category] = (treshold+1, high)
                res += traverse_decision_tree(all_rules, aux_ranges, next_rule)
            ranges[part_category] = (low, treshold)

    res += traverse_decision_tree(all_rules, ranges, starting_default_rule)
    return res


print(traverse_decision_tree(rules_map, {part_category: (1, 4000) for part_category in 'xmas'}, 'in'))
