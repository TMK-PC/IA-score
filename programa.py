import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
    
codificar = LabelEncoder()
    
ia = joblib.load('Configurações/modelo_treinado.pkl')
    

novos_clientes = pd.read_excel('Dados/novos_clientes.xlsx')





for coluna in novos_clientes:
    if novos_clientes[coluna].dtype == 'object' and coluna != 'score_credito':
        novos_clientes[coluna] = codificar.fit_transform(novos_clientes[coluna])
    
novos_clientes['mix_credito'] = ia.predict(novos_clientes)
novos_clientes.to_excel('Dados/novos_clientes_com_score.xlsx', index=False)