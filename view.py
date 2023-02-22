import sqlite3 as lite

con = lite.connect('dados.db')

#inserir
def insertInfomations(i):
    
    with con:
        cur = con.cursor()
        query = 'INSERT INTO formulario (nome , telefone , endereco, data, notas) VALUES (?,?,?,?,?)'
        cur.execute(query, i)

#--showinformarions--------
def show():
    lista = []

    with con:
        cur = con.cursor()
        query = 'SELECT * FROM formulario'
        cur.execute(query)
        infomation = cur.fetchall()
        
        for i in infomation:
            lista.append(i)           
    return lista
    
#Atualizar info
def atualizar_info(i):
    
    with con:
        cur = con.cursor()
        query = 'UPDATE formulario SET nome=?, telefone=?, endereco=?, data=?, notas=? WHERE id=?'
        con.execute(query,i)     

    #Deletar info
    

def delete_info(i):
    
    with con:
        cur = con.cursor()
        query = 'DELETE FROM formulario WHERE id=?'
        cur.execute(query,i)
        

def showinfoInDisplayTwo():
    lista = []

    with con:
        cur = con.cursor()
        query = 'SELECT * FROM formulario'
        cur.execute(query)
        infomation = cur.fetchall()
        
        for i in infomation:
            print(i)        
    return lista


