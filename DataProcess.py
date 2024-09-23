import string
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize  # 引入 NLTK 的分詞模組
from nltk.corpus import stopwords  # 引入 NLTK 的停用詞庫模組
from nltk.text import Text
import os


class Processor():
    def __init__(self) -> None:
        self._data = []
        nltk.download('punkt_tab')
        nltk.download('stopwords')
        nltk.download('punkt')

    def Clear(self):
        self._data.clear()

    def LoadData(self, data):
        self._data.append(data)

    def Normalize(self, keyword):
        self._dictionary = []
        self._nltk_texts = []
        for data in self._data:
            [title, content, path] = data
            content = str(content)

            nltk_texts = {title: Text(nltk.word_tokenize(content))}
            self._nltk_texts.append(nltk_texts)

            self._results = self.analyze_text(content, keyword)
            self._results.update(
                {"Title": title, "Content": content, "Path": path})
            self._dictionary.append(self._results)
            # print("Keywords count:", results["keyword_count"])
            # print("Characters count (including spaces):", results["char_count_including_spaces"])
            # print("Characters count (excluding spaces):", results["char_count_excluding_spaces"])
            # print("Word count:", results["word_count"])
            # print("Sentence count:", results["sentence_count"])
            # print("Non-ASCII characters count:",results["non_ascii_char_count"])
            # print("Non-ASCII words count:", results["non_ascii_word_count"])
        return self._dictionary

    def Search(self, query):
        if len(query) != 0:
            query_tokens = self.preprocess(query)
            search_results = {}
            for item in self._nltk_texts:
                for doc_id, text in item.items():
                    results = []
                    for token in query_tokens:
                        print(f"\nConcordance for '{token}':")
                        results.append(self.display_full_concordance(text, token, 3, 20))
                    
                        #results[doc_id].append(resultline)
                search_results[doc_id] = results

        return search_results

    def preprocess(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        # if word not in stop_words  自行決定是否排除常用字
        filtered_tokens = [word for word in tokens]
        return filtered_tokens

    def display_full_concordance(self, text, token, window=5, lines=10):
        """
        token 的上下文而不截断
        :param text: nltk 的 Text 对象
        :param token: 要搜索的目标 token
        :param window: 上下文范围的词数
        :param lines: 显示结果的行数
        """
        matches = [i for i, t in enumerate(
            text.tokens) if t.lower() == token.lower()]
        result_lines = []

        if not matches:
            return "<br>".join(result_lines)

        for i in matches[:lines]:
            start = max(i - window, 0)
            end = min(i + window + 1, len(text.tokens))

            left_context = ' '.join(text.tokens[start:i])
            right_context = ' '.join(text.tokens[i + 1:end])

            highlighted_token = f"<span style='color: red; background-color: yellow;'>{token}</span>"
            result_lines.append(f"... {left_context} {highlighted_token} {right_context} ...")
        return "<br>".join(result_lines)

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
