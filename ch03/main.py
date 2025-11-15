print('doesn\'t')
print('Py' 'thon')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = []
print(letters)

a, b = 0, 1
while b < 10:
    print(b)
    b += 1

# x = int(input("Please enter an integer: "))
# print(x)

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print("More")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Eleonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

