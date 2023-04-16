import random
print("\n")
print("Rock Paper Scissors Game \n")
while True:
    user_ip = input("Choose : Rock,Paper,Scissors\nNote: To Quit the game type \"quit\"\n")
    pc_ip = random.choice(["Rock","Paper","Scissors"])
    user_ip = user_ip.lower()
    if user_ip in ["rock","paper","scissors","quit"]:
        if pc_ip == user_ip:
            print("We Tied ! \n\n")
            continue
        elif user_ip == "rock" and pc_ip == "Paper" :
            print(f"The computer chose {pc_ip} You Loose ! Try again.\n\n")
            continue
        elif user_ip == "rock" and pc_ip == "Scissors" :
            print(f"The computer chose {pc_ip} You Won ! \n\n")
            continue
        elif user_ip == "scissors" and pc_ip == "Paper" :
            print(f"The computer chose {pc_ip} You Won ! \n\n")
            continue
        elif user_ip == "scissors" and pc_ip == "Rock" :
            print(f"The computer chose {pc_ip} You Loose ! Try again.\n\n")
            continue
        elif user_ip =="paper" and pc_ip == "Rock":
            print(f"The computer chose {pc_ip} You Won ! \n\n")
            continue
        elif user_ip == "paper" and pc_ip == "Scissors":
            print(f"The computer chose {pc_ip} You Loose ! Try again.\n\n")
            continue
        elif user_ip == "quit":
            break
    else:
        print("Enter a Valid Choice please\n")    
        continue
    
            
        
    



