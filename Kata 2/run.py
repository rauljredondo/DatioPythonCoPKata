def digital_root(n):
    return n if n < 10 else digital_root(n % 10 + n//10)
