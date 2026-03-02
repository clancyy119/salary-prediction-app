# This is an updated script for making predictions

import pickle

# Correcting the file path
with open('ML/saved_steps.pkl', 'rb') as file:
    model = pickle.load(file)
    
# The rest of the script follows...