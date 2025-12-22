import base64

flag = "ctfinf{b32_and_b85_flag_crypted}"

b32 = base64.b32encode(flag.encode()).decode()
b85 = base64.b85encode(b32.encode()).decode()
print(f"enc flag: {b85}") #O-?dLO)^YRO<FZqMNL{$Of^wgG+IM9O-VFFOIR~UPEt`<PgpZVPf9dcK{Z51O;R>dJv}`=
