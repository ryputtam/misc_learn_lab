

# Import necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define the text
text = """
Machine Learning, Statistics, Analytics, Pyspark, lambda, sparkMLlib, power analysis, Data Science, Algorithm, Model, Regression, Classification, Clustering, Neural Networks, Deep Learning, Supervised Learning, Unsupervised Learning, Data Mining, Big Data, Predictive Analytics, Descriptive Statistics, Inferential Statistics, Data Visualization, Feature Engineering, Data Preprocessing, Overfitting, Underfitting, Cross-Validation, Training Set, Test Set, Validation Set, Hyperparameter Tuning, Gradient Descent, Decision Trees, Random Forest, Support Vector Machine, K-Nearest Neighbors, Principal Component Analysis, Natural Language Processing, Time Series Analysis, Bayesian Statistics, Hypothesis Testing, Correlation, Causation, Data Cleaning, Data Wrangling, ETL (Extract, Transform, Load), SQL, Python, R, TensorFlow, PyTorch, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
"""

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()