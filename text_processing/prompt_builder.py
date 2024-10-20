from importlib import resources
from jinja2 import Environment, FileSystemLoader, TemplateError

# Set up Jinja2 environment
with resources.path('text_processing', 'prompts') as prompts_path:
    env = Environment(loader=FileSystemLoader(prompts_path))

def render_prompt(template_name, context=None):
    try:
        template = env.get_template(template_name)
        return template.render(context or {})
    except TemplateError:
        raise RuntimeError(f"Error: Issue rendering template: '{template_name}'")
