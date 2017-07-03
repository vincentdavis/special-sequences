def de_bruijn(k, n):
    """
    De Bruijn sequence for alphabet size k (0,1,2...k-1)
    and subsequences of length n.
    From wikipedia Sep 22 2013:
        Modified last line to return a string rather than a list
    """
    a = [0] * k * n
    sequence = []

    def db(t, p, ):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(int(a[t - p]) + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    # return sequence  #original
    return ''.join([str(i) for i in sequence])


################

def de_bruijn_strings(k, n):
    """
    De Bruijn sequence for alphabet size k (0,1,2...k-1)
    and subsequences of length n.
    Modifed wikipedia Sep 22 2013 to use strips
    """
    global sequence
    global a
    a = '0' * k * n
    sequence = ''

    def db(t, p):
        global sequence
        global a
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence = sequence + a[j]
        else:
            a = a[:t] + a[t - p] + a[t + 1:]
            db(t + 1, p)
            for j in range(int(a[t - p]) + 1, k):
                a = a[:t] + str(j) + a[t + 1:]
                db(t + 1, t)
        return sequence

    db(1, 1)
    return sequence


################
_mapping = bytearray(b"?") * 256
_mapping[:10] = b"0123456789"


def de_bruijn_bytes(k, n):
    """
    By Peter Otten on python-list
    """
    a = k * n * bytearray([0])
    sequence = bytearray()
    extend = sequence.extend

    def db(t, p):
        if t > n:
            if n % p == 0:
                extend(a[1: p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return sequence.translate(_mapping).decode("ascii")
