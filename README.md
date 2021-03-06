		  	  _____  ____        _____ _            
		  	 |  __ \|  _ \      / ____(_)           
		  	 | |  | | |_) |____| (___  _ _ __ ___   
		  	 | |  | |  _ <______\___ \| | '_ ` _ \  
		  	 | |__| | |_) |     ____) | | | | | | | 
		  	 |_____/|____/     |_____/|_|_| |_| |_| 

# DB-Sim
A data driven and  queue-based simulation tool for ETE 

# Goals
calculate evacuation time faster and  more accurately

# Methods
-  build basic iterator model[db-sim Framework]
-  build ml model
-  data driven model integration
-  Experiment

# TODOLISTS
## Framework
- [x] parse xml from config
- [x] boost library support
- [x] logging support
- [x] basic iterator develop
- [x] xgboost,randomforest c++ support
- [x] refacting db-sim manage
- [x] refacting config manage 

## Model
- [x] poolnum -> buffernum
- [x] buffernum -> outflow
- [x] sample for every link and node
- [x] add pool and buffer sample
- [x] train model for each node
- [x] import ml model(trained by python and predict by c++)


## Plans
### V0.1.3
- [x] add param configure for better tune.
- [x] add super-dest-point process


### V0.1.4
- [x] add [poolnum -> buffernum] Model
- [x] finished basic iteration for simulation.


### V0.1.5
- [x] add 2out->1in intersection analyais(discard)
- [x] add rotary island intersection analysis(discard)

### V0.1.6
- [x] add long path analysis
- [x] add circle module
- [x] precise link desc with buffersize
- [x] update vehicle generator

### V0.1.7
- [ ] road condition display

### To Be Continue~

# Usage
## Settings
- `config` privoid traffic network and evacuation demand with xml.
- `src` do simulation
    - `core` core code for simulation
    - `utils` some userdefined or 3rd necessary tools ,example parse xml tools
- `test` some test case for this project
- `data` train and test data

```bash

dbsim [options] [ceil|test|gawron|fete] :
  -h [ --help ]           show help
  -c [ --config ] arg     user defined config file
  -s [ --sample ] arg     sample for node and link
  -S [ --simulation ] arg simulation for fast ete
  -t [ --test ]           Test each model

```

## build
```bash
cd ${PROJECT_DIR}
mkdir build
cd build
cmake ..
make
```

## Result 
### link 2571 and 2581
The DB-Sim method is closed with origin mathod ,but run much faster.

![result](https://github.com/lzjqsdd/DB-Sim/blob/master/train/fig/compare.png)


# Reference
- Papers To be add.
