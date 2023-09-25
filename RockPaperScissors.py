#Rock Paper Scissors Game
import random, time
count=0
cpucount=0
#======================================================================
def retry():
    retry=str(input("Would you like to try again? (y/n) "))
    retry=retry.upper()
    if retry=="Y":
        game()
    else:
        return
#========================================================================

def score():
    print("Player Score:",count)
    print("CPU Score:",cpucount)
#=============================================================================
def countdown():
    seconds=3
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds-=1
    
#=====================================================================
def game():
    global count
    global cpucount
    guess= int(input("Do you choose:\n 1)Rock\n 2)Paper\n 3)Scissors "))
    while guess > 3 or guess <=0:
        print("That's not a valid answer, try again!")
        guess= int(input("Do you choose:\n 1)Rock\n 2)Paper\n 3)Scissors "))

    cpu= random.randint(1,3)
#======================================================================
    if guess == 1:
        if cpu==1:
            countdown()
            print("It's a tie!")
            score()


        elif cpu==2:
            countdown()
            print("CPU wins!")
            cpucount+=1
            score()


        elif cpu==3:
            countdown()
            print("Player wins!")
            count+=1
            score()
#========================================================================
    if guess ==2:
        if cpu==guess:
            countdown()
            print("It's a tie!")
            score()

        elif cpu==1:
            countdown()
            print("Player wins!")
            count+=1
            score()

        elif cpu==3:
            countdown()
            print("CPU wins!")
            cpucount+=1
            score()
#===================================================================
    if guess==3:
        if cpu==1:
            countdown()
            print("CPU wins!")
            cpucount+=1
            score()

        elif cpu==guess:
            countdown()
            print("It's a tie!")
            score()

        elif cpu==2:
            countdown()
            print("Player wins!")
            count+=1
            score()
    retry()
        
 #=============================================================================   


game()

#==========================================================================
print("The players final score is",count)
print("The CPU's final score is",cpucount)
if count > cpucount:
    print("Player Wins!!")
elif count == cpucount:
    print("It's a Tie!")
else:
    print("CPU wins!!")


    

