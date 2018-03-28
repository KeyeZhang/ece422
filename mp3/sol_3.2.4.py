import pbp
from math import floor
from fractions import gcd
from Crypto.PublicKey import RSA

# Sources:
# product_tree(): https://facthacks.cr.yp.to/product.html
# remainder_tree(0): https://facthacks.cr.yp.to/remainder.html
# find_gcds(): https://facthacks.cr.yp.to/batchgcd.html
# egcd() and modinv(): https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

def product_tree(X):
    result = [X]
    while len(result[-1]) > 1:
        X = result[-1]
        Y = []
        L = len(X)

        Y = [X[i*2]*X[i*2+1] for i in range(L/2)]
        if L % 2 == 1:
            Y.append(X[L-1])

        result.append(Y)
    return (result[-1][0], result)

def square(X):
    Y = []
    for i in range(len(X)):
        Y.append([X[i][j]**2 for j in range(len(X[i]))])
    return Y

def remainder_tree(P, product_tree):
	result = [P]
	for node in reversed(product_tree):
		# print(result, node)
		result = [result[i//2] % node[i] for i in range(len(node))]
		# print(result, node)
	return result

def find_gcds(R, X):
	V = [gcd(r/n, n) for r, n in zip(R, X)]
	result = []
	for i in range(len(V)):
		if V[i] != 1:
			result.append((V[i], X[i]))
	return result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def find_private_keys(potential_moduli):
	e = long(65537)
	private_keys = []
	for i in range(len(potential_moduli)):
		p = potential_moduli[i][0]
		N = potential_moduli[i][1]
		q = N//p
		d = modinv(e, (p - 1)*(q - 1))
		private_keys.append(RSA.construct((long(N), long(e), long(d))))
	return private_keys

def print_results(private_keys, cipher_content, out):
	for key in private_keys:
		try:
			plaintext = pbp.decrypt(key, cipher_content)
			print(plaintext)
			out.write(plaintext)
		except ValueError:
			a = 1

with open("moduli.hex") as moduli, open("3.2.4_ciphertext.enc.asc") as cipher, open("sol_3.2.4.txt", 'w') as out:
	moduli_list = [i.strip() for i in moduli.readlines()]
	cipher_content = cipher.read().replace("\r\n", "\n")

	# Convert to integer values
	for i in range(0, len(moduli_list)):
		moduli_list[i] = int(moduli_list[i], 16)

	# moduli_list = [1909,2923,291,205,989,62,451,1943,1079,2419]

	print("Calculating Product Tree...")
	(P, product_tree) = product_tree(moduli_list)

	print("Calculating Squares...")
	product_tree = square(product_tree)

	print("Calculating Remainder Tree...")
	remainder_tree = remainder_tree(P, product_tree)

	print("Calculating GCD...")
	potential_moduli = find_gcds(remainder_tree, moduli_list) # Tuple form (gcd, moduli)

	# with open("gcdkey.txt") as gcdkey:
	# 	potential_moduli = [tuple(map(int, i.split(", "))) for i in gcdkey]

	print("Calculating Private Keys...")
	private_keys = find_private_keys(potential_moduli)

	print("Printing Results...")
	print_results(private_keys, cipher_content, out)
