# 1) Ask the user to enter the number of terms and store it in `n`.
n = int(input("Enter the number of terms"))
# 2) Initialize `sum` to 0.
#    (This will store the running total.)
sum = 0
# 3) Initialize `i` to 1.
#    (This is the first number we will add.)
i = 1
# 4) Repeat while `i` is less than or equal to `n`:
#    a) Add `i` to `sum`.
#    b) Increase `i` by 1 to move to the next number.
while i <= n:
    sum = sum+i
    i = i+1
print("The sum is",sum)
# 5) After the loop ends, print the final value of `sum`.