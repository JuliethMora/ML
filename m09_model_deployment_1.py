# Función de predicción adaptada
def predict_popularity(danceability):
    # Aquí deberías construir el DataFrame con todas las columnas que espera tu modelo
    # Por simplicidad, asumimos que el modelo espera solo la columna 'danceability'
    X = pd.DataFrame([[danceability]], columns=['danceability'])

    p1 = reg.predict(X)[0]

    return int(p1)
