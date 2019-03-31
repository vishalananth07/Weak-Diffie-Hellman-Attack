# Weak Diffie-Hellman Attack
A python script which finds the shared key given two Diffie-Hellman public keys, the base g, the prime modulo p and a range using the meet-in-the-middle technique 

## Running the Script
Run the script with
```
python3 wdhattack.py -A <alice_public_key> -B <bob_public_key> -g <base> -p <prime> -r <range>
```
* -A : Alice's public key generated as A = g^a % p 
* -B : Bob's public key generated as B = g^b % p
* -g : Common base
* -p : Prime modulo
* -r : Nearest power of 2 range within which a,b lies. 0 <= a,b < 2^r

### Sample
```
python3 wdhattack.py -A 419 -B 34 -g 10 -p 1357 -r 10

Calculating Alice's private key..
Alice's private key: 521
Calculating Bob's private key..
Bob's private key: 619
Shared secret key : 33
```