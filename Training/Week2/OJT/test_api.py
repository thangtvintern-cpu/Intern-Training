
from datetime import datetime,timezone
from controller import get_user_by_id,get_total_price_by_user_id
def test_get_user_by_id():
    user_id = 'm6zc646sqc8akVQSnJfecq'
    user = {'user_id': 'm6zc646sqc8akVQSnJfecq',
            'purchase_id': 'Gxx5DQkbvYiSrdUuWLQYEa', 
            'package_id': 'eTRQCWWZcPLZ4kbCZGqmTj', 
            'tenant_id': '', 
            'purchased_date': datetime(2024, 10, 8, 3, 44, 2, 544830, tzinfo=timezone.utc), 
            'stock_category': '16時', 
            'attribute': {'name01': '大人', 'price01': 3000, 'value01': 4}, 
            'assign_point': 0,
            'point': 0,
            'have_value': 4}
    assert get_user_by_id(user_id) == user


def test_get_total_price_by_user_id():
    user_id = 'm6zc646sqc8akVQSnJfecq'
    assert get_total_price_by_user_id(user_id) == 12000