from collections import deque
import sys 
import os
import subprocess

command = ['git']
show = ['bat']
orbit = deque()

def run_command(command=command,capture=False):
    try:
        result = subprocess.run(command, capture_output=capture,
                                text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print('An error occurred while running the command:')
        print('Command:', e.cmd)
        print('Return code:', e.returncode)
        print('Output:', e.output)
        print('Error:', e.stderr)
        return None

def add(filename :str):
    run_command(['git','add',filename])

def commit(filename :str, message :str):
    run_command(['git','commit','-m',filename])

def dispaly(filename :str): 
    show.append(filename) 
    run_command(command=show,capture=True)

def handle_orbit_command(args :list):
    pass

def handle_git_command(args :list):
    pass

def init(): 
    args = sys.argv
    args.remove(args[0])
    if os.path.exists(args[0]): 
        handle_orbit_command(args)
    else:
        handle_git_command(args)
