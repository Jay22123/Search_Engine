import string
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize  # 引入 NLTK 的分詞模組
from nltk.corpus import stopwords  # 引入 NLTK 的停用詞庫模組
from nltk.text import Text
import os
import re


class Processor():
    def __init__(self) -> None:
        self._data = []
        nltk.download('punkt_tab')
        nltk.download('stopwords')
        nltk.download('punkt')
        self.total_index_dict = {}

    # 計算每篇文章的ˊ字數.....
    def Normalize(self, data):

        content = str(data["Content"])
        self._results = self.analyze_text(content)
        self._results.update(data)
        # print("Title:", self._results["Title"])
        # print("Characters count (including spaces):", self._results["char_count_including_spaces"])
        # print("Characters count (excluding spaces):", self._results["char_count_excluding_spaces"])
        # print("Word count:", self._results["word_count"])
        # print("Sentence count:", self._results["sentence_count"])
        # print("Non-ASCII characters count:",self._results["non_ascii_char_count"])
        # print("Non-ASCII words count:", self._results["non_ascii_word_count"])
        # print("="*48)

        # 建立搜尋表單
        tokens = word_tokenize(content.lower())
        position = 0
        index_dict = {}
        for word in tokens:
            word_lower = word.lower()  # 將單詞轉為小寫，統一索引
            if word_lower not in index_dict:
                index_dict[word_lower] = []
            index_dict[word_lower].append(position)
            position += len(word) + 1  # 更新位置，考慮到空格
        # 顯示索引結果 0927
        index_text = "\n".join(
            [f"{word}: {positions}" for word, positions in index_dict.items()])
        print(index_text)

        return self._results

    def analyze_text(self, text):

        words = word_tokenize(text.lower())
        cleaned_words = [re.sub(r'[^\w\s]', '', word)
                         for word in words if re.sub(r'[^\w\s]', '', word)]

        # 2. char數(含空格)
        char_count_including_spaces = len(text)

        # 3. char數(不含空格)
        char_count_excluding_spaces = len(text.replace(" ", ""))

        # 4. word數量
        word_count = len(cleaned_words)

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
            "char_count_including_spaces": char_count_including_spaces,
            "char_count_excluding_spaces": char_count_excluding_spaces,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "non_ascii_char_count": non_ascii_char_count,
            "non_ascii_word_count": non_ascii_word_count
        }

    def Search(self, data, query):
        if len(query) != 0:
            # 把nltk處理加進來
            query_tokens = self.preprocess(query)
            search_results = {}
            for item in self._nltk_texts:
                for doc_id, text in item.items():
                    results = []
                    for token in query_tokens:
                        # print(f"\nConcordance for '{token}':")
                        results.append(
                            self.display_full_concordance(text, token, 3, 20))

                        # results[doc_id].append(resultline)
                search_results[doc_id] = results

            return search_results

    def preprocess(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text.lower())
        # stop_words = set(stopwords.words('english'))
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

            highlighted_token = f"<span style='color: red; background-color: yellow;'>{
                token}</span>"
            result_lines.append(f"... {left_context} {
                                highlighted_token} {right_context} ...")
        return "<br>".join(result_lines)
