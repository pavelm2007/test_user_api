import pytest

pytestmark = [pytest.mark.django_db]


def test_get_current_user_view(as_user):
    got = as_user.get('/api/user/')

    assert got['age'] == as_user.user.age
    assert got['first_name'] == as_user.user.first_name
    assert got['gender'] == as_user.user.gender
    assert got['last_name'] == as_user.user.last_name


def test_edit_current_user_view(as_user):
    got = as_user.patch('/api/user/', {
        'age': 99,
        'first_name': 'Luna',
        'gender': 'female',
        'last_name': 'Jagdeep',
    }, expected_status=202)

    assert got['age'] == 99
    assert got['first_name'] == 'Luna'
    assert got['gender'] == 'female'
    assert got['last_name'] == 'Jagdeep'


def test_anon_cant_view_user(as_anon):
    as_anon.get('/api/user/', expected_status=401)
