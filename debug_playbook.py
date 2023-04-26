import ansible_runner
import os

playbook_file = os.path.join(os.path.dirname(__file__), "play-common.yml")
inventory_file = os.path.join(os.path.dirname(__file__), "inventory", "dawg-swarm.yml")

runner = ansible_runner.run(
    private_data_dir=os.path.dirname(__file__),
    playbook=playbook_file,
    inventory=inventory_file,
    cmdline="--extra-vars '{\"var1\": \"value1\", \"var2\": \"value2\"}'",
)

print(runner.stats)
