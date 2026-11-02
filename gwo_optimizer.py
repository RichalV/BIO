"""
Phase 3: Grey Wolf Optimizer (GWO) for CatBoost Hyperparameter Optimization
Course: Bio-Inspired Algorithms (23DS7BSBIO)
Algorithm Reference: Mirjalili et al., "Grey Wolf Optimizer", Advances in Engineering Software, 2014.
"""

import numpy as np
from catboost import CatBoostRegressor
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

class GreyWolfOptimizer:
    """
    Bio-Inspired Grey Wolf Optimizer (GWO) mapped for CatBoost hyperparameter tuning.
    
    Social Hierarchy:
      - Alpha (alpha): Fittest wolf (best hyperparameter set discovered so far)
      - Beta (beta): Second fittest wolf
      - Delta (delta): Third fittest wolf
      - Omega (omega): The remaining wolves following alpha, beta, and delta guidance
      
    Hyperparameter Chromosome Vector:
      [iterations (trees), learning_rate, tree_depth, l2_leaf_reg]
    """
    
    def __init__(self,
                 X_train, y_train,
                 X_val, y_val,
                 num_wolves=10,
                 max_iterations=30,
                 random_seed=42):
        self.X_train = X_train
        self.y_train = y_train
        self.X_val = X_val
        self.y_val = y_val
        self.num_wolves = num_wolves
        self.max_iterations = max_iterations
        self.random_seed = random_seed
        
        # Search space boundaries
        # [iterations, learning_rate, depth, l2_leaf_reg]
        self.lb = np.array([60,   0.02, 3,  1.0])
        self.ub = np.array([350,  0.25, 7, 10.0])
        self.dim = len(self.lb)
        
        # Storage for hierarchy
        self.alpha_pos = np.zeros(self.dim)
        self.alpha_score = float('inf')
        
        self.beta_pos = np.zeros(self.dim)
        self.beta_score = float('inf')
        
        self.delta_pos = np.zeros(self.dim)
        self.delta_score = float('inf')
        
        # Population positions and fitness records
        self.positions = None
        self.convergence_curve = []
        self.history_details = []
        
    def decode_chromosome(self, position):
        """Map continuous position vector into valid CatBoost hyperparameters."""
        clipped = np.clip(position, self.lb, self.ub)
        iterations = int(round(clipped[0]))
        learning_rate = float(clipped[1])
        depth = int(round(clipped[2]))
        l2_leaf_reg = float(clipped[3])
        return {
            'iterations': iterations,
            'learning_rate': learning_rate,
            'depth': depth,
            'l2_leaf_reg': l2_leaf_reg
        }
        
    def evaluate_fitness(self, position):
        """
        Evaluate objective function (minimize Validation RMSE).
        Fitness = RMSE(y_val, y_pred)
        """
        params = self.decode_chromosome(position)
        try:
            model = CatBoostRegressor(
                iterations=params['iterations'],
                learning_rate=params['learning_rate'],
                depth=params['depth'],
                l2_leaf_reg=params['l2_leaf_reg'],
                random_seed=self.random_seed,
                verbose=0,
                thread_count=-1
            )
            model.fit(self.X_train, self.y_train)
            preds = model.predict(self.X_val)
            rmse = root_mean_squared_error(self.y_val, preds)
            return rmse
        except Exception as e:
            return 1e9

    def optimize(self):
        """Execute the bio-inspired GWO search algorithm."""
        np.random.seed(self.random_seed)
        print(f"\n[GWO] Initializing population: {self.num_wolves} wolves across {self.dim} dimensions...")
        
        # Initialize wolf pack randomly within boundaries
        self.positions = np.random.uniform(self.lb, self.ub, (self.num_wolves, self.dim))
        fitness = np.zeros(self.num_wolves)
        
        # Evaluate initial population
        for i in range(self.num_wolves):
            fitness[i] = self.evaluate_fitness(self.positions[i])
            
        # Determine initial Alpha, Beta, Delta
        sorted_indices = np.argsort(fitness)
        self.alpha_pos = self.positions[sorted_indices[0]].copy()
        self.alpha_score = fitness[sorted_indices[0]]
        
        self.beta_pos = self.positions[sorted_indices[1]].copy()
        self.beta_score = fitness[sorted_indices[1]]
        
        self.delta_pos = self.positions[sorted_indices[2]].copy()
        self.delta_score = fitness[sorted_indices[2]]
        
        self.convergence_curve.append(self.alpha_score)
        init_params = self.decode_chromosome(self.alpha_pos)
        print(f"[GWO] Iteration 00/{self.max_iterations} | Best Alpha Val RMSE: {self.alpha_score:.4f} kW")
        
        # Iteration Loop (Hunting & Encircling)
        for t in range(1, self.max_iterations + 1):
            # Coefficient 'a' decreases linearly from 2 to 0 (Exploration -> Exploitation balance)
            a = 2.0 - 2.0 * (t / self.max_iterations)
            
            for i in range(self.num_wolves):
                for j in range(self.dim):
                    # Hunting guidance from Alpha
                    r1, r2 = np.random.rand(), np.random.rand()
                    A1 = 2.0 * a * r1 - a
                    C1 = 2.0 * r2
                    D_alpha = abs(C1 * self.alpha_pos[j] - self.positions[i, j])
                    X1 = self.alpha_pos[j] - A1 * D_alpha
                    
                    # Hunting guidance from Beta
                    r1, r2 = np.random.rand(), np.random.rand()
                    A2 = 2.0 * a * r1 - a
                    C2 = 2.0 * r2
                    D_beta = abs(C2 * self.beta_pos[j] - self.positions[i, j])
                    X2 = self.beta_pos[j] - A2 * D_beta
                    
                    # Hunting guidance from Delta
                    r1, r2 = np.random.rand(), np.random.rand()
                    A3 = 2.0 * a * r1 - a
                    C3 = 2.0 * r2
                    D_delta = abs(C3 * self.delta_pos[j] - self.positions[i, j])
                    X3 = self.delta_pos[j] - A3 * D_delta
                    
                    # Pack position update (Centroid average)
                    self.positions[i, j] = (X1 + X2 + X3) / 3.0
                    
                # Boundary enforcement
                self.positions[i] = np.clip(self.positions[i], self.lb, self.ub)
                
                # Fitness re-evaluation
                f_val = self.evaluate_fitness(self.positions[i])
                
                # Hierarchy Rank Update
                if f_val < self.alpha_score:
                    # Previous alpha shifts to beta, beta shifts to delta
                    self.delta_score = self.beta_score
                    self.delta_pos = self.beta_pos.copy()
                    
                    self.beta_score = self.alpha_score
                    self.beta_pos = self.alpha_pos.copy()
                    
                    self.alpha_score = f_val
                    self.alpha_pos = self.positions[i].copy()
                    
                elif f_val > self.alpha_score and f_val < self.beta_score:
                    self.delta_score = self.beta_score
                    self.delta_pos = self.beta_pos.copy()
                    
                    self.beta_score = f_val
                    self.beta_pos = self.positions[i].copy()
                    
                elif f_val > self.alpha_score and f_val > self.beta_score and f_val < self.delta_score:
                    self.delta_score = f_val
                    self.delta_pos = self.positions[i].copy()
                    
            self.convergence_curve.append(self.alpha_score)
            best_curr = self.decode_chromosome(self.alpha_pos)
            self.history_details.append({
                'iteration': t,
                'a_parameter': a,
                'alpha_rmse': self.alpha_score,
                'beta_rmse': self.beta_score,
                'delta_rmse': self.delta_score,
                'best_params': best_curr
            })
            
            print(f"[GWO] Iteration {t:02d}/{self.max_iterations} | Best Alpha Val RMSE: {self.alpha_score:.4f} kW (a={a:.2f})", flush=True)
            
        optimal_params = self.decode_chromosome(self.alpha_pos)
        print(f"\n[GWO] Optimization Complete!")
        print(f"Optimal Alpha Parameters Discovered:")
        for k, v in optimal_params.items():
            print(f"  * {k}: {v if isinstance(v, int) else round(v, 4)}")
        print(f"Best Validation RMSE: {self.alpha_score:.4f} kW")
        
        return optimal_params, self.convergence_curve, self.history_details

