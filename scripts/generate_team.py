try:
    import tomllib  # type: ignore
except ImportError:
    import tomli as tomllib
import os

# Set paths
TOML_FILE = "context/team.toml"  # Path to the TOML file
TEMPLATE_FILE = "_templates/components/team_template/team_template.html"  # Path to the template file
OUTPUT_DIR = "_templates/team"  # Path to the output directory for HTML files

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Read the team.toml file
with open(TOML_FILE, "rb") as f:
    team_data = tomllib.load(f)

# Read the template file
with open(TEMPLATE_FILE, "r") as f:
    template_content = f.read()

# List of all team collections you want to process
collections = ["team_director", "team_current", "team_alumni"]

# Loop through each collection
for collection in collections:
    # Check if the collection exists in the TOML file
    if collection in team_data:
        # Loop through the members of the current collection
        for member in team_data[collection]:
            # Create a valid filename based on the member's name
            member_name = member["name"].lower().replace(" ", "_")
            output_file = f"{member_name}.html"

            # Replace placeholders in the template
            member_html = template_content

            # Replace collection and member placeholders
            member_html = member_html.replace("{{ collection }}", collection)
            member_html = member_html.replace(
                "{{ member.name }}", member.get("name", "")
            )

            # Write the modified content to a new HTML file
            with open(os.path.join(OUTPUT_DIR, output_file), "w") as f:
                f.write(member_html)

            print(f"Generated {output_file} from collection {collection}")
