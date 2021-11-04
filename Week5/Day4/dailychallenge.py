class Text:
    def __init__ (self, string):
        self.content = string
        self.word_list = self.content.split()
        self.unique = set(self.word_list)

    def word_frequency(self,other):
        freq = self.__word_frequency(word)
        if freq:
            return f"the word {word} shows up {freq} times in the current text"
    
    def __word_frequency(self,word):
        if word in self.word_list:
            return self.word_list.count(word)

    def common_word(self) -> str:
        word_dict = list({word: self.__word_frequency(word) for word in self.unique}.items())
        return sorted(word_dict, key = lambda x:x[1], reverse = True)[0][0]
        
    def unique_words(self):
        return list (self.unique)

    @classmethod
    def from_file(cls,file_name):
        with open(file_name, "r") as f:
            file_text = f.read()
        return cls(file_text)

strange = Text.from_file("the_stranger.txt")
print(strange.common_word())

class TextModification(Text):
    def __init__(self):
        pass
    
    def no_punc(self):
        
