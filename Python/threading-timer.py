# Use the threading module to create a timer while waiting for user input

import threading

QUESTION = 'What is your name? You have 5 seconds to answer.\n'
for i in range(0, 9):
     timeout_switch = False
     def timeout():
          global timeout_switch
          timeout_switch = True
     five_seconds = threading.Timer(5, timeout)
     five_seconds.start()
     answer = input(question)
     print(timeout_switch)
     if timeout_switch == True:
          five_seconds.cancel()
          print('Out of time.')
     elif timeout_switch == False:
          five_seconds.cancel()
          print('Your name is ' + answer)
