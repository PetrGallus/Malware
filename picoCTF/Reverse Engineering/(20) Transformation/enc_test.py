flag = "picoCTF{Test_flag}"

flag_encryption = ''.join([
    chr(
        (
            ord(flag[i]) << 8) + ord(flag[i + 1])
        ) 
        for i in range(0, len(flag), 2)
        ]
)

print(flag_encryption)