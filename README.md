# Chopstick
ABOUT THE CODE:
This code simulates the dining philosophers problem, a classic synchronization problem in computer science.
The phil list represents the state of each philosopher, where 0 means they are thinking and 1 means they are eating.
The chopstick list represents the availability of each chopstick, where 0 means it's available and 1 means it's being used by a philosopher.
The signal(z) function releases the chopsticks held by philosopher z, allowing them to be used by other philosophers.
The wait(y) function implements the logic for a philosopher to wait for both chopsticks to be available before starting to eat. If one of the chopsticks or both are not available, the philosopher waits until they are both available. If the philosopher is already eating, they can choose to stop eating.
The main() function initializes the philosophers and chopsticks, then enters a loop where each philosopher takes turns to either think or eat based on user input.
Inside the loop, the state of each philosopher is printed, and the user is prompted to input which philosopher will eat next. Then, the wait() function is called to handle the eating process.
After each round, the user is asked if they want to continue. If not, the loop breaks, and the program ends.

# Dining Philosophers Simulation 🍽️🤔
This project is a **visual simulation** of the classic **Dining Philosophers Problem** using **Python and Pygame**.  
The philosophers sit around a round table, alternating between **thinking** 💭 and **eating** 🍴. Each philosopher needs two chopsticks to eat, but chopsticks are shared with neighbors.
## 📖 Problem Statement
The Dining Philosophers problem is a famous **synchronization problem** in computer science.  
It illustrates challenges like:
- **Deadlock** (all philosophers waiting forever)
- **Starvation** (one philosopher never gets to eat)
- **Concurrency control** in shared resources.
## 🎮 Features
- Animated simulation with philosophers sitting in a circle.
- Philosophers **change colors**:
  - 🟦 Blue → Thinking
  - 🟩 Green → Eating
- Chopsticks **light up**:
  - ⚪ Gray → Free
  - 🔴 Red → In use
- Random timing for eating/thinking to simulate concurrency.
- Runs in real-time using **threads**.
Run the program:
python chopstick.py

Run the program:

![chopstick-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/45b129c8-46dc-4828-90be-419b4e4b3ff0)

