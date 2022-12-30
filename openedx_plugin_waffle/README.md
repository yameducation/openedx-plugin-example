# Django Waffle Switch for Open edX

[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

Implements a subclass of edx_toggles.toggles.WaffleSwitch which for the sake of continuity we also name WaffleSwitch. edx_toggles' WaffleSwitch itself is a specialized subclass of the django-waffle Switch class, with additional caching features.

With this plugin we further extend the feature set of WaffleSwitch to help us with some plugin-specific challenges. We add the following:

* verbose app logging of Switch status and state during object initialization.
* auto-initialization: attempt to create a record in the django-waffle Django model for the switch. This simplifies managing the switch later on, in that creating the record by hand in Django Admin requires an in-depth knowledge of the switch itself which you understandably might lack at the onset of working with this code.
* add a ´ready´ property: returns True if the switch is fully initialized and can be read programatically.
* adds a more robust ´enabled´ property. The is_enabled() method implemented in edx_toggles.toggles.WaffleSwitch raises an exception if the class is not yet fully initialized. This weakness in edX's implementation is prone to breaking automated build and deployment workflows.
* add an ´initialized´ property that provide a hard confirmation of whether the MySQL database record has been created for the switch.
