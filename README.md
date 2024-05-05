# Chopstick
This code simulates the dining philosophers problem, a classic synchronization problem in computer science.
The phil list represents the state of each philosopher, where 0 means they are thinking and 1 means they are eating.
The chopstick list represents the availability of each chopstick, where 0 means it's available and 1 means it's being used by a philosopher.
The signal(z) function releases the chopsticks held by philosopher z, allowing them to be used by other philosophers.
The wait(y) function implements the logic for a philosopher to wait for both chopsticks to be available before starting to eat. If one of the chopsticks or both are not available, the philosopher waits until they are both available. If the philosopher is already eating, they can choose to stop eating.
The main() function initializes the philosophers and chopsticks, then enters a loop where each philosopher takes turns to either think or eat based on user input.
Inside the loop, the state of each philosopher is printed, and the user is prompted to input which philosopher will eat next. Then, the wait() function is called to handle the eating process.
After each round, the user is asked if they want to continue. If not, the loop breaks, and the program ends.
