import psycopg2

print("Testando...")

try:
    conn = psycopg2.connect(host = "localhost",
    port ="5433",
    database = "postgres", 
    user="felipeweiss", password = "1234")
    print('VOCE ESTA CONECTADO............')

except Exception:
    print('VOCE ESTA SEM CONEXAO..........')


if conn is not None:
    
    print('Sua Conexao está estabilizada!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE  pessoas (id serial, nome VARCHAR(15)NOT NULL, idade integer NOT NULL, altura float NOT NULL, PRIMARY KEY(id));')
    print('Sua tabela pessoas foi criada!')

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30) NOT NULL,  PRIMARY KEY(nickname) );')
    print('Sua tabela usuarios foi criada!')

    conn.commit()
    cursor.close()
    conn.close()