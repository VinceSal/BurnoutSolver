import pandas as pd

def predict_burnout_risk(model, tasks: pd.DataFrame, scaler, feature_names) -> pd.DataFrame:
    """
    Calcola la probabilità di burnout per ciascun dipendente-task
    usando il modello addestrato con scaler.
    """
    # Crea le dummy variables
    X = pd.get_dummies(tasks, drop_first=True)
    
    # Allinea le colonne con quelle usate in addestramento
    X = X.reindex(columns=feature_names, fill_value=0)
    
    # Applica lo scaler
    X_scaled = scaler.transform(X)
    
    # Calcola la probabilità di burnout
    tasks["rischio_burnout"] = model.predict_proba(X_scaled)[:, 1]
    return tasks
