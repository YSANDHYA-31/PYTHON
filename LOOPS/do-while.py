'''Python does not contain Built-in do-while 
  however we can simulate do-while loop using while i.e., 
  loop runs at lest once before checking the condition...'''

Num = 1

# Simulate do-while loop
while True:
    print(Num)  
    Num += 1   
    if Num > 10:
        break  # Exit the loop when Num exceeds 10
