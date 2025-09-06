import pygame
import random
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")  # Normal running
    return os.path.join(base_path, relative_path)

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Load font
font_path = resource_path("Font/Pixeltype.ttf")
font = pygame.font.Font(font_path, 60)

choices = ["rock", "paper", "scissors"]

# Load images
paper_surf = pygame.image.load(resource_path("Graphics/Paper.png")).convert_alpha()
paper_surf_down = pygame.transform.scale(paper_surf, (150, 249))
paper_rect = paper_surf_down.get_rect(midbottom=(400, 300))

rock_surf = pygame.image.load(resource_path("Graphics/Rock.png")).convert_alpha()
rock_surf_down = pygame.transform.scale(rock_surf, (183, 210))
rock_surf_rect = rock_surf_down.get_rect(midbottom=(200, 300))

scissors_surf = pygame.image.load(resource_path("Graphics/Scissors.png")).convert_alpha()
scissors_surf_down = pygame.transform.scale(scissors_surf, (157, 261))
scissors_rect = scissors_surf_down.get_rect(midbottom=(600, 300))

button_surf = pygame.image.load(resource_path("Graphics/button.png")).convert_alpha()
button_surf_down = pygame.transform.scale(button_surf, (250, 125))
button_surf_rect_1 = button_surf_down.get_rect(center=(400, 150))
button_surf_rect_2 = button_surf_down.get_rect(center=(400, 250))
button_surf_rect_3 = button_surf_down.get_rect(center=(400, 350))

# Text
welcome_text = font.render("Welcome to RPS", True, "#000000")
welcome_text_rect = welcome_text.get_rect(center=(400, 60))
play_text = font.render("Play", True, "#000000")
play_text_rect = play_text.get_rect(center=(400, 150))
main_menu_text = font.render("Main Menu", True, "#000000")
main_menu_text_rect = main_menu_text.get_rect(center=(400, 250))
quit_text = font.render("Quit", True, "#000000")
quit_text_rect = quit_text.get_rect(center=(400, 250))
quit_text_rect_2 = quit_text.get_rect(center=(400, 350))

def rps_main(pchoice):
    cchoice = random.choice(choices)
    if pchoice == cchoice:
        return "It's a Draw!"
    elif (pchoice == "rock" and cchoice == "scissors") or \
         (pchoice == "paper" and cchoice == "rock") or \
         (pchoice == "scissors" and cchoice == "paper"):
        return "You Win!"
    else:
        return "You Lose!"

screen_state = "main_menu"
game_result = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if screen_state == "main_menu":
                if button_surf_rect_1.collidepoint(event.pos):
                    screen_state = "game"
                elif button_surf_rect_2.collidepoint(event.pos):
                    pygame.quit()
                    exit()
            elif screen_state == "game":
                if rock_surf_rect.collidepoint(event.pos):
                    game_result = rps_main("rock")
                    screen_state = "result"
                elif paper_rect.collidepoint(event.pos):
                    game_result = rps_main("paper")
                    screen_state = "result"
                elif scissors_rect.collidepoint(event.pos):
                    game_result = rps_main("scissors")
                    screen_state = "result"
            elif screen_state == "result":
                if button_surf_rect_1.collidepoint(event.pos):
                    screen_state = "game"
                elif button_surf_rect_2.collidepoint(event.pos):
                    screen_state = "main_menu"
                elif button_surf_rect_3.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    screen.fill("#fff1f1")

    if screen_state == "main_menu":
        screen.blit(welcome_text, welcome_text_rect)
        screen.blit(button_surf_down, button_surf_rect_1)
        screen.blit(play_text, play_text_rect)
        screen.blit(button_surf_down, button_surf_rect_2)
        screen.blit(quit_text, quit_text_rect)
    elif screen_state == "game":
        screen.blit(rock_surf_down, rock_surf_rect)
        screen.blit(paper_surf_down, paper_rect)
        screen.blit(scissors_surf_down, scissors_rect)
    elif screen_state == "result":
        result_text = font.render(game_result, True, "#000000")
        result_rect = result_text.get_rect(center=(400, 60))
        screen.blit(result_text, result_rect)
        screen.blit(button_surf_down, button_surf_rect_1)
        screen.blit(play_text, play_text_rect)
        screen.blit(button_surf_down, button_surf_rect_2)
        screen.blit(main_menu_text, main_menu_text_rect)
        screen.blit(button_surf_down, button_surf_rect_3)
        screen.blit(quit_text, quit_text_rect_2)

    pygame.display.update()
    clock.tick(60)

