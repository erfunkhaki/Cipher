import random
import math

# encrypts the message using our trigonometry cipher
def trig_encrypt():
    message = input("Please input a message: ")
    message = message.lower()

    for x in message:
        symbols =  ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","`","~","?",",",".","<",">","/",";",":","]"]
        if x in symbols:
            print("can only encrypt letters")
            exit(0)
    values = []
    encrypted_message = [] 
    encrypted_list = []
    # prints the message cleanly to the screen
    printable_list = []
    
    # multiplies each value by private_key
    change_dictionary_1()

    for x in message: 
        for key, value in coord_dict.items():
            if key == x:
                encrypted_list.append(value[random.randrange(0, len(value))])

    for x in encrypted_list:
        printable_list.append(x[0])
        printable_list.append(x[1])

    print("Encrypted message: ", end="")
    print(*printable_list)

    

# decrypts the message using the trigonometry cipher
def trig_decrypt():
    message = input("Please enter a message to be decrypted using our trigonometry cipher: ")
    message = message.lower()
    nums = message.split()
    decrypted_message = ""
    
    # divides the values by the private_key
    change_dictionary_2()

    for x in range(0, len(nums), 2):
        x_coord = float(nums[x])/private_key
        y_coord = float(nums[x+1])/private_key
        # print("Coordinates: ", x_coord, y_coord) 
        other_coord = [x_coord, y_coord] 

        for key, value in coord_dict.items():
            if other_coord in value:
                decrypted_message += key
    
    print("This is the decrypted message: " + decrypted_message)
            

def change_dictionary_1():
    # print("private_key is: ", private_key)
    for key, value in coord_dict.items():
        for x in value:
           x[0] = x[0] * private_key
           x[1] = x[1] * private_key

def change_dictionary_2(): 
    for key, value in coord_dict.items():
        for x in value:
           x[0] = x[0] / private_key
           x[1] = x[1] / private_key

            

# creates a list of size length of non-repeating 3-digit numbers cast into strings
def create_list(length, radius):
    # random_list not needed in final code
    # list of randomly generated numbers
    # random_list = []
    # final list of non-repeating numbers
    final_list = []
    # loop to fill random list
    #for x in range(length*3):
        #random_list.append(random.randrange(100, 999))
    # loop to fill final_list

    # creates an x and y coordinate based on the sin and cosine of
    # the numbers
    for x in range(length):
        new_num = random.randrange(0, 360)
        new_cos = math.cos(new_num)*radius
        new_sin = math.sin(new_num)*radius
        new_coord = [new_cos, new_sin]
        if(new_coord not in final_list):
            final_list.append(new_coord)
        else:
            while(new_coord in final_list):
                new_num = random.randrange(0,360)
                new_cos = math.cos(new_num)*radius
                new_sin = math.sin(new_num)*radius
                new_coord = [new_cos, new_sin]
            final_list.append(new_coord)
    return final_list

def make_dict(num_list, freq):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    new_dict = {}
    # h_iter is the current index of the letter frequency list
    h_iter = 0
    # value index higher/lower used to take the numbers associated with each letter and
    # assign them to that letter
    value_index_higher = freq[h_iter]
    value_index_lower = 0
    for x in range(len(alphabet)):
        # assign to the current key, the values in the number list from [lower : higher]
        new_dict[alphabet[x]] =  num_list[value_index_lower : value_index_higher]
        # increment h_iter, set lower to the current value of higher
        h_iter += 1
        old_higher = value_index_higher
        value_index_lower = old_higher
        if(x == 26):
            value_index_higher = old_higher
        else:
            # add to value of the previous value_index_higher, the next value in the
            # letter frequency index, so now the next higher/lower values are set
            value_index_higher = old_higher + freq[h_iter]

    return new_dict

def generate_prime(maximum):
    new_prime = 8
    while(prime(new_prime) == False):
        new_prime = random.randrange(2, maximum)
    return new_prime

# erfans's prime function
def prime(x):
    cal1 = pow(x, 0.5)
    cal2 = round(cal1, 0)
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    elif x == 1 or x == 4 or x == 6 or x == 8 or x == 9:
        return False
    else:        
        for y in range(2, int(cal2)):
            answer = x % int(y)
            if answer == 0:
                return False
                break
            else:
                continue
        else:
            return True

precision = 2
freq = [8, 2, 3, 4, 12, 2, 2, 6, 6, 1, 1, 4, 2, 6, 7, 2, 1, 6, 6, 9, 3, 1, 2, 1, 2, 1, 7]
alphabet = "abcdefghijklmnopqrstuvwxyz "
radius = random.randrange(0,1000)
private_key = generate_prime(100)
coord_list = create_list(150, radius)
coord_dict =  make_dict(coord_list, freq)

trig_encrypt()
trig_decrypt()
