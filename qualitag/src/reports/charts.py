import os
from io import BytesIO
from typing import Optional

import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud


class ChartReport:

    def __init__(self, stopwords: Optional[list[str]] = None):

        self.__stopwords = stopwords if stopwords else self.__read_stopwords()

    def __read_stopwords(self) -> list[str]:
        stopwords = []
        with open(
            os.path.join(os.path.dirname(__file__), "stopwords.txt"),
            "r",
            encoding="utf-8",
        ) as file:
            for line in file:
                stopwords.append(line.strip())
        return stopwords

    def wordcloud(self, text, **kwargs):
        return WordCloud(
            stopwords=self.__stopwords,
            background_color=kwargs.get("background_color", (255, 255, 255, 0)),
            mode=kwargs.get("mode", "RGBA"),
            colormap=kwargs.get("colormap", "Blues"),
            width=kwargs.get("width", 400),
            height=kwargs.get("height", 200),
            color_func=kwargs.get("color_func", None),
        ).generate(text)

    def most_common_tags(
        self, tags_count: dict[str, int], as_buffer: bool = False, **kwargs
    ):
        # Sort the tags_count dictionary by values in descending order
        sorted_tags = sorted(tags_count.items(), key=lambda x: x[1], reverse=True)

        # Get the top 7 most common tags
        top_tags = sorted_tags[:7]

        # Extract the tags and their counts
        tags = [tag for tag, _ in top_tags]
        counts = [count for _, count in top_tags]

        # Create a bar chart
        plt.bar(tags, counts, **kwargs)
        for i, tag in enumerate(tags):
            plt.text(
                tag, counts[i], f"{tags[i]}:\n{counts[i]}", ha="center", va="bottom"
            )
        plt.axis("off")

        # Save the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close('all')
        if as_buffer:
            return buffer

        # Create a PIL image from the buffer
        image = Image.open(buffer)

        # Return the PIL image
        return image
