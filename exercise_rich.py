from rich.console import Console
from rich.prompt import IntPrompt, Confirm
import numpy

console = Console()

# # Colored text
# console.print("Warning:", style="color(11)")
# console.print("Error:", style="color(9)")
# console.print("Success!", style="color(10)")

# for c in range(256):
#     console.print("Hello", style="color("+str(c)+")", end=",")
    

# # Formatted text
# console.print("bold", style="bold")
# console.print("This text is [italic]Italic[/italic]")
# console.print("And this is [underline]Underlined[/underline] but not italic or bold")

# console.print("[link=https://www.google.com/]Google link[/link]")


def guessing_game():
    game_on = True
    number = numpy.random.randint(100)

    while game_on:
        
        console.print("Lets play the guessing game", style="white on red")
        answer= IntPrompt.ask("guess a number between 1-100: ")
        if answer > number:
            print("Your number is too high")
        elif answer < number:
            print("Your number is too low.")
        else:
            console.print("Success!", style="color(10)")
            if Confirm.ask("Do you want to play again"):
                game_on = False
                guessing_game()
            else:
                break


# guessing_game()


# Something old, something new...


def divide(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except:
        console.print("Error: ", style="color(9)", end="")
        console.print("You've encountered a ", end="")
        console.print("[link=https://www.pylenin.com/blogs/zero-division-error/#:%7E:text=Handling%20ZeroDivisionError%20in%20Python]ZeroDivisionError[/link]", style="color(12)")


divide(2,0)