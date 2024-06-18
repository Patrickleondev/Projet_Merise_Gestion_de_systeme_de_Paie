import unittest
import sqlite3
import os
from systeme_gestion_paie import SystemeGestionPaie

class TestIntegrationSystemeGestionPaie(unittest.TestCase):
    
    def setUp(self):
        self.app = SystemeGestionPaie()
        self.conn = sqlite3.connect('employe.db')
        self.c = self.conn.cursor()

    def tearDown(self):
        self.conn.close()
        os.remove('employe.db')

    def test_ajout_employe(self):
        self.app.champ_nom.insert(0, "Doe")
        self.app.champ_prenom.insert(0, "John")
        self.app.champ_date_naissance.set_date("01/01/1990")
        self.app.champ_date_embauche.set_date("01/01/2020")
        self.app.champ_adresse.insert(0, "123 Rue Exemple")
        self.app.champ_num_ss.insert(0, "123456789")
        self.app.champ_salaire.insert(0, "3000")
        self.app.champ_date_paiement.set_date("01/02/2024")
        
        self.app.ajouter_employe()
        
        self.c.execute("SELECT * FROM Employé WHERE Nom_Employé = 'Doe'")
        employe = self.c.fetchone()
        self.assertIsNotNone(employe)
        self.assertEqual(employe[1], "Doe")
        self.assertEqual(employe[2], "John")

    def test_generer_bulletin_paie(self):
        self.c.execute("INSERT INTO Employé (Nom_Employé, Prénom_Employé, Date_naissance_Employé, Date_embauche_Employé, Adresse_Employé, Num_securite_sociale) VALUES (?, ?, ?, ?, ?, ?)",
                       ("Doe", "John", "01/01/1990", "01/01/2020", "123 Rue Exemple", "123456789"))
        employe_id = self.c.lastrowid
        self.c.execute("INSERT INTO Salaire (Montant_Salaire, Date_paie_Salaire, ID_E_Employé) VALUES (?, ?, ?)",
                       (3000, "01/02/2024", employe_id))
        self.conn.commit()
        
        self.app.champ_nom_employe_exist.insert(0, "Doe")
        self.app.champ_signature.insert(0, "DRH")
        
        fichier_pdf = "bulletin_paie_test.pdf"
        if os.path.exists(fichier_pdf):
            os.remove(fichier_pdf)
        
        self.app.generer_bulletin_paie()
        
        self.assertTrue(os.path.exists(fichier_pdf))

    def test_promotion_employe(self):
        self.c.execute("INSERT INTO Employé (Nom_Employé, Prénom_Employé, Date_naissance_Employé, Date_embauche_Employé, Adresse_Employé, Num_securite_sociale) VALUES (?, ?, ?, ?, ?, ?)",
                       ("Doe", "John", "01/01/1990", "01/01/2020", "123 Rue Exemple", "123456789"))
        employe_id = self.c.lastrowid
        self.conn.commit()
        
        self.app.champ_nom.insert(0, "Doe")
        self.app.champ_prenom.insert(0, "John")
        self.app.champ_date_promo.set_date("01/03/2024")
        self.app.champ_nouveau_poste.insert(0, "Manager")
        
        self.app.ajouter_employe()
        
        self.c.execute("SELECT * FROM Promotion p JOIN obtient o ON p.ID_Promotion = o.ID_Promo_Promotion WHERE o.ID_E_Employé = ?", (employe_id,))
        promotion = self.c.fetchone()
        self.assertIsNotNone(promotion)
        self.assertEqual(promotion[2], "Manager")

if __name__ == '__main__':
    unittest.main()
