from app.models import session, User

query = session.query


def get_user_by_email(email):

    return query(User).filter_by(email=email).first() or None
