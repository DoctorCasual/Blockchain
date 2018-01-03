import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash="0"):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def __str__(self):
        info = "index: {}\ntimestamp: {}\ndata: {}\nprevious hash: {}\nhash: {}"
        info = info.format(self.index, self.timestamp, self.data, self.previous_hash, self.hash)
        return info

    def calculate_hash(self):
        mystring = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        hash_object = hashlib.sha256(mystring.encode('utf-8'))
        # print(hash_object.hexdigest())
        return hash_object.hexdigest()

    def mine_block(self, difficulty):
        check = ""
        for i in range(difficulty):
            check += "0"
        print("Mining block...")
        while self.hash[:difficulty] != check:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined: {}".format(self.hash))

