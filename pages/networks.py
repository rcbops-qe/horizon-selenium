import basepage


class NetworksPageObjects(basepage.BasePage):

    def click_create_network(self):
        self.driver.find_element_by_id(
            'networks__action_create').click()

    def click_delete_networks(self):
        self.driver.find_element_by_id(
            'networks__action_delete').click()


class CreateNetwork(basepage.BasePage):

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
            'id_net_name')
        text_field.clear()
        text_field.send_keys(text)

    def select_admin_state(self, state='True'):
        self.driver.find_element_by_css_selector(
            '.form-control .dropdown-toggle').click()
        self.driver.find_element_by_css_selector(
            'a[data-select-value="{0}"]'.format(state)).click()


class FilterNetworks(basepage.BasePage):

    def search_networks(self, criteria, text):
        self.select_filter_criteria(criteria)
        self.input_filter_text(text)
        self.click_filter_button()

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

