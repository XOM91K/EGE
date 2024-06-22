X = False
Y = True
Z = False
print('а)', X and (not(Z or Y)) or (not Z))
print('б)', (not X) or X and (Y or Z))
print('в)', (X or Y and (not Z)) and Z)
