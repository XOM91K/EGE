for n in range(1, 1000):
    s = "3" + n * "9" + n * "5"
    while "39" in s or "35" in s or "555" in s:
        if "39" in s:
            s = s.replace("39", "55", 1)
        if "35" in s:
            s = s.replace("35", "9", 1)
        if "555" in s:
            s = s.replace("555", "3", 1)
    if (s.count('3') * 3 + s.count('5') * 5 + s.count('9') * 9) % len(s) == n:
        print(n)