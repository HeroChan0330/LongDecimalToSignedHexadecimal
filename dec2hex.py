
# ref:https://blog.csdn.net/weixin_34202952/article/details/91608463

from logging import exception


__digit2hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
__dec_str = ''
__hex_str_bits = []
__hex_str = ''
__BW = 128

def convert_iter(s):
    global __hex_str_bits
    s1 = ''
    num = int(s[0])

    for i in range(1,len(s)):
        num = num*10  + int(s[i])
        if num>=16:
            s1 +=  str(num//16)
            num = num % 16
        else:
            s1 += '0'

    if int(s1)<16:
        # print(str(int(s1)))
        # __hex_str = __hex_str + __digit2hex[int(s1)]
        __hex_str_bits.append(int(s1))
        pass
    else:
        convert_iter(s1)
    # print(num)
    # __hex_str = __hex_str + __digit2hex[num]
    __hex_str_bits.append(num)

def convert(s,bw=128):
    global __hex_str,__dec_str,__hex_str_bits,__BW
    __BW = bw
    __dec_str = s
    __hex_str_bits = []
    __hex_str = ''
    if __dec_str[0] == '-':
        convert_iter(__dec_str[1:])
    else:
        convert_iter(__dec_str)

    if len(__hex_str_bits) > __BW//4:
        raise("overflow")
    elif len(__hex_str_bits) < __BW//4:
        if __dec_str[0] == '-':
            temp = [8]
            temp.extend([0]*(__BW//4-1-len(__hex_str_bits)))
            temp.extend(__hex_str_bits)
            __hex_str_bits = temp
        else:
            temp = [0]*(__BW//4-len(__hex_str_bits))
            temp.extend(__hex_str_bits)
            __hex_str_bits = temp
    else:
        if __dec_str[0] == '-':
            if __hex_str_bits[0] < 8:
                __hex_str_bits[0] += 8
            else:
                raise("overflow")
        else:
            if __hex_str_bits[0] >= 8:
                raise("overflow")

    if __dec_str[0] == '-':
        __hex_str_bits[0] = 23 - __hex_str_bits[0]
        for i in range(1,__BW//4):
            __hex_str_bits[i] = 15 - __hex_str_bits[i]

        __hex_str_bits[__BW//4-1] += 1
        for i in range(__BW//4-1,0,-1):
            if __hex_str_bits[i] >=16:
                __hex_str_bits[i] = __hex_str_bits[i] % 16
                __hex_str_bits[i-1] += 1
    for i in range(0,__BW//4):
        __hex_str += __digit2hex[__hex_str_bits[i]]
    # print(__hex_str)
    return __hex_str

