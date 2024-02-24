def construct_2d_array(rows, cols):
    array_2d = []
    counter = 1  # Starting value for filling the array

    for _ in range(rows):
        row = []  # Create a new row for each iteration
        for _ in range(cols):
            row.append(counter)
            counter += 1  # Increment counter for the next element
        array_2d.append(row)  # Append the row to the 2D array

    return array_2d

def print_2d_array(arr):
    for row in arr:
        for element in row:
            print(element, end="\t")  # Use tab to separate elements
        print()

def main():
    rows = 3
    cols = 3

    array_2d = construct_2d_array(rows, cols)

    print("Constructed 2D Array:")
    print_2d_array(array_2d)

if __name__ == "__main__":
    main()
