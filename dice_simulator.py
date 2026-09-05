import random
def roll_dice(sides=6):
    return random.randint(1, sides)
rounds=int(input("Enter the number of rounds to roll the dice: "))
target_score=int(input("Enter the target score to reach: "))
total=0
history=[]
roundnum=0
while total<target_score and roundnum<rounds:
    roundnum+=1
    roll=roll_dice()
    total+=roll
    history.append(roll)
    print(f"Round {roundnum}: You rolled a {roll}. Total score: {total}")
if total>=target_score:
    print(f"Congratulations! You reached the target score of {target_score} in {roundnum} rounds.")
else:
    print(f"Sorry, you didn't reach the target score of {target_score} in {roundnum} rounds.") 