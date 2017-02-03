import basepage
import time
from selenium.webdriver.support.ui import Select


class InstancesPageObject(basepage.BasePage):

    def click_launch_instance(self):
        self.driver.find_element_by_id(
            'instances__action_launch-ng').click()

    """
    Search and Filter section
    """
    def search_instances(self, criteria, text):
        self.select_filter_criteria(criteria)
        self.input_filter_text(text)
        self.click_filter_button()

    def is_instance_present(self, text):
        self.search_instances(criteria='name', text=text)
        net_table = self.driver.find_element_by_id('instances')
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
        name, status, image, flavor
        """
        self.click_filter_dropdown()
        self.driver.find_element_by_css_selector(
            'a[data-select-value="{0}"]'.format(criteria)).click()

    def click_filter_button(self):
        self.driver.find_element_by_id(
            'instances__action_filter').click()

    def input_filter_text(self, text):
        text_field = self.driver.find_element_by_name(
            'instances__filter__q')
        text_field.clear()
        text_field.send_keys(text)

    """
    Launch instance forms
    """
    def click_cancel(self):
        self.driver.find_element_by_css_selector(
            '.modal-footer .pull-left').click()

    def click_back(self):
        self.driver.find_element_by_css_selector('.back').click()

    def click_next(self):
        self.driver.find_element_by_css_selector('.next').click()

    def click_launch_instance_wizard_button(self):
        self.driver.find_element_by_css_selector('.finish').click()

    def input_instance_name(self, text):
        text_field = self.driver.find_element_by_id('name')
        text_field.clear()
        text_field.send_keys(text)

    def select_availability_zone(self, zone='nova'):
        pass

    def select_instance_count(self, count='1'):
        inst_count = self.driver.find_element_by_css_selector(
            '#instance-count')
        inst_count.clear()
        inst_count.send_keys(count)

    def select_boot_source(self, source='image'):
        """
        :param string source: potential options
        image, snapshot, volume, volume_snapshot
        """
        boot_source = Select(self.driver.find_element_by_css_selector(
            '#boot-source-type'))
        boot_source.select_by_value(source)

    def select_first_image_source(self):
        self.driver.find_elements_by_css_selector(
            'hz-magic-search-context > table.table-rsp '
            '> tbody td.actions_column')[0].click()

    def select_first_flavor(self):
        self.driver.find_elements_by_css_selector(
            'hz-magic-search-context > table.table-rsp '
            '> tbody td.action-col')[0].click()

    def select_first_network(self):
        self.driver.find_elements_by_css_selector(
            'table.table-rsp > tbody td.actions_column '
            'action-list.ng-isolate-scope')[0].click()

    def create_default_instance(self, text):
        state = self.is_instance_present(text)
        if state is True:
            print "Instance already exists."
        else:
            print "Instance did not exist."
            self.click_launch_instance()
            self.input_instance_name(text)
            self.click_next()
            self.select_boot_source(source='image')
            self.select_first_image_source()
            self.click_next()
            self.select_first_flavor()
            self.click_next()
            self.select_first_network()
            self.click_launch_instance_wizard_button()
            time.sleep(5)
