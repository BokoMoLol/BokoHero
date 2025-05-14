import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guitar Hero - Simplified")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Columns and keys
columns = ['c', 'v', 'b', 'n', 'm']
column_width = SCREEN_WIDTH // len(columns)
notes = []
score = 0

# Note class
class Note:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key
        self.width = column_width - 10
        self.height = 20

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def move(self, speed):
        self.y += speed

# Generate random notes
def generate_note():
    key = random.choice(columns)
    x = columns.index(key) * column_width + 5
    return Note(x, 0, key)

# Main game loop
def main():
    global score
    running = True
    note_speed = 5
    spawn_rate = 30  # Frames per note spawn
    frame_count = 0

    while running:
        screen.fill(BLACK)
        frame_count += 1

        # Draw the columns
        for i in range(len(columns)):
            x = i * column_width
            pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT), 2)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get pressed keys
        keys = pygame.key.get_pressed()
        for note in notes[:]:
            if note.y + note.height >= SCREEN_HEIGHT - 50 and keys[pygame.K_c + columns.index(note.key)]:
                score += 1
                notes.remove(note)

        # Update and draw notes
        for note in notes:
            note.move(note_speed)
            note.draw()
            if note.y > SCREEN_HEIGHT:
                notes.remove(note)

        # Generate new notes
        if frame_count % spawn_rate == 0:
            notes.append(generate_note())

        # Draw the score
        score_text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
