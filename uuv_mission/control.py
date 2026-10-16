class PDController:
    """Proportional-derivative controller for the submarine's depth. 

    Implements u[t] = kp * e[t] + kd * (e[t] - e[t-1]), where e[t] = r[t] - y[t]
    is the reference depth minus the observed depth and e[-1] is taken to be zero.
    """ 

    def __init__(self, kp: float = 0.15, kd: float = 0.6) -> None:
        """Store the gains and start with no previous error."""
        self.kp = kp
        self.kd = kd
        self.reset()

    def reset(self) -> None: 
        """Forget the previous error, ready for a new simulation."""
        self.previous_error = 0.0

    def __call__(self, reference_t: float, observation_t: float) -> float:
        """Return the control action for the current time step."""
        raise NotImplementedError
    
    

        
