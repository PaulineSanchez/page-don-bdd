import mysql.connector as mysqlpyth

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    
    bdd = mysqlpyth.connect(user='root', password='root', host='localhost', port="8081", database='asso')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def lire_posts():
    global cursor

    connexion()
    #query = "SELECT * FROM donnateurs JOIN don_materiel ON donnateurs.don_mat = don_materiel.don_mat JOIN don_temps ON donnateurs.don_tps = don_temps.don_tps"

    #query = "SELECT id_donnateur, nom, prenom, email, telephone, don_fin, don_mat, don_tps FROM donnateurs INNER JOIN don_materiel ON donnateurs.don_mat = don_materiel.don_mat INNER JOIN don_temps ON donnateurs.don_tps = don_temps.don_tps"

    query = "SELECT * FROM donnateurs"

    cursor.execute(query)
    donnateurs = []

    for enregistrement in cursor :
        don = {}
        don['id_donnateur'] = enregistrement[0]
        don['nom'] = enregistrement[1]
        don['prenom'] = enregistrement[2]
        don['email'] = enregistrement[3]
        don['telephone'] = enregistrement[4]
        if enregistrement[5] and enregistrement[5] != 0:
            don['don_fin'] = f"{enregistrement[5]} €"
        if enregistrement[6] != "Rien" and enregistrement[6] != "":
            don['don_tps'] = f'"{enregistrement[6]}"'
        if enregistrement[7] != "Rien" and enregistrement[7] != "":
            don['don_mat'] = f'"{enregistrement[7]}"' 
        donnateurs.append(don)

    deconnexion()
    return donnateurs


def insert_don(nom, prenom, email, tel, montant, typetemps, typemateriel):
    global cursor
    global bdd

    connexion()

    if montant == "":
        montant = 0

    query = f"""INSERT INTO donnateurs(nom, prenom, email, telephone, don_fin, don_tps, don_mat) VALUES ('{nom}','{prenom}', '{email}', '{tel}', '{montant}', '{typetemps}', '{typemateriel}');"""

    cursor.execute(query)
    bdd.commit()

    deconnexion()


def get_don():
    global cursor
    global bdd

    connexion()

    query = "SELECT don_fin FROM donnateurs"

    cursor.execute(query)
    dons = cursor.fetchall()
    total = []

    for chaque_don in dons:
        if chaque_don[0]:
            total.append(int(chaque_don[0]))

    deconnexion()
    return sum(total)


    