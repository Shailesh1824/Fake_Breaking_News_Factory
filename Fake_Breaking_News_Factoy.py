#1. import random

import random

# 2. creating subjects 
subjects = [
    'Salman Khan',
    'Prime minister',
    'President of US',
    'Virat Kholi',
    'MS Dhoni',
    'Finance Minister of India',
    'Rahul Ghandi',
    'Railway Minister',
]

actions = [
    'eats somosa',
    'dances',
    'was playing',
    'laughs',
    'beats',
    'was seen smoking',
    'laughs',
    'was shouting',
    'was seen drinking beer',
    'was crying',
    'was riding',
    'will be flying',
    'will be kissing',

]

things_or_places = [
    'near Gate way of India in Mumbai',
    'in car',
    'in Delhi',
    'at Taj Hotel',
    'in jeep',
    'on the top of the building',
    'in dubai'
]

# 3. start the headline generation loop

while True:
    user_input = input('Do you want to generate the headline?: yes/no: ').strip().lower()
    if user_input == 'no':
        print('Thanks for using fake news generator. Have a nice day')
        break
    elif user_input == 'yes':
        subject = random.choice(subjects)
        action = random.choice(actions)
        things_or_place = random.choice(things_or_places)

        headline = f"BREAKING NEWS: {subject} {action} {things_or_place}"
        print(headline)

    else:
        print('use valid input keywords only that is (yes/no)')

      
