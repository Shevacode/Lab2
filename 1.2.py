pyramid_height = int(input("Введіть висоту піраміди: "))
for i in range(pyramid_height):
    print(' ' * (pyramid_height - i - 1) + '*' * (2 * i + 1))