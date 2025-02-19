notes = [10, 20, 30, 40, 50, 60]

type(notes)
# output list

notes.append(70)
notes
# output [10, 20, 30, 40, 50, 60, 70]

notes.pop()
notes
# output [10, 20, 30, 40, 50, 60]

notes.remove(40)
notes
# output [10, 20, 30, 50, 60]

notes.count(20)
# output 1

notes.index(50)
# output 3

notes.reverse()
notes
# output [60, 50, 30, 20, 10]

notes.clear()
notes
# output []

notes[:4]
# output [10, 20, 30, 40]
notes[2:4]
# output [30, 40]

range(len(notes)) # is used in a for loop to iterate over each element of a list or array.
# output range(0, 6) 

# Map and Lambda
# map(function, iterable, ...): Apply function to every item of iterable and return a list of the results.
# lambda: small throwaway functions 

notes = [10, 20, 30, 40]
list(map(lambda x: x * 10, notes))
# output [100, 200, 300, 400]


# filter 

notes = [10, 20, 30, 40, 50, 60]
list(filter(lambda x: x % 6 == 0, notes))
# output [30, 60]


# list comprehension

students = ["Beste", "Damla", "Ahmet", "Mehmet"]

female_students = ["Beste", "Damla"]

[student.upper() if student in female_students else student.lower() for student in students]
# output  ['BESTE', 'DAMLA', 'ahmet', 'mehmet']

notes = [10, 20, 30, 40]

[note * 2 for note in notes]
# output [20, 40, 60, 80]

[note / 2 for note in notes if note < 30]
# output [5, 10]

[note / 2 if note < 30 else note for note in notes]
# output [5, 10, 30, 40]


# dictionary comprehension

numbers = range(10)
{n: n ** 2 for n in numbers if n % 2 == 0}
# output {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# Numpy arrays

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b
# output array([ 2,  6, 12, 20])


# enumerate : enumerate is used in a for loop to iterate over a list, providing both the index and the value of each element.
text = "The goal is to turn data into information, and information into insight."
def case(string):
    x = text.upper()
    for index, letter in enumerate(x):
        if letter == ",":
            x = x.replace(",", " ")
        elif letter == ".":
            x = x.replace(".", " ")
    print(x.split())

case(text)
# output ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']


lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
new_lst = []
new_lst.extend(lst[0:4])
print(new_lst)
# output ['D', 'A', 'T', 'A'] 

dict = {'Christion' : ["America", 18],
        'Daisy' : ["England", 12],
        'Antonio' : ["Spain", 22],
        'Dante' : ["Italy", 25]}

print(dict.keys())
print(dict.values())
print(dict)

print(dict["Daisy"])
dict["Daisy"] = ["England", 13]
dict["Ahmet"] = ["Turkey", 24]

del dict["Antonio"]
dict["Daisy"].pop() # last data deleted
dict.pop("Daisy")


class_code = ["AA105", "BB105", "CC105", "DD105"]
credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

a = zip(class_code, credit, quota)
print(tuple(a))


cluster1 = set(["data", "python"])
cluster2 = set(["data", "function", "qcut","python", "lambda"])

def kms(set1, set2):
    a = set2.difference(set1)
    print(a)

kms(cluster1, cluster2)