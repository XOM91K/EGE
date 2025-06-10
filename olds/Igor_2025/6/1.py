for t in range(1, 1000):
    if ((t - 1) * ((3 * t) - 1) * 2) + ((t + 1) * (t - 1)) > 200_000:
        print(t)
        break