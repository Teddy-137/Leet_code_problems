def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n
        
    result = [0] * n
    
    for i in range(n):
        total = 0
        for j in range(1, abs(k) + 1):
            if k > 0:
                idx = (i + j) % n  # Next k numbers
            else:
                idx = (i - j + n) % n  # Previous k numbers
            total += code[idx]
        result[i] = total
        
    return result
