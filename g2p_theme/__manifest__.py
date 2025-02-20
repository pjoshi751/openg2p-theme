{
    "name": "OpenG2P Theme",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/OpenG2P/openg2p-theme",
    "license": "Other OSI approved licence",
    "depends": ["base", "web"],
    "development_status": "Alpha",
    "data": ["templates/g2p_login_page.xml"],
    "assets": {
        "web.assets_backend": [
            "g2p_theme/static/src/scss/assets_menu.scss",
            "g2p_theme/static/src/js/g2p_window_title.js",
        ],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
