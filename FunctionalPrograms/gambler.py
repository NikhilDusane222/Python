# gambler program

while True:
    try:
        stake = int(input("Enter the amount you want to stake :"))
        goal = int(input("Enter your goal:"))
        number_of_times = int(input("How many times you want to play:"))
        if stake>0 and goal>0 and number_of_times>0:
            break
        else:
            print("Invalid input!!")
    except:
        print("Invalid input!!")

def gambler(stake,goal,number_of_times):
    import random
    bets=0
    win=0
    while win!=goal and stake!=0:
        num=random.random()
        if num<0.5:
            bets+=1
            win+=1
        else:
            bets+=1
            stake-=1
    loss_percentage=((bets-win)/bets)*100
    win_percentage=(win/bets)*100
    print(f"Total number of bets = {bets}")
    print(f"Total win = {win}")
    print(f"win percentage  ={win_percentage}")
    print(f"loss percentage ={loss_percentage}")


gambler(stake,goal,number_of_times)