
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

menu_style = '''
~
caesar cipher cracker
v1.0
~
'''
cli_style = '''

~~~~~~~~~~~~~~~~~~~~
Cracking started
~~~~~~~~~~~~~~~~~~~~
'''

print(menu_style)
encrypted_text = input("[Encrypted text]: ")


while True:
    wordlist = input("[Wordlist path ('Enter' to use default, s to enter settings) ]: ")
    try:
        if wordlist == "":
            wordlist = "google-10000-english-usa-no-swears-long.txt"
            with open("google-10000-english-usa-no-swears-long.txt", 'r') as file:
                wl_content = file.read()
        else:
            with open(wordlist, 'r') as file:
                wl_content = file.read()
        break
    except FileNotFoundError:
        print(f"{wordlist} not found")
            
            
def crack_multiword():
    for i in range(0, word_count):
        target = encrypted_text.split()[i]
        print("----------")
        print("[T] Targeted word: ", encrypted_text.split()[i])
        letters_in_word = len(target)
        print("[L] Letters in word: ", letters_in_word)
        print("----------")

        for y in range(len(alphabet)):
            shifted_word = ''.join(alphabet[(alphabet.index(c) + y) % len(alphabet)] if c in alphabet else c for c in target)

            if shifted_word in wl_content:
                print(f"\n[S] Word match found! -> {shifted_word}")
                print("\n\n------------------------------------")
                print("~~ Encoded text successfully cracked! ~~")
                print(f"[S] Shift: +{y}\n")
                print(''.join((alphabet[(alphabet.index(ch.lower()) + y) % len(alphabet)].upper() if ch.isupper() else alphabet[(alphabet.index(ch.lower()) + y) % len(alphabet)]) if ch.lower() in alphabet else ch for ch in encrypted_text))

                print("\n------------------------------------")
                exit()

    print("\n\n[!] No words have been found in the encrypted text which could match with one of the words in the wordlist ")
    print("[I] Try using a different wordlist\n")
    exit()



def crack_oneword():
    global encrypted_text
    encrypted_text = encrypted_text.lower()
    print("-----------------\n[I] Searching for words in the text to identify shifting\n-----------------")
    for i in range(1, len(encrypted_text) + 1):
        for first_letter in range(len(encrypted_text)):
            selected_letter = encrypted_text[first_letter:i]
            for shift in range(len(alphabet)):
                shifted_word = ''.join(alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in selected_letter)
                if shifted_word in wl_content:
                    print(f"\n[S] Word match found! -> {shifted_word}")
                    print("\n\n------------------------------------")
                    print("~~ Encoded text successfully cracked! ~~")
                    print(f"[S] Shift: +{shift}\n")
                    print(''.join(alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in encrypted_text))

                    print("\n------------------------------------")
                    exit()
    print("\n\n[!] No words have been found in the encrypted text which could match with one of the words in the wordlist ")
    print("[I] Try using a different wordlist\n")
    exit()

    
        

wl_content = wl_content.split()
print(cli_style)
word_count = len(encrypted_text.split())
if word_count == 1:
    crack_oneword()
else:
    crack_multiword()

