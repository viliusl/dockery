from shared.objtypes import *

C_AMQ = Container("viliusl/ubuntu-activemq", 555, 
    {   'ssh'  :  (55522, AppType.SSH),
        'http' :  (55580, AppType.HTTP),
        'http' :  (55581, AppType.HTTP),
        'jms'  :  (61616, AppType.OTHER)})

C_H2 = Container("viliusl/ubuntu-h2-server", 554, 
    {   'ssh'    :    (55422, AppType.SSH),
        'http'   :    (55480, AppType.HTTP),
        'http'   :    (55481, AppType.HTTP),
        'dbport' :    (1541, AppType.OTHER)})

ENVS = [
    Environment('se-h2', 		[C_AMQ, C_H2]),
    Environment('se-oracle',  	[C_AMQ, C_H2])]