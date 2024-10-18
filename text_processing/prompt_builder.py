from importlib import resources
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
with resources.path('text_processing', 'prompts') as prompts_path:
    env = Environment(loader=FileSystemLoader(prompts_path))

def render_prompt(template_name, context):
    template = env.get_template(template_name + '.html')
    return template.render(context)
