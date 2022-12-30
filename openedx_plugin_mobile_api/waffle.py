"""
written by:     Lawrence McDaniel
                https://lawrencemcdaniel.com

date:           dec-2022

usage:          custom Waffle WaffleSwitch to use as feature toggles
                for openedx_plugin_mobile_api.
                see https://waffle.readthedocs.io/en/stable/
"""

# mcdaniel dec-2022: this is a subclass of edx_toggles.toggles.WaffleSwitch
#                    that is part of this openedx-plugin-example repo
from openedx_plugin_waffle.switch import WaffleSwitch

WAFFLE_NAMESPACE = "openedx_plugin_mobile_api"

# .. toggle_name: openedx_plugin_api.OVERRIDE_MOBILE_USER_API_URL_WAFFLE
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: This toggle will override the openedx mobile api url endpoint
# .. toggle_warnings:
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
OVERRIDE_MOBILE_USER_API_URL = f"{WAFFLE_NAMESPACE}.override_mobile_user_api_url"
OVERRIDE_MOBILE_USER_API_URL_WAFFLE = WaffleSwitch(OVERRIDE_MOBILE_USER_API_URL, module_name=__name__)

waffle_switches = {
    OVERRIDE_MOBILE_USER_API_URL: OVERRIDE_MOBILE_USER_API_URL_WAFFLE,
}


def waffle_init():
    import logging

    log = logging.getLogger(__name__)

    log.info(
        "{plugin} {waffle_switches} waffle switches detected".format(
            plugin=WAFFLE_NAMESPACE, waffle_switches=len(waffle_switches.keys())
        )
    )
