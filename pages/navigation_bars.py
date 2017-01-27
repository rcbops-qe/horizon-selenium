import basepage


class NavigationBars(basepage.BasePage):

    def expand_project_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def expand_admin_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-admin"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def expand_identity_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-identity"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def expand_developer_panel(self):
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-developer"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    """
    Project > Compute > Resource
    """

    def expand_project_compute(self):
        NavigationBars.expand_project_panel(self)
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project-compute"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def click_project_compute_overview(self):
        NavigationBars.expand_project_compute(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/"]').click()

    def click_project_compute_instance(self):
        NavigationBars.expand_project_compute(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/instances/"]').click()

    def click_project_compute_volumes(self):
        NavigationBars.expand_project_compute(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/volumes/"]').click()

    def click_project_compute_images(self):
        NavigationBars.expand_project_compute(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/images/"]').click()

    def click_project_compute_access_and_security(self):
        NavigationBars.expand_project_compute(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/access_and_security/"]').click()

    """
    Project > Network > Resource
    """

    def expand_project_network(self):
        NavigationBars.expand_project_panel(self)
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project-network"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def click_project_network_network_topology(self):
        NavigationBars.expand_project_network(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/network_topology/"]').click()

    def click_project_network_networks(self):
        NavigationBars.expand_project_network(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/networks/"]').click()

    def click_project_network_routers(self):
        NavigationBars.expand_project_network(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/routers/"]').click()

    def click_project_network_loadbalancers(self):
        NavigationBars.expand_project_network(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/ngloadbalancersv2/"]').click()

    """
    Project > Orchestration > Resource
    """

    def expand_project_orchestration(self):
        NavigationBars.expand_project_panel(self)
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project-orchestration"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def click_project_orchestration_stacks(self):
        NavigationBars.expand_project_orchestration(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/stacks/"]').click()

    def click_project_orchestration_resource_types(self):
        NavigationBars.expand_project_orchestration(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/stacks/resource_types/"]').click()

    def click_project_orchestration_template_versions(self):
        NavigationBars.expand_project_orchestration(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/stacks/template_versions/"]').click()

    """
    Project > Object Store > Resource
    """

    def expand_project_object_store(self):
        NavigationBars.expand_project_panel(self)
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-project-object_store"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def click_project_object_store_containers(self):
        NavigationBars.expand_project_object_store(self)
        self.driver.find_element_by_css_selector(
            'a[href="/project/containers/"]').click()

    """
    Admin > System > Resource
    """

    def expand_admin_system(self):
        NavigationBars.expand_admin_panel(self)
        elm = self.driver.find_element_by_css_selector(
            'a[data-target="#sidebar-accordion-admin-admin"]')
        state = elm.get_attribute('class')
        if 'collapsed' in state:
            elm.click()
        else:
            pass

    def click_admin_system_overview(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/"]').click()

    def click_admin_system_hypervisors(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/hypervisors/"]').click()

    def click_admin_system_host_aggregates(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/aggregates/"]').click()

    def click_admin_system_instances(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/instances/"]').click()

    def click_admin_system_volumes(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/volumes/"]').click()

    def click_admin_system_flavors(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/flavors/"]').click()

    def click_admin_system_images(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/images/"]').click()

    def click_admin_system_networks(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/networks/"]').click()

    def click_admin_system_routers(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/routers/"]').click()

    def click_admin_system_floating_ips(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/floating_ips/"]').click()

    def click_admin_system_defaults(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/defaults/"]').click()

    def click_admin_system_metadata_definitions(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/metadata_defs/"]').click()

    def click_admin_system_info(self):
        NavigationBars.expand_admin_system(self)
        self.driver.find_element_by_css_selector(
            'a[href="/admin/info/"]').click()

    """
    Identity > Resource
    """

    def click_identity_projects(self):
        NavigationBars.expand_identity_panel(self)
        self.driver.find_element_by_css_selector(
            'a[href="/identity/"]').click()

    def click_identity_users(self):
        NavigationBars.expand_identity_panel(self)
        self.driver.find_element_by_css_selector(
            'a[href="/identity/users/"]').click()

    def click_identity_groups(self):
        NavigationBars.expand_identity_panel(self)
        self.driver.find_element_by_css_selector(
            'a[href="/identity/groups/"]').click()

    def click_identity_roles(self):
        NavigationBars.expand_identity_panel(self)
        self.driver.find_element_by_css_selector(
            'a[href="/identity/roles/"]').click()
