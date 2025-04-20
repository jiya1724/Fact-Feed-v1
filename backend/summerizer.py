# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer

# def summarize_text(text, num_sentences=2):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, num_sentences)
#     return " ".join(str(sentence) for sentence in summary)

import nltk
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    # Tokenize the article into sentences
    sentences = sent_tokenize(text)

    # Edge case: If there are fewer sentences than the desired summary length
    if len(sentences) <= num_sentences:
        return text

    # Convert sentences into numerical vectors using TF-IDF
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences).toarray()

    # Compute cosine similarity between sentence vectors
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = np.dot(sentence_vectors[i], sentence_vectors[j]) / (
                    np.linalg.norm(sentence_vectors[i]) * np.linalg.norm(sentence_vectors[j]))

    # Build a graph and apply TextRank
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    # Rank sentences and select the top ones
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = " ".join([ranked_sentences[i][1] for i in range(min(num_sentences, len(ranked_sentences)))])
    return summary
