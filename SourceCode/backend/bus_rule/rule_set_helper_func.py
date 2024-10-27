### Checks for: Customer Type Discount
def is_standard_customer(customer_type):
    return customer_type == 'standard'

def is_silver_customer(customer_type):
    return customer_type == 'silver'

def is_gold_customer(customer_type):
    return customer_type == 'gold'

def is_platinum_customer(customer_type):
    return customer_type == 'platinum'

### Checks for: Room Type Pricing

def is_single_room(room_type):
    return room_type == 'single'

def is_double_room(room_type):
    return room_type == 'double'

def is_delux_room(room_type):
    return room_type == 'delux'

def is_presidential_suite(room_type):
    return room_type == 'presidential suite'

### Checks for: Holiday Sale Rules

def is_no_sale_discount(sale):
    return sale == 'none'

def is_blackfriday_discount(sale):
    return sale == 'black friday'

def is_singlesday_discount(sale):
    return sale == 'singles day'

def is_boxingday_discount(sale):
    return sale == 'boxing day'