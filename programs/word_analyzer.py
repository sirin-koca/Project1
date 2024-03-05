from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def main():
    # Sample text
    text = ("This is a book about Natural Language Processing. By natural language we mean a language that is used "
            "for everyday communication by humans; languages like English, Hindi or Portuguese. In contrast to "
            "artificial languages such as programming languages and mathematical notations, natural languages have "
            "evolved as they pass from generation to generation, and are hard to pin down with explicit rules. We "
            "will take Natural Language Processing — or NLP for short — in a wide sense to cover any kind of computer "
            "manipulation of natural language. At one extreme, it could be as simple as counting word frequencies to "
            "compare different writing styles. At the other extreme, NLP involves understanding complete human "
            "utterances, at least to the extent of being able to give useful responses to them. Technologies based on "
            "NLP are becoming increasingly widespread. For example, phones and handheld computers support predictive "
            "text and handwriting recognition; web search engines give access to information locked up in "
            "unstructured text; machine translation allows us to retrieve texts written in Chinese and read them in "
            "Spanish; text analysis enables us to detect sentiment in tweets and blogs. By providing more natural "
            "human-machine interfaces, and more sophisticated access to stored information, language processing has "
            "come to play a central role in the multilingual information society.")

    # Tokenize and remove stopwords
    tokens = word_tokenize(text.lower())
    filtered_words = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]

    # Count and get most common words
    word_counts = Counter(filtered_words)
    common_words = word_counts.most_common(5)

    # Print the most common words
    print("Most common words in this text are: ", common_words)


if __name__ == '__main__':
    main()
