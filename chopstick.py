import pygame
import math
import time
import threading
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dining Philosophers Simulation 🍽️")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
GREEN = (0, 200, 0)    # Eating
BLUE = (50, 100, 255)  # Thinking
RED = (200, 0, 0)      # Chopstick in use

# Philosopher & chopstick state
phil_state = ["thinking"] * 5  # possible values: "thinking", "eating"
chopstick_state = [0] * 5      # 0 = free, 1 = in use

# Positions in a circle
RADIUS = 200
CENTER = (WIDTH // 2, HEIGHT // 2)
philosopher_positions = []
chopstick_positions = []

for i in range(5):
    angle = (2 * math.pi / 5) * i
    x = CENTER[0] + RADIUS * math.cos(angle)
    y = CENTER[1] + RADIUS * math.sin(angle)
    philosopher_positions.append((x, y))

    # Chopsticks slightly inward
    cx = CENTER[0] + (RADIUS - 80) * math.cos(angle + math.pi/5)
    cy = CENTER[1] + (RADIUS - 80) * math.sin(angle + math.pi/5)
    chopstick_positions.append((cx, cy))


def draw_scene():
    """Draw philosophers and chopsticks."""
    screen.fill(WHITE)

    # Draw chopsticks
    for i in range(5):
        color = RED if chopstick_state[i] else GRAY
        pygame.draw.circle(screen, color, (int(chopstick_positions[i][0]), int(chopstick_positions[i][1])), 15)

    # Draw philosophers
    for i in range(5):
        color = GREEN if phil_state[i] == "eating" else BLUE
        pygame.draw.circle(screen, color, (int(philosopher_positions[i][0]), int(philosopher_positions[i][1])), 40)
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"P{i}", True, WHITE)
        screen.blit(text, (philosopher_positions[i][0]-10, philosopher_positions[i][1]-10))

    pygame.display.update()


def philosopher(i):
    """Simulate philosopher i alternately thinking and eating."""
    global phil_state, chopstick_state

    while True:
        # Thinking
        phil_state[i] = "thinking"
        draw_scene()
        time.sleep(random.uniform(1, 3))

        # Try to pick chopsticks
        left = i
        right = (i + 1) % 5
        if chopstick_state[left] == 0 and chopstick_state[right] == 0:
            # Pick chopsticks
            chopstick_state[left] = chopstick_state[right] = 1
            phil_state[i] = "eating"
            draw_scene()
            time.sleep(random.uniform(1, 3))
            # Release chopsticks
            chopstick_state[left] = chopstick_state[right] = 0


def main():
    # Start philosophers as threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=philosopher, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)

    running = True
    while running:
        draw_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
