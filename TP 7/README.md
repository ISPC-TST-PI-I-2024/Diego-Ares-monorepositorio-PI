![alt text](./rsc/PI.png)

TP #7

Objetivos 

## Modelo Relacional ## 
Este modelo utiliza tablas para representar datos y relaciones entre esos datos. Es la base de sistemas de bases de datos SQL como MySQL, PostgreSQL y Oracle.

# Estructuración y Organización de Datos #

-Objetivo: Organizar datos en un formato tabular que facilita la estructuración clara y lógica de la información.
-Ventaja: Permite definir esquemas rígidos y relaciones entre tablas mediante claves primarias y foráneas, lo que facilita la integridad y coherencia de los datos.

# Consistencia y Conformidad con ACID #

-Objetivo: Garantizar la integridad y confiabilidad de las transacciones mediante las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad).
-Ventaja: Asegura que las transacciones sean procesadas de manera confiable, incluso en caso de fallos del sistema.

# Consultas Estructuradas y Complejas #

-Objetivo: Permitir consultas complejas y estructuradas utilizando SQL para extraer, manipular y analizar datos.
-Ventaja: Ofrece un lenguaje estandarizado (SQL) para realizar operaciones de consulta y manipulación de datos, lo que facilita el análisis y el reporte.

# Integridad de los Datos #

-Objetivo: Asegurar la consistencia de los datos a través de restricciones y reglas definidas en el esquema.
-Ventaja: Las reglas de integridad y las restricciones de los datos aseguran que los datos almacenados sean precisos y estén bien formados.

# Relaciones entre Datos #

_Objetivo: Modelar y gestionar relaciones entre diferentes conjuntos de datos.
-Ventaja: Permite representar y consultar relaciones entre entidades mediante joins y claves foráneas, facilitando la obtención de información interrelacionada.

## Modelo No Relacional ##
Este modelo utiliza estructuras de datos no tabulares como documentos, pares clave-valor, o grafos. Ejemplos de bases de datos NoSQL incluyen MongoDB, Redis y Neo4j.

# Flexibilidad en el Esquema#
-Objetivo: Permitir un esquema flexible y dinámico que se adapta fácilmente a cambios en la estructura de los datos.
-Ventaja: Los datos se almacenan en formatos como JSON o BSON, lo que permite añadir o modificar campos sin afectar a otras partes del sistema.

# Escalabilidad Horizontal #
-Objetivo: Soportar el crecimiento de datos y usuarios mediante la distribución en múltiples servidores.
-Ventaja: Las bases de datos NoSQL están diseñadas para escalar horizontalmente, permitiendo que la carga se distribuya entre varios nodos.

# Manejo de Datos No Estructurados #
-Objetivo: Gestionar datos no estructurados o semi-estructurados de manera eficiente.
-Ventaja: Ideal para aplicaciones que trabajan con datos que no encajan bien en un esquema tabular rígido, como documentos, imágenes o logs.

# Desempeño y Velocidad #
-Objetivo: Ofrecer alto rendimiento en operaciones de lectura y escritura, especialmente en grandes volúmenes de datos.
-Ventaja: Las bases de datos NoSQL están optimizadas para operaciones rápidas y escalables, adecuadas para aplicaciones con alta demanda de rendimiento.

# Modelado Flexible de Datos #
-Objetivo: Adaptar el modelo de datos a los requerimientos específicos de la aplicación sin necesidad de un esquema rígido.
-Ventaja: Permite modelar datos de forma más acorde con la aplicación, facilitando el almacenamiento y la recuperación según las necesidades de la aplicación.