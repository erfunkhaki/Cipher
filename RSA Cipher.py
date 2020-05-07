import random
#creating random prime numbers
def create_primes():
    new_primes = []
    
    while(len(new_primes) != 2):
        rand_num = random.randrange(100,999)
        if(prime(rand_num) == True):
            new_primes.append(rand_num)
        else:
            continue
    # print("The prime numbers are: ", new_primes[0], new_primes[1])
    return new_primes

def calculate_n():
    prime_list = create_primes()
    n = prime_list[0]*prime_list[1]
    # print("n is: ", n)
    return n

def function_for_e(n):
    e = 2
    while(GCD(e,phi(n)) != 1):
        e += 1
    # print("e is: ", e)
    return e

def function_for_d(e, phi_n):
    d = linear_congruence(e, 1, phi_n)
    # print("d is: ", d)
    return d

def public_key(e, n):
    public_key = [e, n]
    print("Public key is: (", public_key[0], public_key[1], ")")
    return public_key

def private_key(d, n):
    private_key = [d, n]
    print("Private key is: (", private_key[0], private_key[1], ")")
    return private_key
    
# Linear congruence function
def linear_congruence(a, c, m):
    if c % GCD(m, a) !=  0:
        print("No solution")
        return

    x = 0
    solutions = []

    while(x < m):
        if((a*x)%m == c):
            solutions.append(x)
        x += 1
    # print("The solutions are: ")
    return solutions[0]

# Euler Phi function
def phi(a):
    total = 0
    for x in range(1, a):
        if GCD(x, a) == 1:
            total += 1
    return total

#prime function
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

def GCD(a,b):
    if a < b:
        makeb = a
        a = b
        b = makeb
    r = 10 #Just to run in the loop

    while r > 0:
        r = a % b
        newa = b
        newb = r
        a = newa
        b = newb
        if r == 0:
            return newa #Final answer
            break

def RSA_encrypt():
    message = input("Please input a message to be encrypted by the RSA algorithm: ")
    message = message.lower()
    encrypted_message = ""
    three_digit_numbers = []
    c = ""

    for x in range(len(message)):
        current_letter = message[x]
        alphabet_index = alphabet.find(current_letter)
        encrypted_message += values[alphabet_index]

    
    # splitting the encrypted message into 3-digit segments
    for x in range(0, len(encrypted_message), 3):
        num_digit = int(encrypted_message[x:x+3])
        three_digit_numbers.append(num_digit)

    for x in three_digit_numbers:
        mod = (x**e) % n
        c += str(mod)
        c += " "
    c[0:-1]
    
    print("encrypted message: " + c)

    return c

def RSA_decrypt():
    message = input("Please enter ciphertext to be decrypted by the RSA algorithm (make sure no spaces are at the end): ")
    numbers = message.split()
    decrypted_message = ""
    two_digit_numbers = []
    letters = ""
    x_iter = 0

    for x in numbers:
        x = int(x)
        mod = (x**d) % n
        mod = str(mod)
        #print("mod before: " + mod)
        if x_iter != len(numbers)-1:
            if len(mod) == 2:
                mod = '0' + mod
            elif len(mod) == 1:
                mod = '00' + mod
        #print("mod after: " + mod)
        decrypted_message += mod
        x_iter += 1


    for x in range(0, len(decrypted_message), 2):
        new_index = decrypted_message[x:x+2]
        new_letter = alphabet[int(new_index)]
        letters += new_letter

    print("decrypted message: " + letters)
    


alphabet = "abcdefghijklmnopqrstuvwxyz "
values = []

n = calculate_n()
phi_n = phi(n)
e = function_for_e(n)
d = function_for_d(e, phi_n)
public_k = public_key(e, n)
private_k = private_key(d, n)


for x in range(len(alphabet)):
    if x < 10:
        values.append('0'+str(x))
    else:
        values.append(str(x))

RSA_encrypt()
RSA_decrypt()
