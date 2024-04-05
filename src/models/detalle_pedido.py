class Detalle_pedido():
    def __init__(self,id_detalle,cantidad,precio_unitario,precio_total,id_pedido,id_producto) -> None:
        self.id_detalle= id_detalle
        self.cantidad= cantidad
        self.precio_unitario= precio_unitario
        self.precio_total= precio_total
        self.id_pedido= id_pedido
        self.id_producto= id_producto
        