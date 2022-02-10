lloyd = {"homework" : [90.9, 97.0, 75.0, 92.0], "quizzes" : [88.0, 40.0, 94.0], "tests" : [100.0, 90.0]} #Defines every list with

alice = {"homework" : [80.0, 78.0, 78.0, 92.0], "quizzes" : [90.0, 87.0, 94.0], "tests" : [100.0, 90.0]}  #Grades

tyler = {"homework" : [90.0, 87.0, 65.0, 92.0], "quizzes" : [100.0, 30.0, 94.0], "tests" : [75.0, 93.0]}

students = [lloyd, alice, tyler]

#for x in students:
#  print(x)
    
def average(num): #Gets average of the argumet
    total = float(sum(num))
    avg = total/ len(num)
    return avg

print(average(lloyd["homework"]))

def gaverage(student): #Returns
    hw = student["homework"]
    q = student["quizzes"]
    t = student["tests"]
    total = average(hw) * 0.1 + average(q) * 0.3 + average(t) * 0.6
    return total

def geetgrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "You need peer tutoring"

def geetclass(students):
    results = []
    for tea in students:
        results.append(gaverage(tea))
    return average(results)
    
print(geetclass(students))
print(geetgrade(gaverage(students)))
        
    
    
