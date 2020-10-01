import pandas as pd 
import vega_datasets
import matplotlib.pyplot as plt

cr = vega_datasets.data.cars()

plot = plt.scatter(cr['Miles_per_Gallon'], cr['Weight_in_lbs'])

print(plot)