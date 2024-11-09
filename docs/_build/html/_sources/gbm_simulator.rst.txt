GBM Simulator Module
====================

This module simulates stochastic processes, including Brownian motion and geometric Brownian motion (GBM).

Stochastic_Processes Class
--------------------------

The `Stochastic_Processes` class is a base class that provides methods for simulating 1D Brownian motion and plotting the displacement over time.

.. autoclass:: gbm_simulator.Stochastic_Processes
   :members:
   :undoc-members:
   :show-inheritance:

   - **__init__**: Initializes the stochastic process with a starting point.
   - **brownian_motion**: Calculates the Brownian motion random walk.
   - **plot**: Plots displacement over time and saves the plot.

GBMSimulator Class
------------------

The `GBMSimulator` class inherits from `Stochastic_Processes` and simulates 1D geometric Brownian motion (GBM).

.. autoclass:: gbm_simulator.GBMSimulator
   :members:
   :undoc-members:
   :show-inheritance:

   - **__init__**: Initializes the GBM simulator with parameters for mean and standard deviation.
   - **simulate_path**: Simulates the GBM path and plots it.
