alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def code(text,shift,direction):
    if direction == "decode":
        shift *= -1
    text_len = len(text)
    new_text = []
    for a in range(0,text_len):
        for b in range(0, 25):
            if alphabet[b] == text[a]:
                if b + shift <= 25:
                    new_text.append(alphabet[b + shift])
                else:
                    new_text.append(alphabet[(b+shift)-26])
        if text[a] not in alphabet:
            new_text.append(text[a])
    print(f"Your {direction} is: "+"".join(new_text))
end = False
while not end:
    direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text1 = input("Type your message:\n").lower()
    shift1 = int(input("Type the shift number:\n"))
    code(text1, shift1, direction1)
    retart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if retart == "no":
        end = True
print("GOOD BYE !!!!!")