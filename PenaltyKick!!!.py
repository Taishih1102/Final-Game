import pygame, simpleGE, random

UR = "Upper Right"
BR = "Bottom Right"
UL = "Upper Left"
BL = "Bottom Left"
C = "Center"
GOAL = "GOAL"
NOGOAL = "NO GOAL"
uLCImage = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/cul.png"
bLCImage = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/cbl.png"
uLGImage = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/gul.png"
bLGImage = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/gbl.png"
kick_sound = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/ball.mp3"
goal_sound = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/goal.mp3"
save_sound = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/save.mp3"
defeat_sound= "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/defeat.mp3"
victory_sound = "/Users/taishihiraishi/Desktop/Codes/12Penalty Kick/victory.mp3"


class Kicker1(simpleGE.Sprite):
    
    def __init__(self,scene):
        super().__init__(scene)
        self.originalImage = "kicker1.png"
        self.setImage(self.originalImage)
        self.setSize(86, 120)
        self.position = (550, 340)
        self.choiceImage = "kicker2.png"
        
    def kickerkick(self):
        self.setImage(self.choiceImage)
        self.setSize(86, 120)


class Boom(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ball1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (550,420)
        self.setSize = (77,51)
        self.pressImage = ("boom1.png")
        
    def press(self):
        self.setImage(self.pressImage)
        self.position = (550,420)
        self.setSize = (77,51)
        

class Ball(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)   
        self.setImage("ball.png")
        self.setSize(150, 150)
        self.rect = self.image.get_rect()
        self.rect.center = (580, 370)
        self.dx = 0
        self.dy = 0
        self.target = None  
        self.alive = True
        self.outcome = None
        self.noGoalImage = "ball1.png"

    def start_moving(self, target):
        self.target = target
        direction_x = target[0] - self.rect.centerx
        direction_y = target[1] - self.rect.centery
        magnitude = (direction_x**2 + direction_y**2)**0.5
        self.dx = direction_x / magnitude * 20  
        self.dy = direction_y / magnitude * 20
        

    def update(self):
        if not self.alive:
            return  

        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.target:
            distance_x = abs(self.rect.centerx - self.target[0])
            distance_y = abs(self.rect.centery - self.target[1])

            if distance_x < 15:  
                self.alive = False
            
    
class GoalPost(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)   
        self.setImage("goalPost.png")
        self.setSize(300, 150)
        self.position = (200, 325)
    
    
class GoalKeeper(simpleGE.Sprite):
    
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("goalKeeper.png")
        self.setSize(100, 140)
        self.position = (200, 330)
        self.uRGImage = "goalkeeper_goal_ur.png"
        self.bRGImage = "goalkeeper_goal_br.png"
        self.uLGImage = "​​gul.png"
        self.bLGImage = "​​gbl.png"
        self.cGImage = "goalkeeper_goal_c.png"
        self.uRCImage = "goalkeeper_catch_ur.png"
        self.bRCImage = "goalkeeper_catch_br.png"
        self.uLCImage = "​​cul.png"
        self.bLCImage = "​​cbl.png"
        self.cCImage =  "goalkeeper_catch_c.png"
        
    def goalKeeperGoalUR (self):
        self.setImage(self.uRGImage)
        self.setSize(100, 140)
        self.position = (250, 330)
        
    def goalKeeperGoalBR (self):
        self.setImage(self.bRGImage)
        self.setSize(100, 140)
        self.position = (250, 370)

    def goalKeeperGoalUL (self):
        self.setImage(uLGImage)
        self.setSize(100, 140)
        self.position = (150, 330)
        
    def goalKeeperGoalBL (self):
        self.setImage(bLGImage)
        self.setSize(100, 140)
        self.position = (150, 370)
        
    def goalKeeperGoalC (self):
        self.setImage(self.cGImage)
        self.setSize(100, 140)
        self.position = (200, 330)
        
    def goalKeeperCatchUR (self):
        self.setImage(self.uRCImage)
        self.setSize(100, 140)
        self.position = (270, 330)
        
    def goalKeeperCatchBR (self):
        self.setImage(self.bRCImage)
        self.setSize(100, 140)
        self.position = (270, 370)
        
    def goalKeeperCatchUL (self):
        self.setImage(uLCImage)
        self.setSize(100, 140)
        self.position = (150, 330)
        
    def goalKeeperCatchBL (self):
        self.setImage(bLCImage)
        self.setSize(100, 140)
        self.position = (150, 370)        
        
    def goalKeeperCatchC (self):
        self.setImage(self.cCImage)
        self.setSize(100, 140)
        self.position = (200, 330)


class Win(simpleGE.Sprite):
    
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("victory.png")
        self.setSize(280, 233)
        self.position = (320, 210)


class Lost(simpleGE.Sprite):
    
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("defeat.png")
        self.setSize(280, 233)
        self.position = (320, 210)
      
      
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("field.png")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "You are Leonel Messi, playing for Argentina in Quater World Cup 2022.",
            "You reached to the finals and played 120 minutes against France only",
            "to draw by 3-3. Your mission here is to win the penalty shootout",
            "against France and win the World Cup. You will first be a kicker,",
            "then become a goalie, which completes one round. You have to choose which ",
            "direction to kick or dive by pressing the buttons: ur/ul/br/bl/c. You will",
            "have to score more than France within the 5 rounds to win the Wold Cup. Do not",
            "forget to press Next to go to the next round after each decision you make.",
            " ",
            "I wish you a very good luck!!!",
        ]
        
        self.instructions.center = (320, 200)
        self.instructions.size = (600, 350)
        self.instructions.font = pygame.font.Font("freesansbold.ttf", 15)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (R)"
        self.btnPlay.center = (575, 430)
        self.btnPlay.size = (100, 30)
        self.btnPlay.font = pygame.font.Font("freesansbold.ttf", 18)


        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (L)"
        self.btnQuit.center = (75, 430)
        self.btnQuit.size = (100, 30)
        self.btnQuit.font = pygame.font.Font("freesansbold.ttf", 18)

        
        self.btnSetting = simpleGE.Button()
        self.btnSetting.text = "Setting (C)"
        self.btnSetting.center = (325, 430)
        self.btnSetting.size = (100, 30)
        self.btnSetting.font = pygame.font.Font("freesansbold.ttf", 18)
        
        
        self.sprites = [self.instructions, self.btnSetting, self.btnQuit, self.btnPlay]
        
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.btnSetting.clicked:
            self.response = "Setting"
            self.stop()

        if self.isKeyPressed(pygame.K_r):  
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_l): 
            self.response = "Quit"
            self.stop()
        if self.isKeyPressed(pygame.K_c):  
            self.response = "Setting"
            self.stop()


