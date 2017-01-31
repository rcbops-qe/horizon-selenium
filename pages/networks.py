import basepage
from selenium.webdriver.support.ui import Select


class NetworksPageObjects(basepage.BasePage):

    def click_create_network(self):
        self.driver.find_element_by_id(
            'networks__action_create').click()

    def click_delete_networks(self):
        self.driver.find_element_by_id(
            'networks__action_delete').click()

    def click_edit_network(self):
        self.driver.find_element_by_class_name(
            'data-table-action').click()

    def network_dropdown_actions(self):
        pass
    
    """
    Seach Filter Options
    """
    def search_networks(self, criteria, text):
        self.select_filter_criteria(criteria)
        self.input_filter_text(text)
        self.click_filter_button()

    def is_network_present(self, text):
        self.search_networks(criteria='name', text=text)
        net_table = self.driver.find_element_by_id('networks')
        net = net_table.find_element_by_css_selector('tbody tr')
        if net.text == "u'No items to display.'":
            return False
        else:
            net_name = net.get_attribute('data-display')
            if net_name == text:
                return True
            else:
                return False

    def click_filter_dropdown(self):
        self.driver.find_element_by_css_selector(
            '.table_actions .themable-select .btn').click()

    def select_filter_criteria(self, criteria='name'):
        """
        :param string criteria: potential options
        name, shared, router:external, status, admin_state_up
        """
        self.click_filter_dropdown()
        self.driver.find_element_by_css_selector(
            'a[data-select-value="{0}"]'.format(criteria)).click()

    def click_filter_button(self):
        self.driver.find_element_by_id(
            'networks__action_filter_project_networks').click()

    def input_filter_text(self, text):
        text_field = self.driver.find_element_by_name(
            'networks__filter_project_networks__q')
        text_field.clear()
        text_field.send_keys(text)

    """
    Create Network Form
    """
    def click_cancel(self):
        self.driver.find_element_by_class_name('cancel').click()

    def click_back(self):
        self.driver.find_element_by_class_name('button-previous').click()

    def click_next(self):
        self.driver.find_element_by_class_name('button-next').click()

    def click_create(self):
        self.driver.find_element_by_class_name('button-final').click()

    def input_network_name(self, text):
        text_field = self.driver.find_element_by_name(
            'net_name')
        text_field.clear()
        text_field.send_keys(text)

    def select_admin_state(self, state='True'):
        self.driver.find_element_by_css_selector(
            '.form-control .dropdown-toggle').click()
        self.driver.find_element_by_css_selector(
            'a[data-select-value="{0}"]'.format(state)).click()

    def input_subnet_name(self, text):
        text_field = self.driver.find_element_by_name(
            'subnet_name')
        text_field.clear()
        text_field.send_keys(text)

    def input_network_address(self, text):
        text_field = self.driver.find_element_by_name(
            'cidr')
        text_field.clear()
        text_field.send_keys(text)

    def input_gateway_ip(self, text):
        text_field = self.driver.find_element_by_name(
            'gateway_ip')
        text_field.clear()
        text_field.send_keys(text)

    def select_ip_version(self, version='4'):
        ipv = Select(self.driver.find_element_by_id('id_ip_version'))
        if version == '4':
            ipv.select_by_value('4')
        elif version == '6':
            ipv.select_by_value('6')
        else:
            print "Valid options are 4 and 6. {0} was provided".format(version)

    def input_allocation_pools(self, text):
        text_field = self.driver.find_element_by_name(
            'allocation_pools')
        text_field.clear()
        text_field.send_keys(text)

    def input_dns_name_servers(self, text):
        text_field = self.driver.find_element_by_name(
            'dns_nameservers')
        text_field.clear()
        text_field.send_keys(text)

    def input_host_routes(self, text):
        text_field = self.driver.find_element_by_name(
            'host_routes')
        text_field.clear()
        text_field.send_keys(text)

    def create_network(self, text):
        state = self.is_network_present(text)
        if state is True:
            print "Network already exists."
        else:
            self.click_create_network()
            self.input_network_name(text)
            self.select_admin_state()
            self.click_next()
            self.input_subnet_name(text='{0}-subnet'.format(text))
            self.input_network_address('192.168.8.0/24')
            self.select_ip_version()
            self.click_next()
            self.click_create()

    def toggle_shared_checkbox(self):
        pass

    def toggle_create_shortcut_checkbox(self):
        pass

    def toggle_disable_gateway_checkbox(self):
        pass

    def toggle_enable_dhcp(self):
        pass
