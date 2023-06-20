class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class BSTNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.frequency = 0


class HybridDataStructure:
    def __init__(self):
        self.hash_table_size = 1000
        self.hash_table = [None] * self.hash_table_size
        self.bst_root = None
        self.trie_root = TrieNode()

    def _hash_function(self, word):
        return sum(ord(char) for char in word.lower()) % self.hash_table_size

    def _bst_insert(self, root, word):
        if root is None:
            return BSTNode(word)

        if word < root.word:
            root.left = self._bst_insert(root.left, word)
        else:
            root.right = self._bst_insert(root.right, word)

        return root

    def _trie_insert(self, root, word):
        node = root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1

    def insert_word(self, word):
        index = self._hash_function(word)

        node = self.hash_table[index]
        while node:
            if node.word == word.lower():
                node.frequency += 1
                return
            node = node.next

        new_node = BSTNode(word)
        new_node.next = self.hash_table[index]
        self.hash_table[index] = new_node

        self.bst_root = self._bst_insert(self.bst_root, word)
        self._trie_insert(self.trie_root, word)

    def get_word_frequency(self, word):
        index = self._hash_function(word)

        node = self.hash_table[index]
        while node:
            if node.word == word.lower():
                return node.frequency
            node = node.next

        return 0

    def get_total_word_count(self):
        return self.bst_root.frequency if self.bst_root else 0


def main():
    hybrid_data_structure = HybridDataStructure()

    text = """The English language is a fascinating and versatile means of communication. It is spoken by millions of people around the world and serves as a common language for business, education, travel, and more. English has a rich vocabulary and a complex grammar structure that allows for the expression of a wide range of ideas and concepts.

    In addition to its practical uses, English is also a literary powerhouse, with a vast body of literature spanning centuries. From the works of William Shakespeare to contemporary novels, poetry, and plays, English literature offers a window into the human experience and the power of storytelling.

    Learning English opens up a world of opportunities. It enables individuals to connect with people from different cultures, access a wealth of knowledge through books and online resources, and pursue higher education or career prospects in English-speaking countries.

    Moreover, English has become the lingua franca of the internet, with a significant portion of online content available in English. Whether browsing websites, engaging in social media, or accessing global news and information, proficiency in English allows individuals to navigate the digital world with ease.

    Overall, English is a language of immense importance and influence. Its widespread usage and versatility make it a valuable skill to acquire, whether for personal or professional purposes. So, embrace the learning journey and unlock the doors that fluency in English can open!"""

    words = text.lower().split()
    for word in words:
        hybrid_data_structure.insert_word(word)

    print("Word Frequency Counting Program:")
    print("Enter a word to find its frequency or type 'exit' to quit.")

    while True:
        user_input = input("Word: ")
        if user_input == 'exit':
            break

        frequency = hybrid_data_structure.get_word_frequency(user_input)
        print(f"The word '{user_input}' appears {frequency} times.")

    total_word_count = hybrid_data_structure.get_total_word_count()
    print(f"\nTotal word count: {total_word_count}")


if __name__ == "__main__":
    main()
