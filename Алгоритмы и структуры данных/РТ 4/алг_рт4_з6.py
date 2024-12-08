def hanoi(n, source, target, temp):
    if n == 1:
        print(f"Переместить диск {n} с {source} на {target}")
        return
    
    hanoi(n-1, source, temp, target)
    print(f"Переместить диск {n} c {source} на {target}")
    hanoi(n-1, temp, target, source)

n = 3
hanoi(n, "A", "B", "C")