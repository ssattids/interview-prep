class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for str_ in strs:
            encoded_str += str(len(str_)) + "|" + str_
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ls = []
        i = 0
        number_str = ""
        number = True
        while(i < len(s)):
            if s[i] != "|":
                number_str += s[i]
                i+=1
            else:# s[i] == "|":
                part_str = s[i+1:i+1+int(number_str)]
                ls.append(part_str)
                i+=1+int(number_str)
                number_str = ""

        return ls

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))