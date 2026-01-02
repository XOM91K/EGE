from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = inverse(e, phi)

message = b'vsosh{7h3_c0d3_h45_b33n_br0k3n}'
ce = bytes_to_long(message)
c = pow(ce, e, n)
print(f'Шифротекст: {c}')