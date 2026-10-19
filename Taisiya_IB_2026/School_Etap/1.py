# import itertools
# ct = 0
# for x in itertools.product('XYZ', repeat=9):
#     x = ''.join(x)
#     if x.count('X') == 3 and x.count('Y') >= 1 and x.count('Z') <= 2:
#         ct += 1
#         print(x)
# print(ct)
# import string
# alf = string.ascii_lowercase
# flag = 'zwswl{v0x4_f85_r3yv4p_tv0x0g0p_3}'
# for x in flag:
#     if x in alf:
#         print(alf[alf.index(x) - 4], end='')
#     else:
#         print(x,end='')

def main():
    MASK = 0x5A
    ENC = [
        182, 178, 184, 182, 130, 91, 132, 140, 91, 138, 162, 174, 166, 38, 128, 85,
        164, 93, 212, 242, 188, 83, 89, 115
    ]
    def rol1(x):
        return ((x >> 1) | (x << 7)) & 0xFF

    encrypted_input = []
    for i, char in enumerate(ENC):
        final = char ^ MASK
        y = rol1(final)
        x = (y - i) & 0xFF

        encrypted_input.append(x)

    print(bytes(encrypted_input))
if __name__ == "__main__":
    main()