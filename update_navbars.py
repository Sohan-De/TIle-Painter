import os
import re

def update_navbar_in_all_html_files(navbar_file_path, project_path='.'):
    with open(navbar_file_path, 'r', encoding='utf-8') as f:
        new_nav_inner = f.read()

    # Pattern to match <nav class="navbar">...</nav>
    nav_pattern = re.compile(r'(<nav class="navbar">)(.*?)(</nav>)', re.DOTALL)

    for filename in os.listdir(project_path):
        # Update all HTML files except the components themselves
        if filename.endswith('.html') and filename not in ['navbar.html', 'footer.html']:
            file_path = os.path.join(project_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace the inner content of the nav tag
            new_content = nav_pattern.sub(r'\1\n' + new_nav_inner + r'\3', content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filename}")
            else:
                print(f"No changes for: {filename}")

if __name__ == "__main__":
    navbar_path = 'navbar.html'
    update_navbar_in_all_html_files(navbar_path)
