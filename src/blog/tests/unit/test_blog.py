from blog.models import sum_all


def test_add():
    assert sum_all(1, 2, 3, 4) == 10
