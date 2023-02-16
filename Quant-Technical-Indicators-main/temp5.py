import concurrent.futures
import random

class OrderBook:
    def __init__(self):
        self.bids = {} # dictionary to store bid orders
        self.asks = {} # dictionary to store ask orders

    def add_order(self, order_type, price, quantity):
        if order_type == "buy":
            self.bids[price] = quantity
        else:
            self.asks[price] = quantity

    def remove_order(self, order_type, price):
        if order_type == "buy":
            del self.bids[price]
        else:
            del self.asks[price]

    def query_book(self):
        return (self.bids, self.asks)

def simulate_order(order_book):
    order_type = "buy" if random.randint(0,1) == 0 else "sell"
    price = random.randint(1, 100)
    quantity = random.randint(1, 10)
    order_book.add_order(order_type, price, quantity)

if __name__ == "__main__":
    order_book = OrderBook()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(1000):
            executor.submit(simulate_order, order_book)
