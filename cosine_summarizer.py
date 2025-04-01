import nltk
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    # Tokenize the article into sentences
    sentences = sent_tokenize(text)
    
    # Convert sentences into numerical vectors using TF-IDF
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences).toarray()
    
    # Compute cosine similarity between sentence vectors
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            similarity_matrix[i][j] = np.dot(sentence_vectors[i], sentence_vectors[j]) / (
                np.linalg.norm(sentence_vectors[i]) * np.linalg.norm(sentence_vectors[j]))

    # Build a graph and apply TextRank (PageRank for sentences)
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    # Rank sentences and select the top ones
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = " ".join([ranked_sentences[i][1] for i in range(min(num_sentences, len(ranked_sentences)))])

    return summary

# Example usage
news_article = """With global temperatures rising at an unprecedented rate, climate scientists from around the world have issued a stark warning about the acceleration of climate change. A recent report released by the Intergovernmental Panel on Climate Change (IPCC) indicates that 2024 was the hottest year on record, surpassing previous highs set in 2016 and 2020.

The report states that carbon dioxide (CO₂) levels have reached 421 parts per million (ppm), the highest in human history, primarily due to fossil fuel combustion and deforestation. Scientists emphasize that unless drastic reductions in greenhouse gas emissions are implemented, the world is likely to exceed 1.5°C of warming within the next two decades, leading to catastrophic consequences.

Extreme weather events such as hurricanes, droughts, and wildfires have become more frequent and intense, causing widespread destruction. Countries like the United States, Australia, and India have experienced record-breaking heatwaves, resulting in agricultural losses, water shortages, and health crises.

Governments have been urged to take immediate action by transitioning to renewable energy sources such as solar and wind power, enforcing stricter emission regulations, and investing in climate adaptation strategies. The United Nations has also called for wealthier nations to provide financial aid to developing countries most affected by climate change.

Despite growing awareness, many nations continue to struggle with policy implementation due to economic interests and political resistance. Climate activists and organizations are advocating for more aggressive action, stressing that the current efforts are insufficient to prevent irreversible damage.

The IPCC report concludes with a call for global cooperation, emphasizing that without a collective effort, climate change will continue to accelerate, posing a severe threat to ecosystems, biodiversity, and human civilization.
"""
summary = summarize_text(news_article, num_sentences=2)
print("Summary:", summary)
