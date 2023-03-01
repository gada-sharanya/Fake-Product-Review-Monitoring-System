# Fake-Product-Review-Monitoring-System



Sentiment analysis is a subfield of natural language processing (NLP) that focuses on identifying and extracting subjective information from textual data. In other words, sentiment analysis aims to determine the emotional tone or attitude expressed in a piece of text, whether it is positive, negative, or neutral. Sentiment analysis can be used in a variety of contexts, including customer feedback analysis, social media monitoring, and market research.

There are different approaches to sentiment analysis, including rule-based, machine learning-based, and hybrid approaches that combine both. Rule-based methods rely on a set of predefined rules to identify sentiment, while machine learning-based methods use algorithms to learn from data and make predictions. Hybrid approaches combine the strengths of both methods.

**POLARITY**

In the context of sentiment analysis, polarity refers to the sentiment expressed in a piece of text, which can be either positive, negative, or neutral. Negative polarity refers to the expression of negative sentiment, such as sadness, anger, or disappointment, while positive polarity refers to the expression of positive sentiment, such as happiness, excitement, or satisfaction.

The determination of polarity in sentiment analysis is usually based on the analysis of words and phrases that convey positive or negative emotions. For example, words like "great," "amazing," and "fantastic" are often associated with positive polarity, while words like "terrible," "horrible," and "awful" are often associated with negative polarity.

The polarity of a piece of text can have important implications for businesses and organizations, as it can indicate customer satisfaction or dissatisfaction, which in turn can impact brand reputation and customer loyalty. Therefore, sentiment analysis that accurately identifies polarity can be a valuable tool for businesses and organizations looking to better understand their customers' attitudes and emotions.


In this project, I have Multinomail Naive bayes using 5-fold Cross validation.Thereafter, I adopted Machine-learning based sentiment analysis and classified the product reviews as Truthful review and Deceptive Review using polarity. If the polarity of text is identified as a negative polarity by the "Naive Bayes" algorithm the review is termed as deceptive review else it is a truthful review.


Multinomial Naive Bayes is a machine learning algorithm used for text classification tasks such as document classification, spam filtering, and sentiment analysis. It is a variant of the Naive Bayes algorithm that is suitable for discrete data, where the input features are discrete counts, such as word frequencies in a document.

The algorithm works by calculating the probability of a document belonging to a certain class (e.g. spam or ham), given the frequencies of each word in the document. The probability is calculated using Bayes' theorem, which states that the probability of a hypothesis (class) given some observed evidence (word frequencies) is proportional to the product of the prior probability of the hypothesis (class) and the likelihood of the evidence given the hypothesis (class).

The "naive" part of the algorithm comes from the assumption that the features (word frequencies) are independent of each other, which is not always true in practice. However, this assumption simplifies the calculation of the probability and makes the algorithm computationally efficient.
