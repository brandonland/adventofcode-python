f = open("calories.txt","r")
lines = f.readlines()

elves = {}
temp = 0
count = 0

for line in lines:
    if line != "\n":
        temp += int(line.strip())
    else:
        elves[count] = temp
        temp = 0
        count += 1

elves[count] = temp

most_calories = 0

for k, calories in elves.items():
    if calories > most_calories:
        most_calories = calories

print("most calories: ", str(most_calories))  
