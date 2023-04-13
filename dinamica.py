import math

def closest_pair_din(puntos):
    n = len(puntos)
    
    # Crear una tabla para almacenar las distancias entre los puntos
    distances = [[math.inf for _ in range(n)] for _ in range(n)]
    
    # Calcular las distancias iniciales y almacenarlas en la tabla
    for i in range(n):
        for j in range(i+1, n):
            dist = math.sqrt((puntos[i][0]-puntos[j][0])**2 + (puntos[i][1]-puntos[j][1])**2)
            distances[i][j] = dist
            distances[j][i] = dist
    
    # Para cada punto adicional, actualizar las distancias y encontrar la distancia más corta
    for i in range(2, n):
        for j in range(1, i):
            for k in range(j):
                dist1 = distances[j][k]
                dist2 = distances[i][j]
                dist3 = distances[i][k]
                min_dist = min(dist1, dist2, dist3)
                if min_dist < distances[j][i]:
                    distances[j][i] = min_dist
                    distances[i][j] = min_dist
    
    # Encontrar la distancia más corta entre todos los pares de puntos
    min_dist = math.inf
    for i in range(n):
        for j in range(i+1, n):
            if distances[i][j] < min_dist:
                min_dist = distances[i][j]
    
    return min_dist


puntos = [(3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9)]
min_dist = closest_pair_din(puntos)
print("La distancia más corta entre dos puntos es:", min_dist)