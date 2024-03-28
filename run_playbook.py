import ansible_runner
import subprocess

def main():
    playbook_path = "hello.yml"
    print(f"Response: {ansible_runner.interface.run_command(executable_cmd='ansible-playbook ' + playbook_path)[0]}")
    print('\n'.join(subprocess.run(["curl", "http://0.0.0.0"], capture_output=True, text=True).stdout for _ in range(3)))

if __name__ == "__main__":
    main()
