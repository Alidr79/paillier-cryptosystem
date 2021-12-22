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
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/HE_graph.png" alt="HE_use_cases" width="450" height="400">
<h4>
Assume that you want to do some data analytics or some machine learning or other computations on the data.
If you are doing this locally on your system every thing is safe.
<br>
    
But if you want to do this by using cloud computation and cloud services(like Google colab,kaggle kernels,etc) you should <u>upload your data to the cloud server</u>, now you are out of the safe zone... 
<br>
    
To preserve the data privacy, you upload the data in encrypted version(*no one can decrypt the data except you!).
With Homomorphic Encryption the cloud server could compute on the encrypted data without any need for decrypting it...
</h4>

<h2>The dark side of non homomorphic cryptography</h1>
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/CBS_news.png" alt="HE_use_cases" width="450" height="400">
"The weather channel app used its app to track the whereabouts of its users and sold it to third_party websites for targeted ads,
Los Angeles prosecutors said Friday as they sued to stop the practice."

```python
import random
p = 421
q = 439
n = p*q
pill = paillier(p , q)
message1 = 114
message2 = 516
result_plain = message1+message2
cipher1 = pill.encrypt(message1)
cipher2 = pill.encrypt(message2)
cipher_result = pill.add_cipher(cipher1 , cipher2)

print('Message1 = {} ---> Encrypted = {}'.format(message1 , cipher1))
print('Message2 = {} ---> Encrypted = {}'.format(message2 , cipher2))
print("-"*30)
print('{} + {} = {}'.format(message1 , message2 , result_plain))
print('{} % {} = {}'.format(result_plain , n , result_plain%n))
print('{} + {} = {}'.format(cipher1 , cipher2 , cipher_result))
print('Decryption( {} ) = {}'.format(cipher_result , pill.decrypt(cipher_result)))
```
Message1 = 114 ---> Encrypted = 25976634402
Message2 = 516 ---> Encrypted = 10118679904
------------------------------
114 + 516 = 630
630 % 184819 = 630
25976634402 + 10118679904 = 24797061883
Decryption( 24797061883 ) = 630
