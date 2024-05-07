
# Definir las listas separadas por "  "
lista1 = "ID Venta	ID Cliente	Fecha venta	Cliente	Lista de Precios	Clasificacion	Sitio de entrega	Direccion de entrega	ID Vendedor	Vendedor	Estatus	Estatus etapa	Estado venta	Total venta	Total IVA	Gran Total	Forma de pago	Pedido / Orden de compra	Dias de crédito	Contador folio de venta	Folio Venta	Letra sucursal	Sucursal	Nombre sucursal	Uso del CFDI	Folio factura	CFDI	Enum Detalle ventas	Comision	Imp con Letra	Tipo de entrega	Fecha de entrega requerida	Estatus de la entrega	Ruta de reparto	Se remisiono parcial	Productos entregados	Productos pendientes	Nombre cliente público en general	Estatus creacion	Estatus despacho	Contador Cotizacion	Contador Pedido	Contador Remision	Contador Factura	Almacen	Codigo Almacen	Usuario	TimeStamp	ID Historico Cotizaciones	ID Historico Pedidos	ID Historico Remisiones	Trigger historicos	Contador cambios".split("	")
lista2 = "ID Venta	ID Cliente	Fecha venta	Cliente	Clasificacion	Sitio de entrega	Direccion de entrega	ID Vendedor	Vendedor	Estatus	Estatus etapa	Estado venta	Total venta	Total IVA	Gran Total	Forma de pago	Pedido / Orden de compra	Dias de crédito	Contador folio de venta	Folio Venta	Letra sucursal	Sucursal	Nombre sucursal	Uso del CFDI	Folio factura	CFDI	Enum Detalle ventas	Comision	Imp con Letra	Tipo de entrega	Fecha de entrega requerida	Estatus de la entrega	Ruta de reparto	Se remisiono parcial	Productos entregados	Productos pendientes	Nombre cliente público en general	Estatus creacion	Estatus despacho	Contador Cotizacion	Contador Pedido	Contador Remision	Contador Factura	Almacen	Codigo Almacen	Usuario	TimeStamp	Replicar Cotizaciones".split("	")

# Convertir las listas en conjuntos
set_lista1 = set(lista1)
set_lista2 = set(lista2)

# Encontrar la diferencia entre los conjuntos
valores_no_en_lista2 = set_lista1 - set_lista2

# Imprimir los valores que están en la primera lista pero no en la segunda
print("Valores no presentes en la segunda lista:")
print(valores_no_en_lista2)