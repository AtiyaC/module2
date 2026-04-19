# 1) Ask the user to enter a word and store it in `string`.
string = input("Enter a word")
# 2) Ask the user to enter a single character and store it in `char`.
char = input("Enter a single character")
# 3) Set `i` to 0.
#    (This will be used as the index to move through the string.)
i = 0
# 4) Set `count` to 0.
#    (This will store how many times `char` appears.)
count = 0
# 5) While `i` is less than the length of `string`:
#    a) Check if the character at position `i` in `string` is equal to `char`.
#    b) If yes, increase `count` by 1.
#    c) Increase `i` by 1 to move to the next character.
while i < len(string):
    if string[i] == char:
        count = count+1
    i = i+1

# 6) After the loop, print how many times `char` occurred in `string` using `count`.

print("The total amount of times",char,"has occured",count)