
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

# Load the data
file_path = 'weeklydata.csv'
data = pd.read_csv(file_path)

# Transformations
# Log transformation for NLTK_Negative and NLTK_Positive
data['NLTK_Negative_Log'] = np.log(data['NLTK_Negative'] + 0.01)
data['NLTK_Positive_Log'] = np.log(data['NLTK_Positive'] + 0.01)

# Adjusting FlairPolarity for Box-Cox Transformation
data['FlairPolarity_Transformed'] = data['FlairPolarity'] / 2 + 0.5
data['FlairPolarity_BoxCox'], _ = stats.boxcox(data['FlairPolarity_Transformed'])

# Check if NLTK_Compound is positive for Box-Cox Transformation
compound_positive = all(data['NLTK_Compound'] > 0)
if compound_positive:
    data['NLTK_Compound_BoxCox'], _ = stats.boxcox(data['NLTK_Compound'])
else:
    data['NLTK_Compound_BoxCox'] = data['NLTK_Compound']

# Fitting the linear regression model
X_transformed = data[['NLTK_Negative_Log', 'NLTK_Neutral', 'NLTK_Positive_Log', 'NLTK_Compound_BoxCox']]
X_transformed = sm.add_constant(X_transformed)
model = sm.OLS(data['FlairPolarity_BoxCox'], X_transformed).fit()

# Model summary
print(model.summary())

# Correlation matrix and heatmap
corr = data[['FlairPolarity_BoxCox', 'NLTK_Negative_Log', 'NLTK_Neutral', 'NLTK_Positive_Log', 'NLTK_Compound_BoxCox']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
