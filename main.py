from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    # Checks if character is in the alphabet array
      #index() gets position of selected value in array
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount   
      end_text += alphabet[new_position]
    else:
      end_text += char
    
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


# Continue using cipher until user chooses 'No'
cipher_on = True

print(logo)

while cipher_on == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # prevents shift from going out of bounds of array
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  restart_cipher = input("Do you want to restart cipher?\n").lower()
  if restart_cipher == "yes":
    cipher_on = True
  else:
    cipher_on = False
    print("Goodbye")
  
