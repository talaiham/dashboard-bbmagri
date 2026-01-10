#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère un dashboard HTML statique à partir des fichiers Excel nettoyés
Usage: python generer_dashboard_html.py
"""

import pandas as pd
import json
import os
from datetime import datetime

def convertir_excel_en_json():
    """Convertit les fichiers Excel nettoyés en JSON pour le dashboard HTML"""
    data = {}
    
    # Convertir CLTFAM
    fichiers_cltfam = [f for f in os.listdir('.') if f.startswith('CLTFAM') and f.endswith('_clean.xlsx')]
    data['cltfam'] = []
    for fichier in fichiers_cltfam:
        try:
            df = pd.read_excel(fichier, sheet_name=0, skiprows=3)
            annee = fichier.replace('CLTFAM', '').replace('_clean.xlsx', '')
            df['Année'] = annee
            # Convertir en dict
            records = df.to_dict('records')
            # Convertir NaN en None pour JSON
            for record in records:
                for key, value in record.items():
                    if pd.isna(value):
                        record[key] = None
            data['cltfam'].extend(records)
            print(f"  [OK] {fichier}: {len(records)} lignes")
        except Exception as e:
            print(f"  [ERREUR] {fichier}: {e}")
    
    # Convertir CLTART
    fichiers_cltart = [f for f in os.listdir('.') if f.startswith('CLTART') and f.endswith('_clean.xlsx')]
    data['cltart'] = []
    for fichier in fichiers_cltart:
        try:
            df = pd.read_excel(fichier, sheet_name=0, skiprows=3)
            annee = fichier.replace('CLTART', '').replace('_clean.xlsx', '')
            df['Année'] = annee
            records = df.to_dict('records')
            for record in records:
                for key, value in record.items():
                    if pd.isna(value):
                        record[key] = None
            data['cltart'].extend(records)
            print(f"  [OK] {fichier}: {len(records)} lignes")
        except Exception as e:
            print(f"  [ERREUR] {fichier}: {e}")
    
    # Convertir STATARTFAM
    if os.path.exists('STATARTFAM_clean.xlsx'):
        try:
            df = pd.read_excel('STATARTFAM_clean.xlsx', sheet_name=0, skiprows=3)
            records = df.to_dict('records')
            for record in records:
                for key, value in record.items():
                    if pd.isna(value):
                        record[key] = None
            data['statartfam'] = records
            print(f"  [OK] STATARTFAM_clean.xlsx: {len(records)} lignes")
        except Exception as e:
            print(f"  [ERREUR] STATARTFAM_clean.xlsx: {e}")
            data['statartfam'] = []
    else:
        data['statartfam'] = []
    
    # Convertir STATARTART
    if os.path.exists('STATARTART_clean.xlsx'):
        try:
            df = pd.read_excel('STATARTART_clean.xlsx', sheet_name=0, skiprows=3)
            records = df.to_dict('records')
            for record in records:
                for key, value in record.items():
                    if pd.isna(value):
                        record[key] = None
            data['statartart'] = records
            print(f"  [OK] STATARTART_clean.xlsx: {len(records)} lignes")
        except Exception as e:
            print(f"  [ERREUR] STATARTART_clean.xlsx: {e}")
            data['statartart'] = []
    else:
        data['statartart'] = []
    
    return data


def generer_dashboard_html(data_json):
    """Génère le fichier HTML du dashboard"""
    
    # Calculer les KPI
    ca_total = 0
    marge_total = 0
    nb_commerciaux = 0
    nb_familles = 0
    nb_articles = 0
    
    if data_json.get('statartfam'):
        df_fam = pd.DataFrame(data_json['statartfam'])
        if 'CA Net HT' in df_fam.columns:
            ca_total = df_fam['CA Net HT'].sum() or 0
        if 'Marge' in df_fam.columns:
            marge_total = df_fam['Marge'].sum() or 0
        if 'Code Famille' in df_fam.columns:
            nb_familles = df_fam['Code Famille'].nunique()
    
    if data_json.get('statartart'):
        df_art = pd.DataFrame(data_json['statartart'])
        if 'Code Article' in df_art.columns:
            nb_articles = df_art['Code Article'].nunique()
    
    if data_json.get('cltfam'):
        df_cltfam = pd.DataFrame(data_json['cltfam'])
        if 'Commercial' in df_cltfam.columns:
            nb_commerciaux = df_cltfam['Commercial'].nunique()
    
    profitabilite = (marge_total / ca_total * 100) if ca_total > 0 else 0
    
    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Commercial BBM AGRI</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background: linear-gradient(135deg, #1F4E78 0%, #4472C4 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            opacity: 0.9;
            font-size: 1.1em;
        }}
        
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .kpi-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #4472C4;
        }}
        
        .kpi-card h3 {{
            color: #666;
            font-size: 0.9em;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}
        
        .kpi-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #1F4E78;
            margin-bottom: 5px;
        }}
        
        .kpi-card .delta {{
            color: #70AD47;
            font-size: 0.9em;
        }}
        
        .filters {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .filters h3 {{
            margin-bottom: 15px;
            color: #1F4E78;
        }}
        
        .filter-group {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}
        
        .filter-group select {{
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1em;
            min-width: 200px;
        }}
        
        .tabs {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid #ddd;
        }}
        
        .tab {{
            padding: 15px 30px;
            background: #f0f0f0;
            border: none;
            cursor: pointer;
            font-size: 1em;
            border-radius: 5px 5px 0 0;
            transition: all 0.3s;
        }}
        
        .tab.active {{
            background: #1F4E78;
            color: white;
        }}
        
        .tab:hover {{
            background: #4472C4;
            color: white;
        }}
        
        .tab-content {{
            display: none;
        }}
        
        .tab-content.active {{
            display: block;
        }}
        
        .chart-container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .chart-container h3 {{
            margin-bottom: 20px;
            color: #1F4E78;
        }}
        
        .data-table {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        
        th {{
            background: #4472C4;
            color: white;
            font-weight: bold;
        }}
        
        tr:hover {{
            background: #f5f5f5;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            margin-top: 50px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Dashboard Commercial BBM AGRI</h1>
            <p class="subtitle">Données générées le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
        </header>
        
        <div class="kpi-grid">
            <div class="kpi-card">
                <h3>💰 CA Total HT</h3>
                <div class="value" id="ca-total">{(ca_total/1000000):.2f}M MAD</div>
                <div class="delta">Profitabilité: {profitabilite:.2f}%</div>
            </div>
            <div class="kpi-card">
                <h3>📈 Marge Totale</h3>
                <div class="value" id="marge-total">{(marge_total/1000000):.2f}M MAD</div>
                <div class="delta">{(marge_total/ca_total*100):.2f}% du CA</div>
            </div>
            <div class="kpi-card">
                <h3>👥 Commerciaux</h3>
                <div class="value" id="nb-commerciaux">{nb_commerciaux}</div>
                <div class="delta">{nb_familles} familles</div>
            </div>
            <div class="kpi-card">
                <h3>📦 Articles</h3>
                <div class="value" id="nb-articles">{nb_articles}</div>
                <div class="delta">{len(data_json.get('cltart', []))} ventes</div>
            </div>
        </div>
        
        <div class="filters">
            <h3>🔍 Filtres</h3>
            <div class="filter-group">
                <select id="filter-annee">
                    <option value="">Toutes les années</option>
                </select>
                <select id="filter-commercial">
                    <option value="">Tous les commerciaux</option>
                </select>
                <select id="filter-famille">
                    <option value="">Toutes les familles</option>
                </select>
            </div>
        </div>
        
        <div class="tabs">
            <button class="tab active" onclick="showTab('overview')">📊 Vue d'ensemble</button>
            <button class="tab" onclick="showTab('commercial')">👥 Par Commercial</button>
            <button class="tab" onclick="showTab('famille')">🏷️ Par Famille</button>
            <button class="tab" onclick="showTab('article')">📦 Par Article</button>
        </div>
        
        <div id="tab-overview" class="tab-content active">
            <div class="chart-container">
                <h3>CA HT Net par Année</h3>
                <div id="chart-ca-annee" style="height: 400px;"></div>
            </div>
            <div class="chart-container">
                <h3>Répartition du CA par Famille</h3>
                <div id="chart-ca-famille" style="height: 400px;"></div>
            </div>
        </div>
        
        <div id="tab-commercial" class="tab-content">
            <div class="chart-container">
                <h3>Top 10 Commerciaux par CA HT Net</h3>
                <div id="chart-top-commerciaux" style="height: 400px;"></div>
            </div>
            <div class="data-table">
                <h3>Tableau récapitulatif par Commercial</h3>
                <table id="table-commerciaux">
                    <thead>
                        <tr>
                            <th>Commercial</th>
                            <th>CA HT Net</th>
                            <th>Marge</th>
                            <th>Profitabilité</th>
                            <th>Nbre Ventes</th>
                        </tr>
                    </thead>
                    <tbody id="tbody-commerciaux">
                    </tbody>
                </table>
            </div>
        </div>
        
        <div id="tab-famille" class="tab-content">
            <div class="chart-container">
                <h3>CA Net HT par Famille</h3>
                <div id="chart-famille-ca" style="height: 400px;"></div>
            </div>
            <div class="data-table">
                <h3>Tableau récapitulatif par Famille</h3>
                <table id="table-familles">
                    <thead>
                        <tr>
                            <th>Code Famille</th>
                            <th>Désignation</th>
                            <th>CA Net HT</th>
                            <th>Qtés vendues</th>
                            <th>Marge</th>
                            <th>% Marge/CA</th>
                        </tr>
                    </thead>
                    <tbody id="tbody-familles">
                    </tbody>
                </table>
            </div>
        </div>
        
        <div id="tab-article" class="tab-content">
            <div class="chart-container">
                <h3>Top 20 Articles par CA Net HT</h3>
                <div id="chart-top-articles" style="height: 400px;"></div>
            </div>
            <div class="data-table">
                <h3>Tableau récapitulatif des Articles (Top 50)</h3>
                <table id="table-articles">
                    <thead>
                        <tr>
                            <th>Code Article</th>
                            <th>Désignation</th>
                            <th>CA Net HT</th>
                            <th>Qtés vendues</th>
                            <th>Marge</th>
                            <th>% Marge/CA</th>
                        </tr>
                    </thead>
                    <tbody id="tbody-articles">
                    </tbody>
                </table>
            </div>
        </div>
        
        <footer>
            <p>BBM AGRI | Dashboard Commercial | Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
        </footer>
    </div>
    
    <script>
        // Données JSON intégrées
        const data = {json.dumps(data_json, ensure_ascii=False, default=str)};
        
        // Fonctions utilitaires
        function formatMontant(value) {{
            if (!value) return "0.00 MAD";
            if (Math.abs(value) >= 1000000) return (value/1000000).toFixed(2) + "M MAD";
            if (Math.abs(value) >= 1000) return (value/1000).toFixed(2) + "K MAD";
            return value.toFixed(2) + " MAD";
        }}
        
        function formatPercent(value) {{
            if (!value) return "0.00%";
            return (value).toFixed(2) + "%";
        }}
        
        // Gestion des onglets
        function showTab(tabName) {{
            // Masquer tous les onglets
            document.querySelectorAll('.tab-content').forEach(tab => {{
                tab.classList.remove('active');
            }});
            document.querySelectorAll('.tab').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            // Afficher l'onglet sélectionné
            document.getElementById('tab-' + tabName).classList.add('active');
            event.target.classList.add('active');
            
            // Charger les données de l'onglet
            if (tabName === 'overview') loadOverview();
            else if (tabName === 'commercial') loadCommercial();
            else if (tabName === 'famille') loadFamille();
            else if (tabName === 'article') loadArticle();
        }}
        
        // Charger Vue d'ensemble
        function loadOverview() {{
            // CA par année
            if (data.cltfam && data.cltfam.length > 0) {{
                const caByYear = {{}};
                data.cltfam.forEach(row => {{
                    if (row.Année && row['CA HT Net']) {{
                        if (!caByYear[row.Année]) caByYear[row.Année] = 0;
                        caByYear[row.Année] += row['CA HT Net'] || 0;
                    }}
                }});
                
                const trace1 = {{
                    x: Object.keys(caByYear),
                    y: Object.values(caByYear),
                    type: 'bar',
                    marker: {{color: '#4472C4'}}
                }};
                
                Plotly.newPlot('chart-ca-annee', [trace1], {{
                    title: 'CA HT Net par Année',
                    xaxis: {{title: 'Année'}},
                    yaxis: {{title: 'CA HT Net (MAD)'}}
                }});
            }}
            
            // Répartition par famille
            if (data.statartfam && data.statartfam.length > 0) {{
                const familles = data.statartfam
                    .filter(f => f['Code Famille'] && f['CA Net HT'])
                    .sort((a, b) => (b['CA Net HT'] || 0) - (a['CA Net HT'] || 0))
                    .slice(0, 10);
                
                const trace2 = {{
                    values: familles.map(f => f['CA Net HT'] || 0),
                    labels: familles.map(f => f['Code Famille']),
                    type: 'pie',
                    hole: 0.4
                }};
                
                Plotly.newPlot('chart-ca-famille', [trace2], {{
                    title: 'Répartition du CA par Famille (Top 10)'
                }});
            }}
        }}
        
        // Charger données Commercial
        function loadCommercial() {{
            if (!data.cltfam || data.cltfam.length === 0) return;
            
            const summary = {{}};
            data.cltfam.forEach(row => {{
                const commercial = row.Commercial || 'Non spécifié';
                if (!summary[commercial]) {{
                    summary[commercial] = {{ca: 0, marge: 0, count: 0}};
                }}
                summary[commercial].ca += row['CA HT Net'] || 0;
                summary[commercial].marge += row.Marge || 0;
                summary[commercial].count += 1;
            }});
            
            const sorted = Object.entries(summary)
                .map(([com, vals]) => ({{
                    commercial: com,
                    ca: vals.ca,
                    marge: vals.marge,
                    profitabilite: vals.ca > 0 ? (vals.marge / vals.ca * 100) : 0,
                    count: vals.count
                }}))
                .sort((a, b) => b.ca - a.ca)
                .slice(0, 10);
            
            // Graphique
            const trace = {{
                x: sorted.map(s => s.commercial),
                y: sorted.map(s => s.ca),
                type: 'bar',
                marker: {{color: '#4472C4'}}
            }};
            
            Plotly.newPlot('chart-top-commerciaux', [trace], {{
                title: 'Top 10 Commerciaux par CA HT Net',
                xaxis: {{title: 'Commercial'}},
                yaxis: {{title: 'CA HT Net (MAD)'}}
            }});
            
            // Tableau
            const tbody = document.getElementById('tbody-commerciaux');
            tbody.innerHTML = sorted.map(s => `
                <tr>
                    <td>${{s.commercial}}</td>
                    <td>${{formatMontant(s.ca)}}</td>
                    <td>${{formatMontant(s.marge)}}</td>
                    <td>${{formatPercent(s.profitabilite)}}</td>
                    <td>${{s.count}}</td>
                </tr>
            `).join('');
        }}
        
        // Charger données Famille
        function loadFamille() {{
            if (!data.statartfam || data.statartfam.length === 0) return;
            
            const familles = data.statartfam
                .filter(f => f['Code Famille'] && f['CA Net HT'])
                .sort((a, b) => (b['CA Net HT'] || 0) - (a['CA Net HT'] || 0));
            
            // Graphique
            const trace = {{
                x: familles.map(f => f['Code Famille']),
                y: familles.map(f => f['CA Net HT'] || 0),
                type: 'bar',
                marker: {{color: '#4472C4'}}
            }};
            
            Plotly.newPlot('chart-famille-ca', [trace], {{
                title: 'CA Net HT par Famille',
                xaxis: {{title: 'Famille'}},
                yaxis: {{title: 'CA Net HT (MAD)'}}
            }});
            
            // Tableau
            const tbody = document.getElementById('tbody-familles');
            tbody.innerHTML = familles.map(f => `
                <tr>
                    <td>${{f['Code Famille'] || ''}}</td>
                    <td>${{f.Désignation || ''}}</td>
                    <td>${{formatMontant(f['CA Net HT'])}}</td>
                    <td>${{f['Qtés vendues'] || 0}}</td>
                    <td>${{formatMontant(f.Marge)}}</td>
                    <td>${{formatPercent(f['% Marge/CA'])}}</td>
                </tr>
            `).join('');
        }}
        
        // Charger données Article
        function loadArticle() {{
            if (!data.statartart || data.statartart.length === 0) return;
            
            const articles = data.statartart
                .filter(a => a['Code Article'] && a['CA Net HT'])
                .sort((a, b) => (b['CA Net HT'] || 0) - (a['CA Net HT'] || 0));
            
            const top20 = articles.slice(0, 20);
            const top50 = articles.slice(0, 50);
            
            // Graphique
            const trace = {{
                x: top20.map(a => a['Code Article']),
                y: top20.map(a => a['CA Net HT'] || 0),
                type: 'bar',
                marker: {{color: '#4472C4'}}
            }};
            
            Plotly.newPlot('chart-top-articles', [trace], {{
                title: 'Top 20 Articles par CA Net HT',
                xaxis: {{title: 'Article'}},
                yaxis: {{title: 'CA Net HT (MAD)'}}
            }});
            
            // Tableau
            const tbody = document.getElementById('tbody-articles');
            tbody.innerHTML = top50.map(a => `
                <tr>
                    <td>${{a['Code Article'] || ''}}</td>
                    <td>${{a.Désignation || ''}}</td>
                    <td>${{formatMontant(a['CA Net HT'])}}</td>
                    <td>${{a['Qtés vendues'] || 0}}</td>
                    <td>${{formatMontant(a.Marge)}}</td>
                    <td>${{formatPercent(a['% Marge/CA'])}}</td>
                </tr>
            `).join('');
        }}
        
        // Initialiser les filtres
        function initFilters() {{
            // Années
            const annees = new Set();
            if (data.cltfam) {{
                data.cltfam.forEach(row => {{
                    if (row.Année) annees.add(row.Année);
                }});
            }}
            if (data.cltart) {{
                data.cltart.forEach(row => {{
                    if (row.Année) annees.add(row.Année);
                }});
            }}
            const selectAnnee = document.getElementById('filter-annee');
            Array.from(annees).sort().forEach(annee => {{
                const option = document.createElement('option');
                option.value = annee;
                option.textContent = annee;
                selectAnnee.appendChild(option);
            }});
            
            // Commerciaux
            const commerciaux = new Set();
            if (data.cltfam) {{
                data.cltfam.forEach(row => {{
                    if (row.Commercial) commerciaux.add(row.Commercial);
                }});
            }}
            const selectCommercial = document.getElementById('filter-commercial');
            Array.from(commerciaux).sort().forEach(com => {{
                const option = document.createElement('option');
                option.value = com;
                option.textContent = com;
                selectCommercial.appendChild(option);
            }});
            
            // Familles
            const familles = new Set();
            if (data.statartfam) {{
                data.statartfam.forEach(row => {{
                    if (row['Code Famille']) familles.add(row['Code Famille']);
                }});
            }}
            const selectFamille = document.getElementById('filter-famille');
            Array.from(familles).sort().forEach(fam => {{
                const option = document.createElement('option');
                option.value = fam;
                option.textContent = fam;
                selectFamille.appendChild(option);
            }});
        }}
        
        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {{
            initFilters();
            loadOverview();
        }});
    </script>
</body>
</html>"""
    
    return html_content


