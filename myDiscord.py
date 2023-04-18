import pygame
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="myDiscord"
)

mycursor = mydb.cursor()


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([500, 700])
my_font = pygame.font.SysFont('Comic Sans MS', 14)
screen.fill((30, 31, 34))


def loginScreen():
    
    screen.fill((30, 31, 34))
    text_surface = my_font.render("Email", False, (230, 231, 234))
    screen.blit(text_surface, (235, 280))
    pygame.draw.rect(screen, (240, 241, 244), (140, 300, 220, 20))

    text_surface = my_font.render("Password", False, (230, 231, 234))
    screen.blit(text_surface, (227, 330))
    pygame.draw.rect(screen, (240, 241, 244), (140, 350, 220, 20))

    pygame.draw.rect(screen, (50, 51, 54), (150, 400, 125, 20))
    text_surface = my_font.render("Create an account", False, (230, 231, 234))
    screen.blit(text_surface, (155, 400))
    
    pygame.draw.rect(screen, (50, 51, 54), (280, 400, 80, 20))
    text_surface = my_font.render("Login", False, (230, 231, 234))
    screen.blit(text_surface, (305, 400))


def registerScreen():
    
    screen.fill((30, 31, 34))
    title = ["Name", "First Name", "Email", "Password", "re-Password"]
    coord = [(235, 180), (224, 230), (235, 280), (227, 330), (220, 380)]
    
    for a in range(len(title)):
        text_surface = my_font.render(title[a], False, (230, 231, 234))
        screen.blit(text_surface, coord[a])
        pygame.draw.rect(screen, (240, 241, 244), (140, 200 + 50 * a, 220, 20))
        
    pygame.draw.rect(screen, (50, 51, 54), (250, 470, 100, 20))
    text_surface = my_font.render("Register", False, (230, 231, 234))
    screen.blit(text_surface, (275, 470))
    text_surface = my_font.render("already have an", False, (230, 231, 234))
    screen.blit(text_surface, (150, 430))
    text_surface = my_font.render("account ?", False, (230, 231, 234))
    screen.blit(text_surface, (150, 450))
    pygame.draw.rect(screen, (50, 51, 54), (150, 470, 90, 20))
    text_surface = my_font.render("Login", False, (230, 231, 234))
    screen.blit(text_surface, (160, 470))


def logedScreen():
    
    screen.fill((30, 31, 34))
    pygame.draw.rect(screen, (49, 51, 56), (60, 20, 460, 680))
    text_surface = my_font.render("Discart", False, (230, 231, 234))
    screen.blit(text_surface, (10, 0))
    
    pygame.draw.rect(screen, (56, 58, 64), (5, 640, 20, 20))
    #pygame.draw.line(screen, (255, 0, 0), (7, 642), (23, 658), width = 3)
    #pygame.draw.line(screen, (255, 0, 0), (23, 642), (7, 658), width = 3)
    
    pygame.draw.line(screen, (0, 255, 0), (7, 648), (13, 654), width = 3)
    pygame.draw.line(screen, (0, 255, 0), (13, 654), (23, 644), width = 3)
    
    pygame.draw.rect(screen, (56, 58, 64), (35, 640, 20, 20))
    pygame.draw.rect(screen, (230, 10, 12), (40, 642, 10, 16))
    pygame.draw.rect(screen, (56, 58, 64), (42, 644, 6, 12))
    pygame.draw.circle(screen, (230, 10, 12), (47, 649), 1)
    
    pygame.draw.rect(screen, (56, 58, 64), (120, 640, 360, 40))
    pygame.draw.circle(screen, (49, 51, 56), (30, 60), 25)
    pygame.draw.circle(screen, (230, 231, 234), (30,50), 9)
    pygame.draw.rect(screen, (230, 231, 234), (16, 58, 28, 16))


running = True
actual = 0
txt = False

