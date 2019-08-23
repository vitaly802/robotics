print('What is my favourite food?')
answer = 'electricity'
food = input('Guess? ')
while food != answer:
    print('Not even close')
    food = input('Guess? ')
if food == answer:
    print('You guessed it! Buzzzz')
