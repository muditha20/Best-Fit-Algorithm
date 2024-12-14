def best_fit_fixed_memory():
    # Input memory blocks and processes
    no_of_blocks = int(input("Enter number of memory blocks >>> "))
    memory = [int(input(f"Enter size for memory block {i + 1} >>> ")) for i in range(no_of_blocks)]

    no_of_processes = int(input("Enter number of processes >>> "))
    process = [int(input(f"Memory required for process {i + 1} >>> ")) for i in range(no_of_processes)]

    # Initialize allocation tracking
    allocations = [None] * no_of_processes  # Tracks the allocated block for each process
    allocated_blocks = [False] * no_of_blocks  # Tracks whether a block is allocated

    # Best fit allocation logic
    for i, p in enumerate(process):
        best_block = -1
        for j, m in enumerate(memory):
            if not allocated_blocks[j] and m >= p and (best_block == -1 or m < memory[best_block]):
                best_block = j

        if best_block != -1:
            allocations[i] = best_block  # Store the index of the allocated block
            memory[best_block] -= p  # Update remaining memory of the allocated block
            allocated_blocks[best_block] = True  # Mark block as fully allocated

    # Print the results
    print("\n================ Memory Allocations ====================")
    print("Process No.\tMemory Block Allocated")
    for i, block in enumerate(allocations):
        print(f"\t{i + 1}\t\t{'Block ' + str(block + 1) if block is not None else 'Not Allocated'}")

    print("\n================ Remaining Memory Blocks ==============")
    print("Block No.\tRemaining Memory")
    for i, m in enumerate(memory):
        print(f"\t{i + 1}\t\t{m} KB")

# Run the function
best_fit_fixed_memory()
