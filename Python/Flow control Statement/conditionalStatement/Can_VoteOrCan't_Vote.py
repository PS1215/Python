def start():

    age=int(input("Enter your age: "))   ## input from user


    if age>=18:    ## Loop statements
        print("congratulation are an adult")  
        print("you can give the vote")  ## result
    else:
        print("You are the teenager")   
        print("you can't give vote")

    repeat=input("Do you want to run code again? (y--> yes  or n-->no )")

    if repeat=="y":
        start()
    elif repeat=="n":
        print("Thank you")
    else:
        print("Please enter y or n only")
    exit()     
start()