def main():
    print("=" * 70)
    print("GENERATION DASHBOARD HTML STATIQUE")
    print("=" * 70)
    print()
    
    print("1. Conversion des fichiers Excel en JSON...")
    data_json = convertir_excel_en_json()
    print(f"   Total CLTFAM: {len(data_json.get('cltfam', []))} lignes")
    print(f"   Total CLTART: {len(data_json.get('cltart', []))} lignes")
    print(f"   Total STATARTFAM: {len(data_json.get('statartfam', []))} lignes")
    print(f"   Total STATARTART: {len(data_json.get('statartart', []))} lignes")
    print()
    
    print("2. Generation du fichier HTML...")
    html_content = generer_dashboard_html(data_json)
    
    # Créer le dossier dashboard pour le JSON (optionnel)
    if not os.path.exists('dashboard'):
        os.makedirs('dashboard')
    
    # Sauvegarder le HTML à la racine (pour GitHub Pages)
    html_file = 'index.html'
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Sauvegarder aussi dans dashboard pour organisation
    html_file_dashboard = 'dashboard/index.html'
    with open(html_file_dashboard, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Sauvegarder le JSON pour référence (optionnel)
    json_file = 'dashboard/data.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"   [OK] Fichier HTML genere: {html_file} (racine - pour GitHub Pages)")
    print(f"   [OK] Fichier HTML genere: {html_file_dashboard} (dossier dashboard)")
    print(f"   [OK] Fichier JSON genere: {json_file} (optionnel)")
    print()
    
    print("=" * 70)
    print("TERMINE")
    print("=" * 70)
    print()
    print("Pour utiliser le dashboard:")
    print()
    print("Option 1: Ouvrir directement dans le navigateur")
    print(f"   Double-cliquez sur: {html_file} (a la racine)")
    print()
    print("Option 2: Serveur local simple")
    print("   python -m http.server 8000")
    print("   Puis allez sur: http://localhost:8000")
    print()
    print("Option 3: Deployer sur GitHub Pages")
    print("   1. Creer un depot GitHub")
    print("   2. Uploader index.html (a la racine du depot)")
    print("   3. Activer GitHub Pages dans Settings")
    print("   4. URL: https://VOTRE_USERNAME.github.io/nom-depot/")
    print()
    print("Option 4: Deployer sur Netlify/Vercel")
    print("   Uploader index.html ou le dossier complet")


if __name__ == "__main__":
    main()
