"""Rudolph's adventure story is a festive choose-your-own-adventure game. Players must navigate a series of decisions to ensure that
Rudolph, the red-nosed reindeer, successfully delivers all the presents before the arrival of Christmas morning."""

ASCII_ART = '''
         { }
         {^^,
         (   `-;
    _     `;;~~
   /(______);
  (         (
   |:------( )
 _//         \\
/ /          vv
'''
class Game():
    def welcome_message(self):
        print("Welcome to Rudolph's Adventure, a choose-your-own-adventure game.\nIt's Christmas Eve, and Rudolph needs to deliver all of the presents on time for Christmas!")

    def decision_one(self):
        decision = input("Question: Rudolph starts at Santa's Workshop. He needs to choose between taking a shortcut through the snowy mountains or following the longer, safer path through the valley. (shortcut/valley):\n")
        
        if decision.lower().strip() == "shortcut":
            print("Rudolph gets caught in a snowstorm and loses his way.\nGame over.")
            exit()
        elif decision.lower().strip() == "valley":
            print("Rudolph reaches the valley and continues his journey...")
        else:
            exit()
        

    def decision_two(self):
        decision = input("Question: A blizzard hits, and Rudolph faces a choice: should he try to fly above the storm or find shelter in a cave? (cave/fly):\n")

        if decision.lower().strip() == "cave":
            print("Whilst attempting to fly, the strong winds toss Rudolph around, and he crashes into a tree.\nGame over.")
            exit()
        elif decision.lower().strip() == "fly":
            print("Rudolph waits out the storm and continues afterward.")
        else:
            exit()

    def decision_three(self):
        decision = input("Question: Rudolph arrives at the first house to deliver presents. He faces a decision: should he use the chimney to deliver the presents or attempt to open the locked front door? (chimney/door):\n")

        if decision.lower().strip() == "chimney":
            print("Rudolph skillfully slides down and successfully places the presents under the tree.")
        elif decision.lower().strip() == "door":
            print("By attempting to open the locked front door, he accidentally triggers an alarm, leading to his discovery.\nGame over.")
            exit()
        else:
            exit()

    def decision_four(self):
        decision = input("Question: Rudolph is running out of time. He faces a decision: should he push through exhaustion to complete the deliveries or take a quick nap to regain energy? (push/nap):\n")

        if decision.lower().strip() == "push":
            print("Rudolph collapses, and the remaining presents are undelivered.\nGame over.")
            exit()
        elif decision.lower().strip() == "nap":
            print("Rudolph's nap allows him to regain energy, and he successfully completes the rest of the deliveries.")
        else:
            exit()

    def victory_message(self):
        print("Well done!\nYou have earned yourself an energy drink!")
        

if __name__ == "__main__":
    while True:
        print(ASCII_ART)
        session = Game()
        session.welcome_message()
        session.decision_one()
        session.decision_two()
        session.decision_three()
        session.decision_four()
        session.victory_message()
        break
    



