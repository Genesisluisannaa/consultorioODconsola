import json

VALOR_CITA = {"particular": 80000, "eps": 5000, "prepagada": 30000}

VALORES_ATENCION = {
    "particular": {"limpieza": 60000, "calzas": 80000, "extracción": 100000, "diagnóstico": 50000},
    "eps": {"limpieza": 0, "calzas": 40000, "extracción": 40000, "diagnóstico": 0},
    "prepagada": {"limpieza": 0, "calzas": 10000, "extracción": 10000, "diagnóstico": 0}
}

def save_data(data_list):
    try:
        with open("consultorio.txt", "w", encoding="utf-8") as f:
            json.dump(data_list, f)
    except Exception as e:
        print(f"Error al guardar: {e}")

def load_data():
    try:
        with open("consultorio.txt", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 
    except Exception:
        return []

def get_length(data_list):
    count = 0
    for _ in data_list: 
        count += 1
    return count

def add_to_list(data_list, element):
    return data_list + [element]

def sort_customers(data_list):
    n = get_length(data_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_list[j]['total_pagar'] < data_list[j+1]['total_pagar']:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list

def search_by_id(data_list, customer_id):
    for customer in data_list:
        if customer['cedula'] == customer_id:
            return customer
    return None

def capture_data():
    print("\n--- Registro de Nueva Cita ---")
    try:
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        
        
        tipo_c = input("Tipo (Particular, EPS, Prepagada): ").lower()
        if tipo_c not in VALOR_CITA: 
            raise ValueError("Tipo de cliente inválido.")

        tipo_a = input("Atención (Limpieza, Calzas, Extracción, Diagnóstico): ").lower()
        
        
        if tipo_a == "extraccion": tipo_a = "extracción"
        if tipo_a == "diagnostico": tipo_a = "diagnóstico"
        
        if tipo_a not in VALORES_ATENCION[tipo_c]: 
            raise ValueError("Atención inválida.")

        if tipo_a in ["limpieza", "diagnóstico"]:
            cantidad = 1
        else:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0: 
                raise ValueError("Debe ser mayor a 0.")

        prioridad = input("Prioridad (Normal/Urgente): ")
        fecha = input("Fecha (DD/MM/AAAA): ")

        total = VALOR_CITA[tipo_c] + (VALORES_ATENCION[tipo_c][tipo_a] * cantidad)

        return {
            "cedula": cedula, "nombre": nombre, "telefono": telefono,
            "tipo_cliente": tipo_c.upper(), "tipo_atencion": tipo_a.capitalize(),
            "cantidad": cantidad, "prioridad": prioridad,
            "fecha": fecha, "total_pagar": total
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_statistics(data_list):
    total_customers = get_length(data_list)
    total_income = 0
    extraction_count = 0
    for c in data_list:
        total_income += c['total_pagar']
        if c['tipo_atencion'].lower() == "extracción":
            extraction_count += 1
    print(f"\nClientes: {total_customers} | Total Ingresos: ${total_income:,} | Extracciones: {extraction_count}")

def main_menu():
    db_customers = load_data() 
    while True:
        print("\n--- SISTEMA ODONTOLÓGICO (Datos Persistentes) ---")
        print("1. Registrar Cliente | 2. Listado Ordenado | 3. Buscar | 4. Stats | 5. Salir")
        option = input("Seleccione: ")
        
        if option == "1":
            customer = capture_data()
            if customer:
                db_customers = add_to_list(db_customers, customer)
                save_data(db_customers) 
                print("¡Registrado y guardado con éxito!")
        elif option == "2":
            db_customers = sort_customers(db_customers)
            for c in db_customers:
                print(f"[{c['tipo_cliente']}] {c['cedula']} - {c['nombre']}: ${c['total_pagar']:,}")
        elif option == "3":
            search_term = input("Cédula a buscar: ")
            result = search_by_id(db_customers, search_term)
            if result:
                print("\nDatos encontrados:")
                for key, value in result.items():
                    print(f"{key}: {value}")
            else:
                print("Cliente no encontrado.")
        elif option == "4":
            show_statistics(db_customers)
        elif option == "5":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main_menu()