import random
def generate_data():
    x = 90
    massive = [0] * 101
    massive[x] = 1
    print('На элементе -', x)
    return massive

if __name__ == '__main__':
    massive = generate_data()
    count_iter_1 = 0
    count_iter_2 = 0

    for i, ii in enumerate(massive):
        if ii:
            break
        else:
            count_iter_1 += 1

    while True:
        if massive[random.randint(0, 100)]:
            break
        else:
            count_iter_2 += 1

    print(f'count_iter_1 = {count_iter_1}')
    print(f'count_iter_2 = {count_iter_2}')
