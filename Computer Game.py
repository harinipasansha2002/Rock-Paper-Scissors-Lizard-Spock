from graphics import *
import random
import time

def get_user_choice_with_timer(win, timeout, timer_text):
    """ Wait for the user to click on one of the choice ovals within the timeout period and return their choice. """
    global last_selected_oval  # Keep track of the last selected oval
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, timeout - elapsed_time)
        timer_text.setText(f"Time left: {remaining_time:.1f} s")
        
        if remaining_time <= 0:
            return None

        click_point = win.checkMouse()
        if click_point:
            # Determine which oval was clicked
            if aOval.getP1().getX() < click_point.getX() and click_point.getX() < aOval.getP2().getX() and aOval.getP1().getY() < click_point.getY() and click_point.getY() < aOval.getP2().getY():
                choice = "Rock"
                selected_oval = aOval
            elif bOval.getP1().getX() < click_point.getX() and click_point.getX() < bOval.getP2().getX() and bOval.getP1().getY() < click_point.getY() and click_point.getY() < bOval.getP2().getY():
                choice = "Paper"
                selected_oval = bOval
            elif cOval.getP1().getX() < click_point.getX() and click_point.getX() < cOval.getP2().getX() and cOval.getP1().getY() < click_point.getY() and click_point.getY() < cOval.getP2().getY():
                choice = "Scissors"
                selected_oval = cOval
            elif dOval.getP1().getX() < click_point.getX() and click_point.getX() < dOval.getP2().getX() and dOval.getP1().getY() < click_point.getY() and click_point.getY() < dOval.getP2().getY():
                choice = "Lizard"
                selected_oval = dOval
            elif eOval.getP1().getX() < click_point.getX() and click_point.getX() < eOval.getP2().getX() and eOval.getP1().getY() < click_point.getY() and click_point.getY() < eOval.getP2().getY():
                choice = "Spock"
                selected_oval = eOval
            else:
                continue

            # Fill the selected oval with red
            selected_oval.setFill("red")

            # Reset the previously selected oval's color
            if last_selected_oval and last_selected_oval != selected_oval:
                last_selected_oval.setFill("")

            # Update the last selected oval
            last_selected_oval = selected_oval
            
            return choice

def reset_computer_choice_colors():
    """ Reset the color of the computer choice ovals. """
    fOval.setFill("")
    gOval.setFill("")
    hOval.setFill("")
    iOval.setFill("")
    jOval.setFill("")

def highlight_computer_choice(choice):
    """ Highlight the oval corresponding to the computer's choice. """
    if choice == "Rock":
        fOval.setFill("red")
    elif choice == "Paper":
        gOval.setFill("red")
    elif choice == "Scissors":
        hOval.setFill("red")
    elif choice == "Lizard":
        iOval.setFill("red")
    elif choice == "Spock":
        jOval.setFill("red")

# Initialize the window
win = GraphWin("Rock Paper Scissors Lizard Spock", 650, 675)
win.setBackground("gray")

# Create and customize the heading text
my_heading = Text(Point(320, 50), "Rock Paper Scissors Lizard Spock")
my_heading.draw(win)
my_heading.setFace("arial")
my_heading.setSize(22)
my_heading.setStyle("bold")
my_heading.setTextColor("lime")

# Create and customize the "Round No:" text
aText = Text(Point(320, 120), "Round No: 0")
aText.setFace("arial")
aText.setSize(20)
aText.setStyle("bold")
aText.setTextColor("black")
aText.draw(win)

# Create and customize the timer text
timer_text = Text(Point(320, 160), "Time left: 3.0 s")
timer_text.setFace("arial")
timer_text.setSize(18)
timer_text.setStyle("bold")
timer_text.setTextColor("red")
timer_text.draw(win)

# Create and customize the "User Choice" label
bText = Text(Point(150, 190), "User Choice")
bText.setFace("arial")
bText.setSize(18)
bText.setStyle("bold")
bText.setTextColor("cyan")
bText.draw(win)

# Draw options for user choice (as buttons)
aOval = Oval(Point(100, 230), Point(200, 270))
aOval.draw(win)
cText = Text(Point(150, 250), "Rock")
cText.setFace("arial")
cText.setSize(16)
cText.setStyle("bold")
cText.draw(win)

bOval = Oval(Point(100, 290), Point(200, 330))
bOval.draw(win)
dText = Text(Point(150, 310), "Paper")
dText.setFace("arial")
dText.setSize(16)
dText.setStyle("bold")
dText.draw(win)

cOval = Oval(Point(90, 350), Point(210, 390))
cOval.draw(win)
eText = Text(Point(150, 370), "Scissors")
eText.setFace("arial")
eText.setSize(16)
eText.setStyle("bold")
eText.draw(win)

dOval = Oval(Point(100, 410), Point(200, 450))
dOval.draw(win)
fText = Text(Point(150, 430), "Lizard")
fText.setFace("arial")
fText.setSize(16)
fText.setStyle("bold")
fText.draw(win)

eOval = Oval(Point(100, 470), Point(200, 510))
eOval.draw(win)
gText = Text(Point(150, 490), "Spock")
gText.setFace("arial")
gText.setSize(16)
gText.setStyle("bold")
gText.draw(win)

# Create and customize the "Computer Choice" label
hText = Text(Point(480, 190), "Computer Choice")
hText.setFace("arial")
hText.setSize(18)
hText.setStyle("bold")
hText.setTextColor("cyan")
hText.draw(win)

