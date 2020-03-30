# -----------------------   Initialisation           -------------------------
from tkinter import *
import tkinter as tk
from time import *
from tkinter import messagebox
import random


"""
############# { Définition des fonctions utilisées dans le programme } ################
"""

def mot():
    f = open('mots_6_lettres.txt', 'r')
    j = random.randint(1, 7773)
    for i in range(1,j):
        x =f.readline(7)
    f.close()
    x=str(x)
    mot = x[0:6]
    return mot

def game():
    root.destroy()
    entree_joueur()

def re():
    fen.destroy()
    entree_joueur()


"""
            Fonction principale du jeu
"""

def jeu(pseudo1, pseudo2):

    global fen

    def compte():
        global temps, essai
        temps -= 1
        label.config(text=strftime('%M:%S', gmtime(temps)))
        if temps > 0:
            label.after(1000, compte)
        elif temps == 0:
            essai = 10
            decision()
# --------------------------------------------------------------------------------------
# -----------------------   fonction plateau  -------------------------
    def plateau():
        global labelp1, labelp2, joueur, score1, score2, Frame1, Frame2, fen, Jinfos

        Jinfos = Frame(fen, borderwidth=2, relief=GROOVE)
        Jinfos.pack(side=LEFT, expand=YES, padx=10, pady=10)
        Frame1 = Frame(Jinfos, borderwidth=2)  # Cadre du Joueur 1
        Frame1.pack(side=TOP, padx=10, pady=10)

        Frame2 = Frame(Jinfos, borderwidth=2)  # Cadre du Joueur 2
        Frame2.pack(side=BOTTOM, padx=10, pady=10)

        score1 = 0
        score2 = 0

        labelp1 = Label(Frame1, text='Joueur 1\n' + pseudo1 + '\n0 point(s)', font=('Helvetica', '16'))
        labelp1.pack(padx=2, pady=2)  # Afficher joueur 1
        labelp2 = Label(Frame2, text='Joueur 2\n' + pseudo2 + '\n0 point(s)', font=('Helvetica', '16'))
        labelp2.pack()  # Afficher joueur 2
        joueur = 0  # Initialisation de joueur (0 => joueur1 joue, 1 => joueur2 joue)

        rbuttons = Frame(fen, borderwidth=2, relief=GROOVE)

        retour_main = Button(rbuttons, text="Retour main", bg='#24d54d', fg='#ffffff', font=("Courrier","14"), command=retour_m)
        retour_main.pack(side=TOP, padx=10, pady=10)

        recommencer = Button(rbuttons, text="Recommencer", bg='#ffffff', fg='#ba482d', font=("Courrier","14"), command=re)
        recommencer.pack(padx=10, pady=10)

        regle = Button(rbuttons, text="Règles", bg='#ffffff', fg='#ba482d', font=("Courrier","14"), command=rule)
        regle.pack(padx=10, pady=10)

        quitter = Button(rbuttons, text="Quitter", bg='#ba482d', fg='#ffffff', font=("Courrier","14"), command=fen.destroy)
        quitter.pack(side=BOTTOM, padx=10, pady=10)

        rbuttons.pack(side=RIGHT, expand=YES, padx=10, pady=10)
        tour()

    def tour():
        global labelp1, labelp2, label, temps, emot, can, essai, indice, Frame3, Frame0, m, fen
        if joueur == 0:  # Surligner en vert le joueur qui joue
            labelp1.configure(background='#26C4EC')
            labelp2.configure(background='white')
        else:
            labelp1.configure(background='white')
            labelp2.configure(background='#26C4EC')
        Frame0 = Frame(fen, borderwidth=2, relief=GROOVE)
        Frame0.pack(side=TOP, padx=30, pady=30)

        m = mot()
        essai = 0

        Frame3 = Frame(fen, borderwidth=2, relief=GROOVE)
        Frame3.pack(side=TOP, pady=5, padx=5)
        can = Canvas(Frame3, width=300, height=500, bg="white")
        for j in range(10):  # Creation de la grille
            for i in range(6):
                can.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill="blue")

        indice = m[0] + '.....'
        for i in range(6):
            can.create_text((25 + i * 50, 25), text=indice[i], font=('Helvetica', '30'), fill="white")
        can.pack()

        emot = Entry(Frame0)
        emot.pack(padx=2, pady=2)  # Champ de saisie du mot
        b3 = Button(Frame0, text='Entrer mot', command=verification)
        b3.pack(padx=2, pady=2)  # Bouton de validation du mot
        label = Label(Frame0, fg="green", font=('Helvetica', '30'))
        label.pack()
        temps = 181
        compte()

    def decision():
        global essai, indice, score1, score2, joueur, Frame4, fen
        essai += 1

        if proposition == m:  # Si le mot est correct
            if joueur == 0:
                score1 += 1
                labelp1.configure(
                    text='Joueur 1\n' + pseudo1 + '\n' + str(score1) + ' point(s)')  # Modifier score du joueur 1
            else:
                score2 += 1
                labelp2.configure(
                    text='Joueur 2\n' + pseudo2 + '\n' + str(score1) + ' point(s)')  # Modifier score du joueur 2
            joueur = 1 - joueur  # Changement de joueur
            Frame4 = Frame(fen, borderwidth=2, relief=GROOVE)  # Cadre en bas
            Frame4.pack(side=TOP, pady=2, padx=2)
            message = Label(Frame4, text='Bien joué ! Le mot était ' + m)  # Message de congratulation
            message.pack(side=TOP, pady=2, padx=2)
            if score1 == 3:
                message = Label(Frame4, text='VICTOIRE de ' + pseudo1, font="bold")  # Victoire joueur 1
                message.pack(side=TOP, pady=2, padx=2)
            elif score2 == 3:
                message = Label(Frame4, text='VICTOIRE de ' + pseudo2)  # Victoire joueur 2
                message.pack(side=TOP, pady=2, padx=2)
            else:
                bnext = Button(Frame4, text='Continuer', command=nouveautour)  # Bouton pour continuer le jeu
                bnext.pack(side=TOP, pady=2, padx=2)
        elif essai >= 10:  # Si le nombre d'essais est dépassé‚
            joueur = 1 - joueur  # Changement de joueur
            Frame0.destroy()
            Frame4 = Frame(fen, borderwidth=2, relief=GROOVE)  # Cadre en bas
            Frame4.pack(side=TOP, pady=2, padx=2)
            message = Label(Frame4, text='Raté, le mot était ' + m)  # Message d'échec
            message.pack(side=TOP, pady=2, padx=2)
            bnext = Button(Frame4, text='Continuer', command=nouveautour)  # Bouton pour continuer le jeu
            bnext.pack(side=TOP, pady=2, padx=2)
        else:
            for i in range(6):
                can.create_text((25 + i * 50, 25 + 50 * essai), text=indice[i], font=('Helvetica', '30'),
                                fill="white")
