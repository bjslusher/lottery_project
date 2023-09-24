from random import randrange
from performance import performance
from collections import Counter


@performance
def lottery_predictions(iterations: int):
    lottery_numbers = []
    powerball_number = []
    powerball_sequence = []

    i = 0
    while i < iterations:
        seq_1 = []
        seq_2 = []
        while len(seq_1) < 5:  # selects the 5 lottery numbers [1,2,3,4,5]
            num = randrange(1, 69)
            if num not in seq_1:
                seq_1.append(num)
        seq_2.append(randrange(1, 26))  # selects the powerball number [pb]
        seq_1.sort()
        a = tuple(seq_1)
        b = tuple(seq_2)
        lottery_numbers.append(a)
        powerball_number.append(b)
        i += 1

    # creates a sequence of the 5 white balls and 1 powerball [[1, 2, 3, 4, 5], [pb]]
    for idx in range(len(lottery_numbers)):
        temp = (lottery_numbers[idx], powerball_number[idx])
        powerball_sequence.append(temp)
    lottery_numbers.clear()
    powerball_number.clear()
    counter = Counter(powerball_sequence).most_common(5)

    return counter


recurring_sequences = lottery_predictions(100000000)

save_numbers = []

for element in recurring_sequences:
    save_numbers.append(element)

with open("predicted_numbers.txt", mode="a") as save:
    for element in save_numbers:
        text = str(element)
        save.write(text)
        save.write("\n")
