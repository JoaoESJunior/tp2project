# -*- coding: utf-8 -*-
import pandas as pd
import pickle
import os

dataset_path = "/home/datasets/spotify/2023_spotify_ds1.csv"
model_path = "/home/joaojunior/project2-pv2/model.pickle"

print("Carregando o dataset...")
df = pd.read_csv(dataset_path)

print("Processando o dataset...")
df['track_name'] = df['track_name'].astype(str)
rules = df['track_name'].value_counts().to_dict()

print("Treinando o modelo...")
model = {'rules': rules}

print(f"Salvando o modelo em {model_path}...")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("Treinamento concluído!")
