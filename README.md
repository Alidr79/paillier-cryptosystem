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
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/HE_graph.png" alt="HE_use_cases" width="550" height="400">
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

# So Why Aren’t We Using Fully Homomorphic Encryption? Well, It’s Still Pretty Slow…
<img src="https://www.thesslstore.com/blog/wp-content/uploads/2019/06/Slow-encryption-300x300.png" alt="HE_use_cases" width="300" height="300">
Unfortunately, in its current state, homomorphic encryption is impractically slow. In the encryption race, it’s running in last place. This is, in part, because homomorphic encryption has a larger computational overhead than plaintext operations.<br>
IBM released its first version of its HElib C++ library in 2016 — but it reportedly “ran ‘100 trillion times’ slower than plaintext operations.” Since that time, IBM has continued working to combat this issue and have now come up with a version that is 75 times faster… but even that is still incredibly slow in comparison to working with unencrypted data.

Microsoft’s Cryptography Research group came up with Microsoft Simple Encrypted Arithmetic Library (Microsoft SEAL), an open-source homomorphic encryption library. This technology platform, written in C++,
