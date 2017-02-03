import basesetup
import time
import unittest
from pages import networks, instances, loginpage, navigation_bars


class TestInstance(unittest.TestCase, basesetup.BaseSetup):

    def setUp(self):
        self.login_with_credentials()

    def test_create_instance(self, text='succeed1'):
        nav = navigation_bars.NavigationBars(self.driver)
        net = networks.NetworksPageObjects(self.driver)
        inst = instances.InstancesPageObject(self.driver)
        nav.click_project_network_networks()
        net.create_network(text)
        nav.click_project_compute_instance()
        inst.create_default_instance(text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
