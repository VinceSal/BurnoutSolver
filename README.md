<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BurnoutSolver - Predict to Decide</title>
  <style>
    body {
      font-family: 'Segoe UI', Roboto, Arial, sans-serif;
      background-color: #f5f7fa;
      color: #222;
      margin: 0;
      padding: 0;
      line-height: 1.6;
    }
    header {
      background: linear-gradient(135deg, #004aad, #00c2a8);
      color: white;
      padding: 2rem;
      text-align: center;
    }
    h1, h2, h3 {
      color: #004aad;
    }
    h1 {
      font-size: 2.2em;
      margin-bottom: 0.4em;
    }
    h2 {
      margin-top: 1.5em;
      border-left: 5px solid #00c2a8;
      padding-left: 10px;
    }
    section {
      max-width: 900px;
      margin: 2rem auto;
      background: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    ul {
      margin-top: 0.5rem;
    }
    li {
      margin-bottom: 0.5rem;
    }
    .highlight {
      color: #00a884;
      font-weight: bold;
    }
    .emoji {
      font-size: 1.3em;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #004aad;
      color: white;
    }
    footer {
      text-align: center;
      color: #777;
      font-size: 0.9em;
      padding: 2rem 0;
    }
    a {
      color: #0070c9;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    blockquote {
      background: #eef5fb;
      border-left: 5px solid #00c2a8;
      margin: 1.5rem 0;
      padding: 1rem 1.5rem;
      font-style: italic;
      color: #444;
    }
  </style>
</head>

<body>

  <header>
    <h1>🧠 BurnoutSolver</h1>
    <p><strong>Predict to Decide — Ottimizzare l’efficienza operativa con l’AI</strong></p>
    <p>Progetto presentato da <strong>iParthenope Team</strong> durante <em>The Big Hack – Special Edition (25-26 Ottobre 2026)</em></p>
  </header>

  <section>
    <h2>📄 Challenge aziendale: Crédit Agricole – “Predict to Decide”</h2>
    <h3>Contesto e obiettivo</h3>
    <p>In molte organizzazioni, attività operative cruciali sono rallentate da processi ripetitivi, silos informativi, tempi di risposta lunghi e assenza di visione predittiva.</p>
    <p>Le aziende coinvolte evidenziano fabbisogni concreti:</p>
    <ul>
      <li>Ridurre errori umani e automatizzare notifiche e validazioni</li>
      <li>Gestire i turni HR in modo più efficiente</li>
      <li>Snellire flussi logistici e ottimizzare la pianificazione della produzione</li>
      <li>Accedere rapidamente a dati e report per decisioni strategiche</li>
      <li>Eliminare attività a basso valore aggiunto per liberare tempo e risorse</li>
    </ul>
    <p>L’Intelligenza Artificiale, unita a strumenti di analisi e visualizzazione avanzata, può fornire <strong>previsioni affidabili e supporto decisionale in tempo reale</strong>.</p>
  </section>

  <section>
    <h2>🎯 Richiesta della Challenge</h2>
    <p>Progettare una soluzione digitale basata su <strong>strumenti predittivi e decisionali intelligenti</strong> (AI, ML, forecasting, dashboard interattive) che permetta a un’organizzazione di:</p>
    <ul>
      <li>Prevedere eventi critici o colli di bottiglia</li>
      <li>Migliorare l’efficienza in una fase operativa concreta (logistica, amministrazione, HR, ecc.)</li>
      <li>Supportare decisioni in modo tempestivo e visuale</li>
    </ul>
    <p><strong>Obiettivo:</strong> dimostrare come l’AI possa trasformare dati e flussi in <em>insight operativi</em>, riducendo costi, errori e tempi.</p>
  </section>

  <section>
    <h2>💡 Soluzione proposta: BurnoutSolver</h2>
    <h3>Visione</h3>
    <p>Il burnout lavorativo colpisce quasi il <strong>30% dei lavoratori</strong>, causando perdite economiche stimate in <strong>88,5 miliardi di euro l’anno</strong>.</p>
    <p>Nel settore bancario, <strong>oltre l’80%</strong> dei dipendenti soffre di ansia legata agli obiettivi. Prevenire il burnout conviene — e BurnoutSolver lo rende possibile.</p>
  </section>

  <section>
    <h2>⚙️ Come funziona</h2>

    <h3>1️⃣ Raccolta e analisi dei dati</h3>
    <p>Il sistema analizza dati HR storici e correnti provenienti da:</p>
    <ul>
      <li>Ore lavorate in sede e da remoto</li>
      <li>Straordinari e assenze</li>
      <li>Livelli di stress e soddisfazione (survey interne)</li>
      <li>Carichi di lavoro e performance</li>
    </ul>
    <p>Dataset di riferimento: <a href="https://www.kaggle.com/datasets/ankam6010/synthetic-hr-burnout-dataset" target="_blank">Synthetic HR Burnout Dataset (Kaggle)</a></p>

    <h3>2️⃣ Modello predittivo</h3>
    <p>Un modello di <strong>Machine Learning supervisionato</strong> (Random Forest / XGBoost) stima la probabilità di burnout per ogni dipendente.</p>
    <p>L’algoritmo classifica il rischio in <strong>Basso / Medio / Alto</strong> e aggiorna le previsioni in tempo reale.</p>

    <h3>3️⃣ Dashboard interattiva</h3>
    <p>Una dashboard HR (Streamlit / React + Chart.js) mostra:</p>
    <ul>
      <li>Rischio burnout per dipendente e reparto</li>
      <li>Trend settimanali e mensili</li>
      <li>Indicatori di stress aggregati</li>
      <li>Raccomandazioni operative personalizzate</li>
    </ul>

    <h3>4️⃣ Motore di ottimizzazione</h3>
    <p>Il sistema propone <strong>nuove schedulazioni di lavoro</strong> ottimizzate per ridurre lo stress complessivo, bilanciando carichi e turni in base ai vincoli HR.</p>
  </section>

  <section>
    <h2>📈 Impatto e risultati attesi</h2>
    <ul>
      <li>🔻 <strong>-20%</strong> di assenze</li>
      <li>🔻 <strong>-30%</strong> di turnover</li>
      <li>🔺 <strong>+10–15%</strong> di produttività</li>
    </ul>
    <p>Per un’azienda di 1.000 dipendenti, ciò equivale a <strong>2–3 milioni di euro risparmiati ogni anno</strong>.</p>
  </section>

  <section>
    <h2>🧰 Stack Tecnologico</h2>
    <table>
      <tr><th>Categoria</th><th>Strumento</th></tr>
      <tr><td>Dataset</td><td>Kaggle – Synthetic HR Burnout Dataset</td></tr>
      <tr><td>Analisi dati</td><td>Python (Pandas, NumPy, Scikit-learn)</td></tr>
      <tr><td>Modellazione</td><td>Random Forest / XGBoost</td></tr>
      <tr><td>Backend / API</td><td>Flask</td></tr>
      <tr><td>Frontend</td><td>HTML, CSS, JavaScript, Streamlit</td></tr>
      <tr><td>Dashboard / Visual</td><td>Chart.js, Plotly</td></tr>
      <tr><td>Versioning</td><td>Git / GitHub</td></tr>
      <tr><td>Deploy</td><td>Streamlit Cloud / Docker</td></tr>
    </table>
  </section>

  <section>
    <h2>🔒 Valore aggiunto</h2>
    <ul>
      <li><strong>Etico e human-centered:</strong> l’AI supporta, non sostituisce le decisioni HR</li>
      <li><strong>Scalabile:</strong> adattabile a diversi settori</li>
      <li><strong>Predittivo + correttivo:</strong> propone soluzioni, non solo analisi</li>
      <li><strong>Data-driven:</strong> ogni scelta nasce da evidenze quantitative</li>
    </ul>
  </section>

  <section>
    <h2>👥 Team iParthenope</h2>
    <p>Un team multidisciplinare di sviluppatori, data scientist e designer, con l’obiettivo di dimostrare come l’AI possa migliorare la vita lavorativa e l’efficienza aziendale.</p>
  </section>

  <section>
    <h2>🚀 Conclusione</h2>
    <blockquote>
      BurnoutSolver dimostra che prevenire il burnout non è solo una scelta etica, ma una strategia di efficienza e profitto.  
      L’intelligenza artificiale diventa un alleato del benessere umano, capace di trasformare dati in decisioni e decisioni in valore.
    </blockquote>
  </section>

  <footer>
    <p>© 2026 iParthenope Team — The Big Hack Special Edition</p>
  </footer>

</body>
</html>
