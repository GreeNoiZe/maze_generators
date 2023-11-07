from maze_backtracker import Maze
from time import perf_counter

start = perf_counter() # on initialise le compteur pour calculer le temps d'éxécution du programme

maze = Maze(5,5)
maze.backtrack(0,0)

end = perf_counter() # on arrête le chronomètre
execution_time = (end - start) # on calcule le temps d'éxécution

print(maze)

# On inclut le temps d'éxécution à l'affichage dans le terminal et dans le fichier
print(f'Le labyrinthe a été généré en {execution_time} secondes')
with open("maze.txt", "a") as f:
    f.write('\n')
    f.write(f'Le labyrinthe a été généré en {execution_time} secondes')
    f.close()
