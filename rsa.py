messageText = 1234  # Message ,masseage's size depend on n's size

p = 61  # prime one
q = 127  # prime two
e = 17  # public key ,need to be coprime with eulerN
d = 0  # multiplicative inverse (private key)

enMessage = 0   # encrypted message

n = p * q
eulerN = (p - 1) * (q - 1)

deResult = 0


def Encryption():
    global enMessage
    enMessage = pow(messageText, e) % n
    return enMessage


def Decryption():
    global d, deResult
    d = pow(e, -1, eulerN)
    deResult = pow(enMessage, d, n)
    return deResult


Encryption()
Decryption()

print("原訊息:\t", messageText)
print("----傳送以下資訊----")
print("加密後:\t", enMessage)
print("公鑰:\t", e, "\n私鑰:\t", d)
print("----利用以上解碼----")
print("解密後:\t", deResult)
