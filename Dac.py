import math

def closest_pair_Dac(points):
    # Ordenar los puntos por su coordenada x
    points.sort()
    
    # Función auxiliar que encuentra la distancia más corta entre dos puntos en una lista ordenada por coordenadas y
    def closest_pair_rec(left, right):
        n = right - left + 1
        if n <= 3:
            return brute_force(points[left:right+1])
        
        mid = (left + right) // 2
        min_left = closest_pair_rec(left, mid)
        min_right = closest_pair_rec(mid+1, right)
        delta = min(min_left, min_right)
        
        # Encontrar los puntos que están a una distancia delta de la línea vertical que divide la lista
        strip = []
        for i in range(left, right+1):
            if abs(points[i][0] - points[mid][0]) < delta:
                strip.append(points[i])
        
        # Encontrar la distancia más corta entre los puntos en la franja
        strip_min = strip_closest(strip, delta)
        return min(delta, strip_min)
    
    # Función auxiliar que encuentra la distancia más corta entre dos puntos usando fuerza bruta
    def brute_force(points):
        n = len(points)
        min_dist = math.inf
        for i in range(n):
            for j in range(i+1, n):
                dist = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
                min_dist = min(min_dist, dist)
        return min_dist
    
    # Función auxiliar que encuentra la distancia más corta entre dos puntos en una franja
    def strip_closest(strip, delta):
        n = len(strip)
        min_dist = delta
        strip.sort(key=lambda point: point[1])
        for i in range(n):
            for j in range(i+1, min(i+7, n)):
                dist = math.sqrt((strip[i][0]-strip[j][0])**2 + (strip[i][1]-strip[j][1])**2)
                min_dist = min(min_dist, dist)
        return min_dist
    
    # Llamar a la función recursiva
    return closest_pair_rec(0, len(points)-1)


points = [(0,0), (1,1), (2,2), (3,5), (2,4), (1,5)]
min_dist = closest_pair_Dac(points)
print("La distancia más corta entre dos puntos es:", min_dist)
