# SIR-model
This project models an agent-based discrete stochastic SIR model to simulate the spread of a disease in population of size $N$ over time $t$. 
The project was implemented using the python package Mesa. 

## The model
In the model, each individual belongs to one of these three compartments: 
susceptible ($S$), infected ($I$) and recovered ($R$).
In this model, recovered individuals are considered to be immune to the disease.

The number of susceptible agents, $N_{S}$ to infect at a single time step is a 
sample drawn from the binomial distribution

$$
Binomial(N_S, 1 - e^{-\frac{beta * N_I }{N}})
$$

where 

$$ 
\beta = \text{Rate per interaction that susceptible individuals become infected}
$$

$$ 
N_I = \text{Number of infected individuals}
$$

The number of infected agents, $N_{I}$ to recover at a single time step is a
sample drawn from the binomial distribution

$$
Binomial(N_I, 1-e^{-\sigma})
$$

where 

$$
\sigma = \text{Rate that infected individuals recover}
$$

## Project structure

- The `src` folder contains the source code. This folder contains two files: 
    1. `model.py` which contains the `DiseaseModel` class and initializes the model with population parameters and 
    creates the human agents. In this file you will also find the code for what the model does in each time step.

    2. `agent.py` which contains the `Human` class which are the agents of the model. 

- The `tests` folder which contain the unit tests for the model.

- The jupyter notebook `run_model.ipynb` where users can enter model parameters, run the model and
visualize the model results with a graph of the populations of each compartment against time.

- `config.py` contains model configuration such as the class `State`, the color of the agents, path for output etc.

- The `data` folder where the csv output files of the model runs and the test runs are saved.


## How to run

1. Clone the repository onto your device by running the following command in your terminal:

```
git clone https://github.com/angelina-momin/SIR-model.git
```

2. Go to the directory where you cloned the project. Then install the required packages* by running the following command in your terminal:

```
pip install -r requirements.txt
```

3. Open the Jupyter notebook `run_model.ipynb` and adjust the following model inputs as necessary.

```
START_POPULATION = 1000
BETA = 10
SIGMA = 1
N_STEPS_MODEL = 10 # Number of time steps to run the model
OUTPUT_FILE_NAME = "output" 
NO_INITIAL_INFECTIONS = 1

NO_RUNS = 10 # Number of times to run the model
```

4. Run all the cells of the notebooks. 
An output file will be created with the results of the run in the `data` folder and a plot of the SIR populations will be generated in the notebook as shown below.

*Optional but recommended: Create a virtual environment first before installing the required packages.

## Testing 

The 'tests' folder contain unit tests that help ensure the model's behavior and results are as expected when the code is changed i.e. added new features or bug fixes.

To run the test use the following command in the terminal
```
python -m pytest
```

At the moment, the folder contains the following tests:

1. Test to check that none of the SIR populations are negative.

2. Test to check that the sum of the populations 
for the three compartments are always
equal to the model's total population.


For each of the tests, the model is initialized and run a number of steps as given by `n_model_steps`. 
The test assertions are then checked for each
of those time step of the model. 
