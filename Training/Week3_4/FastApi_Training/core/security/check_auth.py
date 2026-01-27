

from repository.user_repository import get_user_repository
def check_auth(access_token):
    return get_user_repository().check_auth(access_token)