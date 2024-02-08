input = "Nvvk upnoa huk nvvk tvyupun pm fvb hyl ylhkpun pa pu aol tvyupun."
input = input.lower()

output = ''
for _ in range(1, 27):
    output = ''
    for c in input:
        if c >= 'a' and c <= 'z':
            val = ord(c)
            if val - _ < 97:
                diff = 97 - (val - _)
                val = 122 - diff + 1
                output += chr(val)
            else:
                output += chr(val - _)
        else:
            output += c
    print(output)