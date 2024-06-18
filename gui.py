"""import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from database import creer_base_de_donnees, ajouter_employe, obtenir_employe_par_nom, obtenir_promotion_employe
from Pdf_Generateur import creer_bulletin_paie_pdf

class SystemeGestionPaie(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Système de Gestion de Paie")
        self.geometry("1080x1080")
        self.configure(background="gray")

        creer_base_de_donnees()
        self.create_widgets()

    def create_widgets(self):
        self.logo = ImageTk.PhotoImage(file="logo.jpg")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, column=2, columnspan=3, pady=10)

        self.lbl_nom = tk.Label(self, text="Nom de l'employé")
        self.lbl_nom.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.champ_nom = tk.Entry(self)
        self.champ_nom.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_prenom = tk.Label(self, text="Prénom de l'employé")
        self.lbl_prenom.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.champ_prenom = tk.Entry(self)
        self.champ_prenom.grid(row=2, column=1, padx=10, pady=5)

        self.lbl_date_naissance = tk.Label(self, text="Date de naissance")
        self.lbl_date_naissance.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.champ_date_naissance = DateEntry(self, date_pattern='dd/mm/yyyy')
        self.champ_date_naissance.grid(row=3, column=1, padx=10, pady=5)

        self.lbl_date_embauche = tk.Label(self, text="Date d'embauche")
        self.lbl_date_embauche.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.champ_date_embauche = DateEntry(self, date_pattern='dd/mm/yyyy')
        self.champ_date_embauche.grid(row=4, column=1, padx=10, pady=5)

        self.lbl_adresse = tk.Label(self, text="Adresse")
        self.lbl_adresse.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.champ_adresse = tk.Entry(self)
        self.champ_adresse.grid(row=5, column=1, padx=10, pady=5)

        self.lbl_num_ss = tk.Label(self, text="Numéro de Sécurité Sociale")
        self.lbl_num_ss.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.champ_num_ss = tk.Entry(self)
        self.champ_num_ss.grid(row=6, column=1, padx=10, pady=5)

        self.lbl_salaire = tk.Label(self, text="Salaire")
        self.lbl_salaire.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.champ_salaire = tk.Entry(self)
        self.champ_salaire.grid(row=7, column=1, padx=10, pady=5)

        self.lbl_date_paiement = tk.Label(self, text="Date de paiement")
        self.lbl_date_paiement.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.champ_date_paiement = DateEntry(self, date_pattern='dd/mm/yyyy')
        self.champ_date_paiement.grid(row=8, column=1, padx=10, pady=5)

        self.lbl_date_promo = tk.Label(self, text="Date de promotion")
        self.lbl_date_promo.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.champ_date_promo = DateEntry(self, date_pattern='dd/mm/yyyy')
        self.champ_date_promo.grid(row=9, column=1, padx=10, pady=5)

        self.lbl_nouveau_poste = tk.Label(self, text="Nouveau poste")
        self.lbl_nouveau_poste.grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.champ_nouveau_poste = tk.Entry(self)
        self.champ_nouveau_poste.grid(row=10, column=1, padx=10, pady=5)

        self.btn_ajouter = tk.Button(self, text="Ajouter l'Employé", command=self.ajouter_employe)
        self.btn_ajouter.grid(row=11, column=0, columnspan=2, pady=10)

        self.lbl_nom_employe_exist = tk.Label(self, text="Nom de l'employé existant")
        self.lbl_nom_employe_exist.grid(row=5, column=5, padx=10, pady=5, sticky="e")
        self.champ_nom_employe_exist = tk.Entry(self)
        self.champ_nom_employe_exist.grid(row=5, column=6, padx=10, pady=5)

        self.btn_generer_paie = tk.Button(self, text="Générer le Bulletin de Paie", command=self.generer_bulletin_paie, bg="skyblue", width="20")
        self.btn_generer_paie.grid(row=7, column=6, columnspan=2, pady=10)

        self.lbl_signature = tk.Label(self, text="Signature du DRH")
        self.lbl_signature.grid(row=6, column=5, padx=10, pady=5, sticky="e")
        self.champ_signature = tk.Entry(self)
        self.champ_signature.grid(row=6, column=6, padx=10, pady=5)

    def ajouter_employe(self):
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        date_naissance = self.champ_date_naissance.get()
        date_embauche = self.champ_date_embauche.get()
        adresse = self.champ_adresse.get()
        num_ss = self.champ_num_ss.get()
        salaire = self.champ_salaire.get()
        date_paiement = self.champ_date_paiement.get()
        date_promo = self.champ_date_promo.get()
        nouveau_poste = self.champ_nouveau_poste.get()

        if not nom or not prenom or not date_naissance or not date_embauche or not salaire or not date_paiement:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        ajouter_employe(nom, prenom, date_naissance, date_embauche, adresse, num_ss, salaire, date_paiement, date_promo, nouveau_poste)

        messagebox.showinfo("Succès", "Employé ajouté avec succès.")

    def generer_bulletin_paie(self):
        nom_employe = self.champ_nom_employe_exist.get()
        signature = self.champ_signature.get()

        if not nom_employe:
            messagebox.showerror("Erreur", "Veuillez entrer le nom de l'employé.")
            return

        employe = obtenir_employe_par_nom(nom_employe)

        if not employe:
            messagebox.showerror("Erreur", "Aucun employé trouvé avec ce nom.")
            return

        employe_id, nom, prenom, salaire, date_paiement = employe

        poste = obtenir_promotion_employe(employe_id)

        if poste:
            titre_poste = poste[0]
        else:
            titre_poste = "Non défini"

        fichier_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if fichier_pdf:
            creer_bulletin_paie_pdf(fichier_pdf, nom, prenom, titre_poste, salaire, date_paiement, signature)
            messagebox.showinfo("Succès", "Bulletin de paie généré avec succès.")"""





