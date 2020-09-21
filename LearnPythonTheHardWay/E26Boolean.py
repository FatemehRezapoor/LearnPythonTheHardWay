# June 4, 2018
# E26
# List of Boolean operators:
# ==, !=, <,>,<=, and, or, not(and) , ...

print(1 == 1)
print(1 == 1 and 1 < 2)
print(1 == 1 and 1 > 2)
print('Hi' == 'Hi')

# Not always the output of boolean operator is True or False:

print('This is a example of situation where out put is not True or False')
print('Hi' and 'Hi')
print('Hi' or 'Hi')

# IMPORTANT POINTS:
# and" returns the first False item (e.g., None, “”, [], (), {}, 0) or the last item if none (e.g. no False found)
# “or" returns the first True item or the last item (e.g. no True found)

# *** In summary they all return the first item that decides the outcome of the statement. ***
# (In the worst case, the last item in the sequence)
# Note this rule also applies to a chained all "and" or all "or" statement


print('How does the order effects on the output?')
print('Hi' and '-')  # The outcome is False, so it prints the first false item (-)
print('Hi' or '-')  # The out put is true, so it prints the first true item (Hi)

print('This is a new order:')

print(':(' and 'Hi')  # Output is flase and the first fasle item is Hi
print(':(' or 'Hi')  # output is True and the first True item is :(

print('Another example')

print(
    'Hi' and ':(' and 'Hi')  # output of Hi and :( is false and returns :(. Output of :( and Hi is Flase and returns Hi
print('Hi' and ':(' and ':(')  # output of Hi and :( is false and returns :(. Output of :( and :( is true and returns :(

print('Here is example with OR')
print('Hi' or 'Hi' or ':(')  # The out put of first part is Hi. Hi or :( is true and returns Hi

print(':(' or 'Hi' or 'Hi')  # The output of :( or Hi is true and is :(. The output of :( or Hi is true and :(.
