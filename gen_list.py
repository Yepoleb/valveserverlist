import json
import jinja2

j2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("."),
    trim_blocks=True,
    lstrip_blocks=True)

servers = json.load(open("servers.json"))
ids = json.load(open("server_ids.json"))

server_list = []
for id_name, ip in sorted(ids.items()):
    services = servers[ip]
    server_list.append({
        "ip": ip,
        "gameservers": len(services),
        "name": id_name,
    })

template = j2_env.get_template("list_template.html")
with open("list.html", "w") as list_file:
    list_file.write(template.render(servers=server_list))
