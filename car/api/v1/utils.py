'''
Module: shared_variables
'''
from datetime import date, datetime


def get_greeting():
    '''Say User Good Morning/Good Afternoon/Good Eveninig'''
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 17:
        return "Good Afternoon!"
    elif 17 <= hour < 21:
        return "Good Evening!"
    else:
        return "Welcome!"
    
    
def calculate_total_price(daily_price, start_date, end_date):
    try:
        start_date_obj = date.fromisoformat(start_date)
        end_date_obj = date.fromisoformat(end_date)

        duration_days = (end_date_obj - start_date_obj).days

        daily_price = float(daily_price)

        total_price = daily_price * duration_days

        return total_price
    except Exception as e:
        print(f"Error calculating total price: {e}")
        return 0

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_rating = sum(review.rating for review in reviews)
    return total_rating / len(reviews)