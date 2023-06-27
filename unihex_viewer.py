f = open("unifont.hex", "r")
# change "unifont.hex" to your unihex font's filename
src = f.readlines()
f.close()
def render()
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

while input("draw? ").lower() in "yes1":
  render()
