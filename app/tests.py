from django.test import SimpleTestCase


class TestHowOld(SimpleTestCase):
    def test_how_old(self):
        response = self.client.get('/age-in/2050/2000')
        self.assertContains(response, 50)

class TestCanITakeYourOrder(SimpleTestCase):
    def test_can_i_take_your_order_111(self):
        response = self.client.get('/order-total/1/1/1')
        self.assertContains(response, 7.0)

    def test_can_i_take_your_order_000(self):
        response = self.client.get('/order-total/0/0/0')
        self.assertContains(response, 0.0)

    def test_can_i_take_your_order_432(self):
        response = self.client.get('/order-total/4/3/2')
        self.assertContains(response, 24.5)
























# class TestHelloWorldView(SimpleTestCase):
#     def test_hello_world_view(self):
#         response = self.client.get('/hello/')
#         self.assertContains(response, "Hello World!")

# class TestHelloView(SimpleTestCase):
#     def test_hello_nate(self):
#         response = self.client.get('/hello_nate/')
#         self.assertContains(response, 'Hello nate')

# class TestAddView(SimpleTestCase):
#     def test_add_1_to_4(self):
#         response = self.client.get('/add/1/4')
#         self.assertContains(response, 5)

# class TestAddView(SimpleTestCase):
#     def test_add_9_123(self):
#         response = self.client.get('/add/9/123')
#         self.assertContains(response, 132)

# class TestHeyYou(SimpleTestCase):
#     def test_hey_nate(self):
#         response = self.client.get("/hey/nate")
#         self.assertContains(response, "Hello, nate!")

#     def test_hey_bcca(self):
#         response = self.client.get("/hey/BCCA")
#         self.assertContains(response, "Hello, BCCA!")


# class TestAgeIn(SimpleTestCase):
#     def test_age_in_2050_born_2000(self):
#         response = self.client.get("/age-in/2050/2000")
#         self.assertContains(response, "50")

#     def test_age_in_2050_born_0(self):
#         response = self.client.get("/age-in/2050/0")
#         self.assertContains(response, "2050")

#     def test_age_in_2010_born_1995(self):
#         response = self.client.get("/age-in/2010/1995")
#         self.assertContains(response, "15")

#     def test_age_in_1950_born_1920(self):
#         response = self.client.get("/age-in/1950/120")
#         self.assertContains(response, "30")


# class TestOrderTotal(SimpleTestCase):
#     def test_order_total_0_0_0(self):
#         response = self.client.get("/order-total/0/0/0")
#         self.assertContains(response, "0.0")

#     def test_order_total_1_1_1(self):
#         response = self.client.get("/order-total/1/1/1")
#         self.assertContains(response, "7.0")

#     def test_order_total_2_3_4(self):
#         response = self.client.get("/order-total/2/3/4")
#         self.assertContains(response, "17.5")

#     def test_order_total_4_3_2(self):
#         response = self.client.get("/order-total/4/3/2")
#         self.assertContains(response, "24.5")

# class TestNearHundred(SimpleTestCase):
#     def test_near_hundred_93(self):
#         response = self.client.get('/warmup-1/near-hundred/93')
#         self.assertContains(response, True)

#     def test_near_hundred_76(self):
#         response = self.client.get('/warmup-1/near-hundred/76')
#         self.assertContains(response, False)

#     def test_near_hundred_0(self):
#         response = self.client.get('/warmup-1/near-hundred/0')
#         self.assertContains(response, False)

#     def test_near_hundred_108(self):
#         response = self.client.get('/warmup-1/near-hundred/108')
#         self.assertContains(response, True)

#     def test_near_hundred_199(self):
#         response = self.client.get('/warmup-1/near-hundred/199')
#         self.assertContains(response, True)

# class TestStringSplosion(SimpleTestCase):
#     def test_string_splosion_pedunculated(self):
#         response = self.client.get('/warmup-2/string-splosion/pedunculated')
#         self.assertContains(response, "ppepedpedupedunpeduncpeduncupedunculpedunculapedunculatpedunculatepedunculated")

#     def test_string_splosion_mom(self):
#         response = self.client.get('/warmup-2/string-splosion/mom')
#         self.assertContains(response, 'mmomom')

#     def test_string_splosion_wander(self):
#         response = self.client.get('/warmup-2/string-splosion/wander')
#         self.assertContains(response, 'wwawanwandwandewander')

# class TestCatDog(SimpleTestCase):
#     def test_cat_dog_catdogmousecatdogmouse(self):
#         response = self.client.get('/string-2/cat-dog/catdogmousecatdogmouse')
#         self.assertContains(response, True)

#     def test_cat_dog_catrabbitdogcatdogcatrabbit(self):
#         response = self.client.get('/string-2/cat-dog/catrabbitdogcatdogcatrabbit')
#         self.assertContains(response, False)

#     def test_cat_dog_dogcatfishcatdogdogcatfish(self):
#         response = self.client.get('/string-2/cat-dog/dogcatfishcatdogdogcatfish')
#         self.assertContains(response, True)

# class TestLoneSum(SimpleTestCase):
#     def test_lone_sum_385(self):
#         response = self.client.get('/logic-2/lone-sum/3_8_5')
#         self.assertContains(response, 16)

#     def test_lone_sum_101010(self):
#         response = self.client.get('/logic-2/lone-sum/10_10_10')
#         self.assertContains(response, 0)

#     def test_lone_sum_10103(self):
#         response = self.client.get('/logic-2/lone-sum/10_10_3')
#         self.assertContains(response, 3)

#     def test_lone_sum_10310(self):
#         response = self.client.get('/logic-2/lone-sum/10_4_10')
#         self.assertContains(response, 4)

#     def test_lone_sum_10544(self):
#         response = self.client.get('/logic-2/lone-sum/105_4_4')
#         self.assertContains(response, 105)