# --------------------------------------------------------------------------------------
# -----------------------   fonction verification   -------------------------
    def verification():
        global indice, proposition,essai
        proposition = emot.get().upper()
        emot.delete(0, 'end')
        print(m)
        occurence = []


        if len(proposition) != 6:

            messagebox.showinfo("Warning","Voulez vous recommencer la partie ?")
            essai = 10
            decision()
        else:

            for i in range(len(proposition)):  # Afficher toutes les lettres
                can.create_rectangle(i * 50, essai * 50, (i + 1) * 50, (essai + 1) * 50, fill="blue")
                can.create_text((25 + i * 50, 25 + essai * 50), text=proposition[i], font=('Helvetica', '30'), fill="white")

            for i in range(len(proposition)):
                lettre = proposition[i]
                if lettre == m[i]:
                    occurence.append(lettre)
                    indice = indice[0:i] + lettre + indice[i + 1:6]
                    can.create_rectangle(i * 50, essai * 50, (i + 1) * 50, (essai + 1) * 50, fill="#CC0000")
                    can.create_text((25 + i * 50, 25 + essai * 50), text=proposition[i], font=('Helvetica', '30'), fill="white")
                elif (lettre in m) and (occurence.count(lettre) < m.count(lettre) and lettre != m[i]):
                    occurence.append(lettre)
                    can.create_rectangle(i * 50, essai * 50, (i + 1) * 50, (essai + 1) * 50, fill="#FFD700")
                    can.create_text((25 + i * 50, 25 + essai * 50), text=proposition[i], font=('Helvetica', '30'), fill="white")
            decision()

    def nouveautour():  # Initialisation d'un nouveau tour
        Frame4.destroy()
        Frame3.destroy()
        Frame0.destroy()
        tour()
