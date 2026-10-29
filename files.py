# Reading the whole file
# with open("notes.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# # Reading line by line (memory-efficient)
# with open("notes.txt", encoding="utf-8") as f:
#     for line in f:
#         print(line.rstrip("\n"))

# Writing (overwrites existing content)
# with open("out.txt", "w", encoding="utf-8") as f:
#     f.write("Hello\n")
#     f.writelines(["line 1\n", "line 2\n"])

# # Appending
# with open("out.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# with open("out.txt", encoding="utf-8") as f:
#     for line in f:
#         print(line.rstrip("\n"))


# with open("out.txt", "a", encoding="utf-8") as f:
#     f.write("another line\n")
#     f.write("michael is learning data and files in python\n")
#     content = f.write("another line\n")  




# f = open("notes.txt")
# try:
#     data = f.read()
# finally:
#     f.close()


with open("notes.txt", "w") as f:             # "w" creates or overwrites
    f.write("Ada\n")
    f.write("Tunde\n")

with open("notes.txt", "a") as f:             # "a" adds to the end
    f.write("Chioma\n")

with open("notes.txt") as f:                  # "r" is the default
    names = [line.strip() for line in f]
print(names)
assert names == ["Ada", "Tunde", "Chioma"]

def read_names(path):
    try:
        with open(path) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"{path} does not exist yet")
        return []
    finally:
        print("done trying")                  # always runs

assert read_names("missing.txt") == []

# Write a small diary program: add_entry(text) appends a line with the date, and read_entries() returns all lines (empty list if the file does not exist yet).