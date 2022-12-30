# mcdaniel dec-2022: this is a subclass of edx_toggles.toggles.WaffleSwitch
#                    that is part of this openedx-plugin-example repo
from openedx_plugin_waffle.switch import WaffleSwitch

WAFFLE_NAMESPACE = "openedx_plugin_cms"

# .. toggle_name: openedx_plugin_api.OVERRIDE_MOBILE_USER_API_URL_WAFFLE
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: This toggle will override the openedx mobile api url endpoint
# .. toggle_warnings:
# .. toggle_use_cases:
# .. toggle_creation_date: 2022-12-27
AUDIT_REPORT = f"{WAFFLE_NAMESPACE}.audit_report"
AUDIT_REPORT_WAFFLE = WaffleSwitch(AUDIT_REPORT, module_name=__name__)


waffle_switches = {
    AUDIT_REPORT: AUDIT_REPORT_WAFFLE,
}


def waffle_init():
    import logging

    log = logging.getLogger(__name__)

    log.info(
        "{plugin} {waffle_switches} waffle switches detected".format(
            plugin=WAFFLE_NAMESPACE, waffle_switches=len(waffle_switches.keys())
        )
    )
