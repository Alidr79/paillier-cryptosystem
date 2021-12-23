# Paillier cryptosystem
A toy implementation of the Paillier cryptosystem in python

## Resources:
1. https://asecuritysite.com/encryption/pal_ex  [paillier cryptosystem Theory & code]
2. https://en.wikipedia.org/wiki/Paillier_cryptosystem [Theory and rules]
3. https://asecuritysite.com/encryption/multgr   [The [Z*] space]
4. https://www.thesslstore.com/blog/what-is-homomorphic-encryption/ [HE Intro]
5. https://www.youtube.com/watch?v=73_PvL_F0hI [Microsoft private AI]
6. https://www.youtube.com/watch?v=Bo00HRuonSk&t=748s [Microsoft private AI]

## Homomorphic Encryption introduction :
1. A new type of encryption
2. Compute on encrypted data without decryption
3. No one sees the result without the private key
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/HE_graph.png" alt="HE_use_cases" width="450" height="300">
Assume that you want to do some data analytics or some machine learning or other computations on the data.
If you are doing this locally on your system every thing is safe.
<br>
    
But if you want to do this by using cloud computation and cloud services(like Google colab,kaggle kernels,etc) you should <u>upload your data to the cloud server</u>, now you are out of the safe zone... 
<br>
    
To preserve the data privacy, you upload the data in encrypted version(*no one can decrypt the data except you!).
With Homomorphic Encryption the cloud server could compute on the encrypted data without any need for decrypting it...

<h2>The dark side of non homomorphic cryptography</h1>
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/CBS_news.png" alt="HE_use_cases" width="500" height="400">
"The weather channel app used its app to track the whereabouts of its users and sold it to third_party websites for targeted ads,
Los Angeles prosecutors said Friday as they sued to stop the practice."

# The Origins of Homomorphic Cryptosystems
<img src="https://www.thesslstore.com/blog/wp-content/uploads/2019/06/History-of-Homomorphic-Encryption-300x267.png" alt="HE_use_cases" width="250" height="250">
The origins of homomorphic encryption dates back to 1978 — shortly after Rivest, Shamir and Adleman presented RSA encryption — which is a long time in the world of technology. Rivest, Adleman, and Dertouzos came up with the concept of privacy homomorphisms. Their concept of encryption was shot down by Brickell and Yacobi nearly 10 years later. Other researchers have “had a go” at the topic — such as Feigenbaum and Merritt — but, really, no major progress was made until Craig Gentry, a graduate student at Stanford University, decided to try his hand at creating an algebraically homomorphic encryption system as his graduate thesis.

# Types of Homomorphic Encryption
<img src="https://www.thesslstore.com/blog/wp-content/uploads/2019/06/Homomorphic-encryption-300x246.png" alt="HE_use_cases" width="250" height="250">
There are <u>three main types</u> of homomorphic encryption.
<br>
The primary difference between them boils down to the types and frequency of mathematical operations that can be performed on their ciphertext.
1. Partially Homomorphic Encryption<br>
2. Somewhat Homomorphic Encryption<br>
3. Fully Homomorphic Encryption <br>-------------------------------------------------------------------<br>

- 1. PHE

Partially homomorphic encryption (PHE) helps sensitive data remain confidential by only allowing select mathematical functions to be performed on encrypted values. This means that one operation can be performed an unlimited number of times on the ciphertext. 
Paillier encryption (an addition scheme).
<br>
- 2. SHE

somewhat homomorphic encryption (SHE) scheme is one that supports limited operations (for example, either addition or multiplication) up to a certain complexity, but these operations can only be performed a set number of times.
<br>
- 3. FHE

Born from a somewhat homomorphic encryption scheme, this holy grail of cryptography is capable of using any efficiently computable functions (such as addition and multiplication, not just one or the other) any number of times and makes secure multi-party computation more efficient. Unlike other forms of homomorphic encryption, it can handle arbitrary computations on your ciphertexts.

## So Why Aren’t We Using Fully Homomorphic Encryption? Well, It’s Still Pretty Slow…
<img src="https://www.thesslstore.com/blog/wp-content/uploads/2019/06/Slow-encryption-300x300.png" alt="HE_use_cases" width="300" height="300">
Unfortunately, in its current state, homomorphic encryption is impractically slow. In the encryption race, it’s running in last place. This is, in part, because homomorphic encryption has a larger computational overhead than plaintext operations.<br>
IBM released its first version of its HElib C++ library in 2016 — but it reportedly “ran ‘100 trillion times’ slower than plaintext operations.” Since that time, IBM has continued working to combat this issue and have now come up with a version that is 75 times faster… but even that is still incredibly slow in comparison to working with unencrypted data.<br>
Microsoft’s Cryptography Research group came up with Microsoft Simple Encrypted Arithmetic Library (Microsoft SEAL), an open-source homomorphic encryption library. This technology platform, written in C++.

# Paillier Encryption
One of the partially homomorphic encryption schemes.<br>
This scheme just supports the addition of ciphertexts.<br>
D(c1+c2) = p1 + p2<br>
c1 and c2 are corresponding ciphertexts of p1 and p2

## Application of Paillier
Consider a simple binary ("for" or "against") vote. Let m voters cast a vote of either 1 (for) or 0 (against). Each voter encrypts their choice before casting their vote. The election official takes the product of the m encrypted votes and then decrypts the result and obtains the value n, which is the sum of all the votes. The election official then knows that n people voted for and m-n people voted against.The role of the random r (check it in the 'Theory', encryption section) ensures that two equivalent votes will encrypt to the same value only with negligible likelihood, hence ensuring voter privacy.

# Theory
<img src="https://asecuritysite.com/public/pal.png" alt="HE theory" width="800" height="800">


⚠️⚠️⚠️ **Note: 
In paillier scheme, p and q must be two large prime numbers.
It will not work properly with small prime numbers.**

# Example of using the Paillier module in python
```python
from Paillier import Paillier

p = 179
q = 1109
pill = Paillier(p , q , fast = False)
message1 = 13
message2 = 123
result_plain = message1+message2
cipher1 = pill.encrypt(message1)
cipher2 = pill.encrypt(message2)
cipher_result = pill.add_cipher(cipher1 , cipher2)

print('Message1 = {} ---> Encrypted = {}'.format(message1 , cipher1))
print('Message2 = {} ---> Encrypted = {}'.format(message2 , cipher2))
print('{} + {} = {}'.format(message1 , message2 , result_plain))
print('{} + {} = {}'.format(cipher1 , cipher2 , cipher_result))
print('Decryption( {} ) = {}'.format(cipher_result , pill.decrypt(cipher_result)))
```

```
Message1 = 13 ---> Encrypted = 20582710652
Message2 = 123 ---> Encrypted = 4688047556
13 + 123 = 136
20582710652 + 4688047556 = 37766671787
Decryption( 37766671787 ) = 136
```
