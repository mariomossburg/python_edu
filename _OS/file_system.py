# mimics file creation. 

class File:
    def __init__(self, name, inode):
        self.name = name
        self.inode = inode

class FileSystem:
    def __init__(self):
        self.files = {}
        self.next_inode = 1

    def create_file(self, name):
        if name in self.files:
            print(f"File '{name}' already exists.")
        else:
            self.files[name] = File(name, self.next_inode)
            print(f"Created '{name}' with inode {self.next_inode}")
            self.next_inode += 1

    def list_files(self):
        print(f"{'File Name':<20} {'Inode':<6}")
        print("-" * 28)
        for f in self.files.values():
            print(f"{f.name:<20} {f.inode:<6}")

if __name__ == "__main__":
    fs = FileSystem()
    print("File System Simulation - Creating files\n")
    fs.create_file("report.txt")
    fs.create_file("data.csv")
    fs.create_file("image.png")
    print("\nListing files:\n")
    fs.list_files()


# Notes:
# inode = unique identifier for a file (like an ID card)
# files = dictionary storing file name -> File object
# create_file assigns a new inode to each new file
# This simulates a simple filesystem inode allocation and file listing.




