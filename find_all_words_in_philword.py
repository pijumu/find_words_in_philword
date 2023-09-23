"""
Function that from the board of letters returns all words that exist in existing_words.
"""


class Trie:
    """
    Class that transform existing_words into trie.

    Methods
    -------
    has_word(word=str)
        Reply if there is a word in the trie.

    has_word_with_prefix(prefix=str)
        Reply if there is a prefix in the trie.

    add_word(word=str)
        Add a word into the trie.
    """

    def __init__(self):
        """
        Init SampleClass.
        """
        self.trie = {}

    def has_word(self, word):
        """
        Reply if there is a word in the trie.
        """

        trie_for_iterations = self.trie
        for char in word:
            if char not in trie_for_iterations:
                return False
            trie_for_iterations = trie_for_iterations.get(char)
        return "end" in trie_for_iterations

    def has_word_with_prefix(self, prefix):
        """
        Reply if there is a prefix in the trie.
        """

        trie_for_iterations = self.trie
        for char in prefix:
            if char not in trie_for_iterations:
                return False
            trie_for_iterations = trie_for_iterations.get(char)
        return True

    def add_word(self, word):
        """
        Add a word into the trie.
        """

        trie_for_iterations = self.trie
        for char in word:
            if char not in trie_for_iterations:
                trie_for_iterations[char] = {}
            trie_for_iterations = trie_for_iterations.get(char)
        trie_for_iterations["end"] = "end"


def node_neighbours(board, node):
    """
    Return node's neighbours from the board.
    """
    neighbours = []

    for neighbour in [[node[0], node[1]-1], [node[0], node[1]+1],
                      [node[0]-1, node[1]], [node[0]+1, node[1]]]:
        if neighbour[0] in range(len(board)) and neighbour[1] in range(len(board[0])):
            neighbours.append(neighbour)
    return neighbours


def dfs(board, node, trie, *, word=None, visited=None, existing_words=None):
    """
    Depth-first search.
    """
    if word is None and visited is None:
        word = []
        visited = []

    word.append(board[node[0]][node[1]])

    if node not in visited:
        prefix = ''.join(word)
        if trie.has_word(prefix):
            existing_words.append(prefix)
        visited.append(node)
        for neighbour in node_neighbours(board, node):
            if neighbour not in visited and trie.has_word_with_prefix(prefix):
                dfs(board, neighbour, trie, word=word, visited=visited,
                    existing_words=existing_words)

    word.pop()
    visited.pop()

    return existing_words


def find_words_in_philword(board, existing_words):
    """
    Return all words that exist in existing_words and in the board.
    """
    trie = Trie()
    found_words = []

    for word in existing_words:
        trie.add_word(word)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            found_words.extend(dfs(board, [i, j], trie, existing_words=[]))
    return list(set(found_words))
