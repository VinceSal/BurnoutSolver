from scheduler.load_model import load_burnout_model
from scheduler.predictor import predict_burnout_risk
from scheduler.optimizer import optimize_schedule
import pandas as pd

# 1. Carica i dati
tasks = pd.read_csv("data/tasks.csv")

# 2. Carica modello, scaler e feature names
model, scaler, feature_names = load_burnout_model("model.pkl")

# 3. Calcola il rischio burnout iniziale
tasks = predict_burnout_risk(model, tasks, scaler, feature_names)

# Controlla se qualcuno è in burnout
burned_initial = tasks[tasks["rischio_burnout"] > 0.7]
if burned_initial.empty:
    print("🔥 Nessuno è in burnout inizialmente.")
else:
    print("🔥 Dipendenti in burnout inizialmente:")
    print(burned_initial[["Name", "JobRole", "Task", "rischio_burnout"]])

# 4. Rischedula i task per ridurre il burnout a livello di team
new_schedule = optimize_schedule(tasks, max_risk=0.7)

# 5. Ricalcola il rischio burnout dopo la nuova pianificazione
new_schedule = predict_burnout_risk(model, new_schedule, scaler, feature_names)

# Controlla se qualcuno è in burnout dopo la nuova pianificazione
burned_after = new_schedule[new_schedule["rischio_burnout"] > 0.7]
if burned_after.empty:
    print("📅 Nessuno è in burnout dopo la nuova pianificazione.")
else:
    print("📅 Dipendenti in burnout dopo la nuova pianificazione:")
    print(burned_after[["Name", "JobRole", "Task", "rischio_burnout"]])

# 6. Verifica se è cambiato qualcosa
if tasks["rischio_burnout"].equals(new_schedule["rischio_burnout"]):
    print("ℹ️ Nessun cambiamento nei valori di burnout.")
else:
    print("ℹ️ I valori di burnout sono cambiati dopo la pianificazione.")