'''import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from database import creer_base_de_donnees, ajouter_employe, obtenir_employe_par_nom, obtenir_promotion_employe
from Pdf_Generateur import creer_bulletin_paie_pdf

class SystemeGestionPaie(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Système de Gestion de Paie")
        self.geometry("1080x1080")

        creer_base_de_donnees()
        self.create_widgets()

    def create_widgets(self):
        # Charger l'image de fond
        self.background_image = Image.open("logo.jpg")
        self.background_image = self.background_image.resize((1080, 1080), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Utiliser un Canvas pour gérer l'image de fond
        self.canvas = tk.Canvas(self, width=1080, height=1080)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Ajouter les widgets sur le Canvas
        self.lbl_entete = tk.Label(self.canvas, text="GROUPE 5 PME", font=("Arial", 18, "bold"), bg="white")
        self.canvas.create_window(540, 30, window=self.lbl_entete)  # Position centrale

        self.lbl_adresse1 = tk.Label(self.canvas, text="33 rue Pasteur", font=("Arial", 12), bg="white")
        self.canvas.create_window(540, 70, window=self.lbl_adresse1)

        self.lbl_adresse2 = tk.Label(self.canvas, text="31000 Lomé-Togo", font=("Arial", 12), bg="white")
        self.canvas.create_window(540, 90, window=self.lbl_adresse2)

        self.lbl_nom = tk.Label(self.canvas, text="Nom de l'employé", bg="white")
        self.canvas.create_window(300, 150, window=self.lbl_nom)
        self.champ_nom = tk.Entry(self.canvas)
        self.canvas.create_window(500, 150, window=self.champ_nom)

        self.lbl_prenom = tk.Label(self.canvas, text="Prénom de l'employé", bg="white")
        self.canvas.create_window(300, 190, window=self.lbl_prenom)
        self.champ_prenom = tk.Entry(self.canvas)
        self.canvas.create_window(500, 190, window=self.champ_prenom)

        self.lbl_date_naissance = tk.Label(self.canvas, text="Date de naissance", bg="white")
        self.canvas.create_window(300, 230, window=self.lbl_date_naissance)
        self.champ_date_naissance = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 230, window=self.champ_date_naissance)

        self.lbl_date_embauche = tk.Label(self.canvas, text="Date d'embauche", bg="white")
        self.canvas.create_window(300, 270, window=self.lbl_date_embauche)
        self.champ_date_embauche = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 270, window=self.champ_date_embauche)

        self.lbl_adresse = tk.Label(self.canvas, text="Adresse", bg="white")
        self.canvas.create_window(300, 310, window=self.lbl_adresse)
        self.champ_adresse = tk.Entry(self.canvas)
        self.canvas.create_window(500, 310, window=self.champ_adresse)

        self.lbl_num_ss = tk.Label(self.canvas, text="Numéro de Sécurité Sociale", bg="white")
        self.canvas.create_window(300, 350, window=self.lbl_num_ss)
        self.champ_num_ss = tk.Entry(self.canvas)
        self.canvas.create_window(500, 350, window=self.champ_num_ss)

        self.lbl_salaire = tk.Label(self.canvas, text="Salaire", bg="white")
        self.canvas.create_window(300, 390, window=self.lbl_salaire)
        self.champ_salaire = tk.Entry(self.canvas)
        self.canvas.create_window(500, 390, window=self.champ_salaire)

        self.lbl_date_paiement = tk.Label(self.canvas, text="Date de paiement", bg="white")
        self.canvas.create_window(300, 430, window=self.lbl_date_paiement)
        self.champ_date_paiement = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 430, window=self.champ_date_paiement)

        self.lbl_date_promo = tk.Label(self.canvas, text="Date de promotion", bg="white")
        self.canvas.create_window(300, 470, window=self.lbl_date_promo)
        self.champ_date_promo = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 470, window=self.champ_date_promo)

        self.lbl_nouveau_poste = tk.Label(self.canvas, text="Nouveau poste", bg="white")
        self.canvas.create_window(300, 510, window=self.lbl_nouveau_poste)
        self.champ_nouveau_poste = tk.Entry(self.canvas)
        self.canvas.create_window(500, 510, window=self.champ_nouveau_poste)

        self.btn_ajouter = tk.Button(self.canvas, text="Ajouter l'Employé", command=self.ajouter_employe, bg="lightgreen")
        self.canvas.create_window(400, 550, window=self.btn_ajouter)

        self.lbl_nom_employe_exist = tk.Label(self.canvas, text="Nom de l'employé existant", bg="white")
        self.canvas.create_window(300, 600, window=self.lbl_nom_employe_exist)
        self.champ_nom_employe_exist = tk.Entry(self.canvas)
        self.canvas.create_window(500, 600, window=self.champ_nom_employe_exist)

        self.lbl_signature = tk.Label(self.canvas, text="Signature du DRH", bg="white")
        self.canvas.create_window(300, 640, window=self.lbl_signature)
        self.champ_signature = tk.Entry(self.canvas)
        self.canvas.create_window(500, 640, window=self.champ_signature)

        self.btn_generer_paie = tk.Button(self.canvas, text="Générer le Bulletin de Paie", command=self.generer_bulletin_paie, bg="skyblue", width=20)
        self.canvas.create_window(400, 680, window=self.btn_generer_paie)

    def ajouter_employe(self):
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        date_naissance = self.champ_date_naissance.get()
        date_embauche = self.champ_date_embauche.get()
        adresse = self.champ_adresse.get()
        num_ss = self.champ_num_ss.get()
        salaire = self.champ_salaire.get()
        date_paiement = self.champ_date_paiement.get()
        date_promo = self.champ_date_promo.get()
        nouveau_poste = self.champ_nouveau_poste.get()

        if not nom or not prenom or  not date_naissance or not date_embauche or not salaire or not date_paiement:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        ajouter_employe(nom, prenom, date_naissance, date_embauche, adresse, num_ss, salaire, date_paiement, date_promo, nouveau_poste)

        messagebox.showinfo("Succès", "Employé ajouté avec succès.")

    def generer_bulletin_paie(self):
        nom_employe = self.champ_nom_employe_exist.get()
        signature = self.champ_signature.get()

        if not nom_employe:
            messagebox.showerror("Erreur", "Veuillez entrer le nom de l'employé.")
            return

        employe = obtenir_employe_par_nom(nom_employe)

        if not employe:
            messagebox.showerror("Erreur", "Aucun employé trouvé avec ce nom.")
            return

        employe_id, nom, prenom, salaire, date_paiement = employe

        poste = obtenir_promotion_employe(employe_id)

        if poste:
            titre_poste = poste[0]
        else:
            titre_poste = "Non défini"

        fichier_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if fichier_pdf:
            creer_bulletin_paie_pdf(fichier_pdf, nom, prenom, titre_poste, salaire, date_paiement, signature)
            messagebox.showinfo("Succès", "Bulletin de paie généré avec succès.")

if __name__ == "__main__":
    app = SystemeGestionPaie()
    app.mainloop()'''





