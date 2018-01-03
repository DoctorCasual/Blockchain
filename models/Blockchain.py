from models.Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(self.create_genesis())
        self.difficulty = 5

    def __str__(self):
        for block in self.chain:
            print(block)

    @staticmethod
    def create_genesis():
        return Block(0, "01/01/2018", {"sender": "Genesis", "receiver": "Genesis", "Amount": 0})

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, block):
        block.previous_hash = self.get_latest_block().hash
        block.mine_block(self.difficulty)
        self.chain.append(block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            curblock = self.chain[i]
            prevblock = self.chain[i-1]
            if curblock.hash != curblock.calculate_hash():
                return False
            if curblock.previous_hash != prevblock.hash:
                return False
            return True

