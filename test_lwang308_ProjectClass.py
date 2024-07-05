from lwang308_ProjectClass import Orders


class TestOrders:

    # test __str__
    def test_details(self):
        o = Orders("Tue Apr 18 20:03:28 2023", 8076, "Kevin Wang", 1234567890, 12.00, 0, 0, 0, 5, 0, 3, 0, 0, 1, 0, 0,
                   0, 0, 0, "Protein Style")
        print("Testing details: Orders")
        assert ("Tue Apr 18 20:03:28 2023", 8076, "Kevin Wang", 1234567890, 12.00,
                0, 0, 0, 5, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, "Protein Style") == (o.order_time, o.order_num,
                                                                               o.order_name, o.order_phone,
                                                                               o.order_cost, o.doubos_num,
                                                                               o.cheebos_num, o.hambos_num,
                                                                               o.double_num, o.cheese_num,
                                                                               o.ham_num, o.fries_num,
                                                                               o.softdrinks_num, o.softdrinkm_num,
                                                                               o.softdrinkl_num, o.softdrinkxl_num,
                                                                               o.chocoshakes_num, o.strawshakes_num,
                                                                               o.vanishakes_num, o.order_note)

