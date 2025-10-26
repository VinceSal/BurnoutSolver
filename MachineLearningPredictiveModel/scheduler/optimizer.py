import pandas as pd
import numpy as np

def optimize_schedule(tasks: pd.DataFrame, max_risk: float = 0.7) -> pd.DataFrame:
    """
    Rischedula i task bilanciando il rischio burnout all'interno dei team.
    Se un membro supera max_risk, ridistribuisce i task di tutto il team (stesso JobRole).
    """
    new_tasks = tasks.copy()
    
    # Identifica i team con membri ad alto rischio
    high_risk_members = new_tasks[new_tasks["rischio_burnout"] > max_risk]
    affected_roles = high_risk_members["JobRole"].unique()

    for role in affected_roles:
        team = new_tasks[new_tasks["JobRole"] == role]
        if team.empty:
            continue
        
        # Ordina i task per livello e randomizza leggermente
        tasks_list = team["TaskScore"].tolist()
        np.random.shuffle(tasks_list)
        
        # Riassegna i task al team in modo bilanciato
        for i, idx in enumerate(team.index):
            new_tasks.loc[idx, "TaskScore"] = tasks_list[i % len(tasks_list)]
            print(f"🔄 {role} {new_tasks.loc[idx, 'Name']} assegnato task '{new_tasks.loc[idx, 'TaskScore']}'")

    return new_tasks
