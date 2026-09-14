---
title: Ghid Național IRIS — Indicații RadioImagistice Structurate
hide:
  - toc
---

# Ghid Național IRIS — Indicații RadioImagistice Structurate

<div class="iris-official-banner">
  <div class="iris-official-badge">🏛️ REFERINȚĂ PRIMARĂ OFICIALĂ</div>
  <p class="iris-official-desc">
    Conținut adaptat după <strong>Ghidul de utilizare a investigațiilor radiologice și imagistice medicale</strong>, aprobat prin <strong>Ordinul Ministerului Sănătății nr. 1342/2012</strong>, elaborat pe baza criteriilor de recomandare imagistică ale Comisiei Europene și Societății Europene de Radiologie (ESR).
  </p>
  <div class="iris-official-links">
    <a href="https://radiologie-pediatrica.ro/iris/" target="_blank" rel="noopener" class="md-button md-button--primary">
      Lansează Aplicația Oficială IRIS (PWA) ↗
    </a>
    <a href="../ct/compare/" class="md-button">
      Compară Protocoale CT
    </a>
  </div>
</div>

=== "🔍 Explorer Interactiv IRIS (Integrat Offline)"

    <div class="iris-role-explainer">
      <div class="role-card iris-card-hl">
        <span class="role-icon">🩺</span>
        <div>
          <strong>1. Ghidul IRIS (Decizie Primară)</strong>
          <p>Răspunde la: <em>Ce investigație este indicată pentru acest tablou clinic (CT, RMN, Ecografie, Rx), cu ce grad de recomandare și ce doză de iradiere?</em></p>
        </div>
      </div>
      <div class="role-arrow">➔</div>
      <div class="role-card ct-card-hl">
        <span class="role-icon">⚡</span>
        <div>
          <strong>2. Ghidul Protocoalelor CT (Execuție Tehnică)</strong>
          <p>Răspunde la: <em>Cum se achiziționează scanarea CT indicată (faze de contrast, bolus tracking, timpi, parametri kV, mAs, AEC și reconstrucții)?</em></p>
        </div>
      </div>
    </div>

    <!-- Aplicația interactivă IRIS generată de iris-browser.js -->
    <div id="iris-explorer-app"></div>

=== "📱 Aplicația Web PWA IRIS (Live)"

    <div class="iris-pwa-container">
      <div class="iris-pwa-bar">
        <span>🌐 Conectat la <strong>https://radiologie-pediatrica.ro/iris/</strong></span>
        <a href="https://radiologie-pediatrica.ro/iris/" target="_blank" rel="noopener" class="iris-open-external-btn">
          Deschide pe tot ecranul ↗
        </a>
      </div>
      <iframe 
        src="https://radiologie-pediatrica.ro/iris/" 
        class="iris-embedded-frame" 
        title="Aplicația Web IRIS Oficială"
        loading="lazy">
      </iframe>
    </div>

=== "📖 Metodologie & Clase de Iradiere (Ordinul MS 1342/2012)"

    ### Gradele de Recomandare Clinică

    Recomandările din Ghidul Național sunt clasificate în funcție de calitatea dovezilor științifice disponibile:

    | Grad Recomandare | Nivel de Dovezi Științifice | Semnificație Clinică |
    |:----------------:|:----------------------------|:---------------------|
    | <span class="iris-grade-pill grade-a">GRAD A</span> | Studii clinice randomizate controlate de înaltă calitate, meta-analize, revizuiri sistematice solide. | Indicație ferm susținută științific; prima linie de investigare. |
    | <span class="iris-grade-pill grade-b">GRAD B</span> | Studii experimentale sau caz-control bine concepute; extrapolări robuste din studii de nivel superior. | Indicație valoroasă, recomandată în scenariile clinice specificate. |
    | <span class="iris-grade-pill grade-c">GRAD C</span> | Consens al comisiilor de experți, rapoarte de caz, opinii ale societăților științifice internaționale. | Utilă în situații particulare sau când modalitățile de primă intenție sunt neconcludente. |

    ---

    ### Scara Dozelor de Iradiere & Principiul ALARA

    Ghidul utilizează simboluri de doze pentru a asigura respectarea principiului **ALARA** (*As Low As Reasonably Achievable*):

    | Simbol Doză | Clasă de Iradiere | Doză Efectivă Estimată | Exemple de Investigații |
    |:-----------:|:-----------------|:----------------------|:------------------------|
    | <span class="iris-dose-pill dose-0">○○○○</span> | **Clasa 0 (Nulă)** | 0 mSv (fără radiații ionizante) | Ecografie (US), Rezonanță Magnetică (RMN/IRM) |
    | <span class="iris-dose-pill dose-1">●○○○</span> | **Clasa 1 (Minimă)** | sub 1 mSv | Radiografie toracică (Rx), Radiografii periferice |
    | <span class="iris-dose-pill dose-2">●●○○</span> | **Clasa 2 (Foarte mică)** | 1 – 5 mSv | Radiografii coloană/bazin, Scintigrafii tiroidiene |
    | <span class="iris-dose-pill dose-3">●●●○</span> | **Clasa 3 (Moderată)** | 5 – 10 mSv | CT Torace, CT Abdomen nativ, Uro-CT |
    | <span class="iris-dose-pill dose-4">●●●●</span> | **Clasa 4 (Ridicată)** | peste 10 mSv | CT Abdomen-Pelvis multifazic, CT Angiografie completă, PET-CT |

    !!! tip "Recomandare de Bună Practică"
        La pacienții pediatrici și la femeile tinere, dacă Ghidul IRIS indică **Ecografia** sau **RMN** cu aceeași acuratețe diagnostică ca și CT-ul, investigația fără radiații ionizante are întotdeauna prioritate absolută.
