import ansible_runner
import json

def main():
    inventory_path = "./hosts.yml"
    inventory = json.loads(ansible_runner.interface.get_inventory(action="list",inventories=[inventory_path])[0])
    
    print("\n".join(f"{host} has an ip of {inventory['_meta']['hostvars'][host]['ansible_host']}" for host in inventory["_meta"]["hostvars"]))
    print("\n".join(f"Hosts that are part of {group}:\n\t" + "\n\t".join(inventory[group]['hosts']) for group in inventory['all']['children']))
    print(f"Response: \n{ansible_runner.interface.run_command(executable_cmd='ansible all:localhost -m ping')[0]}")

if __name__ == "__main__":
    main()