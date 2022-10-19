from broccoli.services import UserService

def test_can_add_broccoli_user():
    us: UserService = UserService()
    uname = "test123"

    assert not us.has_user(uname)
    us.add_user(uname)
    assert us.has_user(uname)
