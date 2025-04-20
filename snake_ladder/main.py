from models import *
import random
def find_new_pos(pos, snakes, ladders):
    for s in snakes:
        if s.start == pos:
            return s.end
    for l in ladders:
        if l.start == pos:
            return l.end
    return pos
    
def play():
    try:
        n = 2
        p1 = Player("Shubham",25,"m")
        p2 = Player("Rahul", 20, "m")
        players = [p1,p2]
        s1 = Snake(30,5)
        s2 = Snake(98,20)
        s3= Snake(40,6)
        snakes = [s1,s2,s3]
        l1= Ladder(45,80)
        l2 = Ladder(68,94)
        l3 = Ladder(4,99)
        ladders = [l1,l2,l3]
        win = False
        while not win:
            for i in range(n):
                print(f"Current Player is {players[i].name} and his position is {players[i].position}, please enter any key to roll the dice")
                input()
                dice_num = random.randint(1, 6)
                print(f"Hey {players[i].name} your Dice num is {dice_num}")
                if dice_num+players[i].position > 100:
                    print(f"oops! your dice is {dice_num} so you can't move")
                    continue
                if dice_num+players[i].position == 100:
                    print(f"Whooo! {players[i].name} is the winner")
                    win = True
                    break
                new_pos = find_new_pos(dice_num+players[i].position, snakes, ladders)
                players[i].position = new_pos
                print(f"New postion of {players[i].name} is {new_pos}")
    except Exception as e:
        print(f"Exception is {e}")

if __name__ == "__main__":
    play()