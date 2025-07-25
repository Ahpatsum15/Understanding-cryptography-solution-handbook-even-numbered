def trivium_warmup_bits():
    # Initialize registers (A: 93 bits, B: 84 bits, C: 111 bits)
    A = [0] * 80 + [0] * 10 + [1, 1, 1]  # Key (80 zeros) + 10 zeros + 111
    B = [0] * 80 + [1, 1, 1, 1]          # IV (80 zeros) + 1111
    C = [0] * 108 + [1, 1, 1]             # 108 zeros + 111

    output_bits = []

    for _ in range(70):
        # Compute intermediate values
        t1 = A[65] ^ A[92] ^ (A[90] & A[91])
        t2 = B[68] ^ B[83] ^ (B[81] & B[82])
        t3 = C[65] ^ C[110] ^ (C[108] & C[109])

        # Generate output bit
        s_i = t1 ^ t2 ^ t3
        output_bits.append(str(s_i))

        # Update registers
        A_new = [t3] + A[:92]
        B_new = [t1] + B[:83]
        C_new = [t2] + C[:110]

        A, B, C = A_new, B_new, C_new

    return ''.join(output_bits)

# Compute and print the first 70 bits
bits_70 = trivium_warmup_bits()
print("First 70 bits:", bits_70)
print("Length:", len(bits_70))