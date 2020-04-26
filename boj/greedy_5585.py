#Author Rekt77

changes = [500,100,50,10,5,1]
money2give = 1000-int(input())
counter = 0
for change in changes:
    condition = money2give//change
    if condition:
        money2give -= (change*condition)
        counter += condition
    elif money2give==0:
        break

print(counter)