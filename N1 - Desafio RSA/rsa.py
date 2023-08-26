
class RSA:
    def encrypt(public_key, plaintext):
        e, n = public_key
        encrypted = [pow(ord(char), e, n) for char in plaintext]
        return encrypted

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def multiplicative_inverse(e, phi):
        d = 0
        x1, x2 = 0, 1
        y1, y2 = 1, 0
        while phi != 0:
            q = e // phi
            temp_phi = phi
            phi = e % phi
            e = temp_phi
            temp_x = x1 - q * x2
            x1 = x2
            x2 = temp_x
            temp_y = y1 - q * y2
            y1 = y2
            y2 = temp_y
        d = x1
        return d

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_prime(bits):
        while True:
            num = random.getrandbits(bits)
            if is_prime(num):
                return num

    def generate_keypair(bit_size):
        p = generate_prime(bit_size)
        q = generate_prime(bit_size)
        n = p * q
        phi = (p - 1) * (q - 1)
        
        while True:
            e = random.randrange(2, phi)
            if gcd(e, phi) == 1:
                break
        
        d = multiplicative_inverse(e, phi)
        
        return ((e, n), (d, n))

    def decrypt(private_key, ciphertext):
        d, n = private_key
        decrypted = [chr(pow(char, d, n)) for char in ciphertext]
        return ''.join(decrypted)