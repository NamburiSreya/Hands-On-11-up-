#include <iostream>

class ExpandableArray {
private:
    int *elements;        // Pointer to the array storing elements
    int currentCapacity;   // Current capacity of the array
    int numElements;       // Number of elements currently in the array

public:
    // Constructor to initialize an empty array
    ExpandableArray() : elements(nullptr), currentCapacity(0), numElements(0) {}

    // Destructor to release the allocated memory
    ~ExpandableArray() {
        delete[] elements;
    }

    // Function to append a new element to the array
    void append(int value) {
        // If the array is full, resize it
        if (numElements >= currentCapacity) {
            int newCapacity = (currentCapacity == 0) ? 1 : currentCapacity * 2;
            int *newElements = new int[newCapacity];
            // Copy old elements to the new array
            for (int i = 0; i < numElements; ++i) {
                newElements[i] = elements[i];
            }
            delete[] elements;  // Free old memory
            elements = newElements;
            currentCapacity = newCapacity;
        }
        elements[numElements++] = value;  // Add new element and increment size
    }

    // Function to get the element at a specific index (with bounds checking)
    int getAt(int index) const {
        if (index < 0 || index >= numElements) {
            std::cerr << "Index out of range\n";
            exit(1);
        }
        return elements[index];
    }

    // Overloaded [] operator for accessing elements
    int& operator[](int index) {
        if (index < 0 || index >= numElements) {
            std::cerr << "Index out of range\n";
            exit(1);
        }
        return elements[index];
    }

    // Function to return the number of elements in the array
    int getSize() const {
        return numElements;
    }
};

int main() {
    ExpandableArray arr;

    // Insert elements into the array
    for (int i = 0; i < 10; ++i) {
        arr.append(i);
    }

    // Output the elements in the array
    for (int i = 0; i < arr.getSize(); ++i) {
        std::cout << arr[i] << " ";
    }

    std::cout << std::endl;

    return 0;
}


//output  0 1 2 3 4 5 6 7 8 9