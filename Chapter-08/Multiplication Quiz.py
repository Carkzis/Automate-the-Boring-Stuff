"""
Marc's Multiplication Quiz.
It's a quiz!
"""

import random, time, re

# Sets variables.
numberOfQuestions = 10
correctAnswers = 0

# Loops to go through questions.
for questionNumber in range(1,numberOfQuestions + 1):
    # Select random numbers to multiply together between 0 and 9.
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    attempts = 0

    while attempts < 3: # Only get 3 attempts, starts at zero for first attempt
        prompt = '#%s: %s x %s= ' % (questionNumber, num1, num2)
        print(prompt)
        start = time.time() # this sets timer for answering question
        answer = input()
        end = time.time() # this stops timer for answering question
        timepassed = end - start # gets the time taken to answer question
        ansRegex = re.compile(r'(^[1-9]\d*)|0') # tests that the input is int
        mo = ansRegex.search(answer)
        if  timepassed > 8: # 8 seconds to finish!
            print('Out of time!')
            break # moves onto next question if you were too slow
        elif mo == None:
            print(answer + ' is not an integer.')
            attempts += 1 # this will use an attempt.
        elif int(answer) != (num1 * num2): # tests if the answer is correct
            print('Incorrect!')
            print(num1 * num2)
            attempts += 1
        else:
            break

    if attempts == 3: # this means you had 3 failed attempts
        print('Out of tries!')
    else:
        # This block runs if no exceptions raised, increments correctAnswers
        print('Correct!')
        correctAnswers += 1

    time.sleep(1) # Brief pause to let the user see the result.

# Prints final score.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))




