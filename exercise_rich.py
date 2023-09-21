from rich.console import Console

console = Console()

# # Colored text
# console.print("Warning:", style="color(11)")
# console.print("Error:", style="color(9)")
# console.print("Success!", style="color(10)")

for c in range(256):
    console.print("Hello", style="color("+str(c)+")", end=",")
    