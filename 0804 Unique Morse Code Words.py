class Solution:
    def transformation(text):
        morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        char_list = list(text)
        temp = ""
        for char in char_list:
            temp = temp + morse_dict[char]
        return temp
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = []
        for word in words:
            morse = self.transformation(word)
            morse_list.append(morse)
        set_morse = set(morse_list)
        return len(set_morse)
