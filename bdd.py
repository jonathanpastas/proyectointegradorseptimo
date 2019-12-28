
import psycopg2

db = psycopg2.connect(host="localhost", database="proyecto", user="postgres", password="1234")
#cur = db.cursor()

def queryDatos(user,contra):
    sql = "SELECT * FROM usuarios WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        email=row[2]
        contrasenia=row[3]

        print(email)
        print(contrasenia)
        if email == user and contrasenia == contra:
            return True
        else:
            return False

def perfiluser(user):
    sql = "SELECT * FROM usuarios WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        perfil = row[4]
    return perfil



def menuopciones(perfil):
    sql="select descripcion,url from perfilxpagina,pagina where perfilxpagina.id_pagina=pagina.id_pagina and id_perfil = "+str(perfil)
    print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data


