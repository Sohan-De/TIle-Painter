import os
import re

def update_navbar_in_all_html_files(navbar_file_path, project_path='.'):
    with open(navbar_file_path, 'r', encoding='utf-8') as f:
        navbar_template = f.read()

    # Pattern to match <nav class="navbar">...</nav>
    nav_pattern = re.compile(r'(<nav class="navbar">)(.*?)(</nav>)', re.DOTALL)

    # Walk through all directories
    for root, dirs, files in os.walk(project_path):
        # Skip some directories if needed
        if '.git' in root or 'node_modules' in root:
            continue

        for filename in files:
            if filename.endswith('.html') and filename not in ['navbar.html', 'footer.html']:
                file_path = os.path.join(root, filename)
                
                # Calculate depth relative to project_path
                relative_path = os.path.relpath(root, project_path)
                depth = 0 if relative_path == '.' else len(relative_path.split(os.sep))
                prefix = '../' * depth

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Adjust navbar links based on depth
                # This simple regex finds href="xyz.html" and adds prefix
                # We only want to prefix relative links that don't start with http/https
                def adjust_links(match):
                    inner_content = match.group(2)
                    # Regex for href="...", src="..."
                    def replace_link(link_match):
                        attr = link_match.group(1)
                        link = link_match.group(2)
                        if not (link.startswith('http') or link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:')):
                            return f'{attr}="{prefix}{link}"'
                        return link_match.group(0)

                    adjusted_inner = re.sub(r'(href|src)="([^"]+)"', replace_link, inner_content)
                    return f'{match.group(1)}\n{adjusted_inner}{match.group(3)}'

                # Use a specific version of navbar_template for this file
                # But wait, the update_navbars.py usually just copies navbar.html
                # Let's adjust navbar_template first
                
                temp_nav = navbar_template
                def replace_template_link(link_match):
                    attr = link_match.group(1)
                    link = link_match.group(2)
                    if not (link.startswith('http') or link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:')):
                        return f'{attr}="{prefix}{link}"'
                    return link_match.group(0)
                
                adjusted_nav = re.sub(r'(href|src)="([^"]+)"', replace_template_link, temp_nav)

                new_content = nav_pattern.sub(r'\1\n' + adjusted_nav + r'\3', content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
                else:
                    print(f"No changes for: {file_path}")

if __name__ == "__main__":
    navbar_path = 'navbar.html'
    update_navbar_in_all_html_files(navbar_path)
