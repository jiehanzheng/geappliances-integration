# GE Appliances Integration

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![Community Forum][forum-shield]][forum]

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=GE+Appliances&category=Integration&repository=https%3A%2F%2Fgithub.com%2Fgeappliances%2Fgeappliances-integration)

_Integration to integrate with [GE Appliances](https://www.geappliances.com/) using the [GE Appliances/FirstBuild Home Assistant adapter](https://firstbuild.com/inventions/home-assistant-adapter/)._

This integration works with the [Home Assistant adapter](https://firstbuild.com/inventions/home-assistant-adapter/) (see [here](https://github.com/geappliances/home-assistant-adapter) for firmware) to automatically configure entities in Home Assistant by using [Appliance API](https://github.com/geappliances/public-appliance-api-documentation) to find public ERDs on an appliance. It is designed to be a "batteries-included" option for users who want to quickly and easily get their appliances talking to Home Assistant with the Home Assistant adapter. Users wanting a more customized experience might be interested in [using YAML with the MQTT integration](https://github.com/geappliances/home-assistant-examples) to communicate with their appliances.

## Installation

The preferred method of installing this integration is through the [Home Assistant Community Store][hacs].

### Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `geappliances`.
1. Download _all_ the files from the `custom_components/geappliances/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "GE Appliances"


## Dependency compatibility

This private fork requires `aiofiles~=25.0`, which means `>=25.0,<26.0` under
[Python's compatible-release rules](https://packaging.python.org/en/latest/specifications/version-specifiers/#compatible-release).
It accepts Home Assistant's 25.1.0 without GE forcing the old 24.1.0 downgrade
in the shared Python process. The [25.1.0 release](https://github.com/Tinche/aiofiles/blob/main/CHANGELOG.md)
also explicitly adds Python 3.14 support, matching the deployed Home Assistant.

`aiofiles` uses calendar versioning. The upper bound is our deliberate review
boundary, not an upstream guarantee of semantic compatibility. Review and test
26.x before raising the bound; if Home Assistant requires 26.x first, update this
fork before upgrading Home Assistant rather than bypassing dependency checks.
The integration uses the public `aiofiles.open`/`read` async context-manager API.

CI tests both the first published 25.x release (25.1.0) and the newest release
allowed by the manifest.
Set `AIOFILES_VERSION=25.1.0` when invoking `./tdd` to select that baseline; omit it
to resolve the newest allowed release. The selected version and all test
requirements are resolved together, so conflicting requirements fail installation.

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/geappliances/geappliances-integration.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/geappliances/geappliances-integration.svg?style=for-the-badge
[releases]: https://github.com/geappliances/geappliances-integration/releases
[hacs]: https://www.hacs.xyz
