# from codigo.configuracion.config import MOTOR_BD

# if MOTOR_BD == "sqlite":
#    pass

# elif MOTOR_BD == "postgres":
#    pass

# else:
#    raise ValueError(f"Motor no soportado: {MOTOR_BD}")
from codigo.configuracion.config import MOTOR_BD

if MOTOR_BD == "sqlite":
    pass

elif MOTOR_BD == "postgres":
    pass

else:
    raise ValueError(f"Motor no soportado: {MOTOR_BD}")
