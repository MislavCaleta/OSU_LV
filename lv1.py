"""
#1. zad
work_hours = float(input("Enter work hours: "))
euro_per_hour = float(input("Enter hourly pay: "))

def calculate_earning(hours, hourly_pay):
    print("total pay: ", hours * hourly_pay)
    return hours * hourly_pay

print(calculate_earning(work_hours, euro_per_hour))
"""

"""
#2. zad
grade = float(input("Input grade between 0.0 and 1.0: "))

try:

    if grade > 1.0 or grade < 0.0:
        raise Exception("Grade is not in interval between 1.0 and 0.0")

    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")
except ValueError as valueError:
    print(valueError)
except Exception as exception:
    print(exception)
"""

"""
song = open("song.txt", "r")
words = []
words_count = {}
for line in song:
    words_in_line = line.split()
    words = words + words_in_line

for word in words:
    if word in words_count.keys():
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)

print("Words that appear once")
for key, value in words_count.items():
    if value == 1:
        print(key)
"""

spams = open("SpamCollection.txt", "r")
count_ham = 0
count_spam = 0
count_ham_w = 0
count_spam_w = 0
count_spam_excl = 0
for line in spams:
    if line.startswith("ham"):
        count_ham += 1
        count_ham_w += len(line.split())
    elif line.startswith("spam"):
        count_spam += 1
        count_spam_w += len(line.split())
        if line.split()[-1][-1] == "!":
            count_spam_excl += 1

mean_w_ham = float(count_ham_w) / count_ham
mean_w_spam = float(count_spam_w) / count_spam

print(mean_w_ham)
print(mean_w_spam)
print(count_spam_excl)


