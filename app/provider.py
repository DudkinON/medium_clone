from app.models import session, User

query = session.query


def get_user_by_email(email):
    """
    Return user by email or None
    :param email: String
    :return object:
    """
    return query(User).filter_by(email=email).first() or None
