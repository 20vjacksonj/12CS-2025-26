class Cipher:

    def __init__(self):
        self.ptm = []
        self.ctm = []

    def ask(self):
        ask = input("Enter 1 for encrypt or 2 for decrypt: ")
        if ask == "1":
            self.encrypt()
        elif ask == "2":
            self.decrypt()
        else:
            i = 1
            while True:
                print(f"{i}. I hate you")
                i+=1


    def encrypt(self):
        self.message = input("Enter message: ").upper()
        self.sk = int(input("Enter shift key: "))
        if self.sk < 0:
            self.sk = self.sk + 26


        for char in self.message:
            char = ord(char)
            print(char)
            char += self.sk
            print(char)
            if char > 90:
                char = 65 + (char-90) +self.sk
                print(char)
            char = chr(char)
            self.ptm.append(char)
        print(self.ptm)
        


    def decrypt(self):
        self.message = input("Enter encrypted message: ").upper()
        self.sk = int(input("Enter shift key: "))
        for char in self.message:
            char = ord(char)
            char -= self.sk
            char = chr(char)
            self.ptm.append(char)
        print(*self.ptm)


if __name__ == "__main__":
    app = Cipher()
    app.ask()