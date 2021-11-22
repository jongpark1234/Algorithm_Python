hr_angle = 0
for h in range(24):
    min_angle = 0
    if hr_angle >= 360 - 1 / 12:
        hr_angle = 0
    for m in range(360):
        angle = abs(min_angle - hr_angle)
        if 90.42 >= angle >= 89.58 or 270.42 >= angle >= 269.58:
            print("%0.2d:%0.2d" % (h, m / 6))
        min_angle += 1
        hr_angle += 1 / 12
