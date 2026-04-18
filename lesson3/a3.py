# 1) Ask the user to enter a number and store it in `num`.
num = int(input("Enter a number"))
# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)
sum = 0
# 3) Copy `num` into `temp`.
#    (We will change `temp` while checking digits, but we must keep `num` unchanged.)
temp = num
# 4) Repeat while `temp` is greater than 0:
#    a) Find the last digit of `temp` and store it in `digit`.
#    b) Add (digit × digit × digit) to `sum`.
#    c) Remove the last digit from `temp` so you can move to the next digit.
while temp > 0:
    digit = temp%10
    sum = digit**3+sum
    temp = temp//10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.