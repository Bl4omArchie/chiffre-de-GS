#coding:utf-8
from Crypto.Util.number import bytes_to_long, long_to_bytes

class GS_NUMBER():
    def __init__(self, message):
        self.message = str(bytes_to_long(message))
        self.l = 0

    def compute(self, block1, block2):
        return str(block1+block2) + str(block1-block2)

    def b_block_enc(self, block): 
        block_permut = [] 
        block_cipher = []
        self.l = len(block)

        if self.l % 2 == 1:
            block.append("0")
            self.l = len(block)
        
        print (block)

        i = 0
        for y in range(self.l//2):
            if int(block[i]) < int(block[i+1]):
                block_permut.append(block[i+1])
                block_permut.append(block[i])
                block_cipher.append(self.compute(int(block[i+1]), int(block[i])))
                self.key += "1"
            else:
                block_permut.append(block[i])
                block_permut.append(block[i+1])
                block_cipher.append(self.compute(int(block[i]), int(block[i+1])))
                self.key += "0"
            i += 2

        self.l = len(block_cipher)
        return block_cipher


    def enc_GSnumber(self):
        block = list(self.message)
        self.key = ""

        while True:
            if self.l == 1:
                return "".join(block).encode("utf-8"), self.key

            block = self.b_block_enc(block)


if __name__ == "__main__":
    test = GS_NUMBER(b"cipher")
    print (test.enc_GSnumber())
