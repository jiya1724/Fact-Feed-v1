from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

article = """With global temperatures rising at an unprecedented rate, climate scientists from around the world have issued a stark warning about the acceleration of climate change. A recent report released by the Intergovernmental Panel on Climate Change (IPCC) indicates that 2024 was the hottest year on record, surpassing previous highs set in 2016 and 2020.

The report states that carbon dioxide (CO₂) levels have reached 421 parts per million (ppm), the highest in human history, primarily due to fossil fuel combustion and deforestation. Scientists emphasize that unless drastic reductions in greenhouse gas emissions are implemented, the world is likely to exceed 1.5°C of warming within the next two decades, leading to catastrophic consequences.

Extreme weather events such as hurricanes, droughts, and wildfires have become more frequent and intense, causing widespread destruction. Countries like the United States, Australia, and India have experienced record-breaking heatwaves, resulting in agricultural losses, water shortages, and health crises.

Governments have been urged to take immediate action by transitioning to renewable energy sources such as solar and wind power, enforcing stricter emission regulations, and investing in climate adaptation strategies. The United Nations has also called for wealthier nations to provide financial aid to developing countries most affected by climate change.

Despite growing awareness, many nations continue to struggle with policy implementation due to economic interests and political resistance. Climate activists and organizations are advocating for more aggressive action, stressing that the current efforts are insufficient to prevent irreversible damage.

The IPCC report concludes with a call for global cooperation, emphasizing that without a collective effort, climate change will continue to accelerate, posing a severe threat to ecosystems, biodiversity, and human civilization."""

print(summarize_text(article))
