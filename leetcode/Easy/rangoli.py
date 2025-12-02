import string
n = 3
L = []

def rangoli():
	alpha = string.ascii_lowercase
	for i in range(0, n):
		s = "-".join(alpha[i:n])
		L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
	print("\n".join(L[:0:-1]+L))
rangoli()