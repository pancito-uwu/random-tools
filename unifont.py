f = open("unifont.hex", "r")
src = f.read().split("\n")
f.close()

line = src[int(input("line number:"))]
codepoint, char = line.split(":")

print(line)
print("\nDIVIDE IN 16 GROUPS")
rows = [char[i:i+len(char)//16] for i in range(0, len(char), len(char)//16)]
print(*rows)
print("")
for i in rows: print(i)
print("\nCONVERT HEXADECIMAL DIGITS TO BINARY")
for i in rows: print(format(int(i, 16), f"0{len(char)//4}b"))
print("\nREPLACE 0 AND 1 WITH ⬛ AND ⬜")
for i in rows: print(format(int(i, 16), f"0{len(char)//4}b").replace("0", "⬛").replace("1", "⬜"))