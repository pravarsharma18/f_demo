from flask import jsonify
from api.db.users import User
from conf.database import db
from conf.database import bcrypt


def get_all_users():
    users = db.session.query(User).all()
    users_list = []
    for user in users:
        users_list.append({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
    return jsonify({"users": users_list})


def add_a_users(data):
    if not data.get('username'):
        return jsonify({"username": "Username Field is required."}), 400
    if not data.get('email'):
        return jsonify({"email": "Email Field is required."}), 400
    if not data.get('password'):
        return jsonify({"password": "Password Field is required."}), 400
    if db.session.query(User).filter_by(username=data.get('username')).first():
        return jsonify({"username": "Username already taken, choose another."}), 400

    hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    user = User(username=data.get('username'), email=data.get('email'),
                password=hashed_password, is_superuser=False,
                is_active=True)
    db.session.add(user)
    db.session.commit()

    return jsonify({"user": "Successfully Created"}), 201


def get_single_user(id):
    user = db.session.query(User).filter_by(id=id).first()
    if not user:
        return jsonify({"user": "User Not Found"}), 400
    data = {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
    return jsonify({"user": data}), 200


def update_single_user(id, data):
    user = db.session.query(User).filter_by(id=id)
    user.update(data)
    db.session.commit()
    return jsonify({"user": data}), 200
