import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture()
def user_list(factory):
    return factory.cycle(5).user()


@pytest.fixture()
def user_list_with_38_age(factory):
    return factory.cycle(5).user(age=38)


def test_get_user_ids_list(user_list, as_user):
    got = as_user.get('/api/users/')

    assert set(got) == set([x.id for x in user_list] + [as_user.user.id, ])  # noqa


def test_get_user_filtered_list(user_list_with_38_age, as_user):
    got = as_user.get('/api/users/', {'age': 38})

    assert set(got) == set([x.id for x in user_list_with_38_age])


def test_user_by_id(as_user):
    got = as_user.get(f'/api/users/{as_user.user.id}/')

    assert got['age'] == as_user.user.age
    assert got['first_name'] == as_user.user.first_name
    assert got['gender'] == as_user.user.gender
    assert got['last_name'] == as_user.user.last_name


def test_anon_cant_view_users(as_anon):
    as_anon.get('/api/users/', expected_status=401)
