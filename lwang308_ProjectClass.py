# Li Kuei Wang CIS345 12:00PM Project

Orders = []


class Orders():

    def __init__(self, order_time='', order_num='', order_name='', order_phone=0, order_cost=0.0, doubos_num=0,
                 cheebos_num=0, hambos_num=0, double_num=0, cheese_num=0, ham_num=0, fries_num=0, softdrinks_num=0,
                 softdrinkm_num=0, softdrinkl_num=0, softdrinkxl_num=0, chocoshakes_num=0, strawshakes_num=0,
                 vanishakes_num=0, order_note=''):

        self.order_time = order_time
        self.order_num = order_num
        self.order_name = order_name
        self.order_phone = order_phone
        self.order_cost = order_cost
        self.doubos_num = doubos_num
        self.cheebos_num = cheebos_num
        self.hambos_num = hambos_num
        self.double_num = double_num
        self.cheese_num = cheese_num
        self.ham_num = ham_num
        self.fries_num = fries_num
        self.softdrinks_num = softdrinks_num
        self.softdrinkm_num = softdrinkm_num
        self.softdrinkl_num = softdrinkl_num
        self.softdrinkxl_num = softdrinkxl_num
        self.chocoshakes_num = chocoshakes_num
        self.strawshakes_num = strawshakes_num
        self.vanishakes_num = vanishakes_num
        self.order_note = order_note

    def __str__(self):
        return f'\n\nOrder Time: {self.order_time}\n' \
               f'Order Number: {self.order_num}\n' \
               f'Order Name: {self.order_name}\n' \
               f'Phone Number: {self.order_phone}\n' \
               f'Order Cost:{self.order_cost}\n\n'\
               f'{self.doubos_num}*DOUBLE-DOUBLE COMBOS\t{self.softdrinks_num}*SOFT DRINK (S)\n' \
               f'{self.cheebos_num}*CHEESEBURGER COMBOS\t{self.softdrinkm_num}*SOFT DRINK (M)\n' \
               f'{self.hambos_num}*HAMBURGER COMBOS\t\t{self.softdrinkl_num}*SOFT DRINK (L)\n' \
               f'{self.double_num}*DOUBLE-DOUBLE\t\t{self.softdrinkxl_num}*SOFT DRINK (XL)\n' \
               f'{self.cheese_num}*CHEESEBURGER\t\t{self.chocoshakes_num}*CHOCOLATE SHAKES\n' \
               f'{self.ham_num}*HAMBURGER\t\t          {self.strawshakes_num}*STRAWBERRY SHAKES\n' \
               f'{self.fries_num}*FRENCH FRIES\t\t\t{self.vanishakes_num}*VANILLA SHAKES\n\n' \
               f'p.s. {self.order_note}\n\n'