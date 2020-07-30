<<<<<<< HEAD
#este metodo no suele ser muy necesario para implementacion de agentes 
#pero en este caso nos resulta muy util cuando el espacio de estados es grande y continuo 
#lo que se puede hacer aqui es divir en cjas o rangos de valores para simplificar su representacion 
#esto tambien reduce el numero de valores que necesita aprender 
#
#comenzamos a dividir nuestro entorno 
#
def discretize(self, obs):#cada una de las obsevaciones que recibamos
        return tuple(((obs-self.obs_low)/self.bin_width).astype(int))
    #pedimos que nos divida el valor actual menos el mas pequeño entre las anchuras
    # lo que hacemos aqui es que cada iteracion la almacenara en una tupla
    #lo convertimos en un numero entero
    # cada paso o movimiento que hace lo almacena de forma que el pueda leerlo siendo en numeros enteros  
    
    
    
     # aqui vamos a definir la accion apartir de una observacion 
    def get_action(self, obs):
        discrete_obs = self.discretize(obs)#inicializamos
        #seleccion de la accion a epsilon-greendey 
        if self.epsilon > EPSILON_MIN:#aquel valor que finaliza el algoritmo
            self.epsilon -= EPSILON_DECAY# que parte vamos perdiendoa cada paso 
        if np.random.random() > self.epsilon:#generamos un nuemro aleatorio para obtener acciones ya sean minimas o maximas 
            return np.argmax(self.Q[discrete_obs])
        else:
            return np.random.choice([a for a in range(self.action_shape)])#con probabilidad de epsilon elegimos una al azar 
        
        #con esto decidira de forma aleatoria, elegira acciones al azar, conforme avanza ira tomando valores 
        #para maximizar el radio de aprendizaje
=======
#este metodo no suele ser muy necesario para implementacion de agentes 
#pero en este caso nos resulta muy util cuando el espacio de estados es grande y continuo 
#lo que se puede hacer aqui es divir en cjas o rangos de valores para simplificar su representacion 
#esto tambien reduce el numero de valores que necesita aprender 
#
#comenzamos a dividir nuestro entorno 
#
def discretize(self, obs):#cada una de las obsevaciones que recibamos
        return tuple(((obs-self.obs_low)/self.bin_width).astype(int))
    #pedimos que nos divida el valor actual menos el mas pequeño entre las anchuras
    # lo que hacemos aqui es que cada iteracion la almacenara en una tupla
    #lo convertimos en un numero entero
    # cada paso o movimiento que hace lo almacena de forma que el pueda leerlo siendo en numeros enteros  
    
    
    
     # aqui vamos a definir la accion apartir de una observacion 
    def get_action(self, obs):
        discrete_obs = self.discretize(obs)#inicializamos
        #seleccion de la accion a epsilon-greendey 
        if self.epsilon > EPSILON_MIN:#aquel valor que finaliza el algoritmo
            self.epsilon -= EPSILON_DECAY# que parte vamos perdiendoa cada paso 
        if np.random.random() > self.epsilon:#generamos un nuemro aleatorio para obtener acciones ya sean minimas o maximas 
            return np.argmax(self.Q[discrete_obs])
        else:
            return np.random.choice([a for a in range(self.action_shape)])#con probabilidad de epsilon elegimos una al azar 
        
        #con esto decidira de forma aleatoria, elegira acciones al azar, conforme avanza ira tomando valores 
        #para maximizar el radio de aprendizaje
>>>>>>> 66b915a2aa1bd0fe650c8b7071f516973d5ec0aa