# --------------------------------------------------------------------------------------
#        -----------------------   fonction retour motus  -------------------------
    def retour_m():
        messagebox.showinfo("Warning","Voulez vous recommencer la partie ?")
        fen.destroy()

        root = Tk() #

        root.title("Jeu Motus")#titre de la fenêtre
        root.config(background='#ba482d')
        root.geometry("1080x720")
        root.minsize(1080,720)
        root.maxsize(1080,720)
        #root.iconbitmap("motus.ico")

        #  créer Frame header pour image + texte

        header = Frame(root, bg='#ba482d')

        titre = Label(header, text="BIENVENUE SUR LE MOTUS", bg='#ba482d', fg='#ffffff', font=("Courrier","45"))
        titre.pack()

        separator = Frame(header, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        img = PhotoImage(file = "motusT.png")
        ImgM = Label(header, image = img, bg='#ba482d')
        ImgM.pack(pady=25)

        separator = Frame(header, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        header.pack(expand=YES)

        buttons = Frame(root, bg='#ba482d')

        jouer = Button(buttons, text="Jouer", bg='#24d54d', fg='#ffffff', font=("Courrier","20"), command=game)
        jouer.pack(side=LEFT, padx=10)

        regle = Button(buttons, text="Règles", bg='#ffffff', fg='#ba482d', font=("Courrier","20"), command=rule)
        regle.pack(side=LEFT)

        quitter = Button(buttons, text="Quitter", bg='#ba482d', fg='#ffffff', font=("Courrier","20"), command=root.destroy)
        quitter.pack(side=LEFT, padx=10)

        buttons.pack(expand=YES)

        bot = Frame(root, bg='#ba482d')

        separator = Frame(bot, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        isn = Label(bot, text="Réalisé par :", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
        isn.pack()

        groupe = Label(bot, text="IBNOU EL KADI Sarah, PIERRE Lauryn, SIVAKARAN Kowsikan", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
        groupe.pack()

        annee = Label(bot, text="Dans le cadre du projet ISN 2018 - 2019", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
        annee.pack()

        lycee = Label(bot, text="Lycée Lucie Aubrac", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
        lycee.pack()

        bot.pack(expand=YES)

        root.mainloop()
# --------------------------------------------------------------------------------------
    fen = Tk()
    fen.title('Motus')
    plateau()
    fen.mainloop()
# --------------------------------------------------------------------------------------
# -----------------------   fonction récupération de pseudos   -------------------------
def entree_joueur():
    def action():
        joueur1 = pseudo1.get()
        joueur2 = pseudo2.get()
        fenetre.destroy()
        jeu(joueur1, joueur2)

    fenetre = Tk()
    fenetre.title("Motus")
    fenetre.geometry("600x210")
    fenetre.config(background="#4065A4")

    frame = Frame(fenetre, bg="#4065A4")

    label_title = Label(frame, text="Tapez les pseudos des joueurs", font="Times 20", bg="#4065A4", fg="white")
    label_title.grid(row=0, column=1)

    pseudo1 = StringVar()
    pseudo2 = StringVar()

    labelj_1 = Label(frame, text="Joueur 1", font="Times 12", bg="#4065A4", fg="white")
    labelj_1.grid(row=1, column=0, pady=0, padx=1)

    labelj_2 = Label(frame, text="Joueur 2", font="Times 12", bg="#4065A4", fg="white")
    labelj_2.grid(row=2, column=0, pady=0, padx=0)

    Champ1 = Entry(frame, textvariable=pseudo1, bg='bisque', fg='black')
    Champ1.focus_set()
    Champ1.grid(row=1, column=1, padx=1, pady=0, sticky=W)

    Champ2 = Entry(frame, textvariable=pseudo2, bg='bisque', fg='black')
    Champ2.focus_set()
    Champ2.grid(row=2, column=1, padx=0, pady=0, sticky=W)

    c_button = Button(frame, text="valider", font="Times 10", bg="white", fg="#4065A4", command=action)
    c_button.grid(row=3, column=1, sticky=W, padx=3, pady=3)

    frame.pack(expand=YES)

    fenetre.mainloop()


# - ------ - - - - - - -- - - - -      FONCTION REGLES
def rule():
    wregles = Tk()
    wregles.title("Règlement")
    wregles.geometry("800x450")
    wregles.minsize(800, 450)
    wregles.maxsize(800, 450)
    wregles.config(background='#FFFFFF')
    w = Frame(wregles, bg='#FFFFFF')
    w.pack(expand=YES)


    label_title = Label(w, text="Règles du jeu", font=("Courrier", 18), bg='#FFFFFF',fg='black')
    label_title.pack()

    #    regles.pack()
    regles = Text(w, width="1000", height="18", font=("Courrier", 13))
    regles.pack()

    regles.insert(INSERT, "                      \n \n            Voici les règles du jeu  : \n\n")
    regles.insert(INSERT, "    Le but du jeu est de retrouver un mot de 6 lettres\n    (pas de verbe conjugué, sauf les participes présents)\n    dans un délais de 1 minute et 30 secondes, ou avant avec 10 essais.\n    La première lettre du mot est donnée. Proposez un mot et déduisez les lettres \n    qui le composent à l'aide du code couleur suivant : \n\n")
    regles.insert(INSERT, "    Une lettre colorée en ROUGE est dans le mot et est bien placée.\n")
    regles.insert(INSERT, "    Une lettre colorée en JAUNE est dans le mot mais est mal placée.\n")
    regles.insert(INSERT, "    Une lettre NON COLOREE n'est pas dans le mot.\n \n")
    regles.insert(INSERT, "    Chaque joueur doit trouver un mot chacun leur tour. \n")

    regles.config(state=DISABLED)

    regles.tag_add('r', 11.26, 11.31)
    regles.tag_add('j', 12.26, 12.31)
    regles.tag_add('n', 13.15, 13.26)
    regles.tag_config('r', background="white", foreground="red", font=("Courrier", 14))
    regles.tag_config('j', background="white", foreground="#E0C046", font=("Courrier", 14))
    regles.tag_config('n', background="#BFBFBF", foreground="snow", font=("Courrier", 14))

    wretour = Button(w, text="Retour", bg='#ba482d', fg='#ffffff', font=("Courrier","12"), command=wregles.destroy)
    wretour.pack(side=BOTTOM, padx=10, pady=10)


    wregles.mainloop()



"""
-----------------------------|||||||||||||||||| { FENETRE PRINICIPALE } ||||||||||||||||||-----------------------------

"""

root = Tk() #

root.title("Jeu Motus")#titre de la fenêtre
root.config(background='#ba482d')
root.geometry("1080x720")
root.minsize(1080,720)
root.maxsize(1080,720)
#root.iconbitmap("motus.ico")

#  créer Frame header pour image + texte

header = Frame(root, bg='#ba482d')

titre = Label(header, text="BIENVENUE SUR LE MOTUS", bg='#ba482d', fg='#ffffff', font=("Courrier","45"))
titre.pack()

separator = Frame(header, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

img = tk.PhotoImage(file = "motusT.png")
ImgM = tk.Label(header, image = img, bg='#ba482d')
ImgM.pack(pady=25)

separator = Frame(header, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

header.pack(expand=YES)

buttons = Frame(root, bg='#ba482d')

jouer = Button(buttons, text="Jouer", bg='#24d54d', fg='#ffffff', font=("Courrier","20"), command=game)
jouer.pack(side=LEFT, padx=10)

regle = Button(buttons, text="Règles", bg='#ffffff', fg='#ba482d', font=("Courrier","20"), command=rule)
regle.pack(side=LEFT)

quitter = Button(buttons, text="Quitter", bg='#ba482d', fg='#ffffff', font=("Courrier","20"), command=root.destroy)
quitter.pack(side=LEFT, padx=10)

buttons.pack(expand=YES)

bot = Frame(root, bg='#ba482d')

separator = Frame(bot, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

isn = Label(bot, text="Réalisé par :", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
isn.pack()

groupe = Label(bot, text="IBNOU EL KADI Sarah, PIERRE Lauryn, SIVAKARAN Kowsikan", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
groupe.pack()

annee = Label(bot, text="Dans le cadre du projet ISN 2018 - 2019", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
annee.pack()

lycee = Label(bot, text="Lycée Lucie Aubrac", bg='#ba482d', fg='#ffffff', font=("Courrier","14"))
lycee.pack()

bot.pack(expand=YES)

root.mainloop()