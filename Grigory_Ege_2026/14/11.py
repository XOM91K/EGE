for x in range(68):
    a1 = 1 * 68**4 + 2 * 68**3 + 3 * 68**2 +x * 68**1 + 5 * 68**0
    a2 = 1 * 68**4 + x * 68**3 + 2 * 68**2 + 3 * 68**1 + 3 * 68**0
    if (a1+a2)%12 == 0:
        print((a1+a2)//12)