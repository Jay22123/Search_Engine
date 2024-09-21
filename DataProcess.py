import string
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize  # 引入 NLTK 的分詞模組
from nltk.corpus import stopwords  # 引入 NLTK 的停用詞庫模組
from nltk.text import Text


class Processor():
    def __init__(self) -> None:
        self._data = []
        nltk.download('punkt_tab')
        nltk.download('stopwords')

    def LoadData(self, data):
        self._data.append(data)

    def Normalize(self, keyword):
        for data in self._data:
            [title, content, path] = data
            content = str(content)
            self._filtered_tokens = self.preprocess(content)

            self._nltk_texts = {title: Text(self.preprocess(content))}

            self._inverted_index = self.build_inverted_index(title)

            print(self._inverted_index)  # 輸出過濾後的 tokens

            results = self.analyze_text(content, keyword)
            print("Keywords count:", results["keyword_count"])
            print("Characters count (including spaces):",
                  results["char_count_including_spaces"])
            print("Characters count (excluding spaces):",
                  results["char_count_excluding_spaces"])
            print("Word count:", results["word_count"])
            print("Sentence count:", results["sentence_count"])
            print("Non-ASCII characters count:",
                  results["non_ascii_char_count"])
            print("Non-ASCII words count:", results["non_ascii_word_count"])

    def build_inverted_index(self, documentsID):
        inverted_index = defaultdict(list)
        # 建立索引，記錄每個單詞出現在的文檔
        for token in self._filtered_tokens:
            inverted_index[token].append(documentsID)

        return inverted_index

    def Search(self, query):
        if len(query) != 0:
            query_tokens = self.preprocess(query)
            results = defaultdict(list)

            for token in query_tokens:
                print(f"\nConcordance for '{token}':")
            for doc_id, text in self._nltk_texts.items():
                if token in text:
                    print(f"\nDocument: {doc_id}")
                    # 使用 concordance 展示上下文
                    text.concordance(token)
                    results[doc_id].append(token)
            return results

    def preprocess(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return filtered_tokens

    def analyze_text(self, text, keywords):
        # 1. 關鍵字數量
        words = word_tokenize(text.lower())
        if len(keywords) == 0:
            keyword_count = 0
        else:
            keywords = self.preprocess(keywords)
            keyword_count = sum(1 for word in words if word in keywords)

        # 2. char數(含空格)
        char_count_including_spaces = len(text)

        # 3. char數(不含空格)
        char_count_excluding_spaces = len(text.replace(" ", ""))

        # 4. word數量
        word_count = len(words)

        # 5. 句子數量
        sentences = sent_tokenize(text)
        sentence_count = len(sentences)

        # 6. 非 ASCII  char
        non_ascii_chars = [char for char in text if ord(char) > 127]
        non_ascii_char_count = len(non_ascii_chars)

        # 7. 非 ASCII word
        non_ascii_words = [word for word in words if any(
            ord(char) > 127 for char in word)]
        non_ascii_word_count = len(non_ascii_words)

        return {
            "keyword_count": keyword_count,
            "char_count_including_spaces": char_count_including_spaces,
            "char_count_excluding_spaces": char_count_excluding_spaces,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "non_ascii_char_count": non_ascii_char_count,
            "non_ascii_word_count": non_ascii_word_count
        }
