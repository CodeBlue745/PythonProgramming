''' For an input velocity, output the time and rocket height if rocket height is greater than 0.'''
rocketVelocity = int(input())

time = 0
rocketHeight = 0

while rocketHeight >= 0:
    rocketHeight = rocketVelocity * time - (5 * time ** 2)
    if rocketHeight >= 0:
        print(f'{time} {rocketHeight}')
    time += 1




