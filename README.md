
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
