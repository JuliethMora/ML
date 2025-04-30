import gdown
import joblib
import pandas as pd
import sys
import os
import requests

# Función para transformar el parametro URL en el formato esperado por el modelo
def predict_popularity(url):

    reg = gdown.download('https://drive.google.com/file/d/1oy3QMpwGA23a_Aeg2DAxAIRAu5oztWCm/view?usp=drive_link','stack_model.pkl', 
                    quiet = False)
    #reg = joblib.load('stack_model.pkl') 
    # Realizar la solicitud GET
    response = requests.get(url)
    data = response.json()

    # Extraer las filas del JSON
    rows = [row["row"] for row in data["rows"]]

    # Crear el DataFrame
    url_ = pd.DataFrame(rows)

    # Verificar las columnas disponibles
    print("Columnas disponibles:", url_.columns)
    
    #url_ = pd.DataFrame([url], columns=['track_id'])
    #print("Columnas disponibles:", url_.columns)

        
    #duration_ms = pd.read_csv('duration_ms.csv')
    explicit_cat = pd.read_csv('explicit.csv')
    danceability_cat = pd.read_csv('danceability.csv')
    energy_cat = pd.read_csv('energy.csv')
    key_cat = pd.read_csv('key.csv')
    #loudness = pd.read_csv('loudness.csv')
    mode_cat = pd.read_csv('mode.csv')
    speechiness_cat = pd.read_csv('speechiness.csv')
    acousticness_cat = pd.read_csv('acousticness.csv')
    #track_genre_encoded = pd.read_csv('track_genre_encoded.csv')

    url_["explicit"] = (url_["explicit"]).astype(int)
    url_["danceability"] = (url_["danceability"]).astype(float)
    url_["energy"] = (url_["energy"]).astype(float)
    url_["key"] = (url_["key"]).astype(int)
    url_["mode"] = (url_["mode"]).astype(int)
    url_["speechiness"] = (url_["speechiness"]).astype(float)
    url_["acousticness"] = (url_["acousticness"]).astype(float)

    #'duration_ms', 'loudness', 'track_genre_encoded''instrumentalness', 'liveness','valence', 'tempo', 'time_signature'
    
    
    
    url_ = url_.join(explicit_cat.set_index("explicit"), on="explicit")
    url_ = url_.join(danceability_cat.set_index("danceability"), on="danceability")
    url_ = url_.join(energy_cat.set_index("energy"), on="energy")
    url_ = url_.join(key_cat.set_index("key"), on="key")
    url_ = url_.join(mode_cat.set_index("mode"), on="mode")
    url_ = url_.join(speechiness_cat.set_index("speechiness"), on="speechiness")
    url_ = url_.join(acousticness_cat.set_index("acousticness"), on="acousticness")
    
    dumm_cols = [ 'explicit', 'danceability', 'energy', 'key', 'mode',
       'speechiness', 'acousticness']
    
    dumm = pd.DataFrame({i+"_"+str(int(url_[i][0])):[1] for i in dumm_cols})
    url_ = url_.join(dumm)
    cols = url_.select_dtypes(include=['object']).columns
    url_.drop(cols, axis=1, inplace=True)
    url_.drop(dumm_cols, axis=1, inplace=True)
    url_ = pd.concat([dataTraining.columns,url_]).fillna(0)
    url_ = url_.iloc[1:]

    #  prediction
    p1 = reg.predict(url_)[0]
    return p1

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add an URL')
        
    else:

        url = sys.argv[1]

        p1 = predict_popularity(url)
        
        print(url)
        print('Prediction: ', p1)
        
