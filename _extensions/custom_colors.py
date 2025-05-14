from docutils import nodes
from docutils.parsers.rst import roles as rst_roles

def make_badge_role(color):
    def badge_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        html = f'<span class="sd-badge sd-bg-{color}">{text}</span>'
        return [nodes.raw('', html, format='html')], []
    return badge_role

def register_badge_roles(app, config):
    for color in config.custom_badge_colors:
        role_name = f"bdg-{color}"    # register :bdg-emerald:, etc.
        rst_roles.register_local_role(role_name,
                                      make_badge_role(color))

def setup(app):
    app.add_config_value('custom_badge_colors', [], 'env')
    app.connect('config-inited', register_badge_roles)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
