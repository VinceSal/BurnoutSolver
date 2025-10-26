import pickle

def load_burnout_model(path: str):
    """
    Carica il modello ML addestrato con scaler e nomi delle feature.
    Restituisce (model, scaler, feature_names)
    """
    with open(path, 'rb') as f:
        model, scaler, feature_names = pickle.load(f)
    print("✅ Modello, scaler e nomi delle feature caricati con successo.")
    print("Colonne attese dal modello:")
    for i, col in enumerate(feature_names):
        print(f"{i+1}. {col}")
    return model, scaler, feature_names
