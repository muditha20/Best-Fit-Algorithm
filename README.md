# Best Fit Memory Allocation Algorithm

This project demonstrates the **Best Fit Memory Allocation Algorithm** implemented in Python. The algorithm efficiently allocates memory blocks to processes based on their memory requirements by choosing the smallest suitable block. If no block is large enough, the process is marked as "Not Allocated."

---

## **Algorithm Overview**

### **How It Works**:
1. Each process is allocated to the smallest memory block that can fit its memory requirement.
2. If no block is available, the process remains unallocated.
3. Allocated memory blocks are updated to reflect their remaining size, but they cannot be reused for other processes.

### **Steps**:
1. Input the number and sizes of memory blocks.
2. Input the number and memory requirements of processes.
3. Iterate through each process:
   - Find the smallest block that can fit the process.
   - Allocate the block and update its remaining size.
   - If no block fits, mark the process as "Not Allocated."
4. Display the allocation results and remaining memory in each block.

---

## **Features**
- Accepts dynamic inputs for memory blocks and processes.
- Allocates memory based on the Best Fit principle.
- Outputs:
  - Process-to-block allocations.
  - Remaining memory in each block after allocation.
  - Unallocated processes.



