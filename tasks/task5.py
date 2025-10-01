# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    numbers = map(int, input().split())
    result = [x * x for x in numbers]
    print(' '.join(map(str, result)))

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()