import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from database import creer_base_de_donnees, ajouter_employe, obtenir_employe_par_nom, obtenir_promotion_employe
from Pdf_Generateur import creer_bulletin_paie_pdf

class SystemeGestionPaie(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Système de Gestion de Paie")
        self.geometry("1080x1080")

        creer_base_de_donnees()
        self.create_widgets()

    def create_widgets(self):
        # Charger l'image de fond
        self.background_image = Image.open("logo.jpg")
        self.background_image = self.background_image.resize((1080, 1080), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Utiliser un Canvas pour gérer l'image de fond
        self.canvas = tk.Canvas(self, width=1080, height=1080)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Ajouter les widgets sur le Canvas
        self.lbl_entete = tk.Label(self.canvas, text="GROUPE 5 PME", font=("Arial", 18, "bold"), bg="white")
        self.canvas.create_window(540, 30, window=self.lbl_entete)  # Position centrale

        self.lbl_adresse1 = tk.Label(self.canvas, text="33 rue Pasteur", font=("Arial", 12), bg="white")
        self.canvas.create_window(540, 70, window=self.lbl_adresse1)

        self.lbl_adresse2 = tk.Label(self.canvas, text="31000 Lomé-Togo", font=("Arial", 12), bg="white")
        self.canvas.create_window(540, 90, window=self.lbl_adresse2)

        self.lbl_nom = tk.Label(self.canvas, text="Nom de l'employé", bg="white")
        self.canvas.create_window(300, 150, window=self.lbl_nom)
        self.champ_nom = tk.Entry(self.canvas)
        self.canvas.create_window(500, 150, window=self.champ_nom)

        self.lbl_prenom = tk.Label(self.canvas, text="Prénom de l'employé", bg="white")
        self.canvas.create_window(300, 190, window=self.lbl_prenom)
        self.champ_prenom = tk.Entry(self.canvas)
        self.canvas.create_window(500, 190, window=self.champ_prenom)

        self.lbl_date_naissance = tk.Label(self.canvas, text="Date de naissance", bg="white")
        self.canvas.create_window(300, 230, window=self.lbl_date_naissance)
        self.champ_date_naissance = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 230, window=self.champ_date_naissance)

        self.lbl_date_embauche = tk.Label(self.canvas, text="Date d'embauche", bg="white")
        self.canvas.create_window(300, 270, window=self.lbl_date_embauche)
        self.champ_date_embauche = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 270, window=self.champ_date_embauche)

        self.lbl_adresse = tk.Label(self.canvas, text="Adresse", bg="white")
        self.canvas.create_window(300, 310, window=self.lbl_adresse)
        self.champ_adresse = tk.Entry(self.canvas)
        self.canvas.create_window(500, 310, window=self.champ_adresse)

        self.lbl_num_ss = tk.Label(self.canvas, text="Numéro de Sécurité Sociale", bg="white")
        self.canvas.create_window(300, 350, window=self.lbl_num_ss)
        self.champ_num_ss = tk.Entry(self.canvas)
        self.canvas.create_window(500, 350, window=self.champ_num_ss)

        self.lbl_salaire = tk.Label(self.canvas, text="Salaire", bg="white")
        self.canvas.create_window(300, 390, window=self.lbl_salaire)
        self.champ_salaire = tk.Entry(self.canvas)
        self.canvas.create_window(500, 390, window=self.champ_salaire)

        self.lbl_date_paiement = tk.Label(self.canvas, text="Date de paiement", bg="white")
        self.canvas.create_window(300, 430, window=self.lbl_date_paiement)
        self.champ_date_paiement = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 430, window=self.champ_date_paiement)

        self.lbl_date_promo = tk.Label(self.canvas, text="Date de promotion", bg="white")
        self.canvas.create_window(300, 470, window=self.lbl_date_promo)
        self.champ_date_promo = DateEntry(self.canvas, date_pattern='dd/mm/yyyy')
        self.canvas.create_window(500, 470, window=self.champ_date_promo)

        self.lbl_nouveau_poste = tk.Label(self.canvas, text="Nouveau poste", bg="white")
        self.canvas.create_window(300, 510, window=self.lbl_nouveau_poste)
        self.champ_nouveau_poste = tk.Entry(self.canvas)
        self.canvas.create_window(500, 510, window=self.champ_nouveau_poste)

        self.btn_ajouter = tk.Button(self.canvas, text="Ajouter l'Employé", command=self.ajouter_employe, bg="lightgreen")
        self.canvas.create_window(400, 550, window=self.btn_ajouter)

        # Déplacer cette partie à droite de l'écran
        self.lbl_nom_employe_exist = tk.Label(self.canvas, text="Nom de l'employé existant", bg="white")
        self.canvas.create_window(750, 310, window=self.lbl_nom_employe_exist)
        self.champ_nom_employe_exist = tk.Entry(self.canvas)
        self.canvas.create_window(950, 310, window=self.champ_nom_employe_exist)

        self.lbl_signature = tk.Label(self.canvas, text="Signature du DRH", bg="white")
        self.canvas.create_window(750, 410, window=self.lbl_signature)
        self.champ_signature = tk.Entry(self.canvas)
        self.canvas.create_window(950, 410, window=self.champ_signature)

        self.btn_generer_paie = tk.Button(self.canvas, text="Générer le Bulletin de Paie", command=self.generer_bulletin_paie, bg="skyblue", width=20)
        self.canvas.create_window(840, 520, window=self.btn_generer_paie)

    def ajouter_employe(self):
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        date_naissance = self.champ_date_naissance.get()
        date_embauche = self.champ_date_embauche.get()
        adresse = self.champ_adresse.get()
        num_ss = self.champ_num_ss.get()
        salaire = self.champ_salaire.get()
        date_paiement = self.champ_date_paiement.get()
        date_promo = self.champ_date_promo.get()
        nouveau_poste = self.champ_nouveau_poste.get()

        if not nom or not prenom or not date_naissance or not date_embauche or not salaire or not date_paiement:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        ajouter_employe(nom, prenom, date_naissance, date_embauche, adresse, num_ss, salaire, date_paiement, date_promo, nouveau_poste)

        messagebox.showinfo("Succès", "Employé ajouté avec succès.")

    def generer_bulletin_paie(self):
        nom_employe = self.champ_nom_employe_exist.get()
        signature = self.champ_signature.get()

        if not nom_employe:
            messagebox.showerror("Erreur", "Veuillez entrer le nom de l'employé.")
            return

        employe = obtenir_employe_par_nom(nom_employe)

        if not employe:
            messagebox.showerror("Erreur", "Aucun employé trouvé avec ce nom.")
            return

        employe_id, nom, prenom, salaire, date_paiement = employe

        poste = obtenir_promotion_employe(employe_id)

        if poste:
            titre_poste = poste[0]
        else:
            titre_poste = "Non défini"

        fichier_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if fichier_pdf:
            creer_bulletin_paie_pdf(fichier_pdf, nom, prenom, titre_poste, salaire, date_paiement, signature)
            messagebox.showinfo("Succès", "Bulletin de paie généré avec succès.")

if __name__ == "__main__":
    app = SystemeGestionPaie()
    app.mainloop()


