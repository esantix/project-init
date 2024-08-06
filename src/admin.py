import jinja2 as j2
import os



template_dir = os.path.join(os.path.dirname(__file__), 'template')
output_dir = 'rendered_templates'
env = j2.Environment(loader=j2.FileSystemLoader(template_dir))

data = {
    'project': {'name': 'fasdf'},
}

# Function to render a single file
def render_file(template_path, output_path, context):
    template = env.get_template(template_path)
    rendered_content = template.render(context)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(rendered_content)

for root, dirs, files in os.walk(template_dir):
    for file in files:
        if file.endswith('.j2'):
            template_path = os.path.relpath(os.path.join(root, file), template_dir)
            output_path = os.path.join(output_dir, template_path[:-3])
            render_file(template_path, output_path, data)