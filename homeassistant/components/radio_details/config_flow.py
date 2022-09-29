"""Config flow for Portuguese Radio Details integration."""
from __future__ import annotations

from typing import Any

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Portuguese Radio Details."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="", data={})

        return self.async_show_form(step_id="user")

    async def async_step_onboarding(
        self, data: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by onboarding."""
        return self.async_create_entry(title="", data={})


# DATA_SCHEMA = vol.Schema({vol.Required(CONF_POOLTIME, default=60): cv.positive_int})


# class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
#     """Handle a config flow for Portuguese Radio Details."""

#     VERSION = 1

#     async def async_step_user(
#         self, user_input: dict[str, Any] | None = None
#     ) -> FlowResult:

#         if user_input is not None:
#             return self.async_create_entry(title="", data=user_input)

#         return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)

#     @staticmethod
#     @callback
#     def async_get_options_flow(
#         config_entry: config_entries.ConfigEntry,
#     ) -> config_entries.OptionsFlow:
#         """Create the options flow."""
#         return OptionsFlowHandler(config_entry)


# class OptionsFlowHandler(config_entries.OptionsFlow):
#     """Config flow options for Portuguese Radio Details."""

#     def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
#         """Initialize options flow."""
#         self.config_entry = config_entry

#     async def async_step_init(
#         self, user_input: dict[str, Any] | None = None
#     ) -> FlowResult:
#         """Manage the options."""
#         if user_input is not None:
#             return self.async_create_entry(title="", data=user_input)

#         return self.async_show_form(
#             step_id="init",
#             data_schema=vol.Schema(
#                 {
#                     vol.Required(
#                         CONF_POOLTIME,
#                         default=self.config_entry.data[CONF_POOLTIME],
#                     ): cv.positive_int
#                 }
#             ),
#         )
