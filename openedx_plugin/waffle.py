"""
written by:     Lawrence McDaniel
                https://lawrencemcdaniel.com

date:           feb-2022

usage:          custom Waffle Switches to use as feature toggles for
                openedx_plugin. see https://waffle.readthedocs.io/en/stable/
"""

# mcdaniel dec-2022: this is a subclass of edx_toggles.toggles.WaffleSwitch
#                    that is part of this openedx-plugin-example repo
from openedx_plugin_waffle.switch import WaffleSwitch


WAFFLE_NAMESPACE = "openedx_plugin"

# .. toggle_name: openedx_plugin.marketing_redirector
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: adds language-specific marketing site urls based on a language parameter added to the http request
# .. toggle_warnings: depends on settings.MKTG_URL_OVERRIDES
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
SIMPLE_REST_API = f"{WAFFLE_NAMESPACE}.simple_rest_api"
SIMPLE_REST_API_WAFFLE = WaffleSwitch(SIMPLE_REST_API, module_name=__name__)


# .. toggle_name: openedx_plugin.override_lms_django_admin_login
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: This toggle will revert the Django Admin login page to the original Django default
# .. toggle_warnings:
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
OVERRIDE_OPENEDX_DJANGO_LOGIN = f"{WAFFLE_NAMESPACE}.override_lms_django_admin_login"
OVERRIDE_OPENEDX_DJANGO_LOGIN_WAFFLE = WaffleSwitch(OVERRIDE_OPENEDX_DJANGO_LOGIN, module_name=__name__)

# .. toggle_name: openedx_plugin.automated_enrollment
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: reads and processes http request parameters 'language' (ie es-419) and 'enroll' (an escaped course key)
# .. toggle_warnings: ensure that you add the languages to your open edx build.
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
AUTOMATED_ENROLLMENT = f"{WAFFLE_NAMESPACE}.automated_enrollment"
AUTOMATED_ENROLLMENT_WAFFLE = WaffleSwitch(OVERRIDE_OPENEDX_DJANGO_LOGIN, module_name=__name__)

# .. toggle_name: openedx_plugin.marketing_redirector
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: adds language-specific marketing site urls based on a language parameter added to the http request
# .. toggle_warnings: depends on settings.MKTG_URL_OVERRIDES
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
MARKETING_REDIRECTOR = f"{WAFFLE_NAMESPACE}.marketing_redirector"
MARKETING_REDIRECTOR_WAFFLE = WaffleSwitch(MARKETING_REDIRECTOR, module_name=__name__)

# .. toggle_name: openedx_plugin.signals
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: adds hooks for Django signals
# .. toggle_warnings:
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
SIGNALS = f"{WAFFLE_NAMESPACE}.signals"
SIGNALS_WAFFLE = WaffleSwitch(SIGNALS, module_name=__name__)

waffle_switches = {
    SIMPLE_REST_API: SIMPLE_REST_API_WAFFLE,
    OVERRIDE_OPENEDX_DJANGO_LOGIN: OVERRIDE_OPENEDX_DJANGO_LOGIN_WAFFLE,
    AUTOMATED_ENROLLMENT: AUTOMATED_ENROLLMENT_WAFFLE,
    MARKETING_REDIRECTOR: MARKETING_REDIRECTOR_WAFFLE,
    SIGNALS: SIGNALS_WAFFLE,
}


def waffle_init():
    import logging

    log = logging.getLogger(__name__)
    log.info(
        "{plugin} {waffle_switches} waffle switches detected".format(
            plugin=WAFFLE_NAMESPACE, waffle_switches=len(waffle_switches.keys())
        )
    )
