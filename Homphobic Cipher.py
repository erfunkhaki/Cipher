import random #Random Library

def homophonic_encrypt():
    print("You are going to encrypt a plaintext using a homophonic cipher")
    message = input("Please enter a message: ")
    encrypted_message = ""
    for x in message:
        if x == " ":
            encrypted_message += " "
            continue
        for key, value in num_dict.items():
            if key == x:
                encrypted_message += str(value[random.randrange(0, len(value))])

    print("Your encrypted message is: " + encrypted_message)


    
def homophonic_decrypt():
    print("You are going to decrypt ciphertext using the homophonic cipher")
    message = input("Please enter the ciphertext: ")
    decrypted_message = ""
    current_letter = 0
    current_num = 0

    for x in range(0, len(message)-1, 3): # +3 because we have 3 digit numbers 
        current_num = message[x:x+3]
        for key in num_dict:
            if current_num in num_dict[key]:
                decrypted_message += key
                break
            else:
                continue
                    
    print("Your decrypted message is: " + decrypted_message)
        
            

def create_list(length): 
    random_list = []
    final_list = []
    for x in range(length*3):
        random_list.append(random.randrange(100, 999)) #3 digit numbers
    for x in range(length):
        new_num = random.randrange(100, 999)
        if(str(new_num) not in final_list):
            final_list.append(str(new_num))
        else:
            while(new_num in final_list):
                new_num = random.randrange(100, 999)
            final_list.append(str(new_num))
    return final_list



def make_dict(num_list, freq): #words
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_dict = {}
    h_iter = 0
    value_index_higher = freq[h_iter]
    value_index_lower = 0
    for x in range(len(alphabet)):
        new_dict[alphabet[x]] =  num_list[value_index_lower : value_index_higher]
        h_iter += 1
        old_higher = value_index_higher
        value_index_lower = old_higher
        if(x == 25):
            value_index_higher = old_higher
        else:
            value_index_higher = old_higher + freq[h_iter]

    return new_dict


freq = [8, 2, 3, 4, 12, 2, 2, 6, 6, 1, 1, 4, 2, 6, 7, 2, 1, 6, 6, 9, 3, 1, 2, 1, 2, 1] #frequencies from power point
number_list = create_list(100) 
num_dict = make_dict(number_list, freq)
print(num_dict) #Just for you so you can see the random dictionary
