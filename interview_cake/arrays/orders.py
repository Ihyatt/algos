def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    #reverse done to mimick stacks
    take_out_orders.reverse()
    dine_in_orders.reverse()
    
    for i in range(len(served_orders)):
        if take_out_orders and served_orders[i] == take_out_orders[-1]:
            take_out_orders.pop()
        elif dine_in_orders and served_orders[i] == dine_in_orders[-1]:
            dine_in_orders.pop()
        else:
            return False
    
    
    
    return not dine_in_orders and not take_out_orders #check corner cases to verify all orders have been checked