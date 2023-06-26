'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_letter(letter, shift):

    def shift_letter(letter, shift):

    dictionary = {' ':'-5','A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','X':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    letterlist = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
    space = dictionary[letter]
    if int(space)<0:
        print(' ')
    elif int(dictionary[letter])+ int(shift) <= 26:
        
        numero = dictionary[letter]
        int(shift)
        shifted= int(numero) + shift
        shifted = shifted - 1
        int(shifted)
        print(letterlist[shifted])
    elif int(dictionary[letter])+ int(shift) > 26:
        
        number = (int(dictionary[letter])+ int(shift))%26
        number= number - 1
        return(str(letterlist[number]))

        
    
    
    
shift_letter('A', 2)
    

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    dictionary = {' ':'-5','A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','X':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    letterlist = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
    encrypted_message= ""
    
    length = int(len(message))

    while length> 0:
        length -= 1
        pos= message[length]
        number = dictionary[pos]
        
        space = dictionary[pos]
        if int(space)<0:
            encrypted_message=  " " + encrypted_message

        elif int(dictionary[pos]) + int(shift) <= 26:
            int(shift)
            shifted= int(number) + shift
            shifted = shifted - 1
            int(shifted)
            encrypted_message=  letterlist[shifted] + encrypted_message
        else:
            numero = (int(dictionary[pos])+ int(shift))%26
            numero= numero - 1
            encrypted_message=  letterlist[numero] + encrypted_message
                
    return(str(encrypted_message))

caesar_cipher('HI', 27) 

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_by_letter(letter, letter_shift):

    dictionary = {' ':'-5','A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','X':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    letterlist = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
    space = dictionary[letter]
    space2= dictionary[letter_shift]
    
    if int(space)<0 or int(space2) <0:
        print(' ')
    elif int(dictionary[letter])+ int(dictionary[letter_shift]) <= 26:
        
        numero = dictionary[letter]
        numero2 = dictionary[letter_shift]
        shifted= int(numero) + int(numero2)
        shifted = shifted - 2
        int(shifted)
        print(letterlist[shifted])
    elif int(dictionary[letter])+ int(dictionary[letter_shift]) > 26:
        
        number = (int(dictionary[letter])+ int(dictionary[letter_shift]))%26
        number= number - 2
        
        return(str(letterlist[number]))


shift_by_letter('B', 'K')

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    dictionary = {' ':'-5','A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','X':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    letterlist = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
    ciphermessage = ""
    
    length = int(len(message))
    length2 = int(len(key))
    multiply = (length/length2)//1
    remainder = length%length2
    newkey = key*int(multiply)
    x= remainder
    y=0
    while x>0:
        x-= 1
        newkey+= key[y]
        y+=1

    x=0
    length = int(len(message))
    while length> 0:
        
        length -= 1
        pos= message[length]
        number = dictionary[pos]
        position2 = newkey[length]
        number2 = dictionary[position2]
                
        if int(number)<0:
            ciphermessage= " "

        elif int(dictionary[pos]) + int(dictionary[position2])<=26:
            shift= int(dictionary[position2])
            shifted= int(number) + int(shift)
            shifted = shifted - 2
            int(shifted)
            ciphermessage=  letterlist[shifted] + ciphermessage
        else:
            numero = (int(dictionary[pos])+ int(dictionary[position2]))%26
            numero= numero - 2
            ciphermessage=  letterlist[numero] + ciphermessage
    return(str(ciphermessage))

vigenere_cipher('BBBBBBBBB','ABAZ')

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
