text = input("Enter some text")
shift = int(input("What is your shift? "))
encrypt = input("Do you want to encrypt or decrypt?")
cypher_text = ""
if encrypt == "encrypt":
    for letter in text:
       if letter.isalpha():
            if (ord(letter)+ shift) > ord('z'):
                letter = chr(ord(letter)+shift-26)
                cypher_text += letter
            else:
                cypher_text += chr(ord(letter)+ shift)
    print(cypher_text)         
if encrypt == "decrypt":
    for letter in text:
        if letter.isalpha():
            if (ord(letter)-shift) < ord('a'):
                letter = chr(ord(letter)-shift+26)
                cypher_text += letter 
            else:
                cypher_text += chr(ord(letter)- shift)
    print(cypher_text)
