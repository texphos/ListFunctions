
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Oscar"))

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()

print(friends2)