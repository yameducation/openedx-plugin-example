"""
written by:     Lawrence McDaniel
                https://lawrencemcdaniel.com

date:           feb-2022

usage:          custom Waffle Switches to use as feature toggles for
                openedx_plugin. see https://waffle.readthedocs.io/en/stable/
"""
import logging

try:
    from waffle.models import Switch
except Exception:
    # to resolve race condition during pre-launch manage.py operations
    Switch = None

from django.core.exceptions import ObjectDoesNotExist

from edx_toggles.toggles import WaffleSwitch as BaseSwitch

log = logging.getLogger(__name__)


class WaffleSwitch(BaseSwitch):
    """
    Additional functionality

    - add a property to report 'ready' status
    - add a property to robustly report 'enabled' status by returning False on any Exception encountered
    - add an 'initialized' property to report whether a persisted Django model record exists
    - try to automatically initialize the Django model record if it does not yet exist
    """

    def __init__(self, name, module_name):
        """
        constructor

        Arguments:
            name (String): The name of the switch. This name must include a dot (".") to indicate namespacing.
            module_name (String): The name of the module where the flag is created. This should be ``__name__`` in most
            cases.

        Try to auto-initialize this WaffleSwitch
        """
        super().__init__(name=name, module_name=module_name)
        if not self.ready:
            log.warning(
                "{cls}: unable to verify initialization status of waffle switch.".format(cls=self.__class__.__name__)
            )
            return

        if self.initialized:
            log.info(
                "WaffleSwitch {switch_name} was previously initialized {and_is_or_is_not} enabled.".format(
                    switch_name=self.name, and_is_or_is_not="and is" if self.enabled else "but is not"
                )
            )
        else:
            if Switch:
                Switch.objects.create(name=self.name, active=False)
                log.info("Initialized WaffleSwitch object {switch_name}".format(switch_name=self.name))

    @property
    def ready(self) -> bool:
        """
        try to get the 'enabled' status of any arbitrary WaffleSwitch. If it
        doesn't raise an error then we're ready.

        This is intended to be used as a way to reduce console logging output during
        application startup, when WaffleSwitch states cannot yet be read, as the
        db service is not yet up.
        """
        try:
            self.is_enabled()
            return True
        except Exception:
            return False

    @property
    def enabled(self) -> bool:
        """
        To resolve a race condition during application launch. The waffle_switches
        are inspected before the db service has initialized.
        """
        try:
            return self.is_enabled()
        except Exception:
            return False

    @property
    def initialized(self) -> bool:
        """
        note: edx_toggles.toggles.WaffleSwitch.is_enabled() is derived from
        waffle.models.Switch.active  (a boolean)
        see
         - https://github.com/django-waffle/django-waffle/blob/master/waffle/models.py#L438
         - https://github.com/openedx/edx-toggles/blob/master/edx_toggles/toggles/internal/waffle/switch.py#L19
        """
        try:
            Switch.objects.get(name=self.name)
            return True
        except ObjectDoesNotExist:
            return False
