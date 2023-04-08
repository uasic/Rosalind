path = "C:/Users/urska/Desktop/longevityHacks.xlsx"
from multiprocessing.sharedctypes import Value
import pandas as pd
All_hacks = pd.read_excel(path)

#print(All_hacks)

# risk scores for Karen:

Sleep = 0.15
Cognition = 0.56
Mood = 0.32
Vascular_health = 0.2
Cardiovascular_fitness = 0.28
Cardiorespiratory_fitness = 0.11
Heart_health = 0.15
Liver_function = 0.7
Glucose_metabolism = 0.8
Weight = 0.16
Vitamins = 0.68
Fat_metabolism = 0.4
Gut_inflammation = 0.46
General_inflammation = 0.68
Immune_system = 0.59
Bone_health = 0.86
Joint_health = 0.9
Muscle_health = 0.77

seznam_izbris = []

if Sleep < 0.25:
        
