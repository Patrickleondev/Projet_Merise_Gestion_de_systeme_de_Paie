import sqlite3

def creer_base_de_donnees():
    conn = sqlite3.connect('employe.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Employé (
                    ID_E_Employé INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nom_Employé TEXT NOT NULL,
                    Prénom_Employé TEXT NOT NULL,
                    Date_naissance_Employé TEXT NOT NULL,
                    Date_embauche_Employé TEXT NOT NULL,
                    Adresse_Employé TEXT,
                    Num_securite_sociale TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Salaire (
                    ID_Salaire INTEGER PRIMARY KEY AUTOINCREMENT,
                    Montant_Salaire REAL NOT NULL,
                    Date_paie_Salaire TEXT NOT NULL,
                    ID_E_Employé INTEGER,
                    FOREIGN KEY(ID_E_Employé) REFERENCES Employé(ID_E_Employé)
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Promotion (
                    ID_Promotion INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date_promo_Promotion TEXT NOT NULL,
                    New_poste_Promotion TEXT NOT NULL
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS obtient (
                    ID_obtient INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_E_Employé INTEGER,
                    ID_Promo_Promotion INTEGER,
                    FOREIGN KEY(ID_E_Employé) REFERENCES Employé(ID_E_Employé),
                    FOREIGN KEY(ID_Promo_Promotion) REFERENCES Promotion(ID_Promotion)
                )''')

    conn.commit()
    conn.close()

def ajouter_employe(nom, prenom, date_naissance, date_embauche, adresse, num_ss, salaire, date_paiement, date_promo, nouveau_poste):
    conn = sqlite3.connect('employe.db')
    c = conn.cursor()

    c.execute("INSERT INTO Employé (Nom_Employé, Prénom_Employé, Date_naissance_Employé, Date_embauche_Employé, Adresse_Employé, Num_securite_sociale) VALUES (?, ?, ?, ?, ?, ?)",
              (nom, prenom, date_naissance, date_embauche, adresse, num_ss))
    employe_id = c.lastrowid

    c.execute("INSERT INTO Salaire (Montant_Salaire, Date_paie_Salaire, ID_E_Employé) VALUES (?, ?, ?)",
              (salaire, date_paiement, employe_id))

    if date_promo and nouveau_poste:
        c.execute("INSERT INTO Promotion (Date_promo_Promotion, New_poste_Promotion) VALUES (?, ?)",
                  (date_promo, nouveau_poste))
        promo_id = c.lastrowid
        c.execute("INSERT INTO obtient (ID_E_Employé, ID_Promo_Promotion) VALUES (?, ?)",
                  (employe_id, promo_id))

    conn.commit()
    conn.close()

def obtenir_employe_par_nom(nom):
    conn = sqlite3.connect('employe.db')
    c = conn.cursor()

    c.execute("SELECT e.ID_E_Employé, e.Nom_Employé, e.Prénom_Employé, s.Montant_Salaire, s.Date_paie_Salaire "
              "FROM Employé e JOIN Salaire s ON e.ID_E_Employé = s.ID_E_Employé WHERE e.Nom_Employé = ?", (nom,))
    employe = c.fetchone()

    conn.close()
    return employe

def obtenir_promotion_employe(employe_id):
    conn = sqlite3.connect('employe.db')
    c = conn.cursor()

    c.execute("SELECT p.New_poste_Promotion FROM Promotion p "
              "JOIN obtient o ON p.ID_Promotion = o.ID_Promo_Promotion WHERE o.ID_E_Employé = ?", (employe_id,))
    poste = c.fetchone()

    conn.close()
    return poste
