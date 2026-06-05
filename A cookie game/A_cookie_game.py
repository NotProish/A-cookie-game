import pygame
import sys
import time
import random

# Initialize pygame
pygame.init()
pygame.mixer.init() 

# Screen size and font (irrelvant now that fullscreen but will keep jic)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 42

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("A Cookie Game")
clock = pygame.time.Clock()

# Load images
cookie_image = pygame.image.load("cookie.png")
Pixelcookie_img = pygame.image.load('Pixelcookie.png')
Candycookie_img = pygame.image.load('Candycookie.png')
gingerbreadcookie_img = pygame.image.load('gingerbreadcookie.png')
macadamiacookie_img = pygame.image.load('macadamiacookie.png')
Donutcookie_img = pygame.image.load('Donutcookie.png')
Onechipcookie_img = pygame.image.load('Onechipcookie.png')
Bird_img = pygame.image.load('Bird.png')
realcandycookie_img = pygame.image.load('realcandycookie.png')
frosted_img = pygame.image.load('frosted.png')
mooncookie_img = pygame.image.load('mooncookie.png')

# Resize images to fit
cookie_img = pygame.transform.scale(cookie_image, (100, 100))
Pixelcookie_img = pygame.transform.scale(Pixelcookie_img, (200, 200))   # its tiny so i doubled it
Candycookie_img = pygame.transform.scale(Candycookie_img, (100, 100))
gingerbreadcookie_img = pygame.transform.scale(gingerbreadcookie_img, (100, 100))
macadamiacookie_img = pygame.transform.scale(macadamiacookie_img, (100, 100))
Donutcookie_img = pygame.transform.scale(Donutcookie_img, (100, 100))
Onechipcookie_img = pygame.transform.scale(Onechipcookie_img, (100, 100))
Bird_img = pygame.transform.scale(Bird_img, (100, 100))
realcandycookie_img = pygame.transform.scale(realcandycookie_img, (100, 100))
frosted_img = pygame.transform.scale(frosted_img, (100, 100))
mooncookie_img = pygame.transform.scale(mooncookie_img, (100, 100))


# Upgrade costs
upgrade_costs = {
   
    
    "The":10,
    "Pixel": 25,  
    "Candy": 40,
    "Gingerbread": 50,
    "Macadamia": 60,
    "Donut": 70,
    "Onechip": 100,
    "Bird": 125,
    "real candy": 250,
    "frosted": 1000,
    "moon": 0
}

# Set the starting cookie image and upgrade level
current_cookie_img = cookie_img
current_upgrade = "The"

# Function to play background music
def play_music(mp3_file):
    try:
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play(-1)
        print(f"Playing: {mp3_file}")
    except pygame.error as e:
        print(f"Error loading music: {e}")

# Load background music file
mp3_file = r"Gamesound.mp3"
play_music(mp3_file)  # Play music at the start

# Load click sound (with error handling)
try:
    click_sound = pygame.mixer.Sound(r"Eat.mp3")
    click_sound.set_volume(1.0)  # Ensure max volume
except pygame.error:
    click_sound = None
    print("Error loading click sound!")

# Load font with error handling
try:
    base_font = pygame.font.Font("font.ttf", FONT_SIZE)
except FileNotFoundError:
    base_font = pygame.font.SysFont(None, FONT_SIZE)

# Load the cookie image

cookie_img = pygame.image.load("cookie.png").convert_alpha()
cookie_img = pygame.transform.scale(cookie_img, (80, 80))  


# Randomize cookie position within screen bounds
cookie_pos = (
    random.randint(50, SCREEN_WIDTH - 50),
    random.randint(50, SCREEN_HEIGHT - 50),
)

start_time = time.time()
cookies = 0  # Start at 0 for better milestone tracking

# List of possible messages
milestone_messages = [
    "Meow", "Very wow", "Thats it buddy?", "YOU CAN DO IT", "sigma",
    "ty Mr. Camden", "You are the best", "You are amazing", "You are a genius",
    "AMAZING", "11/10", "To the moon", "O_O", "I am sad", "just keep clicking",
    "did you know that 1 in 1 people that have played this game played the game?",
    "if you keep clicking you will get a cookie jk", "Are you hungry?",
    "*insert epic gamer music here*", "Whats up?", "I am a cookie",
    "Whats up with the cookie?", "I baked you a pie oh boy what flavor... oh wait its a cookie",
    "Eat me", "lucky you", "this message has a 1 in 100,000 chance of being displayed",
    "click me", "BEHIND YOU!!!!!!!!", "STOP THE COOKIE JOKES!", "Drink water",
    "Whats big and round and has a lot of chocolate", "1+1=3",
    "Google how to cookie", "Yipee", "Nihad wuz here","Its raining cookies", "I am floating", "Ilyas wuz here",
    "Look outside", "touch some grass", "alr alr you gotta stop playing now", "thats hilarious", "Omar I am not trying to add",
    "ok bro ok bro", "You.. Yes you", "Goblin!!!", "25 punds", "sad nka", "blub",
    "Yup", "Oh uhm", "Cookie N & N's why?", "making a full replica", "CoKieS",
    "TrY My COoogIEs", "Nom Nom Nom", "hahaha so funny", "Speak louder I can't hear you", "Oh i have a funny one",
    "NO", "Me too", "Wait I wasn't ready", "i go back to work", "why bcuz its not nice", "mix diet cookies and mens toes",
    "because immmm shinay", "Look", "Move on to the next one", "You can also remove it", "that might be the easiest way",
    "please elaborate", "Y H Z", "You mined one cookie", "Oh thats actually pretty fast", "I'm drowning.. In cookies",
    "I'll pass", "is this msg inconsistant?", "dont let them", "I lied", "CTRL + W to win", "cat cookie?"
]

