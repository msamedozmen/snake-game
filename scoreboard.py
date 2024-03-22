from turtle import Turtle,Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score=0
        # with open("myfile.txt",mode="w") as f:
        #     f.write("0")
        with open("myfile.txt",mode="r") as f:
            self.cont = int(f.read()) 
               
        self.color("white")
        self.penup()
        self.goto(0,360)
        self.hideturtle()
        self.write(f" Score: {self.score}    High Score: {self.cont} ", True, align="center",font=("Arial",20,"normal"))
        
    def new_score(self):
        self.score+=1
        self.clear()
        self.penup()
        self.goto(0,360)
        self.hideturtle()
        self.write(f" Score: {self.score}    High Score: {self.cont} ", True, align="center",font=("Arial",20,"normal"))
    
    def reset_game(self):
        self.clear()
        if self.score > self.cont:
            self.cont = self.score

            with open("myfile.txt",mode="w") as f:
                f.write(f"{self.cont}")
            
            with open("myfile.txt",mode="r") as f:
                self.cont = int(f.read())
              
        self.score = 0
        self.penup()
        self.goto(0,360)
        self.write(f" Score: {self.score}    High Score: {self.cont} ", True, align="center",font=("Arial",20,"normal"))
    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("GAME OVER", True, align="center",font=("Arial",30,"normal"))
    #     self.hideturtle()

        
