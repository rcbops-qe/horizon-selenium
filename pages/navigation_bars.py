import basepage


class NavigationBars(basepage.BasePage):

    def expand_project_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()

    def click_admin_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-admin"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()

    def click_identity_panel(self):
        self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-identity"]').click()

    def click_developer_panel(self):
        self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-developer"]').click()

    def click_project_compute(self):
        self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project-compute"]').click()

    def click_project_compute_instance(self):
        self.driver.find_element_by_css_selector(
            'a[href="/project/instances/"]').click()