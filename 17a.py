class ExpandableArray:
    def __init__(self):
        # Initialize with a default capacity of 1 and no elements
        self.current_capacity = 1
        self.items = [None] * self.current_capacity
        self.num_items = 0

    def add(self, element):
        # Insert a new element, resize if the array is full
        if self.num_items == self.current_capacity:
            self.increase_capacity(self.current_capacity * 2)
        self.items[self.num_items] = element
        self.num_items += 1

    def increase_capacity(self, new_capacity):
        # Resizes the array to the new capacity
        new_items = [None] * new_capacity
        for i in range(self.num_items):
            new_items[i] = self.items[i]
        self.items = new_items
        self.current_capacity = new_capacity

    def compute_amortized_runtime(self, n):
        # Calculate the aggregate amortized runtime of inserting n elements
        total_cost = 0
        for i in range(n):
            # If array is full, resizing cost is added
            if self.num_items == self.current_capacity:
                total_cost += self.current_capacity
                self.increase_capacity(self.current_capacity * 2)
            total_cost += 1  # Adding one for each insertion
            self.num_items += 1
        return total_cost / n

# Example usage
expandable_array = ExpandableArray()
n = 100
amortized_runtime = expandable_array.compute_amortized_runtime(n)

# Output statement
print(f"The aggregate amortized runtime for {n} insertions is: {amortized_runtime}")


##output -The aggregate amortized runtime for 100 insertions is: 2.27