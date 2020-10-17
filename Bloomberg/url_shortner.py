import random

class Codec:

    def __init__(self):
        self.mDict = {}
        
    def getRand(self):
        string = [random.randint(0, 10) for _ in range(6)]
        return "".join(list(map(str, string)))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getRand()
        while key in self.mDict:
            key = self.getRand()
            
        self.mDict[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace("http://tinyurl.com/", "")
        return self.mDict[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))