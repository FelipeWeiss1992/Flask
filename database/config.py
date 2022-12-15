SECRET_KEY = 'moredevs'

#string conexao
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "felipeweiss",
    senha = "1234",
    servidor = "localhost:5433",
    database = "postgres"
)