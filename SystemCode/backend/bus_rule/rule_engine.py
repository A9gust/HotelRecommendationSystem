#### GC IRS Business Rule Engine (Group 5)

# Reference:
# https://pypi.org/project/business-rule-engine/

### Dictionary to Hold Order Details
# order_details(booking_start_string, booking_end_string, price_of_single_room, number_of_room=1, customer_type='standard', room_type='single', sale = 'none') <br>
# **booking_start_string**: dtring, example: "1 jan 2024"
# **booking_end_string**: string,  "5 jan 2024"
# **price_of_single_room**: int 
# **number_of_room**: int, default=1 
# **customer_type**: string, ['standard', 'silver', 'gold', 'platinum'], default = 'standard' 
# **room_type**: string, ['single', 'double', 'delux', 'presidential suite'], default = 'single'
# **sale**: string, ['none', 'black friday', 'singles day', 'boxing day'], default = 'none'

# Install Packages (As Required)
# !pip install business-rule-engine
# !pip install holidays==0.58

from datetime import datetime
from business_rule_engine import RuleParser
from .rule_set_helper_func import *
from .calculate import *

### Define Required Functions
def order_details(booking_start_string, booking_end_string, price_of_single_room, number_of_room=1, customer_type='standard', room_type='single', sale = 'none'):
    start_date_object = datetime.strptime(booking_start_string, "%Y-%m-%d").date()
    end_date_object = datetime.strptime(booking_end_string, "%Y-%m-%d").date()
    number_of_days = abs((end_date_object - start_date_object).days) + 1
    order_details = {
      'booking_start_date' : start_date_object,
      'booking_end_date' : end_date_object,
      'price_of_single_room': price_of_single_room,
      'number_of_room': number_of_room,
      'customer_type': customer_type,
      'room_type': room_type,
      'sale': sale,
      # derived values
      'number_of_days' : number_of_days,
      'holiday_count' : count_holidays_in_range(start_date_object, end_date_object),
      'customer_price' : calculate_base_price(number_of_days, price_of_single_room, number_of_room)
    }
    return order_details


def calculate_discount(rate):
    order['customer_price'] = order['customer_price'] * rate


def calculate_holiday_surcharge():
    order['customer_price'] = order['customer_price'] + (order['price_of_single_room'] * order['holiday_count'] * order['number_of_room'])


# Import Business Rules
try:
    file_path = './bus_rule/customer_type_rules.txt'
    with open(file_path, 'r') as file:
        customer_type_rules = file.read()

    file_path = './bus_rule/room_type_rules.txt'
    with open(file_path, 'r') as file:
        room_type_rules = file.read()

    file_path = './bus_rule/sale_discount_rules.txt'
    with open(file_path, 'r') as file:
        sale_discount_rules = file.read()

    file_path = './bus_rule/holiday_surcharge_rule.txt'
    with open(file_path, 'r') as file:
        holiday_surcharge_rule = file.read()
except OSError as e:
    print(e)


# Initialize Rule Parser
def parser_init(rule_set):
    parser = RuleParser()

    parser.register_function(calculate_discount)
    parser.register_function(calculate_holiday_surcharge)

    parser.register_function(is_standard_customer)
    parser.register_function(is_silver_customer)
    parser.register_function(is_gold_customer)
    parser.register_function(is_platinum_customer)

    parser.register_function(is_single_room)
    parser.register_function(is_double_room)
    parser.register_function(is_delux_room)
    parser.register_function(is_presidential_suite)

    parser.register_function(is_no_sale_discount)
    parser.register_function(is_blackfriday_discount)
    parser.register_function(is_singlesday_discount)
    parser.register_function(is_boxingday_discount)

    parser.parsestr(rule_set)

    return parser


with open("./bus_rule/order.txt", "r") as file:
    content = file.read().strip()
    order = content.split(", ")
checkInDate = order[0]
checkOutDate = order[1]
number_of_room = int(order[2])
member = order[3]

order = order_details(checkInDate, checkOutDate, 100, number_of_room=number_of_room, customer_type=member, room_type = 'double', sale = 'singles day')


def test_rule(order):
    try:
        # 1st Rule Set
        org = order['customer_price']
        parser = parser_init(customer_type_rules)
        ret = parser.execute(order)
        pri_1 = order['customer_price']
        if ret is False:
            print("No conditions matched")
        # 2nd Rule Set
        parser = parser_init(room_type_rules)
        ret = parser.execute(order)
        pri_2 = order['customer_price']
        if ret is False:
            print("No conditions matched")
        # 3rd Rule Set
        parser = parser_init(sale_discount_rules)
        ret = parser.execute(order)
        pri_3 = order['customer_price']
        if ret is False:
            print("No conditions matched")
        # 4th Rule Set
        parser = parser_init(holiday_surcharge_rule)
        ret = parser.execute(order)
        pri_4 = order['customer_price']
        if ret is False:
            print("No conditions matched")
        minimum_value = min(pri_1, pri_2, pri_3, pri_4)
        print(pri_1)
        print(org)
        rate = pri_1 / org
        return rate
    except ValueError as e:
        print(e)


def result():
    return test_rule(order)


if __name__ == "__main__":
    print(test_rule(order))