# Track the last displayed message
last_milestone = 0
message_text = ""
message_pos = (0, 0)
message_font = None

# Function to draw the upgrade menu
def draw_upgrade_menu():
    upgrade_text = f"Upgrade: {current_upgrade} Cookie"
    cost_text = f"Cost: {upgrade_costs[current_upgrade] if current_upgrade != 'moon' else 'Maxed Out'}"

    upgrade_surface = base_font.render(upgrade_text, True, (255, 255, 255))
    cost_surface = base_font.render(cost_text, True, (255, 255, 255))

    screen.blit(upgrade_surface, (SCREEN_WIDTH // 2 - upgrade_surface.get_width() // 2, SCREEN_HEIGHT - 100))
    screen.blit(cost_surface, (SCREEN_WIDTH // 2 - cost_surface.get_width() // 2, SCREEN_HEIGHT - 50))

# Modify handle_upgrade() function
def handle_upgrade():
    global current_cookie_img, current_upgrade, cookies

    if cookies >= upgrade_costs.get(current_upgrade, float('inf')): 
        if current_upgrade == "The":
            cookies -= upgrade_costs["The"] 
            current_cookie_img = Pixelcookie_img 
            current_upgrade = "Pixel"

        elif current_upgrade == "Pixel":
            cookies -= upgrade_costs["Pixel"]
            current_cookie_img = Candycookie_img
            current_upgrade = "Candy"

        elif current_upgrade == "Candy":
            cookies -= upgrade_costs["Candy"]
            current_cookie_img = gingerbreadcookie_img
            current_upgrade = "Gingerbread"

        elif current_upgrade == "Gingerbread":
            cookies -= upgrade_costs["Gingerbread"]
            current_cookie_img = macadamiacookie_img
            current_upgrade = "Macadamia"

        elif current_upgrade == "Macadamia":
            cookies -= upgrade_costs["Macadamia"]
            current_cookie_img = Donutcookie_img
            current_upgrade = "Donut"

        elif current_upgrade == "Donut":
            cookies -= upgrade_costs["Donut"]
            current_cookie_img = Onechipcookie_img
            current_upgrade = "Onechip"

        elif current_upgrade == "Onechip":
            cookies -= upgrade_costs["Onechip"]
            current_cookie_img = Bird_img
            current_upgrade = "Bird"

        elif current_upgrade == "Bird":
            cookies -= upgrade_costs["Bird"]
            current_cookie_img = realcandycookie_img
            current_upgrade = "real candy"

        elif current_upgrade == "real candy":
            cookies -= upgrade_costs["real candy"]
            current_cookie_img = frosted_img
            current_upgrade = "frosted"

        elif current_upgrade == "frosted":
            cookies -= upgrade_costs["frosted"]
            current_cookie_img = mooncookie_img
            current_upgrade = "moon"

if cookies >= upgrade_costs[current_upgrade]:
    handle_upgrade()

# Main game loop
def main():
    global cookie_pos, cookies, last_milestone, message_text, message_pos, message_font
    running = True

    while running:
        screen.fill((69, 69, 69))

        # Load background image
        background_img = pygame.image.load("Background.png") 

        # In your main loop, before drawing anything else
        screen.blit(background_img, (0, 0))  

        # Update cookie position rectangle
        cookie_rect = current_cookie_img.get_rect(center=cookie_pos)

        # Draw the cookie image
        screen.blit(current_cookie_img, cookie_rect)

        # Display cookies and time
        text = f"cookies: {cookies}    Time: {int(time.time() - start_time)}"
        text_surface = base_font.render(text, True, "gold")
        screen.blit(text_surface, text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50)))

        # Increments by 2 for a random message
        if cookies % 2 == 0 and cookies > 0 and cookies != last_milestone:
            last_milestone = cookies  # Update last milestone
            message_text = random.choice(milestone_messages)  # Choose a random message

            # Randomize position within the same bounds as the cookie
            message_pos = (
                random.randint(100, SCREEN_WIDTH - 100),
                random.randint(100, SCREEN_HEIGHT - 100)
            )

            message_font_size = random.randint(30, 40)
            message_font = pygame.font.SysFont(None, message_font_size)

        
        if message_text and message_font:
            message_surface = message_font.render(message_text, True, "red")
            screen.blit(message_surface, message_surface.get_rect(center=message_pos))

        
        draw_upgrade_menu()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and cookie_rect.collidepoint(event.pos):
                if click_sound:
                    click_sound.play()  # Play click sound

                # Move cookie
                cookie_pos = (
                    random.randint(50, SCREEN_WIDTH - 50),
                    random.randint(50, SCREEN_HEIGHT - 50)
                )
                cookies += 1

            # Handle mouse clicks for upgrading
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Checks if the player clicks on the upgrade menu area
                if (SCREEN_WIDTH // 2 - 100 <= mouse_x <= SCREEN_WIDTH // 2 + 100) and (SCREEN_HEIGHT - 100 <= mouse_y <= SCREEN_HEIGHT - 50):
                    handle_upgrade()

        if cookies < 0:
          cookies = 0

        clock.tick(69) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()