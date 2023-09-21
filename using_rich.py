from rich.console import Console


console = Console()

# print([1,2,3])
# console.print([1,2,3])

# console.print("[blue underline]Ser ut som en länk")

# console.print("[bold]Fetstil[/bold] [italic]kursiv[/italic]")

# console.print("Vit text på röd bakgrund", style="white on red")

# console.log("När vi använder log får vi en tidpunkt")
# console.rule("[bold red] Rubriken till ny avdelning")

from rich.progress import track
import time

# creating a progressbar that takes 10 seconds
# for n in track(range(10), description="Processing.."):
#     time.sleep(1)

from rich.tree import Tree

group1 = Tree("[red]Grupp1")
group1.add("Araz")
group1.add("Kalle")
group1.add("Kavat")
group1.add("Yaya")

group2 = Tree("[green]Grupp2")
group2.add("Tom")
group2.add("Tawan")
group2.add("KChorf")
group2.add("bang")

groups = Tree("[blue]Grupper")
groups.add(group2)
groups.add(group1)

console.print(groups)