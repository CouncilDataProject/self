# CDP - Self

[![Infrastructure Deployment Status](https://github.com/CouncilDataProject/self/workflows/Infrastructure/badge.svg)](https://github.com/CouncilDataProject/self/actions?query=workflow%3A%22Infrastructure%22)
[![Event Processing Pipeline](https://github.com/CouncilDataProject/self/workflows/Event%20Gather/badge.svg)](https://github.com/CouncilDataProject/self/actions?query=workflow%3A%22Event+Gather%22)
[![Event Index Pipeline](https://github.com/CouncilDataProject/self/workflows/Event%20Index/badge.svg)](https://github.com/CouncilDataProject/self/actions?query=workflow%3A%22Event+Index%22)
[![Web Deployment Status](https://github.com/CouncilDataProject/self/workflows/Web%20App/badge.svg)](https://CouncilDataProject.github.io/self)
[![Repo Build Status](https://github.com/CouncilDataProject/self/workflows/Build%20Main/badge.svg)](https://github.com/CouncilDataProject/self/actions?query=workflow%3A%22Build+Main%22)

---

## Council Data Project

Council Data Project is an open-source project dedicated to providing journalists, activists, researchers, and all members of each community we serve with the tools they need to stay informed and hold their Council Members accountable.

For more information about Council Data Project, please visit [our website](https://councildataproject.org/).

## Instance Information

This instance serves as a public archive for CDP team meetings.

_While we will try to upload all of our meetings, we may forget sometimes!_

## Contributing

If you wish to contribute to CDP please note that the best method to do so is to contribute to the upstream libraries that compose the CDP Instances themselves. These are detailed below.

-   [cdp-backend](https://github.com/CouncilDataProject/cdp-backend): Contains all the database models, data processing pipelines, and infrastructure-as-code for CDP deployments. Contributions here will be available to all CDP Instances. Entirely written in Python.
-   [cdp-frontend](https://github.com/CouncilDataProject/cdp-frontend): Contains all of the components used by the web apps to be hosted on GitHub Pages. Contributions here will be available to all CDP Instances. Entirely written in TypeScript and React.
-   [cookiecutter-cdp-deployment](https://github.com/CouncilDataProject/cookiecutter-cdp-deployment): The repo used to generate new CDP Instance deployments. Like this repo!
-   [councildataproject.org](https://github.com/CouncilDataProject/councildataproject.github.io): Our landing page! Contributions here should largely be text changes and admin updates.

## Instance Admin Documentation

You can find documentation on how to customize, update, and maintain this CDP instance
in the
[admin-docs directory](https://github.com/CouncilDataProject/self/tree/main/admin-docs).
