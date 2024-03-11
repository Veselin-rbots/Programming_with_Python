companian = int(input())
days = int(input())

coins = days * 50

for n_day in range(1, days + 1):
    if n_day % 10 == 0:
        companian -= 2

    if n_day % 15 == 0:
        companian += 5

    coins -= companian * 2

    if n_day % 3 == 0:
        coins -= companian * 3

    if n_day % 5 == 0:
        coins += 20 * companian
        # if n_day % 3 == 0:
        #     coins += companian * 2

print(f'{companian} companions received {coins//companian} coins each.')