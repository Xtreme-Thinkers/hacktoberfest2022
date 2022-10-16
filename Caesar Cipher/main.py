alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_dir,start_text,shift_amount) :

    end_text=''
    if cipher_dir=="D" :
        shift_amount *= -1

    for char in start_text:
        char=str(char)
        
        if char.isalpha():
            i=alphabet.index(char)
            i += shift_amount
            end_text += alphabet[i]
        else:
            end_text += char

    print(f"Here's the result: {end_text}")    


from Art import logo

print(logo)

choice='y'
while choice=="y" :
    direction=''
    while direction!='E' and direction!='D' :
        direction=input("Type 'E' to Encrypt or 'D' to Decrypt!\n").upper()
        if direction!='E' and direction!='D':
           print("Wrong input! Try again!\n")
    
    text=input("Type your Message : ").lower()
    shift = int(input("Type the shift number:\n"))

    shift=shift%26

    caesar(direction,text,shift)
    
    choice=input("Want to Encode/Decode again ? Type 'Y' or 'N' .\nEnter : ").lower()
    
    if choice!='y' and choice!='n' :
        print("\nWrong input ! Program terminated !")
