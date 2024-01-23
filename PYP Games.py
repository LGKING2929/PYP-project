import pygame
import sys

pygame.init()

# Set up game window (fullscreen)
screen_info = pygame.display.Info()
window_size = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
pygame.display.set_caption("Microorganism Quiz")

# Define colors
blue = (0, 0, 255)
green = (0, 255, 0)
highlight_color = (255, 255, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Introduction screen
intro_text = font.render("Welcome to the Microorganism Quiz!", True, (255, 255, 255))
intro_rect = intro_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 - 50))
start_button_text = font.render("Start Quiz", True, (255, 255, 255))
start_button_rect = start_button_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 + 50))

info_text = [
    "Test your knowledge about microorganisms!",
    "Each question has multiple-choice options.",
    "Click on the correct answer to score points.",
    "You can navigate to the next question using the 'Next' button.",
    "Good luck!"
]

info_rects = [font.render(line, True, (255, 255, 255)).get_rect(center=(window_size[0] // 2, (i + 1) * 50))
              for i, line in enumerate(info_text)]

screen.fill(blue)
screen.blit(intro_text, intro_rect)
pygame.draw.rect(screen, highlight_color, start_button_rect, 2)
screen.blit(start_button_text, start_button_rect)

for info_rect, info_line in zip(info_rects, info_text):
    screen.blit(font.render(info_line, True, (255, 255, 255)), info_rect)

pygame.display.flip()

# Wait for user to click "Start Quiz" button
waiting_for_start = True
while waiting_for_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button_rect.collidepoint(event.pos):
                waiting_for_start = False

# Define quiz questions and answers
quiz = [
    {"question": "What makes bread rise?",
     "options": ["Yeast", "Sugar", "Salt", "Water"],
     "correct_answer": "Yeast",
     "background": blue},

    {"question": "What is the powerhouse of the cell?",
     "options": ["Nucleus", "Mitochondria", "Cell Membrane", "Cytoplasm"],
     "correct_answer": "Mitochondria",
     "background": green},

    {"question": "What causes tooth decay?",
     "options": ["Sugar", "Bacteria", "Acid", "Plaque"],
     "correct_answer": "Bacteria",
     "background": green},

    {"question": "Which microorganism is used to make yogurt?",
     "options": ["Yeast", "Bacteria", "Mold", "Virus"],
     "correct_answer": "Bacteria",
     "background": blue},

    {"question": "What is the main component of bacterial cell walls?",
     "options": ["Protein", "DNA", "Lipids", "Peptidoglycan"],
     "correct_answer": "Peptidoglycan",
     "background": green},

    {"question": "What causes the common cold?",
     "options": ["Bacteria", "Virus", "Allergens", "Fungi"],
     "correct_answer": "Virus",
     "background": blue},

    {"question": "What is the structure of a virus?",
     "options": ["Protein Coat", "Nucleic Acid", "Cell Membrane", "Mitochondria"],
     "correct_answer": "Nucleic Acid",
     "background": green},

    {"question": "Which microorganism is used in brewing beer?",
     "options": ["Yeast", "Bacteria", "Mold", "Virus"],
     "correct_answer": "Yeast",
     "background": green},

    {"question": "What is the smallest unit of life?",
     "options": ["Cell", "Molecule", "Atom", "Organism"],
     "correct_answer": "Cell",
     "background": blue},

    {"question": "Which microorganism is used to make antibiotics?",
     "options": ["Yeast", "Bacteria", "Mold", "Virus"],
     "correct_answer": "Mold",
     "background": blue},
]

current_question = 0
score = 0

# Main game loop
while current_question < len(quiz):
    screen.fill(quiz[current_question]["background"])

    # Display question
    question_text = font.render(quiz[current_question]["question"], True, (255, 255, 255))
    question_rect = question_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 - 50))
    screen.blit(question_text, question_rect)

    # Display options with highlighting on hover
    option_width = window_size[0] // len(quiz[current_question]["options"])
    option_rects = []
    for i, option in enumerate(quiz[current_question]["options"]):
        option_text = font.render(option, True, (255, 255, 255))
        option_rect = option_text.get_rect(center=(i * option_width + option_width // 2, window_size[1] - 75))
        option_rects.append(option_rect)

        # Highlight the option if the cursor is over it
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, highlight_color, option_rect)

        screen.blit(option_text, option_rect)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            # Check if the mouse click is in the option area
            for i, option_rect in enumerate(option_rects):
                if option_rect.collidepoint(event.pos):
                    # Check if the selected option is correct
                    if quiz[current_question]["options"][i] == quiz[current_question]["correct_answer"]:
                        score += 1

                    # Move to the next question
                    current_question += 1

                    # If there are more questions, clear the screen for the next one
                    if current_question < len(quiz):
                        screen.fill(quiz[current_question]["background"])

                    break

# Display the score summary
summary_text = font.render(f"Quiz Completed! Your Score: {score}/{len(quiz)}", True, (255, 255, 255))
summary_rect = summary_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 - 50))
screen.fill(blue)  # You can change the background color for the summary
screen.blit(summary_text, summary_rect)
pygame.display.flip()

# Wait for a moment before quitting
pygame.time.delay(5000)

# End the game loop
pygame.quit()
sys.exit()
