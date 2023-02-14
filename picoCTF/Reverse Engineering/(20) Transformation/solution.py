flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"

print("Given input: ", flag)

print("\nTest of first chinese char into hex:\n",hex(ord(flag[0])))

print("\nSolution in hex: ")
for c in flag:
    print(hex(ord(c)).lstrip('0x'), end='')

print("\n\nSolution in ASCII: ")
hex_str = "7069636f4354467b31365f626974735f696e73743334645f6f665f385f64353263366239337d"
ascii_str = bytes.fromhex(hex_str).decode()
print(ascii_str)