# -*- coding: utf-8 -*-
{
    "name": "CRM Stage: Multiple Sales Teams",
    "summary": "Allow assigning multiple Sales Teams to one CRM Stage",
    "version": "18.0.1.0.0",
    "author": "Your Company",
    "license": "LGPL-3",
    "website": "https://example.com",
    "category": "Sales/CRM",
    "depends": ["crm"],
    "data": [
        "views/crm_stage_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
