from rich.console import Console
from rich.progress import track
import time

console = Console()

# print([1,2,3])
# console.print([1,2,3])

# console.print("[blue underline]Ser ut som en länk")

# console.print("[bold]Fetstil[/bold] [italic]kursiv[/italic]")

# console.print("Vit text på röd bakgrund", style="white on red")

# console.log("När vi använder log får vi en tidpunkt")
# console.rule("[bold red] Rubriken till ny avdelning")

# creating a progressbar that takes 10 seconds
for n in track(range(10), description="Processing.."):
    time.sleep(1)