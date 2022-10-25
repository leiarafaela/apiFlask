from bd import users

class User():
    def getAll():
        return users

    def getById(user_id):
        for user in users:
            if user['id'] == user_id:
                return user

    def create(user):
        users.append(user)

    def delete(user_id):
        for user in users:
            if user['id'] == user_id:
                users.remove(user)

    def update(id, body):
        for user in users:
            if user['id'] == id:
                user['nome'] = body['nome']
                user['email'] = body['email']
                user['cel'] = body['cel']
