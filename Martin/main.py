#queremos ser capacez de medir como ha ido todo lo que ha aprendido sometiendolo a una prueba, un test
def test(agent, environment, policy): #dado el agente, dado el entorno y dada la política de actuación ver como la ha ido
    #devolver la recompensa global del episodio
    #en este caso no le dejamos que actualice el valor de qlearning
    done = False 
    obs = environment.reset()
    total_reward = 0.0
    while not done:
        action = policy[agent.discretize(obs)] #la acció no la hacemos ni aleatoria ni con el ratio de aprendizaje sino con la política
        #acción que dictamina la política que hemos entrenado
        #parecido al get_action mediante una observación con la política de acuerdo al lugar dónde se encuentra
        next_obs, reward, done, info = environment.step(action) #los psrámetros con el entorno con los pasos de esa acción
        total_reward += reward #concatenamos la recompensa total anterior mas la recompensa nueva actual
    return total_reward #regresamos nuestra recompensa total