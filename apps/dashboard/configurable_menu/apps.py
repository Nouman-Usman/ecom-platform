from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class ConfigurableMenuConfig(OscarConfig):
    name = 'apps.dashboard.configurable_menu'
    label = 'configurable_menu'
    verbose_name = _('Configurable Menu')
    namespace = 'configurable_menu'
    default_permissions = ['is_staff']
    permissions_map = _map = {
        'partner-configurable-menu-create': (['is_staff'], ['partner.dashboard_access']),
    }
    def ready(self):
        self.partner_configurable_menu_create_view = get_class('dashboard.configurable_menu.views','PartnerConfigurableMenuCreateView')

    def get_urls(self):
        urls = [
            url(r'^create/$',
                self.partner_configurable_menu_create_view.as_view(), name='partner-configurable-menu-create')
        ]
        return self.post_process_urls(urls)
