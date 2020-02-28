#Author: Hasret Özkan
#Date: 2020
#Description: Pokemon Data Analyzing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./data/pokemon.csv')

#Water Type Pokemons
x = data[(data['Type 1']=='Water')]

#All Water Type Pokemons Name
for i in x['Name']:
    print('Water Type Pokemon: ', i)
print('#############')
    
#About All Water Type Pokemons
y = x.describe()
print('Most Water Type Pokemons Generations: ', y['Generation']['max'])
print('Least Water Type Pokemons Generations: ', y['Generation']['min'])
print('Most Water Type Pokemons Attack: ', y['Attack']['max'])
print('Least Water Type Pokemons Attack: ', y['Attack']['min'])
print('Most Water Type Pokemons Defense: ', y['Defense']['max'])
print('Least Water Type Pokemons Defense: ', y['Defense']['min'])
print('Most Water Type Pokemons HP: ', y['HP']['max'])
print('Least Water Type Pokemons HP: ', y['HP']['min'])
print('#############')

#Water Type Pokemons Analyze
y = x.describe()
print('HP Mean: ', y['HP']['mean'])
print('Attack Mean: ', y['Attack']['mean'])
print('Defence Mean: ', y['Defense']['mean'])
print('HP Median: ', y['HP']['50%'])
print('Attack Median: ', y['Attack']['50%'])
print('Defence Median: ', y['Defense']['50%'])
print('#############')
      
#Legendary Water Type Pokemons
legendarypokemons = data[(data['Type 1']=='Water') & (data['Legendary']==True)]

#Legendary Water Type Pokemons Name
for i in legendarypokemons['Name']:
    print('Legendary Water Type Pokemon: ', i)
print('#############')
      
#Water Type Pokemons Analyze
y = legendarypokemons.describe()
print('HP Mean: ', y['HP']['mean'])
print('Attack Mean: ', y['Attack']['mean'])
print('Defence Mean: ', y['Defense']['mean'])
print('HP Median: ', y['HP']['50%'])
print('Attack Median: ', y['Attack']['50%'])
print('Defence Median: ', y['Defense']['50%'])
print('#############')