# Draw options for computer choice
fOval = Oval(Point(430, 230), Point(530, 270))
fOval.draw(win)
iText = Text(Point(480, 250), "Rock")
iText.setFace("arial")
iText.setSize(16)
iText.setStyle("bold")
iText.draw(win)

gOval = Oval(Point(430, 290), Point(530, 330))
gOval.draw(win)
jText = Text(Point(480, 310), "Paper")
jText.setFace("arial")
jText.setSize(16)
jText.setStyle("bold")
jText.draw(win)

hOval = Oval(Point(420, 350), Point(540, 390))
hOval.draw(win)
kText = Text(Point(480, 370), "Scissors")
kText.setFace("arial")
kText.setSize(16)
kText.setStyle("bold")
kText.draw(win)

iOval = Oval(Point(430, 410), Point(530, 450))
iOval.draw(win)
lText = Text(Point(480, 430), "Lizard")
lText.setFace("arial")
lText.setSize(16)
lText.setStyle("bold")
lText.draw(win)

jOval = Oval(Point(430, 470), Point(530, 510))
jOval.draw(win)
mText = Text(Point(480, 490), "Spock")
mText.setFace("arial")
mText.setSize(16)
mText.setStyle("bold")
mText.draw(win)

# Create and customize the user and computer points labels
nText = Text(Point(150, 560), "User Point: 0")
nText.setFace("arial")
nText.setSize(18)
nText.setStyle("bold")
nText.setTextColor("white")
nText.draw(win)

oText = Text(Point(480, 560), "Computer Point: 0")
oText.setFace("arial")
oText.setSize(18)
oText.setStyle("bold")
oText.setTextColor("white")
oText.draw(win)

# Create and customize the exit button
exit_button = Rectangle(Point(560, 620), Point(630, 655))
exit_button.setFill("green")
exit_button.draw(win)
exit_text = Text(Point(595, 637), "Exit")
exit_text.setFace("arial")
exit_text.setSize(18)
exit_text.setStyle("bold")
exit_text.setTextColor("white")
exit_text.draw(win)

# Choices List
choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
user_win = {
    'Rock': ['Scissors', 'Lizard'],
    'Paper': ['Rock', 'Spock'],
    'Scissors': ['Paper', 'Lizard'],
    'Lizard': ['Paper', 'Spock'],
    'Spock': ['Rock', 'Scissors']
}

# Initialize points
user_point = 0
computer_point = 0
last_selected_oval = None  # Variable to keep track of the last selected oval

# Function to update the round number
def update_round(round_num):
    aText.setText(f"Round No: {round_num}")

# Function to update user point
def update_user_point(point):
    nText.setText(f"User Point: {point}")

# Function to update computer point
def update_computer_point(point):
    oText.setText(f"Computer Point: {point}")

# Function to display the final result
def display_final_result(user_point, computer_point):
    if user_point > computer_point:
        final_result = "User wins the game!"
    elif computer_point > user_point:
        final_result = "Computer wins the game!"
    else:
        final_result = "The game Drawn!"
    
    result_text = Text(Point(320, 640), final_result)
    result_text.setFace("arial")
    result_text.setSize(25)
    result_text.setStyle("bold")
    result_text.setTextColor("firebrick")
    result_text.draw(win)

# Loop to simulate the game rounds
timeout = 3  # Timeout period in seconds
for i in range(1, 8):
    update_round(i)
    
    # Wait for the user to click and check for exit button
    while True:
        click_point = win.checkMouse()
        if click_point:
            # Check if the click is within the exit button area
            if (550 < click_point.getX() < 620) and (600 < click_point.getY() < 635):
                # Exit button clicked, display results and exit
                display_final_result(user_point, computer_point)
                win.getMouse()  # Wait for user to see the result
                win.close()
                exit()

        user_choice = get_user_choice_with_timer(win, timeout, timer_text)
        if user_choice is None:
            # Timeout occurred
            computer_point += 1
            update_computer_point(computer_point)
            timeout_text = Text(Point(320, 600), "Time is up. Computer gets one point.")
            timeout_text.setFace("arial")
            timeout_text.setSize(16)
            timeout_text.setStyle("bold")
            timeout_text.setTextColor("yellow")
            timeout_text.draw(win)
            time.sleep(3)  # Wait for 3 seconds before going to the next round
            timeout_text.undraw()
            break  # Exit the loop to go to the next round
        
        reset_computer_choice_colors()
        
        # Randomly select computer's choice
        computer_choice = random.choice(choices)
        highlight_computer_choice(computer_choice)

        # Determine winner
        if user_choice == computer_choice:
            pass  # Tie
        elif computer_choice in user_win.get(user_choice, []):
            user_point += 1
            update_user_point(user_point)
        else:
            computer_point += 1
            update_computer_point(computer_point)

        time.sleep(1) # Wait for 3 seconds before going to the next round    
        if last_selected_oval:
            last_selected_oval.setFill("")  # Reset the last selected oval's color at the start of the break
        reset_computer_choice_colors() # Reset the computer choice colors

        time.sleep(2) # Wait for 2 seconds before going to the next round    
        break  # Exit the loop to go to the next round

# Display the final result if game ends normally
display_final_result(user_point, computer_point)
win.getMouse()  # Wait for user to see the result
