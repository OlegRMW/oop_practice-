class StoreText:
    def __init__(self, text):
        print("Start StoreText.__init__")
        self.text = text
        print("End StoreText.__init__")


class PalindromeChecker(StoreText):
    def __init__(self, text):
        print("Start PalindromeChecker.__init__")
        super().__init__(text)
        self.palindromes = self._find_palindromes()
        print("End PalindromeChecker.__init__")
    
    def _find_palindromes(self):
        words = self.text.split()
        palindromes = []
        for word in words:
            cleaned_word = ''.join(filter(str.isalnum, word)).lower()
            if cleaned_word and cleaned_word == cleaned_word[::-1]:
                palindromes.append(word)
        return palindromes


class PalindromeCounter(StoreText):
    def __init__(self, text):
        print("Start PalindromeCounter.__init__")
        super().__init__(text)
        self.count = self._count_palindromes()
        print("End PalindromeCounter.__init__")
    
    def _count_palindromes(self):
        words = self.text.split()
        count = 0
        for word in words:
            cleaned_word = ''.join(filter(str.isalnum, word)).lower()
            if cleaned_word and cleaned_word == cleaned_word[::-1]:
                count += 1
        return count


class PalindromeAnalyzer(PalindromeCounter, PalindromeChecker):
    def __init__(self, text):
        print("Start PalindromeAnalyzer.__init__")
        super().__init__(text)
        print("End PalindromeAnalyzer.__init__")
    
    def print_results(self):
        print("\nРезультаты анализа:")
        print(f"Исходный текст: {self.text}")
        print(f"Палиндромы: {self.palindromes}")
        print(f"Количество палиндромов: {self.count}")


text = "level radar hello world madam kayak python"
analyzer = PalindromeAnalyzer(text)
analyzer.print_results()