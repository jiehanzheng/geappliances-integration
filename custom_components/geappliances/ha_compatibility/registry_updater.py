"""Home Assistant compatibility class for adding and updating devices and entities."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.dispatcher import async_dispatcher_send

from ..const import DOMAIN, GEA_ENTITY_NEW
from ..models import GeaEntityConfig

_LOGGER = logging.getLogger()


class RegistryUpdater:
    """Class to add and update devices and entities in their HA registries."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize registry updater class."""
        self._device_registry = dr.async_get(hass)
        self._hass = hass
        self._entry = entry
        self._dispatched_entities: set[tuple[str, str]] = set()

    async def add_entity_to_device(
        self, config: GeaEntityConfig, device_name: str
    ) -> None:
        """Create an entity from the config and add it to the device."""
        _LOGGER.debug("Adding %s to %s", config.platform, device_name)
        if "reserved" not in config.name and "Reserved" not in config.name:
            key = (config.platform, config.unique_identifier)
            if key in self._dispatched_entities:
                return
            # Paired entities subscribe to their status ERD, so subscriptions do not
            # identify registered entities. Reserve the ID before asynchronous setup.
            self._dispatched_entities.add(key)
            async_dispatcher_send(
                self._hass, GEA_ENTITY_NEW.format(config.platform), config
            )

    async def create_device(self, device_name: str) -> str:
        """Create a device and add it to the registry."""
        return self._device_registry.async_get_or_create(
            config_entry_id=self._entry.entry_id,
            identifiers={(DOMAIN, device_name)},
            name=device_name,
        ).id
