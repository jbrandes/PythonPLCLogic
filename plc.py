

def AND(IN1, IN2):
    if IN1 == "on" and IN2 == "on":
        print("motor is on")
        
    else: 
        print("motor is off")
        
def NOT(IN1, IN2):
    if IN1 == "on":
        print("motor is off")
        
    else: 
        print("motor is on")
        
def OR(IN1, IN2):
    if IN1 or IN2 == "on":
        print("motor is on")
    else:
        print("motor is off")
    
        


function = input("Which function would you like to use? AND, OR, NOT  ")
IN1 = input("What is your first action? on or off?   ")
IN2 = input("What is your second action? on or off  ")
print(IN1 + " " + IN2)

if function == "AND":
    AND(IN1, IN2)
if function == "OR":
    OR(IN1, IN2)
if function == "NOT":
    NOT(IN1, IN2)