class Setting(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.setImage("white.png")
        
        self.response = "Play"
        
        self.setting = simpleGE.MultiLabel()
        self.setting.textLines = [
            "In this game, you have to be both kicker and goalie.",
            "When both playing kicker and goalie, there will be 5 options",
            "for you to choose to determine the direction of the kick or dive.",
            "When you chose the direction, the computer also decides the",
            "direction of which the opponent moves.",
            "Direction Options / Scoring Possibilities: ",
        ]
        
        self.setting.center = (320, 90)
        self.setting.size = (600, 180)
        self.setting.bgColor = (255,255,255)
        self.setting.font = pygame.font.Font("freesansbold.ttf", 15)
        
        self.scoringP = simpleGE.MultiLabel()
        self.scoringP.textLines = [
            "Situation             Kicker's Choice      Goalie's Choice      Scoring Probability",
            "------------------------------------------------------------------------------------------------------------------------------------------",
            "Both made the      BR / Bottom Right    BR / Bottom Right       0                            ",
            "same decision                                                                                                          ",
            "------------------------------------------------------------------------------------------------------------------------------------------",
            "     Both made the      BR / Bottom Right    BL / Bottom Left         100                              ",
            "              different decision                                                                                                                        ",
            "------------------------------------------------------------------------------------------------------------------------------------------",
            "                                 Both made differet    UR / Upper Right     UL / Upper Left            0                                                                  ",
            "   decision on direction                                                                                                        ",
            "            but the same on height                                                                                                                 ",                                                                                   
            "------------------------------------------------------------------------------------------------------------------------------------------",
            "                                                                  Both made same       UR / Upper Right     BR / Bottom Right         50                                                                                              ",
            " decision on direction                                                                                                      ",
            "but different on height                                                                                                        ",
            " ",
        ]
        
        self.scoringP.center = (320, 340)
        self.scoringP.size = (450, 225)
        self.scoringP.bgColor = (255,255,255)
        self.scoringP.font = pygame.font.Font("freesansbold.ttf", 10)
        
        
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "                  Go Back (R)             "
        self.btnPlay.center = (575, 400)
        self.btnPlay.size = (110, 20)
        self.btnPlay.font = pygame.font.Font("freesansbold.ttf", 10)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (L)        "
        self.btnQuit.center = (75, 400)
        self.btnQuit.size = (110, 20)
        self.btnQuit.font = pygame.font.Font("freesansbold.ttf", 10)
        
        self.sprites = [self.setting, self.btnQuit, self.btnPlay, self.scoringP]
        
        self.lblUR = simpleGE.Label()
        self.lblUR.text = "Upper Right / UR"
        self.lblBR = simpleGE.Label()
        self.lblBR.text = "Bottom Right / BR"
        self.lblUL = simpleGE.Label()
        self.lblUL.text = "Upper Left / UL"
        self.lblBL = simpleGE.Label()
        self.lblBL.text = "Bottom Left / BL"
        self.lblC = simpleGE.Label()
        self.lblC.text = "Center / C"

        lblFont = pygame.font.Font("freesansbold.ttf", 12)
        bgColor = (211, 211, 211)
        fgColor =(0, 0, 0)
        lblSize = (110, 20)
        
        for lbl in [self.lblUR, self.lblBR, self.lblUL, self.lblBL, self.lblC]:
            lbl.bgColor = bgColor
            lbl.fgColor = fgColor
            lbl.size = lblSize
            lbl.font = lblFont
            
        self.lblUR.center = (440, 195 )
        self.lblBR.center = (440, 220)
        self.lblUL.center = (200, 195)
        self.lblBL.center = (200, 220)
        self.lblC.center = (320, 195)
        
        self.sprites.extend([self.lblUR, self.lblBR, self.lblUL, self.lblBL, self.lblC])
        
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        if self.isKeyPressed(pygame.K_r):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_l):
            self.response = "Quit"
            self.stop()

  
