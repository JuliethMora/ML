import gdown
import joblib
import pandas as pd
import sys
import os

# Función para transformar el parametro URL en el formato esperado por el modelo
def predict_popularity(url):

    reg = gdown.download('https://drive.google.com/file/d/1oy3QMpwGA23a_Aeg2DAxAIRAu5oztWCm/view?usp=drive_link','stack_model.pkl', 
                    quiet = False)
    #reg = joblib.load('stack_model.pkl') 

    url_ = pd.DataFrame([url], columns=['song'])

        
    #duration_ms = pd.read_csv('duration_ms.csv')
    explicit = pd.read_csv('explicit.csv')
    danceability = pd.read_csv('danceability.csv')
    energy = pd.read_csv('energy.csv')
    key = pd.read_csv('key.csv')
    #loudness = pd.read_csv('loudness.csv')
    mode = pd.read_csv('mode.csv')
    speechiness = pd.read_csv('speechiness.csv')
    acousticness = pd.read_csv('acousticness.csv')
    #track_genre_encoded = pd.read_csv('track_genre_encoded.csv')

    url_["explicit"] = int(url_["explicit"])
    url_["danceability"] = float(url_["danceability"])
    url_["energy"] = float(url_["energy"])
    url_["key"] = int(url_["key"])
    url_["mode"] = int(url_["mode"])
    url_["speechiness"] = float(url_["speechiness"])
    url_["acousticness"] = float(url_["acousticness"])

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
        
