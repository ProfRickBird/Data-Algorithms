import math
from time import sleep 

list = ['Jack', 'Sue', 'Antonio', 'Beth', 'Steve', 'Tammy', 'Xerces']

# "Big O One"
# O(1)
_ = input('Press Enter to see O(1) speed...')
sleep(0.1)
print( list[5] )
print( 'Done!' )

# "Big O N"
# O(n)    - based on the number of items
_ = input('Press Enter to see O(n) speed...')
for item in list:
    sleep(0.1)
    print( item )
    
print('Done!')

# "Big O N Squared"     -- Nested Loop
# O(n^2)
_ = input('Press Enter to see O(n^2) speed...')
for item in list:
    sleep(0.1)
    print(item)
    for each in list:
        sleep(0.1)
        print('\t' + each)
print('Done!')

# "Big O N Cubed"   - Nested Loop INSIDE a Nested Loop
# O(n^3)
_ = input('Press Enter to see O(n^3) speed...')
for n in list:
    sleep(0.1)
    print(n)
    for m in list:
        sleep(0.1)
        print('\t' + m)
        for o in list:
            sleep(0.1)
            print('\t\t' + o)