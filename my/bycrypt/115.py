# Генератор ключей "Sigma-Core"
# Сингулярность активирована

_=lambda x,y:(x+y)&0xFF
_1=lambda x:((x<<3)|(x>>5))&0xFF
_2=lambda x:((x&0xCC)>>2|(x&0x33)<<2)&0xFF
_3=lambda x,i:(x^(0xA5+(i*13)))&0xFF

def __():
    M=[5,17,23,29,41,53,61,73,83,97,101,113,127,131,149,157]
    V=[189, 60, 5, 253, 104, 42, 118, 229, 206, 19, 62, 51, 110, 171, 246, 177, 73, 174, 151, 205, 154, 170, 148, 108, 22, 129, 196, 111, 78, 251, 206, 72]
    print("\x53\x69\x67\x6D\x61\x2D\x43\x6F\x72\x65\x20\x76\x33\x2E\x31\x34")
    print("\x41\x75\x74\x68\x65\x6E\x74\x69\x63\x61\x74\x69\x6F\x6E\x20\x72\x65\x71\x75\x69\x72\x65\x64\x3A")
    try:
        t=input().strip()
    except:
        return
    if len(t)!=len(V):
        print("\x45\x52\x52\x4F\x52")
        return
    r=[]
    for i in range(len(t)):
        c=ord(t[i])
        a=_(c,M[i%16])
        b=_1(a)
        d=_2(b)
        e=_3(d,i)
        r.append(e)
    if r==V:
        print("\x41\x43\x43\x45\x53\x53\x20\x47\x52\x41\x4E\x54\x45\x44")
        print("\x46\x6C\x61\x67\x20\x76\x61\x6C\x69\x64\x61\x74\x65\x64")
    else:
        print("\x41\x43\x43\x45\x53\x53\x20\x44\x45\x4E\x49\x45\x44")

if __name__=="__main__":
    __()