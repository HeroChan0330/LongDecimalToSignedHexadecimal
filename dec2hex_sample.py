
import dec2hex

if __name__ == "__main__":
    a = dec2hex.convert("123456789012345678901234567890123456789",128)
    print(a)
    b = dec2hex.convert("-123456789012345678901234567890123456789",128)
    print(b)