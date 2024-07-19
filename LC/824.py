"I speak Goat Latin"
"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

class Solution:

    def toGoatLatin(self, sentence: str) -> str:

        a_s = {letter:('a'*i) for i, letter in enumerate(list("abcdefghijklmnopqrstuvwyxz"))}

        new_sentence = ""
        i = 0
        word_count = 1

        new_word_str = ""
        while i < len(sentence):
            current_character = sentence[i]

            if (current_character == " "):
                if new_word_str[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                    new_sentence += new_word_str + "ma" + word_count*'a'
                else:
                    new_sentence += new_word_str[1:] + new_word_str[0] + "ma" + word_count*'a'
                word_count +=1
                new_word_str = ""
                new_sentence += " "
            else:
                new_word_str += current_character
            i+=1

        if new_word_str != "":
            if new_word_str[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                    new_sentence += new_word_str + "ma" + word_count*'a'
            else:
                new_sentence += new_word_str[1:] + new_word_str[0] + "ma" + word_count*'a'


        return new_sentence

            