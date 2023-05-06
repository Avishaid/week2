MORSE_CODE_DICT = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
                    '-..': 'D',      '.': 'E',   '..-.': 'F',
                    '--.': 'G',   '....': 'H',     '..': 'I',
                    '.---': 'J',    '-.-': 'K',   '.-..': 'L',
                    '--': 'M',     '-.': 'N',    '---': 'O',
                    '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
                    '...': 'S',      '-': 'T',    '..-': 'U',
                    '...-': 'V',    '.--': 'W',   '-..-': 'X',
                    '-.--': 'Y',   '--..': 'Z',  '-----': '0',
                    '.----': '1',  '..---': '2',  '...--': '3',
                    '....-': '4',  '.....': '5',  '-....': '6',
                    '--...': '7',  '---..': '8',  '----.': '9','--..--':', ', '.-.-.-': '.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')'}
COUNT_DICT = {}

def decrypt(file_name):
    decrypt_text = ""
    input_file = open(file_name, "r")
    for line in input_file:
        letters_list = line.split()
        for letter in letters_list:
            if letter in MORSE_CODE_DICT.keys():
                decrypt_text += MORSE_CODE_DICT[letter]
                if MORSE_CODE_DICT[letter] in COUNT_DICT.keys():
                    COUNT_DICT[MORSE_CODE_DICT[letter]] += 1
                else:
                    COUNT_DICT[MORSE_CODE_DICT[letter]] = 1
            elif letter == '/':
                decrypt_text += " "
            else:
                print (letter)
                return "Error in Morse Code."
    return decrypt_text


def print_incidences():
    sorted_keys = sorted(COUNT_DICT, key = COUNT_DICT.get) #list
    reverse_sorted_keys = sorted_keys[::-1]
    for key in reverse_sorted_keys:
        print(key + f" - {COUNT_DICT[key]}")

def main():
    file_name = r"morse2.txt"
    decrypt_text = decrypt(file_name)
    print(decrypt_text)
    print_incidences()



if __name__ == '__main__':
        main()