class KickerState(simpleGE.Scene):
        
    def __init__(self, rounds=1, scoreArg=0, scoreFra=0):
        super().__init__()
        pygame.font.init()
        pygame.mixer.init()
        self.argChoice = " "
        self.fraChoice = " "
        self.outcome = " "

        direction = random.randint(1, 100)
        catchRate = random.randint(1, 100)
        
        self.setImage("field.png")
        
        self.kick_sound = pygame.mixer.Sound("ball.mp3")
        self.goal_sound = pygame.mixer.Sound("goal.mp3")
        self.save_sound = pygame.mixer.Sound("save.mp3")

        self.rounds = rounds
        self.scoreArg = scoreArg
        self.scoreFra = scoreFra
        
        self.kicker1 = Kicker1(self)
        self.goalKeeper = GoalKeeper(self)
        self.goalPost = GoalPost(self)
        self.ball = Ball(self)
        self.boom = Boom(self)

        self.lblScoreArg = simpleGE.Label()
        self.lblScoreFra = simpleGE.Label()
        self.lblRounds = simpleGE.Label()
        self.lbldirectionArg = simpleGE.Label()
        
        self.lblScoreArg.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblScoreArg.fgColor = (116,172,223)
        self.lblScoreFra.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblScoreFra.fgColor = (49,140,231)
        self.lblRounds.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lbldirectionArg.font = pygame.font.Font("freesansbold.ttf", 30)
        self.lbldirectionArg.fgColor = (255,49,49)
        bgColor = (132, 140, 207)

        
        for lbl in [self.lblScoreArg, self.lblScoreFra, self.lblRounds, self.lbldirectionArg]:
            lbl.bgColor = bgColor
            
        self.lblScoreArg.center = (420, 150)
        self.lblScoreArg.size = (120,60)
        self.lblScoreFra.center = (540, 150)
        self.lblScoreFra.size = (120,60)
        self.lblRounds.center = (480, 90)
        self.lblRounds.size = (240,60)
        self.lbldirectionArg.center = (390,155)
        self.lbldirectionArg.size = (30,28)
        
        self.lblTitle = simpleGE.Label()
        self.lblChoiceArg = simpleGE.Label()
        self.lblChoiceFra = simpleGE.Label()
        self.lblOutcome = simpleGE.Label()
        
        self.lblTitle.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceArg.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceArg.fgColor = (116,172,223)
        self.lblChoiceFra.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceFra.fgColor = (49,140,231)
        self.lblOutcome.font = pygame.font.Font("freesansbold.ttf", 16)
        bgColor = (132, 140, 207)

        
        for lbl in [self.lblChoiceArg, self.lblChoiceFra, self.lblTitle, self.lblOutcome]:
            lbl.bgColor = bgColor
            
        self.lblChoiceArg.center = (160, 105)
        self.lblChoiceArg.size = (240,30)
        self.lblChoiceFra.center = (160, 135)
        self.lblChoiceFra.size = (240,30)
        self.lblTitle.center = (160, 75)
        self.lblTitle.size = (240,30)
        self.lblOutcome.center = (160,165)
        self.lblOutcome.size = (240,30)      
        
        self.btnUR = simpleGE.Button()
        self.btnUR.text = "UR"
        self.btnBR = simpleGE.Button()
        self.btnBR.text = "BR"
        self.btnUL = simpleGE.Button()
        self.btnUL.text = "UL"
        self.btnBL = simpleGE.Button()
        self.btnBL.text = "BL"
        self.btnC = simpleGE.Button()
        self.btnC.text = "C"
        

        btnFont = pygame.font.Font("freesansbold.ttf", 15)
        bgColor = (211, 211, 211)
        fgColor =(0, 0, 0)
        btnSize = (20, 20)
        
        for btn in [self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC]:
            btn.bgColor = bgColor
            btn.fgColor = fgColor
            btn.size = btnSize
            btn.font = btnFont
            
        self.btnUR.center = (580, 240)
        self.btnBR.center = (580, 265)
        self.btnUL.center = (530, 240)
        self.btnBL.center = (530, 265)
        self.btnC.center = (555, 240)
        
        self.btnNext = simpleGE.Button()
        self.btnNext.text = "NEXT"
        self.btnNext.font = pygame.font.Font("freesansbold.ttf", 15)
        self.btnNext.bgColor = (211, 211, 211)
        self.btnNext.fgColor =(255, 255, 255)
        self.btnNext.center = (550,420)
        self.btnNext.size = (50,25)
        
        self.sprites = [self.kicker1, self.goalPost, self.goalKeeper, self.ball, self.boom, self.lblTitle, self.lblChoiceArg, self.lblChoiceFra, self.lblOutcome, self.btnNext, self.lblScoreArg, self.lblScoreFra, self.lblRounds, self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC, self.lbldirectionArg]
        self.updateLabels()
        
    def updateLabels(self):
        
        self.lblTitle.text = "Chosen directions & Outcome"
        self.lblChoiceArg.text = f"ARG : {self.argChoice}"
        self.lblChoiceFra.text = f"FRA : {self.fraChoice}"
        self.lblOutcome.text = f"Outcome : {self.outcome}"
        
        self.lblScoreArg.text = f"Argentina  :  {self.scoreArg}"
        self.lblScoreFra.text = f"{self.scoreFra}  :  France"
        self.lblRounds.text = f"Rounds  : {self.rounds}"
        self.lbldirectionArg.text = "<-"
        
    def updateButtons(self):
        btnFont = pygame.font.Font("freesansbold.ttf", 1)
        bgColor = (255, 255, 255)
        fgColor =(255, 255, 255)
        btnSize = (1, 1)
        
        for btn in [self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC]:
            btn.bgColor = bgColor
            btn.fgColor = fgColor
            btn.size = btnSize
            btn.font = btnFont
            
        self.btnUR.center = (0, 480)
        self.btnBR.center = (0, 480)
        self.btnUL.center = (0, 480)
        self.btnBL.center = (0, 480)
        self.btnC.center = (0, 480)
        
    def process(self):
        direction = random.randint(1, 100)
        catchRate = random.randint(1, 100)
        if self.btnUR.clicked:
            self.argChoice = UR
            self.kicker1.kickerkick()
            self.boom.press()
            self.ball.start_moving((330, 300))
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchUR()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 41 <= direction <= 60:
                if 1 <= catchRate <= 50:
                    self.fraChoice = BR
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalBR()
                    self.goal_sound.play()
                    self.scoreArg += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = BR
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchBR()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreArg += 1
        elif self.btnBR.clicked:
            self.argChoice = BR
            self.kicker1.kickerkick()
            self.boom.press()
            self.ball.start_moving((330, 360))
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 21 <= direction <= 40:
                if 1 <= catchRate <= 50:
                    self.fraChoice = UR
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalUR()
                    self.goal_sound.play()
                    self.scoreArg += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = UR
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchUR()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchBR()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreArg += 1
        elif self.btnUL.clicked:
            self.argChoice = UL
            self.kicker1.kickerkick()
            self.boom.press()
            self.ball.start_moving((160, 290))
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchUL()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 81 <= direction <= 100:
                if 1 <= catchRate <= 50:
                    self.fraChoice = BL
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalBL()
                    self.goal_sound.play()
                    self.scoreArg += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = BL
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchBL()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
        elif self.btnBL.clicked:
            self.argChoice = BL
            self.kicker1.kickerkick()
            self.boom.press()
            self.ball.start_moving((160, 360))
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 61 <= direction <= 80:
                if 1 <= catchRate <= 50:
                    self.fraChoice = UL
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalUL()
                    self.goal_sound.play()
                    self.scoreArg += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = UL
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchUL()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchBL()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
        elif self.btnC.clicked:
            self.argChoice = C
            self.kicker1.kickerkick()
            self.boom.press()
            self.ball.start_moving((250, 290))
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchC()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreArg += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreArg += 1
        elif self.outcome != " ":
            if self.btnNext.clicked:
                self.response = "Next"
                self.stop()

        self.ball.update()
        self.updateLabels()


