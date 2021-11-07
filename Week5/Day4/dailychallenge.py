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

# import nltk
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize

class TextModification(Text):
    def no_punc (self, text):
        self.text = text.translate(str.maketrans('', '', string.punctuation))

    def no_english_stop(self,text):
        # for word in text: 
        #     if word not in en_stops:
        #         print
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        return (tokens_without_sw)


    def no_special_char(self,text):
        new_text = ''.join(char for char in text if char.isalnum())
        return(new_text)

text_mod= TextModification()
print(text_mod.no_punc(strange))
print(text_mod.no_english_stop(strange))
print(text_mod.no_special_char(strange))
