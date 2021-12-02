#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cdp_backend.infrastructure import CDPStack
from pulumi import export

###############################################################################

cdp_stack = CDPStack(
    gcp_project_id="cdp-self-chjtigrp",
    municipality_name="Self",
    firestore_location="us-central",
    hosting_github_url="https://github.com/CouncilDataProject/self",
    hosting_web_app_address="https://CouncilDataProject.github.io/self",
    governing_body="other",
)

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
