class ResizableArray:
    def __init__(self):
        # Initialize the array with an initial capacity of 1 and no elements
        self.capacity = 1
        self.items = [None] * self.capacity
        self.item_count = 0

    def add(self, value):
        # Add an element to the array, resize if the array is full
        if self.item_count == self.capacity:
            self.expand(self.capacity * 2)

        self.items[self.item_count] = value
        self.item_count += 1

    def expand(self, new_capacity):
        # Resize the array to a new capacity
        new_items = [None] * new_capacity
        for i in range(self.item_count):
            new_items[i] = self.items[i]
        self.items = new_items
        self.capacity = new_capacity

    def calculate_amortized_cost(self, num_operations):
        # Calculate the amortized cost for 'num_operations' insertions
        total_cost = 0
        for i in range(num_operations):
            # If the array is full, resize it and add the resize cost
            if self.item_count == self.capacity:
                total_cost += self.capacity
                self.expand(self.capacity * 2)

            # Add the cost for each insertion (inserting and incrementing count)
            total_cost += 2
            self.item_count += 1

        # Return the average (amortized) cost per insertion
        return total_cost / num_operations

# Example usage
array = ResizableArray()
num_insertions = 1000  # Number of elements to insert
amortized_cost = array.calculate_amortized_cost(num_insertions)

print("Amortized cost using the accounting method:", amortized_cost)

##output Amortized cost using the accounting method: 3.023