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
<img src="https://raw.githubusercontent.com/Alidr79/paillier-cryptosystem/main/CBS_news.png" alt="HE_use_cases" width="500" height="400">
"The weather channel app used its app to track the whereabouts of its users and sold it to third_party websites for targeted ads,
Los Angeles prosecutors said Friday as they sued to stop the practice."

# The Origins of Homomorphic Cryptosystems
<img src="https://www.thesslstore.com/blog/wp-content/uploads/2019/06/History-of-Homomorphic-Encryption-300x267.png" alt="HE_use_cases" width="300" height="300">
