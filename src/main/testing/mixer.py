import uuid

from mixer.backend.django import mixer  # type: ignore

__all__ = [
    mixer,
]


def _random_user_name() -> str:
    return str(uuid.uuid4())


def _random_email() -> str:
    uuid_as_str = str(uuid.uuid4()).replace('-', '_')
    return f'{uuid_as_str}@mail.com'


mixer.register(
    'users.User',
    username=_random_user_name,
    email=_random_email,
    password=mixer.SKIP,
    referred_by=mixer.SKIP,
)
