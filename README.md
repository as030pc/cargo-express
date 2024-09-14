
# Cargo Express

## Entidades Principales:
Productos: Los diferentes productos que ofrece la empresa.
Repartidores: La flota de repartidores.
Pedidos: Los pedidos que los clientes realizan, que pueden contener uno o más productos.
Entregas: El registro de cuándo y por quién fue entregado el pedido.

## Modelo de Datos Relacional:
1. Tabla: productos
Esta tabla contiene los detalles del catálogo de productos.

Campo	Tipo	Descripción
IdProducto	VARCHAR(10)	Identificador único del producto (PK)
Producto	VARCHAR(100)	Nombre del producto
Precio	DECIMAL(5,2)	Precio del producto

2. Tabla: repartidores
Almacena la información de los repartidores.

Campo	Tipo	Descripción
IdRepartidor	INT	Identificador único del repartidor (PK)
Nombre	VARCHAR(100)	Nombre del repartidor

3. Tabla: pedidos
Registra los pedidos hechos por los clientes. Un pedido puede tener varios productos.

Campo	Tipo	Descripción
IdPedido	SERIAL	Identificador único del pedido (PK)
FechaPedido	TIMESTAMP	Fecha y hora en que se realizó el pedido
Total	DECIMAL(10,2)	Total del pedido

4. Tabla: detalle_pedido
Esta tabla es una tabla intermedia que registra los productos asociados a cada pedido, dado que un pedido puede incluir múltiples productos.

Campo	Tipo	Descripción
IdPedido	INT	Identificador del pedido (FK)
IdProducto	VARCHAR(10)	Identificador del producto (FK)
Cantidad	INT	Cantidad de ese producto en el pedido

5. Tabla: entregas
Registra las entregas realizadas por los repartidores. Cada entrega está vinculada a un pedido y a un repartidor.

Campo	Tipo	Descripción
IdEntrega	SERIAL	Identificador único de la entrega (PK)
IdPedido	INT	Identificador del pedido (FK)
IdRepartidor	INT	Identificador del repartidor que realizó la entrega (FK)
FechaEntrega	TIMESTAMP	Fecha y hora en que se registró la entrega

## Relaciones:
Un pedido puede tener muchos productos. Esto se refleja en la relación entre pedidos y detalle_pedido.
Un repartidor puede realizar muchas entregas, reflejado en la relación entre repartidores y entregas.
Un pedido puede tener una entrega, y cada entrega tiene un pedido asociado.

## Diagrama Relacional
productos (1) → (N) detalle_pedido
pedidos (1) → (N) detalle_pedido
pedidos (1) → (1) entregas
repartidores (1) → (N) entregas


## Preguntas teoricas:

La empresa proyecta una expansión del 500% en el próximo año y duplicar su tamaño en el segundo. Para asegurar que la operación pueda soportar este crecimiento, se sugieren las siguientes acciones:

Migrar a la Nube y Arquitecturas Serverless: Utilizar AWS (o una plataforma similar) para escalar dinámicamente los recursos según la demanda.
Adopción de tecnologías serverless (AWS Lambda) para reducir la gestión de servidores y escalar sin complicaciones.

Escalabilidad y Optimización: Implementar cachés (Redis) para mejorar el rendimiento y reducir la carga de la base de datos.
Descomponer la aplicación en microservicios para que los módulos de pedidos y monitoreo puedan escalar de manera independiente.
Usar colas de mensajería (SQS o Kafka) para evitar cuellos de botella en el procesamiento de pedidos.

Monitoreo y Autoescalado:Configurar autoescalado de instancias y bases de datos para ajustar automáticamente los recursos según la demanda.
Implementar herramientas de monitoreo en tiempo real (CloudWatch, Prometheus) para identificar problemas antes de que afecten el rendimiento.

Alta Disponibilidad y Resiliencia: Implementar balanceadores de carga para distribuir tráfico y garantizar la alta disponibilidad. Establecer planes de recuperación ante desastres con replicación de datos en múltiples regiones.

Evaluación de la Solución Actual
La solución actual con Flask, JWT, y PostgreSQL es adecuada para una carga limitada, pero no soportará el crecimiento masivo proyectado sin optimizaciones. Recomendamos migrar hacia FastAPI o microservicios para mejorar el rendimiento, y usar bases de datos más escalables como Amazon Aurora.

Conclusión: Se deben hacer mejoras significativas en infraestructura y arquitectura para soportar el crecimiento de Cargo Express en los próximos dos años.
