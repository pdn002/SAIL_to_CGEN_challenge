# YAML to S-Expression Converter

## About
This project is for the coding challenge from the SAIL to CGEN position in the LFX Mentorship program. More details [here](https://riscv.org/job/sail-to-cgen-risc-v-mentorship/). <br>
The posed challenge is to make aprogram that read in structure data in the form of tables and nested trees a produce an S-expression representation of the same data. The structured data that this project will deal with is YAML files.

## Dependencies
This project requires a python installation to run and will use the yaml library and sys library. The yaml library can be installed using either of the following commands depending on if the desired package manager is pip or conda.
```
conda install pyyaml
```
```
pip install pyyaml
```

## Execution
The main program will be executed through the file yaml_to_S.py <br>
The program takes in the name of the yaml file that is to be read as a command line argument then outputs the S-expression to the command line as text. below is an example.
```
python yaml_to_S.py [file name]
```
```
$ python yaml_to_S.py yaml_examples/map_seq.yaml

(name "Alice") (age 30) (skills ("Python" "Verilog")) (active True)
```
The yaml_examples/ directory has a few more yaml files that the program can be tested with.