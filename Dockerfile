# Derivando da imagem oficial do postgres
FROM postgres

# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/
