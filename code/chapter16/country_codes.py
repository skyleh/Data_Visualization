from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name or name == country_name.title():
            return code
    #如果没有找到指定的国家，返回NONE
    return None
