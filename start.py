import subprocess
import time
import argparse
parser = argparse.ArgumentParser(description='Measurements')
parser.add_argument('-ht', '--height', type=str, default=170.5, help='Custome height of body')

args=parser.parse_args()

def run_script1(script_path, conda_env):
    # Activate the Conda environment
    activate_cmd = f'conda activate {conda_env} && '
    
    # Execute the script within the environment
    subprocess.run(activate_cmd + 'python ' + script_path, shell=True, check=True)

def run_script2(script_path, conda_env):
    # Activate the Conda environment
    activate_cmd = f'conda activate {conda_env} && '
    
    # Execute the script within the environment
    subprocess.run(activate_cmd + 'python ' + script_path +'--height ' + args.height, shell=True, check=True)

def integrate_scripts(script1_path, script3_path, env1_conda_env, env2_conda_env):
    start_time = time.time()
    # Run the first script in its environment
    run_script1(script1_path, env1_conda_env)
    #run_script.wait()
    
    # Run the second script in its environment
    # run_module(module_path, env2_conda_env)
    # transfer_process.wait()

    run_script2(script2_path, env2_conda_env)

    end_time = time.time()  # End time for measuring program execution
    total_time = end_time - start_time
    #print(f"Total time taken: {total_time} seconds")
    

# Paths to your Python scripts
script1_path = './engine/demos/demo_fit_body.py '
# module_path = 'transfer_model'
script2_path = './main.py '

# Names of the Conda environments
env1_conda_env = '3d_body'
env2_conda_env = 'measure'

# Integrate the two scripts
integrate_scripts(script1_path, script2_path, env1_conda_env, env2_conda_env)
