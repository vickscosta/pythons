import string
from graph import Graph, Vertex
import random

def get_words_from_text(text_path):
    with open(text_path,'r',encoding='utf-8') as f:
        text=f.read()
        text=' '.join(text.split())
        text=text.lower()
        text=text.translate(str.maketrans('','',string.punctuation))

    words=text.split()
    return words

def make_graph(words):
    g=Graph()

    previous_word=None

    for word in words:
        word_vertex=g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word=word_vertex

    g.generate_probability_mappings()

    return g

def compose(g, words, lenght=50):
    composition=[]
    word=g.get_vertex(random.choice(words))

    for _ in range(lenght):
        composition.append(word.value)
        word=g.get_next_word(word)

    return composition


def main():
    words=get_words_from_text('Lusiadas.txt')
    g=make_graph(words)
    composition=compose(g, words,500)
    return ' '.join(composition)

if __name__ == '__main__':
    print()
    print()
    print(main())
    print()
    print()