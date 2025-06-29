------Operating Systems------
*Imagine a factory*



## 1. process & threads  
--workers and their tasks
- A **process** is a worker
- A **thread** a task the worker performs  


## 2. CPU Scheduling
📋 *Shift manager assigning tasks*
- **Round Robin** every worker gets a short shift, rotates  
- **FCFS** first worker in gets served first  
- **Priority** urgent shipments go first


## 3. Memory Management
📦 *Warehouse shelf system*
- **Paging** shelves split into same-sized boxes  
- **Segmentation** shelves split by item type (books, tools, clothes)  
- **Virtual Memory** = borrow a nearby storage unit when space is full

## 4. Synchronization
🚪 *Shared tools or rooms*
- **Mutex** = only one worker can use a tool at a time (1 key)  
- **Semaphore** = multiple allowed, but limited (tickets to use printer)  
- **Deadlock** = two workers holding tools each other needs — stuck

## 5. Deadlocks
🚧 *Blocked workflow in the warehouse*
- Forklift A waits for B’s path, B waits for A  
- Prevention = limit tool holding or re-route traffic


## 6. File Systems
📁 *Inventory and labeling system*
- **File** = stored item  
- **Inode** = ID tag with location  
- **Directory** = shelf that holds items

## 7. I/O Systems
📦 *Shipping & receiving docks*
- **Buffer** = packages waiting to load  
- **Driver** = person who knows how to talk to trucks  
- **Interrupt** = urgent truck honks — needs loading now

## 8. Security & Protection
🔐 *Access badges and surveillance*
- **User mode** = guest worker, limited access  
- **Kernel mode** = supervisor access  
- **ACLs** = who can enter which rooms


## 9. Virtualization
🏢 *Mini-factories inside the big Amazon warehouse*
- Each **VM** = its own section with fake walls  
- **Hypervisor** = warehouse floor manager keeping each section running


## 10. System Calls & APIs
📞 *Employees calling HQ*
- Need permission to: print labels, load truck, access secure data  
- **System call** = formal request to OS (HQ) to act

----OS Runs the show, I/O is one act of----

