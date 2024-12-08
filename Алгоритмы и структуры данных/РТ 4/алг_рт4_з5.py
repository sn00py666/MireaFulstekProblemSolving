def deykstra(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return deykstra(n // 2) 
    else:
        return deykstra(n // 2) + deykstra((n // 2) + 1)
        
print(deykstra(14))
