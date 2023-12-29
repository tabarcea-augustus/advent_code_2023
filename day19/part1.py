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

print(rules_map)

print(items_list)

s = 0
for item in items_list:
    current_rule = 'in'

    while current_rule != 'A' and current_rule != 'R':
        rules, default_rule = rules_map[current_rule]
        rule_applied = False

        for part_category, operation, treshold, next_rule in rules:
            part_value = item[part_category]
            if (operation == '<' and part_value < treshold) or (operation == '>' and part_value > treshold):
                current_rule = next_rule
                rule_applied = True
                break

        if not rule_applied:
            current_rule = default_rule

    if current_rule == 'A':
        s += sum(item.values())

print(s)