#import sys
#sys.path.append(r"F:/Task/222/6_3D_Human_body_reconstruction/reference/measurements/SMPL-Anthropometry")

# main.py
import subprocess
import measure
import argparse
parser = argparse.ArgumentParser(description='Measurements')
parser.add_argument('-ht', '--height', type=str, default=170.5, help='Custome height of body')

args=parser.parse_args()

#from .smplx.transfer_model import __main__
#from transfer_model import app

# Run the first file
transfer_process = subprocess.Popen(['python', '-m','transfer_model'])
transfer_process.wait()
# Run the second file

measure_process = subprocess.Popen(['python', 'measure.py', '--height', args.height])
measure_process.wait()