class GoalKeeperState(simpleGE.Scene):
        
    def __init__(self, rounds=1, scoreArg=0, scoreFra=0):
        super().__init__()
        pygame.font.init()
        pygame.mixer.init()
        self.argChoice = " "
        self.fraChoice = " "
        self.outcome = " "

        direction = random.randint(1, 100)
        catchRate = random.randint(1, 100)
        
        self.setImage("field.png")
        
        self.kick_sound = pygame.mixer.Sound("ball.mp3")
        self.goal_sound = pygame.mixer.Sound("goal.mp3")
        self.save_sound = pygame.mixer.Sound("save.mp3")

        self.rounds = rounds
        self.scoreArg = scoreArg
        self.scoreFra = scoreFra
        
        self.kicker1 = Kicker1(self)
        self.goalKeeper = GoalKeeper(self)
        self.goalPost = GoalPost(self)
        self.ball = Ball(self)
        self.boom = Boom(self)

        self.lblScoreArg = simpleGE.Label()
        self.lblScoreFra = simpleGE.Label()
        self.lblRounds = simpleGE.Label()
        self.lbldirectionArg = simpleGE.Label()
        
        self.lblScoreArg.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblScoreArg.fgColor = (116,172,223)
        self.lblScoreFra.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblScoreFra.fgColor = (49,140,231)
        self.lblRounds.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lbldirectionArg.font = pygame.font.Font("freesansbold.ttf", 30)
        self.lbldirectionArg.fgColor = (255,49,49)
        bgColor = (132, 140, 207)

        
        for lbl in [self.lblScoreArg, self.lblScoreFra, self.lblRounds, self.lbldirectionArg]:
            lbl.bgColor = bgColor
            
        self.lblScoreArg.center = (420, 150)
        self.lblScoreArg.size = (120,60)
        self.lblScoreFra.center = (540, 150)
        self.lblScoreFra.size = (120,60)
        self.lblRounds.center = (480, 90)
        self.lblRounds.size = (240,60)
        self.lbldirectionArg.center = (560,155)
        self.lbldirectionArg.size = (30,28)
        
        self.lblTitle = simpleGE.Label()
        self.lblChoiceArg = simpleGE.Label()
        self.lblChoiceFra = simpleGE.Label()
        self.lblOutcome = simpleGE.Label()
        
        self.lblTitle.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceArg.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceArg.fgColor = (116,172,223)
        self.lblChoiceFra.font = pygame.font.Font("freesansbold.ttf", 16)
        self.lblChoiceFra.fgColor = (49,140,231)
        self.lblOutcome.font = pygame.font.Font("freesansbold.ttf", 16)
        bgColor = (132, 140, 207)

        
        for lbl in [self.lblChoiceArg, self.lblChoiceFra, self.lblTitle, self.lblOutcome]:
            lbl.bgColor = bgColor
            
        self.lblChoiceArg.center = (160, 105)
        self.lblChoiceArg.size = (240,30)
        self.lblChoiceFra.center = (160, 135)
        self.lblChoiceFra.size = (240,30)
        self.lblTitle.center = (160, 75)
        self.lblTitle.size = (240,30)
        self.lblOutcome.center = (160,165)
        self.lblOutcome.size = (240,30)      
        
        self.btnUR = simpleGE.Button()
        self.btnUR.text = "UR"
        self.btnBR = simpleGE.Button()
        self.btnBR.text = "BR"
        self.btnUL = simpleGE.Button()
        self.btnUL.text = "UL"
        self.btnBL = simpleGE.Button()
        self.btnBL.text = "BL"
        self.btnC = simpleGE.Button()
        self.btnC.text = "C"
        

        btnFont = pygame.font.Font("freesansbold.ttf", 15)
        bgColor = (211, 211, 211)
        fgColor =(0, 0, 0)
        btnSize = (20, 20)
        
        for btn in [self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC]:
            btn.bgColor = bgColor
            btn.fgColor = fgColor
            btn.size = btnSize
            btn.font = btnFont
            
        self.btnUR.center = (225, 410)
        self.btnBR.center = (225, 435)
        self.btnUL.center = (175, 410)
        self.btnBL.center = (175, 435)
        self.btnC.center = (200, 410)
        
        self.btnNext = simpleGE.Button()
        self.btnNext.text = "NEXT"
        self.btnNext.font = pygame.font.Font("freesansbold.ttf", 15)
        self.btnNext.bgColor = (211, 211, 211)
        self.btnNext.fgColor =(255, 255, 255)
        self.btnNext.center = (550,420)
        self.btnNext.size = (50,25)
        
        self.sprites = [self.kicker1, self.goalPost, self.goalKeeper, self.ball, self.boom, self.lblTitle, self.lblChoiceArg, self.lblChoiceFra, self.lblOutcome, self.btnNext, self.lblScoreArg, self.lblScoreFra, self.lblRounds, self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC, self.lbldirectionArg]
        
        self.updateLabels()
        
    def updateLabels(self):
        
        self.lblTitle.text = "Chosen directions & Outcome"
        self.lblChoiceArg.text = f"ARG : {self.argChoice}"
        self.lblChoiceFra.text = f"FRA : {self.fraChoice}"
        self.lblOutcome.text = f"Outcome : {self.outcome}"
        
        self.lblScoreArg.text = f"Argentina  :  {self.scoreArg}"
        self.lblScoreFra.text = f"{self.scoreFra}  :  France"
        self.lblRounds.text = f"Rounds  : {self.rounds}"
        self.lbldirectionArg.text = "->"
        
    def updateButtons(self):
        btnFont = pygame.font.Font("freesansbold.ttf", 1)
        bgColor = (255, 255, 255)
        fgColor =(255, 255, 255)
        btnSize = (1, 1)
        
        for btn in [self.btnUR, self.btnBR, self.btnUL, self.btnBL, self.btnC]:
            btn.bgColor = bgColor
            btn.fgColor = fgColor
            btn.size = btnSize
            btn.font = btnFont
            
        self.btnUR.center = (0, 480)
        self.btnBR.center = (0, 480)
        self.btnUL.center = (0, 480)
        self.btnBL.center = (0, 480)
        self.btnC.center = (0, 480)
        
    def process(self):
        direction = random.randint(1, 100)
        catchRate = random.randint(1, 100)
        
        if self.btnUR.clicked:
            self.argChoice = UR
            self.kicker1.kickerkick()
            self.boom.press()
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.ball.start_moving((250, 290))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.ball.start_moving((330, 300))
                self.ball.update()
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchUR()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 41 <= direction <= 60:
                if 1 <= catchRate <= 50:
                    self.fraChoice = BR
                    self.ball.start_moving((330, 360))
                    self.ball.update
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalUR()
                    self.goal_sound.play()
                    self.scoreFra += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = BR
                    self.ball.start_moving((330, 360))
                    self.ball.update
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchUR()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.ball.start_moving((160, 290))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.ball.start_moving((160, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUR()
                self.goal_sound.play()
                self.scoreFra += 1
        elif self.btnBR.clicked:
            self.argChoice = BR
            self.kicker1.kickerkick()
            self.boom.press()
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.ball.start_moving((250, 290))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 21 <= direction <= 40:
                if 1 <= catchRate <= 50:
                    self.fraChoice = UR
                    self.ball.start_moving((330, 300))
                    self.ball.update()
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalBR()
                    self.goal_sound.play()
                    self.scoreFra += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = UR
                    self.ball.start_moving((330, 300))
                    self.ball.update()
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchBR()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.ball.start_moving((330, 360))
                self.ball.update
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchBR()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.ball.start_moving((160, 290))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.ball.start_moving((160, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBR()
                self.goal_sound.play()
                self.scoreFra += 1
        elif self.btnUL.clicked:
            self.argChoice = UL
            self.kicker1.kickerkick()
            self.boom.press()
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.ball.start_moving((250, 290))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.ball.start_moving((330, 300))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.ball.start_moving((330, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalUL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.ball.start_moving((160, 290))
                self.ball.update
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchUL()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 81 <= direction <= 100:
                if 1 <= catchRate <= 50:
                    self.fraChoice = BL
                    self.ball.start_moving((160, 360))
                    self.ball.update
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalUL()
                    self.goal_sound.play()
                    self.scoreFra += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = BL
                    self.ball.start_moving((160, 360))
                    self.ball.update
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchUL()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
        elif self.btnBL.clicked:
            self.argChoice = BL
            self.kicker1.kickerkick()
            self.boom.press()
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.ball.start_moving((250, 290))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.ball.start_moving((330, 300))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.ball.start_moving((330, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalBL()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 61 <= direction <= 80:
                if 1 <= catchRate <= 50:
                    self.fraChoice = UL
                    self.ball.start_moving((160, 290))
                    self.ball.update
                    self.outcome = GOAL
                    self.goalKeeper.goalKeeperGoalBL()
                    self.goal_sound.play()
                    self.scoreFra += 1
                if 51 <= catchRate <= 100:
                    self.fraChoice = UL
                    self.ball.start_moving((160, 290))
                    self.ball.update
                    self.outcome = NOGOAL
                    self.goalKeeper.goalKeeperCatchBL()
                    self.save_sound.play()
                    self.ball.setImage(self.ball.noGoalImage)
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.ball.start_moving((160, 360))
                self.ball.update
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchBL()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
        elif self.btnC.clicked:
            self.argChoice = C
            self.kicker1.kickerkick()
            self.boom.press()
            self.kick_sound.play()
            self.updateButtons()
            if 1 <= direction <= 20:
                self.fraChoice = C
                self.ball.start_moving((250, 290))
                self.ball.update()
                self.outcome = NOGOAL
                self.goalKeeper.goalKeeperCatchC()
                self.save_sound.play()
                self.ball.setImage(self.ball.noGoalImage)
            elif 21 <= direction <= 40:
                self.fraChoice = UR
                self.ball.start_moving((330, 300))
                self.ball.update()
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 41 <= direction <= 60:
                self.fraChoice = BR
                self.ball.start_moving((330, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 61 <= direction <= 80:
                self.fraChoice = UL
                self.ball.start_moving((160, 290))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreFra += 1
            elif 81 <= direction <= 100:
                self.fraChoice = BL
                self.ball.start_moving((160, 360))
                self.ball.update
                self.outcome = GOAL
                self.goalKeeper.goalKeeperGoalC()
                self.goal_sound.play()
                self.scoreFra += 1        
        elif self.outcome != " ":
            if self.btnNext.clicked:
                self.response = "Next"
                self.stop()

        self.ball.update()
        self.updateLabels()


class Victory(simpleGE.Scene):
    
    def __init__(self, scoreArg=0, scoreFra=0):
        super().__init__()
        pygame.font.init()
        pygame.mixer.init()
        
        self.setImage("white.png")
        
        self.victory_sound = pygame.mixer.Sound("victory.mp3")
        
        self.scoreArg = scoreArg
        self.scoreFra = scoreFra
        
        self.win = Win(self)
        
        self.lblScoreArg = simpleGE.Label()
        self.lblScoreFra = simpleGE.Label()
        self.lblVictory = simpleGE.Label()
        self.lblVictory1 = simpleGE.Label()
        
        self.lblScoreArg.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblScoreArg.fgColor = (116,172,223)
        self.lblScoreArg.bgColor = (255,255,255)
        self.lblScoreFra.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblScoreFra.fgColor = (49,140,231)
        self.lblScoreFra.bgColor = (255,255,255)
        self.lblVictory.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblVictory.fgColor = (253,220,2)
        self.lblVictory.bgColor = (25, 174, 71)
        self.lblVictory1.bgColor = (253,220,2)
            
        self.lblScoreArg.center = (200, 80)
        self.lblScoreArg.size = (240,60)
        self.lblScoreFra.center = (440, 80)
        self.lblScoreFra.size = (240,60)
        self.lblVictory.center = (320, 350)
        self.lblVictory.size = (640,40)
        self.lblVictory1.center = (320, 350)
        self.lblVictory1.size = (640,50)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "      Go Back (C)             "
        self.btnPlay.center = (320, 400)
        self.btnPlay.size = (110, 20)
        self.btnPlay.font = pygame.font.Font("freesansbold.ttf", 10)
        
        self.sprites = [self.lblScoreArg, self.lblScoreFra, self.lblVictory1, self.lblVictory, self.btnPlay, self.win]
        
    def updatelabels(self):
        
        self.lblScoreArg.text = f"Argentina  :  {self.scoreArg}"
        self.lblScoreFra.text = f"{self.scoreFra}  :  France"
        self.lblVictory.text = f"YOU WON!!! ARGENTINA WON THE WORLD CUP!!!"
        
    def process(self):
        self.victory_sound.play()
        self.updatelabels()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        if self.isKeyPressed(pygame.K_c):
            self.response = "Play"
            self.stop()
            
class Defeat(simpleGE.Scene):
    
    def __init__(self, scoreArg=0, scoreFra=0):
        super().__init__()
        pygame.font.init()
        pygame.mixer.init()
        
        self.setImage("white.png")
        
        self.defeat_sound = pygame.mixer.Sound("defeat.mp3")
        
        self.scoreArg = scoreArg
        self.scoreFra = scoreFra
        
        self.lost = Lost(self)
        
        self.lblScoreArg = simpleGE.Label()
        self.lblScoreFra = simpleGE.Label()
        self.lblDefeat = simpleGE.Label()
        self.lblDefeat1 = simpleGE.Label()
        
        self.lblScoreArg.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblScoreArg.fgColor = (116,172,223)
        self.lblScoreArg.bgColor = (255,255,255)
        self.lblScoreFra.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblScoreFra.fgColor = (49,140,231)
        self.lblScoreFra.bgColor = (255,255,255)
        self.lblDefeat.font = pygame.font.Font("freesansbold.ttf", 25)
        self.lblDefeat.fgColor = (116,108,112)
        self.lblDefeat.bgColor = (135, 206,250)
        self.lblDefeat1.bgColor = (116,108,112)
            
        self.lblScoreArg.center = (200, 80)
        self.lblScoreArg.size = (240,60)
        self.lblScoreFra.center = (440, 80)
        self.lblScoreFra.size = (240,60)
        self.lblDefeat.center = (320, 350)
        self.lblDefeat.size = (640,40)
        self.lblDefeat1.center = (320, 350)
        self.lblDefeat1.size = (640,50)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "            Go Back (C)             "
        self.btnPlay.center = (320, 400)
        self.btnPlay.size = (110, 20)
        self.btnPlay.font = pygame.font.Font("freesansbold.ttf", 10)
        
        self.sprites = [self.lblScoreArg, self.lblScoreFra, self.lblDefeat1, self.lblDefeat, self.btnPlay, self.lost]
        
    def updatelabels(self):
        
        self.lblScoreArg.text = f"Argentina  :  {self.scoreArg}"
        self.lblScoreFra.text = f"{self.scoreFra}  :  France"
        self.lblDefeat.text = f"YOU LOST... FRANCE WON THE WORLD CUP..."
        
    def process(self):
        self.defeat_sound.play()
        self.updatelabels()
        if self.btnPlay.clicked:
            self.response = "GoBack"
            self.stop()

        if self.isKeyPressed(pygame.K_c):
            self.response = "GoBack"
            self.stop()

def main():
    pygame.init()
    pygame.mixer.init() 
    
    keepGoing = True
    
    while keepGoing:
        instructions = Instructions()
        instructions.start()
        
        if instructions.response == "Quit":
            keepGoing = False
            break
        elif instructions.response == "Play":
            rounds = 1
            scoreArg = 0
            scoreFra = 0
            
            while rounds <= 5 and keepGoing:
                kickerState = KickerState(rounds, scoreArg, scoreFra)
                kickerState.start()
                if kickerState.response == "Quit":
                    keepGoing = False
                    break
                
                scoreArg = kickerState.scoreArg
                scoreFra = kickerState.scoreFra
                
                goalkeeperState = GoalKeeperState(rounds, scoreArg, scoreFra)
                goalkeeperState.start()
                if goalkeeperState.response == "Quit":
                    keepGoing = False
                    break
                
                scoreArg = goalkeeperState.scoreArg
                scoreFra = goalkeeperState.scoreFra
                
                rounds += 1

            while scoreArg == scoreFra and keepGoing:
                kickerState = KickerState(rounds, scoreArg, scoreFra)
                kickerState.start()
                if kickerState.response == "Quit":
                    keepGoing = False
                    break
                
                scoreArg = kickerState.scoreArg
                scoreFra = kickerState.scoreFra
                
                goalkeeperState = GoalKeeperState(rounds, scoreArg, scoreFra)
                goalkeeperState.start()
                if goalkeeperState.response == "Quit":
                    keepGoing = False
                    break
                
                scoreArg = goalkeeperState.scoreArg
                scoreFra = goalkeeperState.scoreFra
                
                rounds += 1
            
            if keepGoing:
                if scoreArg > scoreFra:
                    victory = Victory(scoreArg, scoreFra)
                    victory.start()
                    if victory.response == "Play":
                        continue  
                    elif victory.response == "Quit":
                        keepGoing = False
                        break
                elif scoreArg < scoreFra:
                    defeat = Defeat(scoreArg, scoreFra)
                    defeat.start()
                    if defeat.response == "Play":
                        continue  
                    elif defeat.response == "Quit":
                        keepGoing = False
                        break

    pygame.quit()


if __name__ == "__main__":
    main()


