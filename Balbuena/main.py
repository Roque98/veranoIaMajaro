# CREACIÓN DE MÉTODO PARA APRENDER

# Se define la función que permitirá al agente poder añadir el conocimiento
# a esta función se le pasan los parametros 'self', 'obs', 'action', 'reward', 'next_obs'
# los cuales se definen en las funciones anteriores ya creadas 
def learn(self, obs, action, reward, next_obs):
    # Se inicializa una variable para almacenar un nuevo valor creado 
        discrete_obs = self.discretize(obs)
        discrete_next_obs = self.discretize(next_obs)
    # Se inicializa una nueva variable la cual almacenará la recompenza obtenida hasta el momento 
        td_target = reward + self.gamma * np.max(self.Q[discrete_next_obs])
    # Si se encuentra con algún error se guardará en una variable para indicar dónde se generó
        td_error = td_target - self.Q[discrete_obs][action]
    # Se guardará la acción o el error
        self.Q[discrete_obs][action] += self.alpha*td_error