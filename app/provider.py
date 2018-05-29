from app.models import session, User

query = session.query


def get_user_by_email(email):
    """
    Return user by email or None
    :param email: String
    :return object:
    """
    return query(User).filter_by(email=email).first() or None


def create_user(email, password, first_name, last_name):
    """
    Create a new user

    :param email: String
    :param password: String
    :param first_name: String
    :param last_name: String
    :return object:
    """
    user = User(email=email, first_name=first_name, last_name=last_name)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return user
