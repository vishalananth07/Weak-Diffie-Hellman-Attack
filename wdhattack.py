import math
from collections import defaultdict
from argparse import ArgumentParser
from gmpy2 import powmod
from gmpy2 import divm

def mitm(h,g,p,R):
	mapping = defaultdict(lambda: -1)
	for i in range (0,R):
		x0 = powmod(g,i*R,p)
		mapping[x0] = i;

	for i in range (0,R):
		x1 = divm(h,powmod(g,i,p),p)
		if mapping[x1] != -1:
			return i+mapping[x1]*R
	return -1

def main():
	parser = ArgumentParser()
	parser.add_argument("-A", "--alice",required=True)
	parser.add_argument("-B", "--bob",required=True)
	parser.add_argument("-g", "--base",required=True)
	parser.add_argument("-p", "--prime",required=True)
	parser.add_argument("-r", "--range",required=True)
	args = parser.parse_args()

	A = int(args.alice)
	B = int(args.bob)
	g = int(args.base)
	p = int(args.prime)
	R = int(2**(int(args.range)/2))

	print("Calculating Alice's private key..")
	a = mitm(A,g,p,R)
	if a != -1:
		print("Alice's private key:",a)
	else:
		print("Could not find the Alice's private key :(")

	print("Calculating Bob's private key..")
	b = mitm(B,g,p,R)
	if b != -1:
		print("Bob's private key:",b)
	else:
		print("Could not find the Bob's private key :(")

	if a != -1 and b != -1:
		K = powmod(g,a*b,p)
		print("Shared secret key :",K)
	else:
		print("Could not find the shared key :(")

if __name__ == "__main__":
	main()
