# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

true_love = str(true) + str(love)
true_love_int = int(true_love)

if true_love_int <= 10 or true_love_int >= 90:
    print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int > 40 and true_love_int < 50:
    print(f"Your score is {true_love_int}, you are alright together")
else:
    print(f"Your score is {true_love_int}.")