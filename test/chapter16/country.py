from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """获取国家码"""
    for code, name in COUNTRIES.items():
        if name == country_name or name == country_name.title():
            return code
    return None
