# SIR-model

## The model
This is a SIR model with a starting population of $N$. 
Each individual belongs to one of these three compartments: 
susceptible ($S$), infected ($I$) and recovered ($R$).

The deterministic differential equations governing the model are:

$ 
\begin{equation}
\frac{dS}{dt} = -\beta \times S \times \frac{I}{N}
\end{equation}
$

$ 
\begin{equation}
\frac{dI}{dt} = \beta \times S \times \frac{I}{N} -\sigma I
\end{equation}
$

$ 
\begin{equation}
\frac{dR}{dt} = \sigma I
\end{equation}
$

where 

$$ 
\beta = \text{Rate per interaction that susceptible individuals become infected}
$$

$$
\sigma = \text{Rate that infected individuals recover}
$$

## Stochastic model

Imagine that in a small period of time $dt$ the chance of an event happening
follows a Bernoulli trial.

For discrete time step of size $dt$

## How to run


## Testing 

The 'tests' folder contain unit tests that GitHub automatically runs in the background.
This ensures that each time the model's code is changed i.e. added new features or the bug fixes, 
we automatically check that model still yields expectable results and
its basic functionalities are working as expected.