while running:
    
    if actual == 0:
        loginScreen()
        loginEmail = ""
        loginPassword = ""
        login = [loginEmail, loginPassword]
    
    while actual == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                actual = -1
            if event.type == pygame.MOUSEBUTTONUP:
                xy = pygame.mouse.get_pos()
                if 150 <= xy[0] <= 350 and 300 <= xy[1] <= 320:txt = 0
                elif 150 <= xy[0] <= 350 and 350 <= xy[1] <= 370:txt = 1
                elif 150 <= xy[0] <= 280 and 400 <= xy[1] <= 420:actual = 1
                elif 280 <= xy[0] <= 360 and 400 <= xy[1] <= 420:
                    mycursor.execute('select * from login where email = "' + login[0] +'" and password = "' + login[1] + '";')
                    temp = mycursor.fetchall()
                    if len(temp)==0 or True not in [login[0] == x[3] and login[1] == x[4] for x in temp]:
                        text_surface = my_font.render("Something went wrong :/", False, (255, 0, 0))
                        screen.blit(text_surface, (170, 550))
                    else:
                        actual = 2
                else:txt = False
            letter = str(event)
            if event.type == pygame.KEYUP and letter[30:34] == "\\x08" and txt >= 0 and str(txt) != "False":
                if len(login[txt]) > 0:
                    login[txt] = login[txt][:-1]
                    loginScreen()
                    for a in range(2):
                        text_surface = my_font.render(login[a], False, (20,21,24))
                        screen.blit(text_surface, (142, 300 + a * 50))
            if event.type == pygame.TEXTINPUT and txt >= 0 and str(txt) != "False":
                if len(login[txt]) <= 48:
                    login[txt] += letter[31]
                    for a in range(2):
                        text_surface = my_font.render(login[a], False, (20,21,24))
                        screen.blit(text_surface, (142, 300 + a * 50))
        pygame.display.flip()
    
    
    if actual == 1:
        registerScreen()
        registerName, registerFirstName, registerEmail, registerPassword, registerRe_Password = ("",)*5
        register = [registerName, registerFirstName, registerEmail, registerPassword, registerRe_Password]
    
    while actual == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                actual = -1
            if event.type == pygame.MOUSEBUTTONUP:
                xy = pygame.mouse.get_pos()
                if 150 <= xy[0] <= 350 and 200 <= xy[1] <= 220:txt = 0
                elif 150 <= xy[0] <= 350 and 250 <= xy[1] <= 270:txt = 1
                elif 150 <= xy[0] <= 350 and 300 <= xy[1] <= 320:txt = 2
                elif 150 <= xy[0] <= 350 and 350 <= xy[1] <= 370:txt = 3
                elif 150 <= xy[0] <= 350 and 400 <= xy[1] <= 420:txt = 4
                elif 150 <= xy[0] <= 240 and 470 <= xy[1] <= 490:actual = 0
                elif 250 <= xy[0] <= 350 and 470 <= xy[1] <= 490:
                    if len(register[0]) <= 0 or len(register[1]) <= 1  or len(register[2]) <= 12 or "@" not in register[2] or len(register[3]) <= 6 or register[3] != register[4]:
                        text_surface = my_font.render("Something went wrong :/", False, (255, 0, 0))
                        screen.blit(text_surface, (170, 550))
                    
                    else:
                        mycursor.execute('SELECT * FROM login WHERE email = "' + register[2] + '";')
                        temp = mycursor.fetchall()
                        if len(temp) > 0:
                            text_surface = my_font.render("Something went wrong :/", False, (255, 0, 0))
                            screen.blit(text_surface, (170, 550))
                        else:
                            
                            mycursor.execute('INSERT INTO login (name, firstname, email, password) VALUES ("{}", "{}", "{}", "{}");'.format(register[0], register[1], register[2], register[3]))
                            mydb.commit()
                            mycursor.execute('SELECT * FROM login;')
                            temp = mycursor.fetchall()
                            mycursor.execute("CREATE TABLE user" + str(temp[-1][0]) + "(source varchar (255), txt text, hour int);")
                            mydb.commit()
                            actual = 0
                else:txt = False
            letter = str(event)
            if event.type == pygame.KEYUP and letter[30:34] == "\\x08" and txt >= 0 and str(txt) != "False":
                if len(register[txt]) > 0:
                    register[txt] = register[txt][:-1]
                    registerScreen()
                    for a in range(5):
                        text_surface = my_font.render(register[a], False, (20,21,24))
                        screen.blit(text_surface, (142, 200 + a * 50))
            if event.type == pygame.TEXTINPUT and txt >= 0 and str(txt) != "False":
                if len(register[txt]) <= 48:
                    register[txt] += letter[31]
                    for a in range(5):
                        text_surface = my_font.render(register[a], False, (20,21,24))
                        screen.blit(text_surface, (142, 200 + a * 50))
        pygame.display.flip()            
    
    
    if actual == 2:
        logedScreen()
        logedWrite = ""
        loged = 0
        
        mycursor.execute('select id from login where email = "' + login[0] + '" and password = "' + login[1] + '";')
        temp = mycursor.fetchall()
        text_surface = my_font.render("ID : " + str(temp[0][0]), False, (230,231,234))
        screen.blit(text_surface, (9 - (len(str(temp[0][0])) - 1) * 4, 675))
    
    while actual == 2:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
                actual = -1
            if event.type == pygame.MOUSEBUTTONUP:
                xy = pygame.mouse.get_pos()
                if 120 <= xy[0] <= 480 and 640 <= xy[1] <= 680:txt = 0
                elif 5 <= xy[0] <= 55 and 35 <= xy[1] <= 85 and loged == 0:
                    loged = 1
                    pygame.draw.circle(screen, (230, 231, 234), (30, 60), 25)
                    pygame.draw.circle(screen, (49, 51, 56), (30,50), 9)
                    pygame.draw.rect(screen, (49, 51, 56), (16, 58, 28, 16))
                    
                elif 5 <= xy[0] <= 55 and 35 <= xy[1] <= 85 and loged == 1:
                    loged = 0
                    pygame.draw.circle(screen, (49, 51, 56), (30, 60), 25)
                    pygame.draw.circle(screen, (230, 231, 234), (30,50), 9)
                    pygame.draw.rect(screen, (230, 231, 234), (16, 58, 28, 16))
                elif 35 <= xy[0] <= 55 and 640 <= xy[1] <= 660:
                    actual = 0

        pygame.display.flip()
        
pygame.quit()
