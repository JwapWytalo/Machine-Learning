import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('Credit.csv')
print(base_credit.head(10))


print(np.unique(base_credit['default'], return_counts=True))
sns.countplot(base_credit['default'])
plt.show()
plt.hist(x=base_credit['age'])
plt.show()
plt.hist(x = base_credit['income']);
plt.show()
plt.hist(x = base_credit['loan_amnt']);
plt.show()

grafico = px.scatter(base_credit, x='age', y='income')
grafico.show()

grafico = px.scatter_matrix(base_credit,
                            dimensions=['age', 'income'],
                            color='default')
grafico.show()


