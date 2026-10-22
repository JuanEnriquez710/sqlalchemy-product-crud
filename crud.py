from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Product

# CREATE: crear y guardar un producto
def create_product(db: Session, name: str, price: float, stock: int = 0) -> Product:
    product = Product(name=name, price=price, stock=stock)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# READ: listar todos los productos
def get_products(db: Session) -> list[Product]:
    return list(db.scalars(select(Product).order_by(Product.id)).all())

# READ: buscar un producto por ID
def get_product(db: Session, product_id: int) -> Product | None:
    return db.get(Product, product_id)

# UPDATE: actualizar los campos indicados
def update_product(db: Session, product_id: int, *, name: str | None = None,
                   price: float | None = None, stock: int | None = None) -> Product | None:
    product = db.get(Product, product_id)
    if product is None:
        return None
    if name is not None:
        product.name = name
    if price is not None:
        product.price = price
    if stock is not None:
        product.stock = stock
    db.commit()
    db.refresh(product)
    return product

# DELETE: eliminar por ID
def delete_product(db: Session, product_id: int) -> bool:
    product = db.get(Product, product_id)
    if product is None:
        return False
    db.delete(product)
    db.commit()
    return True
