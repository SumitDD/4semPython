import string


class TextContainer():
    
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def count_chars(self):
        return len(self.text)
    
    def count_letters(self):
        count = 0
        for element in self.text:
            if element in string.ascii_letters:
                count = count + 1
                    
        return count

    def remove_punctuation(self):
        for element in self.text:  
            if element in string.punctuation:  
                self.text = self.text.replace(element, "")

        return self.text