from database import SessionLocal, init_db
from crud import create_product, get_products, get_product, update_product, delete_product

def show_product(product):
    if product is None:
        print("Producto no encontrado.")
    else:
        print(f"ID={product.id} | Nombre={product.name} | Precio={product.price:.2f} | Stock={product.stock}")

def menu():
    print("\n=== CRUD DE PRODUCTOS (SQLAlchemy) ===")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("0. Salir")

def main():
    init_db()
    while True:
        menu()
        option = input("Elige una opción: ").strip()
        try:
            if option == "1":
                name = input("Nombre: ").strip()
                if not name:
                    print("El nombre no puede estar vacío.")
                    continue
                price = float(input("Precio: "))
                stock_text = input("Stock [0 por defecto]: ").strip()
                stock = int(stock_text) if stock_text else 0
                if price < 0 or stock < 0:
                    print("Precio y stock no pueden ser negativos.")
                    continue
                with SessionLocal() as db:
                    show_product(create_product(db, name, price, stock))
            elif option == "2":
                with SessionLocal() as db:
                    products = get_products(db)
                    if not products:
                        print("No hay productos registrados.")
                    for product in products:
                        show_product(product)
            elif option == "3":
                product_id = int(input("ID del producto: "))
                with SessionLocal() as db:
                    show_product(get_product(db, product_id))
            elif option == "4":
                product_id = int(input("ID a actualizar: "))
                name = input("Nuevo nombre (Enter para conservar): ").strip()
                price_text = input("Nuevo precio (Enter para conservar): ").strip()
                stock_text = input("Nuevo stock (Enter para conservar): ").strip()
                with SessionLocal() as db:
                    product = update_product(
                        db, product_id,
                        name=name if name else None,
                        price=float(price_text) if price_text else None,
                        stock=int(stock_text) if stock_text else None,
                    )
                    show_product(product)
            elif option == "5":
                product_id = int(input("ID a eliminar: "))
                with SessionLocal() as db:
                    print("Producto eliminado." if delete_product(db, product_id) else "Producto no encontrado.")
            elif option == "0":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida: revisa que precio/stock/ID sean números.")
        except Exception as exc:
            print(f"Ocurrió un error: {exc}")

if __name__ == "__main__":
    main()
