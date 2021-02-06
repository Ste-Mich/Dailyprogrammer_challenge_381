
def yahtzee_upper(rolls):
    dot_score = [0, 0, 0, 0, 0, 0]
    for roll in rolls:
        dot_score[roll-1] += roll
    dot_score.sort()
    return dot_score[-1]


print("yahtzee_upper function:")
print(yahtzee_upper([2, 3, 5, 5, 6]))  # => 10
print(yahtzee_upper([1, 1, 1, 1, 3]))  # => 4
print(yahtzee_upper([1, 1, 1, 3, 3]))  # => 6
print(yahtzee_upper([1, 2, 3, 4, 5]))  # => 5
print(yahtzee_upper([6, 6, 6, 6, 6]))  # => 30
