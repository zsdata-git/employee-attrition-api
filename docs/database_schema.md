erDiagram
    EMPLOYEES {
        int id PK
        float age
        string genre
        float revenu_mensuel
        string statut_marital
        string departement
        string poste
        float nombre_experiences_precedentes
        float annees_dans_l_entreprise
        float annees_dans_le_poste_actuel
        float satisfaction_employee_environnement
        float satisfaction_employee_nature_travail
        float satisfaction_employee_equipe
        float satisfaction_employee_equilibre_pro_perso
        float note_evaluation_actuelle
        float augmentation_salaire_precedente_pct
        int heures_supplementaires
        int a_quitte_l_entreprise
        float distance_domicile_travail
        float niveau_education
        string domaine_etude
        string frequence_deplacement
        float annees_depuis_la_derniere_promotion
        float annee_sous_responsable_actuel
        int a_suivi_formation
        float annee_experience_avant_entreprise
        int mobilite_interne
        float evolution_note
        int utilisation_pee
    }

    PREDICTIONS {
        int id PK
        json input_data
        int prediction
        float probability
        datetime created_at
    }



La base PostgreSQL du projet repose sur deux tables principales.

La table employees contient le dataset source des employés avec l’ensemble des variables utilisées par le modèle, ainsi que la variable cible a_quitte_l_entreprise.

La table predictions stocke les prédictions réalisées via l’API. Chaque enregistrement contient les données d’entrée envoyées au modèle au format JSON, la classe prédite, la probabilité associée et l’horodatage de la prédiction.

Cette structure permet d’assurer la traçabilité des échanges entre l’API et la base de données.