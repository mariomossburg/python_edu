# Actually creating reading and writing a file in python
def write_weather_to_file(filename="data.txt"):
    with open(filename, "a") as f:
        f.write("weather = 79\n")

def read_file(filename="data.txt"):
    print("\nContents of data.txt:")
    print("-" * 25)
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    print("Simulating File I/O:\n")
    write_weather_to_file()
    read_file()

# Notes:
# This simulates basic OS file I/O.
# On each run:
# 1. Appends the line "weather = 79" to a file named data.txt
# 2. Reads and displays all lines from the file
# Demonstrates persistent storage across executions — like writing to disk.
